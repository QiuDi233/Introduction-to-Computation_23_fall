def reverse_sort(n):
    def custom_sort(x):
        reverse_x = int(str(x)[::-1])
        return (reverse_x, -x)

    sorted_numbers = sorted(range(1, n + 1), key=custom_sort, reverse=True)
    return sorted_numbers

n = int(input())
result = reverse_sort(n)
print(' '.join(map(str, result)))