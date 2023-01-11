names = ['Mosh', 'Bob', 'John', 'Harry']
print(names[0])

# Find max element in list

numbers = [23, 55, 66, 21, 48, 90]
target = 21
# linear search
# for i in range(len(numbers)):
#     if numbers[i] == target:
#         print(f"{numbers[i]} found")
#         break
# else:
#     print("Not found")

# bineary search
start = 0
end = len(numbers)
while start <= end:
    mid = int(start + (end - start) / 2)
    if numbers[mid] == target:
        print(f"{numbers[mid]} found")
        break
    elif target < numbers[mid]:
        end = mid - 1
    else:
        start = mid + 1
else:
    print("Number not found")
