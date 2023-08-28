import json

class Saldytuvas:
    def __init__(self) -> None:
        self.atidaryti()


    #3 Istraukti 
    def istraukti_produkta(self):
        istraukimas_produktas = input("pasirinkite produkta: ")
        if not istraukimas_produktas in self.saldytuvas.keys():
            print("produkto nera")
        else:
            istraukimas_kiekis = float(input("pasirinkite kieki: "))
            if self.saldytuvas[istraukimas_produktas] < istraukimas_kiekis:
                print("tiek daug produkto nera")
            if self.saldytuvas[istraukimas_produktas] >= istraukimas_kiekis:
                self.saldytuvas[istraukimas_produktas] -= istraukimas_kiekis
            if self.saldytuvas[istraukimas_produktas] == 0:
                self.saldytuvas.pop(istraukimas_produktas)
        return istraukimas_produktas

    #1 Prideti nauja ir papildyti sena
    def papildyti(self):
        produktas = input('Įveskite produktą kurį norite papildyti arba prideti: ')
        kiekis = float(input('Įveskite produkto kiekį: '))
        if produktas in self.saldytuvas:
            self.saldytuvas[produktas] += kiekis
        else:
            self.saldytuvas[produktas] = kiekis

    #2 Svoris -- Ruslanas
    def skaiciuoti_turinio_svori(self):
        return sum(self.saldytuvas.values())
        
    #6 Receptas
    def ar_iseina(self):
        ivedimas = input("Iveskite recepta: ")
        ingridientu_sarasas = ivedimas.split(",")
        uztenka = []
        for ingredientas in ingridientu_sarasas:
            ingredientas, kiekis = ingredientas.split(":")
            ingredientas = ingredientas.strip()
            kiekis = float(kiekis)
            if ingredientas in self.saldytuvas:
                if self.saldytuvas[ingredientas] - kiekis < 0:
                    neuzteknka_kiekis = (self.saldytuvas[ingredientas] - kiekis) * (-1)
                    print(f"{ingredientas} truksta: {neuzteknka_kiekis}")
                    uztenka.append(False)
                else:
                    uztenka.append(self.saldytuvas[ingredientas] / kiekis)
            else:
                uztenka.append(False)
        if False in uztenka:
            return print("neimanoma pagaminti")
        else:
            print(f"uztenka {min(uztenka)} porcijoms")
            return min(uztenka)

    #4 Turinys 
    def turinys(self):
        turi = "Šaldytuve yra:\n"  
        for daiktas, kiekis in self.saldytuvas.items():
            turi += "{} : {}\n".format(daiktas, kiekis)
        return turi  

    #5 Ieskoti
    def ieskoti_produktu(self):
        produktai = input('produkto paieška: ')
        if produktai in self.saldytuvas:
            grizo = print(f'{produktai} yra: {self.saldytuvas[produktai]}')
        else:
            print('produkto nera saldytuve')
        return grizo

    def atidaryti(self):
        with open("saldytuvo_turinys.json", "r", encoding="utf-8") as saldytuvo_turinys:
            self.saldytuvas = json.load(saldytuvo_turinys)    

    def uzdaryti(self):
        with open("saldytuvo_turinys.json", "w", encoding="utf-8") as saldytuvo_turinys:
            json.dump(self.saldytuvas, saldytuvo_turinys, ensure_ascii=False)
    

saldytuvas = Saldytuvas()

while True:
    pasirinkimas = input("0 - išeiti iš šaldytuvo\n1 - Prideti nauja ir papildyti produktus\n2 - Skaiciuoti saldytuvo svori\n3 - ištraukti produktą\n4 - peržiūrėti produktus\n5 - ieškoti produktų\n6 - Receptas\npasirinkite:")
    if pasirinkimas == "0":
        saldytuvas.uzdaryti()
        print("Uzdarete saldytuva!")
        break
    elif pasirinkimas == "1":
        saldytuvas.papildyti()

    elif pasirinkimas == "2":
        print(f"Šaldytuvo svoris: {saldytuvas.skaiciuoti_turinio_svori()}...")
        print("\n")

    elif pasirinkimas == "3":
        print(f"Istrauktas produktas: {saldytuvas.istraukti_produkta()}")

    elif pasirinkimas == "4":
        print(saldytuvas.turinys())
        
    elif pasirinkimas == "5":
        saldytuvas.ieskoti_produktu()
        
    elif pasirinkimas == "6":
        saldytuvas.ar_iseina()
        

