def rgb_to_grayscale(image):
    if not image or not image[0]:
        return -1

    H = len(image)
    W = len(image[0])

    for row in image:
        if len(row) != W:
            return -1
        for pixel in row:
            if not isinstance(pixel, (list, tuple)):
                return -1
            if len(pixel) != 3:
                return -1
            if any(c < 0 or c > 255 for c in pixel):
                return -1

    result = []
    for row in image:
        gray_row = []
        for R, G, B in row:
            gray = 0.299 * R + 0.587 * G + 0.114 * B
            gray_row.append(round(gray))
        result.append(gray_row)

    return result
