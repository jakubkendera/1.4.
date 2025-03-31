def spracuj_riadok(riadok):
    vystup = []
    for i in range(0, len(riadok), 2):
        hex_hodnota = riadok[i:i+2]
        des_hodnota = int(hex_hodnota, 16)
        if des_hodnota < 128:
            vystup.append("0")
        else:
            vystup.append("1")
    return " ".join(vystup)

with open("ciernobiely_obrazok_1.txt", "r", encoding="UTF-8") as fr, \
     open("konverzia_suboru_1_vystup.txt", "w", encoding="UTF-8") as fw:

    prvy_riadok = fr.readline().strip()
    fw.write(prvy_riadok + "\n")

    for riadok in fr:
        riadok = riadok.strip()
        binarna_riadok = spracuj_riadok(riadok)
        fw.write(binarna_riadok + "\n")
