from flask import Flask, render_template
from flask_sse import sse
import pyqrcode
from io import BytesIO

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix="/stream")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<thenote>")
def publish_messages(thenote):
    sse.publish({"message": "thenote"}, type="greeting")
    return "Message sent!"


@app.route("/qr/<LNURL>")
def publish_qr(LNURL):
    qr = pyqrcode.create(LNURL)
    stream = BytesIO()
    qr.svg(stream, scale=10)
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
