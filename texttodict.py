import pyperclip

f = open('prompts.txt', encoding='utf8')
g = []
n = 1
m = 0
situations = '['
for line in f.readlines():
    line = line[:-1]
    if n == 1:
        prompt = line
    elif n == 2:
        questiona = line
    elif n == 3:
        questionb = line
    elif n == 4:
        questionc = line
    elif n == 5:
        anwsera = line
    elif n == 6:
        anwserb = line
    elif n == 7:
        anwserc = line

    
    if n == 8:
        tempstring1 = '{prompt: \'' + prompt + '\', choice : [\'' + questiona + '\',\'' + questionb + '\',\'' + questionc + '\'], feedback : [\'' + anwsera + '\',\'' + anwserb + '\',\'' + anwserc + '\']}'
        prompt = line
    elif n == 9:
        questiona = line
    elif n == 10:
        questionb = line
    elif n == 11:
        questionc = line
    elif n == 12:
        anwsera = line
    elif n == 13:
        anwserb = line
    elif n == 14:
        anwserc = line
    
    n +=1
    
    if n ==15:
        tempstring2 = '{prompt: \'' + prompt + '\', choice : [\'' + questiona + '\',\'' + questionb + '\',\'' + questionc + '\'], feedback : [\'' + anwsera + '\',\'' + anwserb + '\',\'' + anwserc + '\']}'
        situations += '[' + tempstring1 + ',' + tempstring2 + '], \n'
        m +=1
        n = 1

pyperclip.copy(situations)
spam = pyperclip.paste()