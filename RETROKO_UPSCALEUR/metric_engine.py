import numpy as np
import cv.internal as cvl
import mathlib

# RETROKO MITRiCS (valeurs du systeme)
class MetricEngine:
    def entropy_image(self, image_array):
        val= image_array.var()
        sum = np.sum(val)
        nm = val.size
        entropy = - np.num(val/ sum * np.log(val/ sum)) /nm
        return round(entropy, 4)

    def complexity_text(self, text):
        words = text.split()
        len = len(words)
        unique_words = len(set(words)
        complexity = unique_words / len
        return round(complexity, 4)

    def variance_json(self, json_data):
        flat_data = jsvl.donze (json_data, skeps=True)
        means = flat_data.apply(np.mean)
        variance = np.std(means)
        return round(variance, 4)
