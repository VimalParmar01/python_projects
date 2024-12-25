# Advanced Network Packet Analyzer

## Description
The **Advanced Network Packet Analyzer** is a Python-based tool for real-time network traffic capture and analysis. Designed for network professionals, developers, and cybersecurity enthusiasts, this tool provides a detailed view of network activity with protocol detection, HTTP request monitoring, packet size distribution visualization, and comprehensive logging.

## Key Features
- **Real-Time Packet Capture**: Sniffs network packets and provides instant analysis.
- **Protocol Identification**: Tracks TCP, UDP, ICMP, and other protocols.
- **HTTP Monitoring**: Captures HTTP request details, including method, host, and path.
- **Packet Size Analysis**: Visualizes packet size distribution with real-time bar charts.
- **Detailed Logging**: Saves packet details in a structured log file for post-analysis.
- **Interactive Metrics**: Displays protocol-specific packet counts in real time.

## Prerequisites
- **Python 3.x** installed.
- Libraries: `scapy`, `prettytable`, and `matplotlib`. Install them using:
  ```bash
  pip install scapy prettytable matplotlib
  ```

## How to Use
1. Clone the repository and navigate to the project folder:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Run the program:
   ```bash
   python advanced_packet_analyzer.py
   ```
3. Accept the terms and start capturing packets.
4. View real-time metrics, packet size distribution, and check the log file (`advanced_packet_analyzer_log.txt`) for detailed analysis.

## Important Notes
- **Permission**: Requires administrative privileges to sniff network traffic.
- **Ethical Use**: Use only on authorized networks.
