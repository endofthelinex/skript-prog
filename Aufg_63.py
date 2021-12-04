import random as rnd

def f01():
    """ Seite 11 Kluges Mischen """
    rnd.seed(0)
    l1 = create_list_rand_4()
    l2 = create_list_rand_4()
    sort_list(l1)
    sort_list(l2)
    lst_result = combine_sort_list(l1, l2)
    print(lst_result)


def create_list_rand_4():  # vorher rand_16
    lst = list()
    for i in range(4):
        lst.append(rnd.randrange(10,100))
    return lst


def sort_list(lst):
    bereitsSortiert = 0
    tausch = True
    while tausch:
        tausch = False
        for i in range(len(lst) - 1 - bereitsSortiert):  # -1, da Zugriffe auf i+1 erfolgen, sonst Indexfehler!
            if lst[i] > lst[i + 1]:
                (lst[i], lst[i + 1]) = (lst[i + 1], lst[i])
                tausch = True
        bereitsSortiert += 1


def combine_sort_list(l1, l2):
    lst = list()
    while (len(l1) > 0) and (len(l2) > 0):
        if l1[0] <= l2[0]:
            lst.append(l1.pop(0))
        elif l1[0] > l2[0]:
            lst.append(l2.pop(0))
    if len(l1) > 0:
        lst.extend(l1)
        l1.clear()
    elif len(l2) > 0:
        lst.extend(l2)
        l2.clear()
    return lst


def split(lst):
    """ S. 12, Kluges Teilen """
    if len(lst) == 1:
        return lst
    half = len(lst) // 2  # Ganzzahldivision
    lst1 = lst[:half]
    lst2 = lst[half:]
    return lst1, lst2


def split_and_merge(lst):
    """ S. 13, Split and merge """
    if len(lst) <= 1:
        return lst
    half = len(lst) // 2  # Ganzzahldivision
    split1 = lst[:half]
    split2 = lst[half:]
    lst1 = split_and_merge(split1)
    lst2 = split_and_merge(split2)

    lst_res = combine_sort_list(lst1, lst2)

    return lst_res


if __name__ == '__main__':
    # split(create_list_rand_16())
    # f01()
    res = split_and_merge(create_list_rand_4())
    print(res)


