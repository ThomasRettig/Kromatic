from flask import Flask, render_template, request
import requests, time
import os
from urllib.parse import urlparse

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def get_value():
    url = request.form["url"]
    path = urlparse(url).path
    ext = os.path.splitext(path)[1]
    # validate the URL
    if ext != "png" or "jpg" or "jpeg":
        print("Bad URL")
        return render_template("500.html"), 500
    else:
        print(url)
        r = requests.post(
            "https://api.deepai.org/api/colorizer",
            data={"image": {url}},
            headers={"api-key": "7e7a76a4-3e3c-4176-8a42-a77a7fbf349c"},
        )
        print("Reached!")

        time.sleep(10)
        data = r.json()
        print(data)
        print(data["output_url"])
        return render_template("io.html", org=url, data=data["output_url"])


# Handle 404 errors
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

# Handle 404 errors
@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run()
