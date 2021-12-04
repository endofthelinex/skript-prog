import hashlib
import os
import re


def file_to_string():
    with open("data/dictionary.txt", "r") as f:
        str_comb = str()
        for line in f:
            str_comb = str_comb + line
    return str_comb


def f01():
    # mindestens einen Vokal
    src = file_to_string()
    reg = r"\b\w*[aeiouAEIOU]\w*\b"
    res = re.findall(reg, src)

    None


def f02():
    # Ganzzahl
    src = file_to_string()
    reg = r"\d+"
    res = re.findall(reg, src)

    None


def f03():
    # Fließkommazahl
    src = file_to_string()
    reg = r"\d+.\d+"
    res = re.findall(reg, src)

    None


def f04():
    # vier aufeinanderfolgende Vokale
    src = file_to_string()
    reg = r"\w*[aeiouAEIOU]{4}\w*"
    res = re.findall(reg, src)

    None


def f05():
    # nur Buchstaben A bis F
    src = file_to_string()
    reg = r"\b[A-F]+\b"
    res = re.findall(reg, src)

    None


def f06():
    # 6 aufeinanderfolgende Konsonanten > klappt so noch nicht
    src = file_to_string()
    reg = r"\w*[b-df-hj-np-tv-z]{6}\w*"
    # reg = r"([b-df-hj-np-tv-z])\1{2,}"  # Online gefunden
    res = re.findall(reg, src)

    None


def f07():
    # RGB hex color code
    src = file_to_string()
    # reg = r"#\w{6}"  # FALSCH! Hex nur A-F und 0-9
    reg = r"#[a-fA-F0-9]{6}"
    res = re.findall(reg, src)

    None


def f08():
    # Palindrome aus 5 Buchstaben
    src = file_to_string()
    reg = r""
    res = re.findall(reg, src)

    None


def f09(year, month, day):
    # Bonusaufgabe: Prüfen auf valides Datum - 29. Februar soll z.B. nicht gehen
    year_ex = int(re.search(r"\d{4}", str(year)).group())
    month_ex = int(re.search(r"(0\d|1[0-2])", str(month)).group())
    day_ex = int(re.search("([0-2]\d|3[0-1])", str(day)).group())

    month_days = {
        1: 31,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    # Schaltjahr?
    feb_days = 28
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        feb_days = 29

    okay = True

    if month_ex != 2 and (day_ex > month_days[month_ex] or day_ex < 1):
        okay = False
    elif month_ex == 2 and (day_ex > feb_days or day_ex < 1):
        okay = False

    return okay


def f10(year, month, day):
    # Version f09 vom Prof

    isLeapYear = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    year = int(year)
    month = int(month)
    day = int(day)

    maxDays = {
        1: 31,
        2: 29 if isLeapYear else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if year >= 1800 and year <= 9999:
        if month >= 1 and month <= 12:
            if day >= 1 and day <= maxDays[month]:
                return True
    return False


def f11():
    # Vergleich von 2 Dateien, ob sie identisch sind über Hashes
    with open("data/dictionary.txt", "rb") as f:
        h1 = hashlib.sha1(f.read())
    with open("data/dictionary_copy.txt", "rb") as f:
        h2 = hashlib.sha1(f.read())
    h1 = h1.hexdigest()
    h2 = h2.hexdigest()
    if h1 == h2:
        print("identical")
    else:
        print("different")


def f12():
    # Suchen nach Duplikaten in Verzeichnis
    files = os.listdir("data/")
    filesize = dict()
    for f in files:
        filesize[f] = os.stat("data/" + f).st_size

    # Suchen nach identischen Dateigrößen
    rev_filesize = {}
    for key, value in filesize.items():
        rev_filesize.setdefault(value, set()).add(key)
    result = filter(lambda x: len(x) > 1, rev_filesize.values())
    # Alle Duplikate, nicht nur Grüppchen von gleich großen Dateien :(
    print(list(result))

    None

if __name__ == '__main__':
    # res1 = f10(2005, "3", 31)
    f12()
    None
