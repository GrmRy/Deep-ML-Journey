import numpy as np

def patch_embed_reconstruct(image: np.ndarray, patch_size: int):
    H, W = image.shape
    p = patch_size

    if H % p != 0 or W % p != 0:
        return -1

    num_patches_h = H // p
    num_patches_w = W // p
    N = num_patches_h * num_patches_w

    embedding = []
    for i in range(num_patches_h):
        for j in range(num_patches_w):
            patch = image[i*p:(i+1)*p, j*p:(j+1)*p]
            embedding.append(patch.flatten())
    embedding = np.array(embedding)  

    result = np.zeros((H, W), dtype=image.dtype)
    for idx in range(N):
        i = idx // num_patches_w
        j = idx  % num_patches_w
        result[i*p:(i+1)*p, j*p:(j+1)*p] = embedding[idx].reshape(p, p)

    return result.tolist()
