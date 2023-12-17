from collections import Counter

def c_frequency(s, stop_chars):
    filtered_s = ''.join(char for char in s if char not in stop_chars)
    char_counts = Counter(filtered_s)
    sorted_counts = sorted(char_counts.items(), key=lambda x: (-x[1], x[0]))
    
    for char, frequency in sorted_counts:
        print(f"{char} {frequency}")

s = input()
t = input()

c_frequency(s, t)