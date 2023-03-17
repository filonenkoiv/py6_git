def spam(number):
    return 'bulochka' * number


def my_sum(list_of_numbers):

    pass
    sum = 0
    for num in list_of_numbers:
        sum += num
    return sum

def shortener(string):

    pass
    return " ".join(list(map(lambda stri: stri if len(stri) < 6 else stri[:6] + '*', string.split())))


def compare_ends(words):

    pass
    count = 0
    for s in words:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count
