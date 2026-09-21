import numpy as np

def calculate_contrast(img) -> int:
    return int(img.max() - img.min())
