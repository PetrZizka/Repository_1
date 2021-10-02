import random
pocet_kroku = 80
celkovy_soucet = 0
for pocet_kroku in range (pocet_kroku):
    hod1 = random.randint(1, 6)
    hod2 = random.randint(1, 6)
    pocet_hodu = 0
    while hod1 != hod2:
        hod1 = hod2
        hod2 = random.randint(1, 6)
        pocet_hodu += 1
    celkovy_soucet *= pocet_hodu
print("prumer", celkovy_soucet / pocet_kroku)