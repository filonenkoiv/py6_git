def spam(number):
    number = int(input("Number: "))
    return 'bulochka' * number


def my_sum(list_of_numbers):

    pass
    list_one = [10, 2, 0]
    list_two = [10, 20, 100, 14]
    list_three = [-50, 200, -100, -50, 12]

    return list_one[0] + list_one[1] + list_one[2]
    return list_two[0] + list_two[1] + list_two[2] + list_two[3]
    return list_three[0] + list_three[1] + list_three[2] + list_three[3] + list_three[4]

def shortener(string):

    pass
    st = string.split()
    return " ".join(list(map(lambda stri: stri if len(stri) < 6 else stri[:6] + '*', st)))


def compare_ends(words):

    pass
    count = 0
    for s in words:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count
