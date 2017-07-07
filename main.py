from flask import request, send_file
from flask_api import FlaskAPI
from ImageTracer.ImageTracerClass import ImageTracerClass

app = FlaskAPI(__name__)



@app.route("/PrepareCorpusTest", methods=['GET'])
def preparation():
    createSVG("base64_image", "input.jpg")
    return "pepe"
