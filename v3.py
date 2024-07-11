bonus = {}
with open("demo.txt", "r") as f:
    for line in f:
        if line.strip(): 
            qismlar = line.split()
            bonus_qiymati = int(qismlar[3])
            bolim = qismlar[4]

            if bolim not in bonus:
                bonus[bolim] = 0
            bonus[bolim] += bonus_qiymati

print(max(bonus, key=bonus.get)) 
