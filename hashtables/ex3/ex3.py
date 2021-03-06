def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = set()
    intersects = []

    for each in arrays:
        for number in each:
            if number not in cache:
                cache.add(number)
            else:
                intersects.append(number)
    
    result = []
    for index in intersects:
        if index not in result:
            result.append(index)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
