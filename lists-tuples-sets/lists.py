print("Hello, world! 👨‍🍳")

# LISTS

dinner = ['salad', 'steak', 'baked sweet potato', 'rolls', 'greek yogurt', 'berries']

print(dinner)
# print(len(dinner))
# print(dinner[0])   # first item
# print(dinner[3])   # last item
# print(dinner[-1])  # last item
# print(dinner[4])   # list index out of range
# print(dinner[0:2]) # first index inclusive; second is not
# print(dinner[:2])  # same result as above

# list methods

# dinner.append('jalepeno poppers')             # add an item
# dinner.insert(0, 'street corn on the cob')    # add an item by index location

# dinner_2 = ['shrimp kabobs', 'olives']        # new list of dinner items

# dinner.extend(dinner_2)                       # combine lists
# print(dinner)

# dinner.remove('jalepeno poppers')             # remove an item
# popped = dinner.pop()                         # remove the last item (returns a value)

# print(popped)                                 # return popped value

# sorted_dinner = sorted(dinner)                # sort list alphabetically
# print(sorted_dinner)                          

# print(dinner.index('steak'))                  # return an item index

# for item in enumerate(dinner, start=1):       # enumerate items in a list
#         print(item)

# course_str = ' - '.join(dinner)               # convert list to a string
# print(course_str)

# new_list = course_str.split(' - ')            # convert back into a list
# print(new_list)



# nums = [6, 2, 8, 6, 9]      # list of numbers

# nums.sort()
# print(nums)

# nums.sort(reverse=True)     # sort (descending)
# print(nums)

# print(min(nums))            # min
# print(max(nums))            # max
# print(sum(nums))            # sum