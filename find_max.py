numbers = [-1, -4, -6]

def find_max(numbers):
    max = numbers[0]
    for num in numbers[1:]:
        if num > max:
            max = num
    return max

print(find_max(numbers))