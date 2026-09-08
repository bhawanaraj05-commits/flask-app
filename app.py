from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>My Flask Website</title>
        </head>
        <body>
            <h1>Hello! My Flask Website is Running</h1>
            <p>Deployed using Jenkins on Ubuntu.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
