# Reski Dwi Ramadhani Irawan
# F55121050
import itertools
def calculate_distance(points, permutation):
    total_distance = 0
    num_points = len(points)

    for i in range(num_points - 1):
        current_point = permutation[i]
        next_point = permutation[i + 1]
        distance = points[current_point][next_point]
        total_distance += distance

    start_point = permutation[num_points - 1]
    end_point = permutation[0]
    distance = points[start_point][end_point]
    total_distance += distance

    return total_distance


def tsp(points):
    num_points = len(points)
    all_permutations = list(itertools.permutations(range(1, num_points)))
    min_distance = float('inf')
    optimal_path = None

    for permutation in all_permutations:
        permutation = (0,) + permutation
        distance = calculate_distance(points, permutation)

        if distance < min_distance:
            min_distance = distance
            optimal_path = permutation

    return min_distance, optimal_path

points = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_distance, optimal_path = tsp(points)
print("Minimum distance:", min_distance)
print("Optimal path:", optimal_path)
