# SSL Expiry Checker

This repository is set up to check the expiration dates of SSL certificates for specified hostnames. It includes a Jenkins pipeline to automate the process and send email notifications when certificates are close to expiring.

## Files

- **Jenkinsfile**: Contains the Jenkins pipeline configuration to trigger the SSL expiry check.
- **main.py**: The main script that checks SSL certificate expiration for each hostname and triggers email notifications if certificates are nearing expiration.
- **mail_script.py**: A helper script for sending email notifications.
- **ssl_expire.py**: Contains the core functionality for fetching SSL certificate information, such as expiration date and remaining days.

## Getting Started

To set up and run the SSL expiry checker:

1. **Add Environment Variables**: Ensure you have the following environment variables set up:
   - `HOSTNAMES`: A comma-separated list of hostnames to check for SSL expiry.
   - `TO_EMAIL`: The email address to send notifications to.
   - `SMTP_PASSWORD`: The SMTP password, stored securely in Jenkins credentials.

2. **Run with Jenkins**: The Jenkins pipeline (`Jenkinsfile`) is configured to execute the SSL expiry check at a scheduled time. It retrieves SSL certificate information for each specified hostname and sends an email if any certificate is set to expire in fewer than 10 days.

## Usage

The `main.py` script iterates over each hostname in `HOSTNAMES` and checks for SSL certificate expiration. If any certificate has fewer than 10 days remaining, an email is sent to the specified `TO_EMAIL` address.

### Running Locally

To run the SSL expiry check locally, execute:

```bash
python3 main.py
