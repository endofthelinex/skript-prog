# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


def test01():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(lst[0:9])


def test02():
    d = {"k1":3, "k2":4, "k3":5, "k4":6}
    d["k5"] = 7
    print(d)
    print(d.pop("k2"))
    print(d.popitem())
    print(d)
    print(d.keys())
    print(d.values())
    print(d.items())
    print(d.get("k4", None))
    print(d.get("k5", None), ",", type(None))

def test03():
    anz = 3
    for i in anz: # Geht nicht!
        print("test")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    test03()

