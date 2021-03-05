from flask import Flask, render_template, request, jsonify
from flask_sse import sse
import pyqrcode
from io import BytesIO

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix="/stream")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/message/", methods=["POST"])
def publish_messages():
    request_data = request.json
    sse.publish({"message": request_data["comment"]}, type="greeting")
    return "Message sent!"


@app.route("/lnurl/<lnurl>")
def publish_lnurl(lnurl):
    sse.publish({"lnurl": lnurl}, type="lnurlevent")
    return "Message sent!"


@app.route("/qr/<LNURL>")
def publish_qr(LNURL):
    qr = pyqrcode.create(LNURL)
    stream = BytesIO()
    qr.svg(stream, scale=10, background="#fff")
    return (
        stream.getvalue(),
        200,
        {
            "Content-Type": "image/svg+xml",
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
        },
    )
