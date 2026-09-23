def zero_pad_image(img, pad_width):
    if not isinstance(pad_width, int) or pad_width < 0:
        return -1

    if not img or not img[0]:
        return -1

    if not isinstance(img[0], (list, tuple)):
        return -1

    W = len(img[0])
    if any(len(row) != W for row in img):
        return -1

    new_W    = W + 2 * pad_width
    zero_row = [0] * new_W

    result = []
    result += [zero_row[:] for _ in range(pad_width)]                        
    result += [[0]*pad_width + list(row) + [0]*pad_width for row in img]    
    result += [zero_row[:] for _ in range(pad_width)]                     

    return result
