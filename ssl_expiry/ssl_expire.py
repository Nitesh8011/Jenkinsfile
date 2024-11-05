import ssl
import socket
from datetime import datetime

# Function to get SSL certificate information for a hostname
def get_ssl_info(hostname):
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)

    try:
        conn.connect((hostname, 443))
        cert = conn.getpeercert()

        not_after = datetime.strptime(cert.get("notAfter"), '%b %d %H:%M:%S %Y GMT')
        today = datetime.today()
        remaining_days = (not_after - today).days

        # Return the collected data as a dictionary
        return {
            "hostname": hostname,
            "expiration_date": not_after,
            "remaining_days": remaining_days
        }

    except Exception as e:
        print(f"Hostname: {hostname}")
        print(f"Certificate information could not be obtained. Error: {str(e)}")
        return None
    finally:
        conn.close()
