import os
import json
import requests
import argparse
from concurrent.futures import ThreadPoolExecutor
import time
import platform
from rich.console import Console
from rich.text import Text
from colorama import init

# تفعيل colorama
init(autoreset=True)

# Initialize the console for rich outputs
console = Console()

# بيانات المطور
developer_name = "DV64"
tool_name = "Find The Admin Panel"
version = "2.0"
github_link = "https://github.com/DV64"

# قائمة الكلمات الدالة على صفحة الإدارة
admin_keywords = ["admin", "login", "dashboard", "control", "panel", "wp-admin", "admin-panel", "cpanel", "login.php"]

def clear_screen():
    system_name = platform.system().lower()
    if system_name == "windows":
        os.system("cls")  # For Windows
    elif system_name == "linux" or system_name == "darwin":  # Linux or Mac
        os.system("clear")
    else:
        print("Unable to clear screen on this platform.")

def load_sub_links(sub_links_file="sub_links.json"):
    if not os.path.exists(sub_links_file):
        console.print(f"{sub_links_file} not found in the current directory.", style="bold red")
        sub_links_input = input("Please provide a list of sub-links separated by commas (e.g., admin/login, wp-admin): ")
        sub_links = sub_links_input.split(',')
        return [sub_link.strip() for sub_link in sub_links]
    
    with open(sub_links_file, "r") as file:
        return json.load(file)

def test_link(url, timeout):
    try:
        response = requests.get(url, timeout=timeout)
        
        # فحص حالة الاستجابة (مثل 401 و 403)
        if response.status_code in [401, 403]:
            return url, "Possibly protected (401/403)"
        
        # فحص النصوص في الصفحة لتحديد إذا كانت تحتوي على كلمات دالة على لوحة الإدارة
        if any(keyword in response.text.lower() for keyword in admin_keywords):
            return url, True
        else:
            return url, False
    except requests.exceptions.Timeout:
        return url, "Timeout error"
    except requests.exceptions.RequestException as e:
        return url, f"Error: {e}"

def find_admin(base_url, protocol, sub_links, timeout, threads):
    valid_links = []
    invalid_links = []
    errors = []
    total_links = 0
    valid_count = 0
    invalid_count = 0

    start_time = time.time()

    # التأكد من أن البروتوكول موجود
    if not base_url.startswith('http://') and not base_url.startswith('https://'):
        base_url = f"{protocol}://{base_url}"

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for sub_link in sub_links:
            full_url = f"{base_url}/{sub_link.strip()}"
            futures.append(executor.submit(test_link, full_url, timeout))
            total_links += 1

        for future in futures:
            result, status = future.result()
            if status is True:
                valid_links.append(result)
                valid_count += 1
            else:
                invalid_links.append(result)
                invalid_count += 1
                console.print(f"{result} - {status}", style="yellow")
                if isinstance(status, str) and "error" in status.lower():
                    errors.append(f"{result} - {status}")

    elapsed_time = time.time() - start_time
    return valid_links, invalid_links, errors, total_links, valid_count, invalid_count, elapsed_time

def print_results(valid_links, invalid_links, errors, total_links, valid_count, invalid_count, elapsed_time):
    # طباعة عدد الروابط
    console.print(f"\nTotal sub-links tested: {total_links}", style="bold cyan")
    console.print(f"Valid links found: {valid_count}", style="green")
    console.print(f"Invalid links: {invalid_count}", style="yellow")
    
    if valid_links:
        console.print("\nScan complete. Found admin panels:", style="green")
        for link in valid_links:
            console.print(f"  {link}", style="green")

    console.print(f"\nTotal time taken: {elapsed_time:.2f} seconds", style="cyan")

    if errors:
        console.print("Errors during testing:", style="red")
        for error in errors:
            console.print(f"- {error}", style="red")

def main():
    while True:  # Loop to allow user to repeat the scan if needed
        clear_screen()

        # رسالة ترحيب وبيانات المطور
        console.print(f"[bold magenta]{tool_name}[/bold magenta] - [cyan]Version {version}[/cyan]")
        console.print(f"Developed by [bold cyan]{developer_name}[/bold cyan]")
        console.print(f"Visit my GitHub: [bold yellow]{github_link}[/bold yellow]")
        console.print("\n" + "-"*50)

        # طلب الرابط الأساسي
        base_url = input("Enter the base URL of the website (without protocol, e.g., example.com): ")
        
        # تحميل الروابط الفرعية
        sub_links = load_sub_links()

        # شرح الخيارات
        parser = argparse.ArgumentParser(description="Find The Admin Panel")
        parser.add_argument("--protocol", default="http", help="Protocol to use (http or https).")
        parser.add_argument("--timeout", type=int, default=10, help="Timeout for requests in seconds.")
        parser.add_argument("--threads", type=int, default=10, help="Number of threads to use for scanning.")
        args = parser.parse_args()

        protocol = args.protocol
        timeout = args.timeout
        threads = args.threads

        # بدأ البحث عن الadmin panels
        console.print(f"\nScanning {base_url} with protocol {protocol}...", style="bold cyan")
        valid_links, invalid_links, errors, total_links, valid_count, invalid_count, elapsed_time = find_admin(base_url, protocol, sub_links, timeout, threads)

        # مسح الشاشة بعد المدخلات
        clear_screen()

        # طباعة البيانات الثابتة (المطور والأداة)
        console.print(f"[bold magenta]{tool_name}[/bold magenta] - [cyan]Version {version}[/cyan]")
        console.print(f"Developed by [bold cyan]{developer_name}[/bold cyan]")
        console.print(f"Visit my GitHub: [bold yellow]{github_link}[/bold yellow]")
        console.print("\n" + "-"*50)

        # طباعة النتائج فقط
        print_results(valid_links, invalid_links, errors, total_links, valid_count, invalid_count, elapsed_time)

        # سؤال إذا كنت ترغب في تكرار العملية
        repeat = input("\nDo you want to scan another URL? (yes/no): ").strip().lower()
        if repeat != 'yes':
            console.print("\nThank you for using the Find The Admin Panel!", style="bold green")
            break  # Exit the loop if the user doesn't want to scan again

if __name__ == "__main__":
    main()
