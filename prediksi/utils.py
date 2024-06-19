def weighted_moving_average(data, weights):
    weighted_sum = sum(w * d for w, d in zip(weights, data))
    return weighted_sum / sum(weights)
