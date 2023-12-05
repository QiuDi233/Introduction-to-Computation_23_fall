def count_payment_methods(n):
    count = 0

    for num_1 in range(n+1):
        for num_2 in range(n+1):
            for num_5 in range(n+1):
                total = num_1 + 2*num_2 + 5*num_5
                if total == n:
                    count += 1
                elif total > n:
                    break

    return count

n = int(input())

result = count_payment_methods(n)
print(result)