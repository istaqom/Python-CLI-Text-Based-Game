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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class PS:
    playerName = nameSuffix = misi = jarakMisi = tempatPrefix = tempat = str()
    playerHP = playerCurHP = playerMP = playerCurMP = playerATK = playerDTMin = playerDTMax = int()

    @classmethod
    def updatePlayer(cls, nama, suffix, misi, tempatPrefix, tempat, jarak):
        PS.playerName = nama
        PS.nameSuffix = suffix
        PS.misi = misi
        PS.tempatPrefix = tempatPrefix
        PS.tempat = tempat
        PS.jarakMisi = jarak

class ES:
    musuh = musuhSuffix = str()
    musuhATK = musuhHP = int()

def player():
    namaPlayer = str(input("Masukkan Nama : "))
    suffixPlayer = random.choice(nameSuffixList)
    misi = random.choice(misiList)
    tempatPrefix = random.choice(tempatPrefixList)
    tempat = random.choice(tempatList)
    jarak = random.randint(10, 150)
    PS.updatePlayer(namaPlayer, suffixPlayer, misi, tempatPrefix, tempat, jarak)

def main():
    player()
    print(f"Nama : {PS.playerName} {PS.nameSuffix}"
          f"\nMisi : {PS.misi} di {PS.tempatPrefix} {PS.tempat} | Jarak : {PS.jarakMisi} KM")

main()
