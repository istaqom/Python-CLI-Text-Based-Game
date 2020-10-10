import os
import random
import cutie
from progress.bar import ShadyBar
import time

nameSuffixList = [
    "si Pemberani",
    "si Penakut",
    "si Monyet"
]

misiList = [
    "Beli Eskrim",
    "Bunuh Naga",
    "Belajar Ngoding"
]

tempatPrefixList = [
    "Kerajaan",
    "Hutan",
    "Desa",
    "Kota"
]

tempatList = [
    "Samarinda",
    "Hyrule",
    "Narnia"
]

pilihanMusuhPasif = [
    "Lawan",
    "Gunakan Item",
    "Lanjutkan Perjalanan"
]

musuhPasifList = [
    "Naga",
    "Ayam",
    "Kroco Bandit",
    "Kasir Indomaret",
    "Teller Bankaltim"
]

musuhPasifSuffix = [
    "Jahat",
    "Penakut",
    "Sedih",
    "Kuat",
    "Sekarat"
]

geludChoice = [
    "Serang",
    "Bertahan",
    "Tidur",
    "Skill",
    "Kabur"
]


class PS:
    playerName = ""
    nameSuffix = random.choice(nameSuffixList)
    misi = random.choice(misiList)
    jarakMisi = random.randint(1, 100)
    tempatPrefix = random.choice(tempatPrefixList)
    tempat = random.choice(tempatList)
    playerHP = 100
    playerCurHP = 100
    playerMP = 10
    playerCurMP = 10
    playerATK = 10
    playerDTMin = 30
    playerDTMax = 50

    @classmethod
    def updateNama(cls, update):
        PS.playerName = update

    @classmethod
    def updateCurDarah(cls, tipe, update):
        if tipe == "tambah":
            if PS.playerHP + update >= PS.playerHP:
                PS.playerCurHP = PS.playerHP
            else:
                PS.playerCurHP += update
        elif tipe == "kurang":
            if update < 0:
                update = 0
                PS.playerCurHP -= update
            else:
                PS.playerCurHP -= update

    @classmethod
    def updateCurMP(cls, tipe, update):
        if tipe == "tambah":
            if PS.playerMP + update >= PS.playerMP:
                PS.playerCurMP = PS.playerMP
            else:
                PS.playerCurMP += update
        elif tipe == "kurang":
            if update < 0:
                update = 0
                PS.playerCurMP -= update
            else:
                PS.playerCurMP -= update


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def playIntro():
    playerName = input("Masukkan Nama : ")
    PS.updateNama(playerName)
    clear()
    print("======================================================"
          f"\nNama Player : {playerName + ' ' + PS.nameSuffix}"
          f"\nMisi : {PS.misi} di {PS.tempatPrefix} {PS.tempat}"
          f"\nJarak : {PS.jarakMisi} KM"
          "\n======================================================"
          "\nStatus Player"
          f"\nHP : {PS.playerHP} | MP : {PS.playerMP} | Serangan : {PS.playerATK}"
          "\n======================================================")
    if cutie.prompt_yes_or_no("Apakah kau sudah siap?",
                              yes_text="Sudah",
                              no_text="Belum",
                              has_to_match_case=False,
                              enter_empty_confirms=False,
                              char_prompt=False
                              ):
        with ShadyBar('Perjalanan', max=PS.jarakMisi) as bar:
            for i in range(PS.jarakMisi):
                time.sleep(1)
                randEnt = random.randint(1, 10)
                if randEnt == 1:
                    ketemuMusuhPasif()
                bar.next()
    else:
        print("Huh, Kukira kau pemberani")
        exit()

def ketemuMusuhPasif():
    clear()
    musuh = random.choice(musuhPasifList)
    suffixMusuh = random.choice(musuhPasifSuffix)
    musuhHP = random.randint(1, 200)
    musuhATK = random.randint(1, 100)

    if suffixMusuh == "Jahat":
        musuhATK *= 1.25
    elif suffixMusuh == "Kuat":
        musuhHP *= 1.5
        musuhATK *= 1.5
    elif suffixMusuh == "Sedih":
        musuhHP *= 0.85
        musuhATK *= 0.85
    elif suffixMusuh == "Sekarat":
        musuhHP *= 0.01
        musuhATK *= 0
    elif suffixMusuh == "Penakut":
        musuhATK *= 0.5

    print(f"Kau bertemu {musuh} {suffixMusuh}")
    print("======================================================"
          f"\n{musuh} {suffixMusuh} | HP = {musuhHP} | ATK = {musuhATK}"
          f"\n{PS.playerName} {PS.nameSuffix} | HP = {PS.playerCurHP} | MP = {PS.playerCurMP}"
          "\n======================================================")
    pilihan = pilihanMusuhPasif[cutie.select(pilihanMusuhPasif)]

    if pilihan == "Lawan":
        while musuhHP >= 0 and PS.playerCurHP >= 0:
            clear()
            print("======================================================"
                  f"\n{musuh} {suffixMusuh} | HP = {musuhHP} | ATK = {musuhATK}"
                  f"\n{PS.playerName} {PS.nameSuffix} | HP = {PS.playerCurHP} | MP = {PS.playerCurMP}"
                  "\n======================================================")
            pilihan = geludChoice[cutie.select(geludChoice)]

            if pilihan == "Serang":
                hitChance = random.randint(1, 10)

                if hitChance == 1:
                    print("Sial! Kamu Lepas")

                else:
                    musuhHP -= PS.playerATK

                if hitChance == 10:
                    print("Musuhnya Lepas")

                else:
                    PS.updateCurDarah("kurang", musuhATK)

            elif pilihan == "Bertahan":
                hitChance = random.randint(1, 10)

                if hitChance == 10:
                    print("Musuhnya Lepas")

                else:
                    shield = 0

                    if shield:
                        print()

                    else:
                        reductionATK = musuhATK - random.randint(PS.playerDTMin, PS.playerDTMax)
                        PS.updateCurDarah("kurang", reductionATK)

            elif pilihan == "Tidur":
                hitChance = random.randint(1, 10)
                healHP = (PS.playerHP * 10) / 100
                healMP = (PS.playerMP * 75) / 100
                PS.updateCurDarah("tambah", healHP)
                PS.updateCurMP("tambah", healMP)

                if hitChance == 10:
                    print("Musuhnya Lepas")

                else:
                    PS.updateCurDarah("kurang", musuhATK)

            elif pilihan == "Skill":
                print("Skill")

            elif pilihan == "Kabur":
                hitChance = random.randint(1, 10)
                kaburChance = random.randint(1, 20)

                if kaburChance == 1:
                    musuhHP -= musuhHP - 4869

                if hitChance == 10:
                    print("Kamu Berhasil Menghindari Serangan")

                else:
                    PS.updateCurDarah("kurang", musuhATK)

        if musuhHP < 0 < PS.playerCurHP:
            clear()
            print(f"Kamu mengalahkan {musuh} {suffixMusuh}")

        elif musuhHP < -4869 and PS.playerCurHP > 0:
            clear()
            print("Kamu Berhasil Kabur")

        else:
            clear()
            print("Kamu mati")
            exit()

    elif pilihan == "Gunakan Item":
        print("Item")

    elif pilihan == "Lanjutkan Perjalanan":
        print("Lanjut")


clear()
playIntro()