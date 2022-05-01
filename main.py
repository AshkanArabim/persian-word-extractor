from unittest import result
import requests

def noAccent(src):
    src = src.replace('ك','ک')
    for x in src:
        if x not in {'ا','ب','پ','ت','ث','ج','چ','ح','خ','د','ذ','ر','ز','ژ','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ک','گ','ل','م','ن','و','ه','ی','آ','أ','إ','ؤ','ئ','ء','ٌ','ٍ','ً','ُ','ِ','َ','ّ',' '}:
            src = src.replace(x,' ')

    splitted = src.split()
    wordset = set(splitted)
    rm = []
    for x in wordset:
        if len(x) == 1 :
            rm.append(x)
        for z in ['ْ','ٌ','ٍ','ً','ُ','ِ','َ','ّ']:
            if z in x:
                rm.append(x)
    rm = set(rm)
    for x in rm:
        wordset.remove(x)

    out = []
    for x in wordset:
        out.append((x,splitted.count(x)))

    def num(e):
        return e[1]
    out.sort(reverse= True ,key= num)

    output = ''

    n = 0
    for x in out:
        output += (str(list(out)[n][0]) + "\n")
        n += 1
    
    return output

def withAccent(src):
    src = src.replace('ك','ک')
    for x in src:
        if x not in {'ا','ب','پ','ت','ث','ج','چ','ح','خ','د','ذ','ر','ز','ژ','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ک','گ','ل','م','ن','و','ه','ی','آ','أ','إ','ؤ','ئ','ء','ْ','ٌ','ٍ','ً','ُ','ِ','ّ','ّ','‌',' '}:
            src = src.replace(x,' ')

    splitted = src.split()
    wordset = set(splitted)
    rm = []
    for x in wordset:
        if len(x) == 1 :
            rm.append(x)
    rm = set(rm)
    for x in rm:
        wordset.remove(x)

    out = []
    for x in wordset:
        out.append((x,splitted.count(x)))

    def num(e):
        return e[1]
    out.sort(reverse= True ,key= num)

    output = ''

    n = 0
    for x in out:
        output += (str(list(out)[n][0]) + "\n")
        n += 1

    return output

def htmlFinder():
    url = ['https://fa.wikipedia.org/wiki/%D8%A7%DB%8C%D8%B1%D8%A7%D9%86', 'https://fa.wikipedia.org/wiki/%D8%AC%D9%85%D9%87%D9%88%D8%B1%DB%8C_%D8%A2%D8%B0%D8%B1%D8%A8%D8%A7%DB%8C%D8%AC%D8%A7%D9%86']
    open('source.txt','w').close()
    for link in url:
        content = requests.get(link).content
        with open("source.txt", 'wb') as f:
            f.write(content)
def txtSrc():
    return open('source.txt' , encoding='UTF-8').read()

results = open('output.txt','w', encoding='UTF-8')

def asker():
    accentAnswer = input('Include accents? (y/n) ')
    if accentAnswer == 'y':
        srcAnswer = input('Choose location type: \n  online (random wikipedia link) \n  offline (source.txt file in root directory) ')
        if srcAnswer == 'online':
            htmlFinder()
            results.write(withAccent(txtSrc()))
        elif srcAnswer == 'offline':
            results.write(withAccent(txtSrc()))
        else:
            print('That is not a valid option. Abort.')
            exit()
    elif accentAnswer == 'n':
        srcAnswer = input('Choose location type: \n  online (random wikipedia link) \n  offline (source.txt file in root directory) ')
        if srcAnswer == 'online':
            htmlFinder()
            results.write(noAccent(txtSrc()))
        elif srcAnswer == 'offline':
            results.write(noAccent(txtSrc()))
        else:
            print('That is not a valid option. Abort.')
            exit()
    else:
        print('Than is not a valid option. Abort.')
        exit()

    print('Words extracted successfully. Check output.txt')

asker()