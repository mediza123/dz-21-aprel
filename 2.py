import random
import math
import statistics

def get_random_numbers(number_count=100, min_value=1, max_value=100):
    return [random.randint(min_value, max_value) for _ in range(number_count)]

def compute_statistics(number_sequence):
    average_value = statistics.mean(number_sequence)
    median_value = statistics.median(number_sequence)
    deviation_value = statistics.stdev(number_sequence)
    root_sum_value = math.sqrt(sum(number_sequence))
    
    return {
        'average': average_value,
        'median': median_value,
        'deviation': deviation_value,
        'root_sum': root_sum_value
    }

if __name__ == "__main__":
    numbers = get_random_numbers()
    results = compute_statistics(numbers)
    
    print(f"Среднее: {results['average']:.2f}, "
          f"Медиана: {results['median']}, "
          f"Стандартное отклонение: {results['deviation']:.2f}, "
          f"Корень из суммы: {results['root_sum']:.2f}")
