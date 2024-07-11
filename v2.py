def fill_dict(n):
    dict1 = {}
    for i in range(n):
        key = input("Key = ")
        value = int(input("Value = (0 yoki 1 kiritng): "))
        dict1[key] = value
    return dict1
def sorting(dict1):
    count = []
    count2 = []
    for key,val in enumerate(dict1):
        if dict1[val] == 1:
            count.append(val)
        elif dict1[val] == 0:
            count2.append(val)
    if len(count) > len(count2):
        print(f"1 \n {count}")
    elif len(count2) > len(count):
        print(f"0 \n {str(count2)}")
    else :
        print(f"0 \n {count2}\n 1 \n {count}")

n = int(input("n = "))
# dict1 = {"Anvar":0, "Lobar" : 1, "Asror" : 0}
sorting(fill_dict(n))