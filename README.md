# SecEdge : Security Web Application Firewall


![Hack the Planet](https://img.shields.io/badge/hack-the%20planet-brightgreen.svg)

🚀 SecEdge is a basic implementation of a Python-based Web Application Firewall. 🚀 Attach it to your running Nginx server, and watch the magic happen.

## Features

- 🤖 Rule-based protection against XSS, SQL Injection, and Path Traversal (More to come)
- 🚫 Path-based blocking for protected routes
- 🚀 Customizable rate limiting with customization for per path, ip, etc. (also uses redis caching to scale)
- 📜 IP allow and deny lists for that extra layer of security

## Quick Start

1. **Clone this repository:**

   ```bash
   git clone https://github.com/MattKeeley/SecEdge.git
   ```

2. **Run with Docker:**

   ```bash
   docker-compose up --build
   ```

3. **Attach to your Nginx:**

   Update your Nginx config to forward requests to PySecWAF.

   ```nginx
   server {
       listen 80;
       server_name your_domain.com;

       location / {
           proxy_pass http://localhost:3000;
           # Add more proxy settings if needed
       }

       # Add other server configurations
   }
   ```

---

"Crack the code, shield the server." 💻🔒
