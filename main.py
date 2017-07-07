from flask import request, send_file
from flask_api import FlaskAPI
from ImageTracer.ImageTracerClass import ImageTracerClass

app = FlaskAPI(__name__)



@app.route("/PandaPNG_Test", methods=['GET'])
def preparation():    
    return ImageTracerClass.createSVG("base64_image", "panda.png")




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
