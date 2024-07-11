def fill_list(n):
    lst1 = []
    for i in range(n):
        lst1.append(int(input(f"{i+1} inchi element: "))) 
    return lst1

def sorting(numbers):
    result = []
    for i in range(len(numbers) - 1):
        if (numbers[i] > 0 and numbers[i + 1] > 0) or (numbers[i] < 0 and numbers[i + 1] < 0):
            result.append((numbers[i], numbers[i + 1]))
    return result
n = int(input("n = "))
for j in sorting(fill_list(n)):
    print(j)