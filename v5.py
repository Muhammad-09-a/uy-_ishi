def fill_list(n):
    lst = []
    for i in range(n):
        element = input(f"{i+1} elementni kiriting: ") 
        lst.append(element)
    return lst
def output(lst):
    if len(lst) == 1:
        return 2
    else:
        return len(lst) * 2 + (len(lst) - 1)

n = int(input("Nechta element kiritmoqchisiz? "))
print(output(fill_list(n)))
