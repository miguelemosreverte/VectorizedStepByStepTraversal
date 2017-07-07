from Base64Helper.Base64HelperClass import Base64HelperClass

import subprocess

class ImageTracerClass:

    @staticmethod
    def createSVG(base64_image, filename):

        #first we save the file to work with it
        #Base64HelperClass.base64_to_image(base64_image, filename)
        #then we work with it
        subprocess.call(["java","-jar","./ImageTracer/imagetracerjava/ImageTracer.jar",filename])

        #finally we return the SVG
        return  Base64HelperClass.filepath_to_base64(filename + ".svg")
