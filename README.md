# Apache vs Nginx Configuration Comparison

This repository contains a Python script that demonstrates the differences between Apache and Nginx web server configurations. The script generates mock configuration snippets for both servers and prints a comparison of their key features. This is intended as an educational tool to help understand how each server handles virtual host configurations and other core functionalities.

## Overview

The Python script in this repository showcases:

- **Apache Configuration Mockup:**  
  Generates a sample Apache virtual host configuration. It highlights the use of per-directory overrides (using `.htaccess`) and the typical structure of an Apache config file.

- **Nginx Configuration Mockup:**  
  Generates a sample Nginx server block. It illustrates the centralized configuration model used by Nginx and how it handles static file serving and request routing.

- **Feature Comparison:**  
  Prints a side-by-side comparison of key differences between Apache and Nginx, including aspects like configuration flexibility, architecture, performance, and module management.

## Features

- **Mock Configuration Generators:**  
  - `generate_apache_config(server_name, doc_root)`: Creates a mock Apache configuration snippet.
  - `generate_nginx_config(server_name, doc_root)`: Creates a mock Nginx configuration snippet.

- **Comparison Display:**  
  - `print_comparison()`: Outputs a summary of the differences between Apache and Nginx regarding configuration style, architecture, performance, and module support.

- **Easy to Run:**  
  A simple `main()` function demonstrates the use of both configuration generators and the comparison function.

## Requirements

- Python 3.x

## How to Run

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/apache-nginx-config-comparison.git
   cd apache-nginx-config-comparison
