#!/usr/bin/env python3
"""
ZERO Platform - Proxy Server for Port 12001
© 2025 ZERO Platform. All rights reserved.
"""

from flask import Flask, request, Response
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Target server
TARGET_URL = 'http://localhost:5000'

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def proxy(path):
    """Proxy all requests to the target server"""
    try:
        # Build target URL
        target_url = f"{TARGET_URL}/{path}"
        
        # Forward the request
        if request.method == 'GET':
            resp = requests.get(target_url, params=request.args, headers=request.headers, timeout=30)
        elif request.method == 'POST':
            resp = requests.post(target_url, 
                               data=request.get_data(), 
                               params=request.args, 
                               headers=request.headers, 
                               timeout=30)
        else:
            resp = requests.request(request.method, target_url, 
                                  data=request.get_data(), 
                                  params=request.args, 
                                  headers=request.headers, 
                                  timeout=30)
        
        # Create response
        response = Response(resp.content, resp.status_code)
        
        # Copy headers (excluding some that shouldn't be forwarded)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        for key, value in resp.headers.items():
            if key.lower() not in excluded_headers:
                response.headers[key] = value
                
        return response
        
    except Exception as e:
        logging.error(f"Proxy error: {e}")
        return f"Proxy Error: {e}", 500

if __name__ == '__main__':
    print("Starting ZERO Platform Proxy Server...")
    print("Proxying port 12001 -> 5000")
    app.run(host='0.0.0.0', port=12001, debug=False, threaded=True)