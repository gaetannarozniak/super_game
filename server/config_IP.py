import socket

def get_local_ip():
    """Finds the local IP address of the machine."""
    try:
        # Create a socket and connect to an external server (Google DNS)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        return f"Error finding IP: {e}"

# Auto-detect local IP
IP = get_local_ip()

# Optionally, set a STATIC_IP if needed
STATIC_IP = "192.168.1.100"  # Change this if you want a fixed IP

# Define a default port
PORT = 8080  # Change this if you need a different port

if __name__ == "__main__":
    print(f"Local IP Address: {IP}")
    print(f"Port: {PORT}")