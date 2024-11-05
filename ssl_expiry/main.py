from ssl_expire import get_ssl_info
from mail_script import send_email
import os

# Retrieve environment variables
hostnames = os.environ.get('HOSTNAMES')

if not hostnames:
    print("Error: HOSTNAMES environment variables are not set.")
else:
    # Split hostnames by commas and clean up whitespace
    hostname_list = [hostname.strip() for hostname in hostnames.split(',') if hostname.strip()]

    for hostname in hostname_list:
        ssl_info = get_ssl_info(hostname)
        if ssl_info:
            print(f"Hostname: {ssl_info['hostname']}")
            print(f"Certificate Expiration Date: {ssl_info['expiration_date']}")
            print(f"Remaining Days: {ssl_info['remaining_days']} days")

            # Send an email if certificate expiration is within 10 days
            if ssl_info['remaining_days'] < 10:
                subject = f"SSL Certificate Expiration Warning for {ssl_info['hostname']}"
                message = (f"\n\nWarning: \nThe SSL certificate for {ssl_info['hostname']} "
                           f"\nexpires in {ssl_info['remaining_days']} days!")
                
                to_email = os.environ.get('TO_EMAIL')
                send_email(subject, message, to_email)
        else:
            print(f"Could not retrieve SSL info for {hostname}")
