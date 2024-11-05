from ssl_expire import get_ssl_info
from mail_script import send_email
import os

hostnames = os.environ.get('HOSTNAMES')

for hostname in hostnames:
    ssl_info = get_ssl_info(hostname)
    if ssl_info:
        print(f"Hostname: {ssl_info['hostname']}")
        print(f"Certificate Expiration Date: {ssl_info['expiration_date']}")
        print(f"Remaining Days: {ssl_info['remaining_days']} days")

        mail_condition = ssl_info['remaining_days']

        if mail_condition < 10:
            subject = f"SSL Certificate Expiration Warning for {ssl_info['hostname']}"
            message = (f"\n\nWarning: \nThe SSL certificate for {ssl_info['hostname']} "
                       f"\nexpires in {mail_condition} days!")
            to_email = os.environ.get('TO_EMAIL')

            send_email(subject, message, to_email)
    else:
        print(f"Could not retrieve SSL info for {hostname}")
