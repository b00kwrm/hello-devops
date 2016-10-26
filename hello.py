from flask import Flask
app = Flask(__name__)

page = b"""
<!doctype html>
<html>
<head>
<title>hello world</title>
</head>
<body>
<h1>hello, world</h1>
</body>
</html>
"""

@app.route("/")
def hello():
    return page

if __name__ == "__main__":
    app.run(host="0.0.0.0")
