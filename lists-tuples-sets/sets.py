# sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses)   # does not care about order

# find common items in two sets
print(cs_courses.intersection(art_courses))

# find differences in two sets
print(cs_courses.difference(art_courses))

# join two sets
print(cs_courses.union(art_courses))