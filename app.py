from flask import Flask, render_template, request
import requests, time

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def get_value():
    url = request.form["url"]
    print(url)
    r = requests.post(
        "https://api.deepai.org/api/colorizer",
        data={
            "image": {url},
        },
        headers={"api-key": "7e7a76a4-3e3c-4176-8a42-a77a7fbf349c"},
    )
    print("reached")

    time.sleep(10)
    data = r.json()
    print(data)
    print(data["output_url"])
    return render_template("io.html", org=url, data=data["output_url"])


# Handle 404 errors
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run()
