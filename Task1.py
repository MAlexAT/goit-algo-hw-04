import timeit
import random
import matplotlib.pyplot as plt

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Функція для вимірювання часу виконання алгоритму
def time_sorting_algorithm(algorithm, arr):
    if algorithm == 'timsort':
        stmt = "sorted(arr)"
        setup_code = "arr = " + str(arr)
        return timeit.timeit(stmt, setup=setup_code, globals=globals(), number=1)
    else:
        setup_code = f"from __main__ import {algorithm.__name__}; arr = {arr}"
        stmt = f"{algorithm.__name__}(arr)"
        return timeit.timeit(stmt, setup=setup_code, globals=globals(), number=1)

# Генерація випадкових наборів даних
data_sizes = [100, 1000, 5000]
data = {
    size: [random.randint(1, 10000) for _ in range(size)]
    for size in data_sizes
}

# Словник для збереження результатів
results = {
    'merge_sort': [],
    'insertion_sort': [],
    'timsort': []
}

# Запуск сортувань та вимір часу
for size, arr in data.items():
    results['merge_sort'].append(time_sorting_algorithm(merge_sort, arr[:]))
    results['insertion_sort'].append(time_sorting_algorithm(insertion_sort, arr[:]))
    results['timsort'].append(time_sorting_algorithm('timsort', arr[:]))

# Виведення результатів
for algorithm, times in results.items():
    print(f"\nЧас виконання для {algorithm}:")
    for size, time in zip(data_sizes, times):
        print(f"Розмір масиву: {size} - Час: {time:.6f} секунд")

import pandas as pd  # pip install pandas - Встановлення бібліотеки pandas, якщо її немає

# Створення таблиці результатів
results_df = pd.DataFrame(results, index=[f"{size} елементів" for size in data_sizes])
print(results_df)

# Зберігаємо цю таблицю в CSV для подальшого використання
results_df.to_csv("sorting_results.csv")

# Побудова графіків
plt.figure(figsize=(10, 6))
for algorithm in results:
    plt.plot(data_sizes, results[algorithm], label=algorithm)

plt.xlabel("Розмір масиву")
plt.ylabel("Час виконання (секунди)")
plt.title("Порівняння алгоритмів сортування")
plt.legend()
plt.grid(True)
plt.show()

