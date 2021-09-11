courses = ['History', 'Math', 'Physics', 'Computer']
# print(courses)
# print(courses[2:])
courses.append('Art')
courses.insert(0, 'programing')
courses_2 = ['AI', 'Sci']
# courses.insert(0, courses_2)
courses.extend(courses_2)
# print(courses)
# popped = courses.pop()
# print(popped)

#sorting

num = [1,2,3,4,5]
num.sort(reverse=True)
# courses.reverse()
courses.sort()
# print(courses)
#
# sorted_num = sorted(num)
# print(sorted_num)
#
# for index, course in enumerate(courses): # enumerate returns 2 values index they are on it an the value
#     print(index, course)
#
# for index, course in enumerate(courses, start=1): # enumerate returns 2 values index they are on it an the value
#     print(index, course)
#
# course_str = ', '.join(courses)
# print(course_str)
#
# course_str = '- '.join(courses)
# print(course_str)
#
# new_list = course_str.split('- ')
# print(new_list)


"""
sets
"""


cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))