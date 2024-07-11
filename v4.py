def fill_list(n):
    lst = []
    for i in range(n):
        lst.append(int(input(f"{i+1} inchi element: "))) 
    return lst

def sorting(lst):
    lst.sort(key=lambda x: sum(map(int, str(x))))
    return lst
n = int(input("Nechtalik kiritmoqchisiz: "))
print(sorting(fill_list(n)))
