from flask import Flask
import os
import time
import psutil
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system information
    name = "Suseendharan S B"  # Replace with your full name
    username = os.environ.get('USER', 'unknown')  # Get the system username (using environment variable)
    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')  # Get server time in IST
    
    # Get 'top' output (simplified as list of running processes here)
    top_output = "\n".join([f"PID: {pid}, Name: {psutil.Process(pid).name()}" for pid in psutil.pids()[:10]])  # Get a list of top 10 process names

    # HTML Output
    return f'''
    <html>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <h3>Top Output (Processes)</h3>
            <pre>{top_output}</pre>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Make the app accessible from outside the codespace
