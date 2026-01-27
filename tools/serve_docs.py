#!/usr/bin/env python3
import socket
import os
import subprocess
import sys
import webbrowser
from time import sleep

def is_port_free(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) != 0

def find_free_port(start_port):
    port = start_port
    while not is_port_free(port):
        print(f"Port {port} is busy, trying next...")
        port += 1
    return port

def serve_docs(directory, start_port):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' not found.")
        return

    port = find_free_port(start_port)
    print(f"Starting documentation server for '{directory}' on port {port}...")

    # Check if docsify is available via npx
    try:
        # We use docsify-cli if available as it's better for these docs
        cmd = ["npx", "-y", "docsify-cli", "serve", directory, "-p", str(port)]
        
        # Open browser after a short delay
        url = f"http://localhost:{port}"
        print(f"Opening {url} in your browser...")
        
        process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        sleep(2)
        webbrowser.open(url)
        
        print("\nServer is running. Press Ctrl+C to stop.")
        process.wait()
    except KeyboardInterrupt:
        print("\nStopping server...")
        process.terminate()
    except Exception as e:
        print(f"Failed to start docsify, falling back to python http.server: {e}")
        # Fallback to simple python server if npx fails
        os.chdir(directory)
        import http.server
        import socketserver
        
        handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", port), handler) as httpd:
            url = f"http://localhost:{port}"
            print(f"Serving at {url}")
            webbrowser.open(url)
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nStopping server...")
                httpd.shutdown()

if __name__ == "__main__":
    # Default to 'docs' folder in current directory
    # For traccar-web, we can put it in tools/ if we want, but let's just make it available
    docs_dir = "docs"
    default_port = 4002 # Different default for frontend
    
    if len(sys.argv) > 1:
        docs_dir = sys.argv[1]
    if len(sys.argv) > 2:
        default_port = int(sys.argv[2])
        
    serve_docs(docs_dir, default_port)
