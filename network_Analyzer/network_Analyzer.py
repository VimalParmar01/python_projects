import scapy.all as scapy
from scapy.layers.http import HTTPRequest, HTTPResponse
from prettytable import PrettyTable
import threading
import time
import os
import sys
import matplotlib.pyplot as plt
from collections import Counter

log_file_path = "advanced_packet_analyzer_log.txt"

packet_count = 0
protocol_count = {"TCP": 0, "UDP": 0, "ICMP": 0, "Other": 0}
packet_size_distribution = Counter()

# Lock for thread-safe operations
lock = threading.Lock()


def log_packet(packet):
    global packet_count
    with lock:
        packet_count += 1
    
    src_ip = packet[scapy.IP].src if scapy.IP in packet else "N/A"
    dst_ip = packet[scapy.IP].dst if scapy.IP in packet else "N/A"
    protocol = "Other"
    if scapy.TCP in packet:
        protocol = "TCP"
    elif scapy.UDP in packet:
        protocol = "UDP"
    elif scapy.ICMP in packet:
        protocol = "ICMP"
    
    with lock:
        if protocol in protocol_count:
            protocol_count[protocol] += 1
        else:
            protocol_count["Other"] += 1

        if scapy.Raw in packet:
            packet_size = len(packet[scapy.Raw].load)
            packet_size_distribution[packet_size] += 1

    if HTTPRequest in packet:
        method = packet[HTTPRequest].Method.decode() if packet[HTTPRequest].Method else "N/A"
        host = packet[HTTPRequest].Host.decode() if packet[HTTPRequest].Host else "N/A"
        path = packet[HTTPRequest].Path.decode() if packet[HTTPRequest].Path else "N/A"
        print(f"[HTTP Request] {method} {host}{path}")
    
    log_data = (
        f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Source IP: {src_ip}\n"
        f"Destination IP: {dst_ip}\n"
        f"Protocol: {protocol}\n"
        f"Raw Payload: {packet.summary()}\n"
        + "-" * 50 + "\n"
    )

    with open(log_file_path, "a") as log_file:
        log_file.write(log_data)

# Real-time metrics display
def display_metrics():
    table = PrettyTable()
    table.field_names = ["Protocol", "Packet Count"]
    while True:
        with lock:
            table.clear_rows()
            for proto, count in protocol_count.items():
                table.add_row([proto, count])
        
        os.system("clear" if os.name == "posix" else "cls")
        print("Real-Time Packet Statistics")
        print(table)
        print(f"Total Packets: {packet_count}")

        
        if packet_size_distribution:
            sizes, counts = zip(*packet_size_distribution.items())
            plt.clf()
            plt.bar(sizes, counts, color='blue')
            plt.xlabel("Packet Sizes")
            plt.ylabel("Count")
            plt.title("Packet Size Distribution")
            plt.pause(0.5)
        else:
            print("No packet size distribution data available.")

        time.sleep(1)

# this is Main sniffing function
def packet_sniffer():
    try:
        print("Starting packet capture... Press Ctrl+C to stop.")
        scapy.sniff(prn=log_packet, store=False)
    except KeyboardInterrupt:
        print("\nPacket capture stopped.")
        print(f"\nThe log file has been saved to: {os.path.abspath(log_file_path)}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit()

def main():
    print("---------------- Advanced Network Packet Analyzer ----------------")
    print("This tool captures and analyzes network packets in real-time.")
    print("It displays real-time statistics and logs packet details for deeper analysis.")
    print("Ensure you have explicit permission to use this tool on any network or system.")


    accept_terms = input("\nDo you accept these terms and conditions? (Yes/No): ")
    if accept_terms.strip().lower() != 'yes':
        
        print("You must accept the terms and conditions before using this program.")
        sys.exit()
    # Start real-time metrics display in a separate thread
    metrics_thread = threading.Thread(target=display_metrics, daemon=True)
    metrics_thread.start()
    packet_sniffer()

if __name__ == "__main__":
    plt.ion()  
    main()
