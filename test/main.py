from functools import reduce

def queue_time(customers, n):
    # TODO
    customers.sort(reverse=True)
    print(customers)
    tills=list(0 for i in range(n))
    for customer in customers:
        minTime = tills[0]+customer
        index = 0
        print(minTime)
        for till in range(1,n):
            if tills[till]+customer < minTime:
                minTime = tills[till]+customer
                index = till
        tills[index] += customer
        print(tills)

    return max(tills)


def digital_root(n):
    while n >= 10:
        n = reduce(lambda x,y:int(x)+int(y), list(str(n)))
    return n

def MORSE_CODE(x):
    '''
    function:返回对应的摩斯码
    '''
    dic = {'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.',
           'G': '__.', 'H': '....', 'I': '..', 'J': '.___', 'K': '_._', 'L': '._..',
           'M': '__', 'N': '_.', 'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.',
           'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._',
           'Y': '_.__', 'Z': '__..',
           '1': '.____', '2': '..___', '3': '...__', '4': '...._', '5': '.....',
           '6': '_....', '7': '__...', '8': '___..', '9': '____.', '0': '_____',
           ' ': ' '}
    if x in dic:
        return dic[x]


# from preloaded import MORSE_CODE
#
# def decode_morse(morse_code):
#     # Remember - you can use the preloaded MORSE_CODE dictionary:
#     # For example:
#     # MORSE_CODE['.-'] = 'A'
#     # MORSE_CODE['--...'] = '7'
#     # MORSE_CODE['...-..-'] = '$'
#     #print(morse_code)
#     words=morse_code.strip().split('   ')
#     #print(words)
#     str=''
#     for word in words:
#         letters=word.split()
#         #print(letters)
#         for letter in letters:
#             str+=MORSE_CODE[letter]
#         str+=' '
#     return str[:-1]
#     pass

def expanded_form(num):
    bits = list(str(num))
    bits.reverse()
    print(bits)
    for i in range(len(bits)):
        print(i)
        print(bits[i])
        if bits[i] != '0':
            bits[i]=str(int(bits[i])*10**i)
        else:
            bits.pop(i)
    bits.reverse()
    return ' + '.join(bits)
    pass

if __name__ == '__main__':
    # print(queue_time([3, 13, 34, 21, 23, 24, 41, 47, 38, 40, 38, 3, 40, 21, 43, 38, 28, 8, 5, 38], 3))
    # print(digital_root(132189))
    # print(decode_morse('._'))
    print(expanded_form(70304))