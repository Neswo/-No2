import random, string, os
os.system('color B')
os.system('cls')

nbr = int(input('Nombre de codes: '))
os.system('cls')
os.system('color 9')

f = open('codes.txt', "a+")
f.write(f'|| Nitro codes generated with -No2 by Neswo > https://github.com/Neswo/-No2 < ||\n')
f.close()

truc = 1
while truc <= nbr:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print("\n\n║ -No2 | Nitro Generator | by Neswo")
    print('║ Généré ->',code,'(',truc,' codes','sur',nbr,')','| Progression:',100*truc//nbr,"%")
    truc += 1
else:
    os.system('cls')
    os.system('color A')
    print("║ -No2 | Nitro Generator | by Neswo")
    print('║',nbr,'codes ont été générés avec succès !\n')
    os.system('pause')
    os.system('color 07')
    os.system('cls')