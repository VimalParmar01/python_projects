import socket
import requests
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from urllib.parse import urljoin

def scan_port(ip, port, results):
    """
    Scans a single port to check if it's open and attempts a basic banner grab.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            banner = ""
            try:
                # Try grabbing a banner
                sock.send(b"HEAD / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip).encode())
                banner = sock.recv(1024).decode().strip()
            except:
                banner = "Unknown Service"
            results.append((port, banner))
            print(f"[+] Port {port} is OPEN - {banner}")
        sock.close()
    except Exception as e:
        pass  # Ignore errors silently

def real_time_port_scanner(ip, start_port, end_port, threads):
    """
    Scans a range of ports on a given IP address in real-time.
    """
    print(f"\nStarting real-time port scan on {ip}...")
    print(f"Scanning ports {start_port} to {end_port}")
    print("Start time:", datetime.now())
    
    open_ports = []  # List to store open ports and banners

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port, open_ports)

    print("\nScan completed.")
    print("End time:", datetime.now())
    print(f"Open ports: {open_ports if open_ports else 'None found'}")

    return open_ports

def test_xss(website):
    """
    Tests if the given website is vulnerable to a basic reflected XSS attack.
    """
    print(f"\n[+] Testing {website} for XSS vulnerabilities...")
    payload = "<script>alert('XSS')</script>"
    test_url = urljoin(website, "?test=" + payload)

    try:
        response = requests.get(test_url, timeout=5)
        if payload in response.text:
            print("[!] Website is VULNERABLE to XSS!")
        else:
            print("[-] Website is NOT vulnerable to XSS.")
    except Exception as e:
        print(f"[-] Error testing for XSS: {e}")

def main():
    """
    Main function to handle argument parsing and execution.
    """
    parser = argparse.ArgumentParser(description="Website Scanner: Port Scan, Vulnerability Check, and XSS Test")
    parser.add_argument("website", help="Target website (e.g., https://example.com)")
    parser.add_argument("-s", "--start-port", type=int, default=1, help="Starting port (default: 1)")
    parser.add_argument("-e", "--end-port", type=int, default=65535, help="Ending port (default: 65535)")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads for port scanning (default: 100)")
    args = parser.parse_args()

    # Extract IP from website
    try:
        target_ip = socket.gethostbyname(args.website.replace("https://", "").replace("http://", "").split("/")[0])
        print(f"[+] Resolved IP for {args.website}: {target_ip}")
    except socket.gaierror as e:
        print(f"[-] Could not resolve IP for {args.website}: {e}")
        return

    # Perform port scan
    open_ports = real_time_port_scanner(target_ip, args.start_port, args.end_port, args.threads)

    # Perform basic vulnerability checks (example: Banner info)
    if open_ports:
        print("\n[+] Basic vulnerability check:")
        for port, banner in open_ports:
            print(f"    Port {port}: {banner}")

    # Test for XSS vulnerabilities
    test_xss(args.website)

if __name__ == "__main__":
    main()
