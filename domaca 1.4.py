from PIL import image

fr= open("ciernobiely_obrazok_1.txt', 'r', encoding="UTF-8")
fw= open("ciernobiely_obrazok_1._vystup.txt', 'w', encoding="UTF-8")

def spracuj_riadok(vstup):
    vystup = ''   #prazdne, aby sme mohli neskor vpisovat
    for i in range(0, len(vstup) - 1, 2):
        odtien = vstup[i:i+2]
        if odtien > '7f':      # zisťujeme, či je to odtieň sivej
            vystup += '1 '
        else:                  # ak nie je, tak je tmavý
            vystup += '0 '
    vystup = vystup.strip() + '\n'  # odstranujeme neviditelne znaky
    return vystup

prvy_riadok = vstupny_subor.readline()
vystupny_subor.write(prvy_riadok)

casti = prvy_riadok.split()
sirka = int(casti[0])
vyska = int(casti[1])

for riadok in vstupny_subor:
    novy_riadok = spracuj_riadok(riadok.strip())  # zas odstrani neviditelne znaky
    vystupny_subor.write(novy_riadok)
