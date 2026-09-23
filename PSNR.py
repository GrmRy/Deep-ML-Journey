import numpy as np

def compute_psnr(original: np.ndarray, reconstructed: np.ndarray, max_pixel_value: float) -> float:
    diff = original - reconstructed

    diff_squared = diff ** 2

    mse = np.mean(diff_squared)

    if mse == 0:
        return float('inf')
    max_squared = max_pixel_value ** 2
    ratio = max_squared / mse
    psnr = 10 * np.log10(ratio)

    return round(psnr, 4)
