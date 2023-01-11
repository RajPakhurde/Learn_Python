while start <= end:
    mid = int(start + (end - start) / 2)
    if numbers[mid] == target:
        print(f"{numbers[i]} found")
    elif numbers[mid] < target:
        end = mid - 1
    else:
        start = mid + 1
else:
    print("Number not found")