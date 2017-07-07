#!/usr/bin/python

import sys
import os
import base64

class Base64HelperClass:
    @staticmethod
    def image_to_base64(image):
        return base64.encodestring(image.read())

    @staticmethod
    def base64_to_image(image_64_encode):
        return base64.decodestring(image_64_encode)


    @staticmethod
    def filepath_to_base64(filepath):
        with open(filepath, 'rb') as image:
            return Base64HelperClass.image_to_base64(image)

    @staticmethod
    def base64_to_file(image_64_encode):
        with open(filepath, 'wb') as image:
            image.write(Base64HelperClass.base64_to_image(image_64_encode))
