def flip_image(image, direction):
    if direction not in ('horizontal', 'vertical'):
        return -1
    if not image or not image[0]:
        return -1
    if not isinstance(image[0], (list, tuple)):
        return -1
    W = len(image[0])
    if any(len(row) != W for row in image):
        return -1
    if direction == 'horizontal':
        return [row[::-1] for row in image]   
    if direction == 'vertical':
        return image[::-1]                     
