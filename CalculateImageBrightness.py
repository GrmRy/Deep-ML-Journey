def calculate_brightness(img):
    if not img or not img[0]:
        return -1

    row_len = len(img[0])
    if any(len(row) != row_len for row in img):
        return -1

    if any(px < 0 or px > 255 for row in img for px in row):
        return -1

    total_pixels = len(img) * len(img[0])
    total_brightness = sum(px for row in img for px in row)
    return round(total_brightness / total_pixels, 2)
