from flask import Flask
import os
import datetime
import subprocess
import pytz

app = Flask(__name__)


@app.route("/htop")
def htop_endpoint():
    name = "Your Full Name"
    username = os.getlogin()
    ist = pytz.timezone("Asia/Kolkata")
    server_time_ist = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z%z")

    try:
        top_output = subprocess.getoutput("top -bn1")
    except Exception as e:
        top_output = f"Error running top: {e}"

    html_output = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>/htop Endpoint</title>
    </head>
    <body>
        <h1>/htop Endpoint</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time_ist}</p>
        <h2>Top Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return html_output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
