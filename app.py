import os
import subprocess
import datetime
import pytz
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/htop')
def htop():
    # 1. Name - your full name
    full_name = os.getenv('USER', 'Unknown')

    # 2. Username - system username
    username = os.getenv('USER', 'Unknown')

    # 3. Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    # 4. Top output
    try:
        top_output = subprocess.check_output(['top', '-bn1'], universal_newlines=True)
    except subprocess.CalledProcessError:
        top_output = "Error: Unable to fetch top output"

    html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HTOP Information</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }
            h1 { color: #333; }
            pre { background-color: #f4f4f4; padding: 10px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>HTOP Information</h1>
        <p><strong>1. Full Name:</strong> Rakesh Prabhugowda Gowdra</p>
        <p><strong>2. Username:</strong> {{ username }}</p>
        <p><strong>3. Server Time (IST):</strong> {{ server_time }}</p>
        <h2>4. Top Output:</h2>
        <pre>{{ top_output }}</pre>
    </body>
    </html>
    '''

    return render_template_string(html_template, full_name=full_name, username=username, server_time=server_time, top_output=top_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)