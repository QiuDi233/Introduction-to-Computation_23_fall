
numbers_str = input()  
  
numbers_list = list(map(int, numbers_str.split()))  
  
unique_numbers = sorted(list(set(numbers_list)))  

for num in unique_numbers:  
    print(num, end=' ')