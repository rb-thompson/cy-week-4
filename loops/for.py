import random

# FOR LOOPS

nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 2:
        continue

    if num == 3:
        print('Target found.')
        break

    # print(num)

# LOOPS ALL THE WAY DOWN

BUS_ID = '7005'
u_key = '0000'

# for num in nums:
#     for letter in 'xyz':
#         multiple = (num + 2) * 42
#         print(f"{BUS_ID}{num}{letter}{multiple}{u_key}")


rates = [1, 5, 10, 20, 50, 100]
count = 0
total = 0

for i in range(15):
    for letter in 'xyz':
        for num in nums:
            count += 1
            multiple = (num + 2) * 42
            luck = random.choice(rates)
            bonus = 1000 * (luck / 1)
            total += bonus
#             print(f"CUSTOMER({BUS_ID}{num}{letter}{multiple}{u_key})Your bonus is ${bonus} - {luck}% bonus rate.")

# print(f"Found {count} customer bonuses.")
print(f"Total payout: ${total}")

def count_occurrences(items, target):
    count = 0
    for i in items:
        if i == target:
            count += 1
    print(count)

count_occurrences(['apple', 'banana', 'apple'], 'apple')