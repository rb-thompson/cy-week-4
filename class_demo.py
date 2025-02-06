# loops and lists

print("The zoo list contains: ")

zoo = ["Chimpanzee", "Crocodile", "Elephant", "King Cobra", "Gorilla", "Tiger", "Toucan"]

# for animal in zoo:
#     print(animal)


# while True:
#     print("-" * 80)
#     user_choice = input("Which index would you like to view? (Or input 'End' to end program)")

#     if user_choice == "End":
#         print("Ending...")
#         break

#     print(f"Index {user_choice} contains {zoo[int(user_choice)]}")

count = 0
for i in zoo:
    print(f"Index: {count}, Animal: {i}")
    count += 1

