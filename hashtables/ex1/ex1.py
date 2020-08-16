def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    for index, weight in enumerate(weights):
        cache[weight] = index

    for index, weight in enumerate(weights):
            diff = limit - weight
            if diff in cache:
                return (max(index, cache[diff]), min(index, cache[diff]))

    return None
