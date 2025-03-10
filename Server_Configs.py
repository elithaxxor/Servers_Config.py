#!/usr/bin/env python3

def generate_apache_config(server_name, doc_root):
    """
    Generate a mock Apache configuration snippet.
    Apache supports per-directory overrides using .htaccess files.
    """
    return f"""
<VirtualHost *:80>
    ServerName {server_name}
    DocumentRoot {doc_root}
    <Directory {doc_root}>
        Options Indexes FollowSymLinks
        AllowOverride All  # Enables .htaccess overrides
        Require all granted
    </Directory>
</VirtualHost>
"""

def generate_nginx_config(server_name, doc_root):
    """
    Generate a mock Nginx configuration snippet.
    Nginx uses a centralized configuration model.
    """
    return f"""
server {{
    listen 80;
    server_name {server_name};
    root {doc_root};
    index index.html index.htm;
    
    location / {{
        try_files $uri $uri/ =404;
    }}
    # Note: Nginx does not support per-directory .htaccess files.
}}
"""

def print_comparison():
    """
    Print a comparison between Apache and Nginx highlighting their differences.
    """
    differences = {
        "Configuration":
            {"Apache": "Uses .htaccess for per-directory configuration.",
             "Nginx": "Centralized configuration without per-directory overrides."},
        "Architecture":
            {"Apache": "Process-based; each request spawns a process/thread.",
             "Nginx": "Event-driven, asynchronous handling for high concurrency."},
        "Performance":
            {"Apache": "Great for dynamic content but may use more memory.",
             "Nginx": "Highly efficient with static files and many concurrent connections."},
        "Modules":
            {"Apache": "Loads modules dynamically and has extensive module support.",
             "Nginx": "Modules are typically compiled into the binary, less flexible at runtime."}
    }
    
    print("Key Differences between Apache and Nginx:\n")
    for aspect, details in differences.items():
        print(f"{aspect}:")
        print(f"  Apache: {details['Apache']}")
        print(f"  Nginx:  {details['Nginx']}\n")

def main():
    server_name = "example.com"
    doc_root = "/var/www/html"
    
    print("=== Apache Configuration Mockup ===")
    print(generate_apache_config(server_name, doc_root))
    
    print("=== Nginx Configuration Mockup ===")
    print(generate_nginx_config(server_name, doc_root))
    
    print("=== Comparison of Key Features ===")
    print_comparison()

if __name__ == "__main__":
    main()
