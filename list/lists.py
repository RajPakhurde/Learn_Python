# names = ['Mosh', 'Bob', 'John', 'Harry']
# print(names[0])

# # Find max element in list

# numbers = [23, 55, 66, 21, 48, 90]
# target = 21
# # linear search
# # for i in range(len(numbers)):
# #     if numbers[i] == target:
# #         print(f"{numbers[i]} found")
# #         break
# # else:
# #     print("Not found")

# # bineary search
# start = 0
# end = len(numbers)
# while start <= end:
#     mid = int(start + (end - start) / 2)
#     if numbers[mid] == target:
#         print(f"{numbers[mid]} found")
#         break
#     elif target < numbers[mid]:
#         end = mid - 1
#     else:
#         start = mid + 1
# else:
#     print("Number not found")

# # 2D list in python

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[0][2])

# for row in matrix:
#     for item in row:
#         print(item)

# # Operations on list
# # copy list as it is if we change numbers list than it will not affect list2
# list2 = numbers.copy()
# print(list2)
# numbers.append(100)  # add 100 at end of list
# print(numbers)
# numbers.insert(0, 100)  # add 100 at 0th index
# print(numbers)
# print(numbers.count(100))  # return how much 100 is there in list out:-2
# numbers.pop()  # remove last element from list
# print(numbers)
# numbers.sort()  # sort list in assecnding order [21,23,48,55,...]
# numbers.reverse()  # reverse list in [..,55,48,23,21]
# print(numbers)
# print(list2)

# Write a program to remove duplicate numbers from list.

# num_list = [1, 4, 5, 2, 3, 2]
# dublicate_num = -1
# i = 0
# j = 0
# while i < len(num_list):
#     dub = num_list.count(num_list[i])
#     if dub != 1:
#         dublicate_num = num_list[i]
#         while j < dub:
#             num_list.remove(dublicate_num)
#             j += 1
#     i += 1

# print(num_list)

# Ans:-
numbers_list = [2, 3, 4, 6, 7, 2, 3, 6]
uniques = []

for number in numbers_list:
    if number not in uniques:
        uniques.append(number)

print(uniques)
