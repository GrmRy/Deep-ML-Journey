def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n = len(vectors[0]) 
    means = [sum(v) / n for v in vectors]

    def cov(x, y, mean_x, mean_y):
        return sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / (n - 1)

    num_features = len(vectors)
    return [
        [cov(vectors[i], vectors[j], means[i], means[j]) for j in range(num_features)]
        for i in range(num_features)
    ]
