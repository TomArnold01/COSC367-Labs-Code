import math
from collections import Counter

def euclidean_distance(v1, v2):
    result = 0
    
    for i in range(0, len(v1)):
        result += (v1[i] - v2[i])**2

    return math.sqrt(result)

def majority_element(labels):
    lable_counts = Counter(labels)
    most_common = lable_counts.most_common(1)
    return most_common[0][0]


def knn_predict(input, examples, distance, combine, k):


    sorted_examples = sorted(examples, key=lambda ex: distance(input, ex[0]))
    other_neighbors = []
    nearest_neighbors = sorted_examples[:k]    
    farthest_distance = distance(input, nearest_neighbors[-1][0])
    
    for example in sorted_examples[k:]:
        if distance(input, example[0]) == farthest_distance:
            other_neighbors.append(example)
        else:
            break

    neighbor_outputs = [neighbor[1] for neighbor in nearest_neighbors + other_neighbors]
    result = combine(neighbor_outputs)
    
    return result


def main():

    examples = [
        ([2], '-'),
        ([3], '-'),
        ([5], '+'),
        ([8], '+'),
        ([9], '+'),
    ]

    distance = euclidean_distance
    combine = majority_element

    for k in range(1, 6, 2):
        print("k =", k)
        print("x", "prediction")
        for x in range(0,10):
            print(x, knn_predict([x], examples, distance, combine, k))
        print()

    # using knn for predicting numeric values

    examples = [
        ([1], 5),
        ([2], -1),
        ([5], 1),
        ([7], 4),
        ([9], 8),
    ]

    def average(values):
        return sum(values) / len(values)

    distance = euclidean_distance
    combine = average

    for k in range(1, 6, 2):
        print("k =", k)
        print("x", "prediction")
        for x in range(0,10):
            print("{} {:4.2f}".format(x, knn_predict([x], examples, distance, combine, k)))
        print()

if __name__ == "__main__":
    main()