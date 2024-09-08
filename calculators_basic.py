#Calculator basic
def cal_sth (input_string):
        
    a = float(input_string[0])
    b = float(input_string[2])
    anw = 0

    if '+' in input_string:
        anw = a + b
    elif '-' in input_string:
        anw = a - b
    elif'x' in input_string:
        anw = a * b
    elif '/' in input_string:
        anw = a/b
    if anw % 10 == 0:
        return print(int(anw))
    else:   
        return print(anw)

print('Write like this: a _ b = ')
input_string = list(input('a _ b = \n').split(' '))
cal_sth(input_string)
