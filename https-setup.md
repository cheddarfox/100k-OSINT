# HTTPS Configuration Guide

This guide will help you set up HTTPS for your OSINT Research System using Let's Encrypt and Certbot.

## Prerequisites

- A domain name pointing to your server's IP address
- Ubuntu 20.04 or later
- Nginx installed and configured

## Steps

1. Install Certbot and Nginx plugin:
   ```
   sudo apt update
   sudo apt install certbot python3-certbot-nginx
   ```

2. Obtain and install a certificate:
   ```
   sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
   ```

3. Follow the prompts to configure HTTPS settings

4. Test automatic renewal:
   ```
   sudo certbot renew --dry-run
   ```

5. Update your Nginx configuration to force HTTPS:

   Edit `/etc/nginx/sites-available/default`:
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com www.yourdomain.com;
       return 301 https://$server_name$request_uri;
   }

   server {
       listen 443 ssl;
       server_name yourdomain.com www.yourdomain.com;

       ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
       ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

       # Other SSL settings...

       location / {
           proxy_pass http://localhost:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

6. Test Nginx configuration:
   ```
   sudo nginx -t
   ```

7. Reload Nginx:
   ```
   sudo systemctl reload nginx
   ```

Your OSINT Research System should now be accessible via HTTPS.
