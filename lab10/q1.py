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

def main():

    print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))

    print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
    print(majority_element("ababc") in "ab")

if __name__ == "__main__":
    main()