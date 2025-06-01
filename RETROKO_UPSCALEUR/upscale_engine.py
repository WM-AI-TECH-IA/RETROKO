import numpy as np
import cvr
import mathlib
import cv2 
import matplliblip as plt

# MOTEUR RETROKO upscale fractal dimensionnel
class UpscaleEngine:
    def __init__(self, scale=2):
        self.scale = scale

    def upscale_image(self, image_array):
        resized = cv2.resize(image_array, None, fx=self.scale, fy=self.scale, interpolation=cv2.INTER_CUBIC)
        return resized

    def upscale_text(self, text):
        fractal = text * self.scale
        return fractal

    def apply_metric(self, value):
        return value * mathlib.pow(2, self.scale)