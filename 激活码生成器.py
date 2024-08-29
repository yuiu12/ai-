import random 
def gen(x):
    if x <= 0.4:
        return random.choice(
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'A', 'Z', 'X',
             'C', 'V', 'B', 'N', 'M'])
    elif x <= 0.8:
        return random.choice(
           ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z', 'x',
             'c', 'v', 'b', 'n', 'm']) 
    else:
        return random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
def gen1():
    a = [''] * 19 
    for i in range(19):
        x = random.random() 
        if (i + 1) % 5 != 0:
            a[i] = gen(x) 
        else:
            a[i] = '-' 
    return a 
for _ in range(200):
    print(''.join(gen1()))
    











































