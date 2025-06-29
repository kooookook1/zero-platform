#!/usr/bin/env python3
"""
ZERO Platform - Port 12000 Server
© 2025 ZERO Platform. All rights reserved.
"""

import socket
import threading
import requests
from urllib.parse import urlparse, parse_qs
import time

def handle_request(client_socket, client_address):
    """Handle incoming HTTP requests"""
    try:
        # Receive request
        request = client_socket.recv(4096).decode('utf-8')
        if not request:
            return
            
        # Parse request
        lines = request.split('\n')
        if not lines:
            return
            
        request_line = lines[0]
        method, path, protocol = request_line.split(' ')
        
        # Forward to main server
        target_url = f"http://localhost:5000{path}"
        
        try:
            if method == 'GET':
                response = requests.get(target_url, timeout=10)
            elif method == 'POST':
                # Extract body from request
                body_start = request.find('\r\n\r\n')
                body = request[body_start + 4:] if body_start != -1 else ''
                response = requests.post(target_url, data=body, timeout=10)
            else:
                response = requests.request(method, target_url, timeout=10)
                
            # Send response
            http_response = f"HTTP/1.1 {response.status_code} OK\r\n"
            http_response += "Content-Type: text/html; charset=utf-8\r\n"
            http_response += "Access-Control-Allow-Origin: *\r\n"
            http_response += f"Content-Length: {len(response.content)}\r\n"
            http_response += "Connection: close\r\n\r\n"
            
            client_socket.send(http_response.encode('utf-8'))
            client_socket.send(response.content)
            
        except Exception as e:
            # Send error response
            error_html = f"""
            <!DOCTYPE html>
            <html lang="ar" dir="rtl">
            <head><meta charset="UTF-8"><title>خطأ - ZERO Platform</title></head>
            <body style="font-family: Arial; text-align: center; padding: 50px;">
                <h1>🔥 ZERO Platform</h1>
                <h2>الخادم الرئيسي غير متاح</h2>
                <p>جاري إعادة توجيهك للخادم الرئيسي...</p>
                <script>
                    setTimeout(function() {{
                        window.location.href = 'http://localhost:5000{path}';
                    }}, 2000);
                </script>
                <p><a href="http://localhost:5000{path}">اضغط هنا للانتقال يدوياً</a></p>
            </body>
            </html>
            """
            http_response = "HTTP/1.1 503 Service Unavailable\r\n"
            http_response += "Content-Type: text/html; charset=utf-8\r\n"
            http_response += f"Content-Length: {len(error_html.encode('utf-8'))}\r\n"
            http_response += "Connection: close\r\n\r\n"
            
            client_socket.send(http_response.encode('utf-8'))
            client_socket.send(error_html.encode('utf-8'))
            
    except Exception as e:
        print(f"Error handling request: {e}")
    finally:
        client_socket.close()

def start_server():
    """Start the proxy server on port 12000"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind(('0.0.0.0', 8888))
        server_socket.listen(5)
        print("🔥 ZERO Platform Proxy Server")
        print("© 2025 ZERO Platform. All rights reserved.")
        print(f"Server running on port 8888")
        print(f"Proxying to: http://localhost:5000")
        print("Press Ctrl+C to stop")
        
        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(
                target=handle_request, 
                args=(client_socket, client_address)
            )
            client_thread.daemon = True
            client_thread.start()
            
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()

if __name__ == '__main__':
    start_server()