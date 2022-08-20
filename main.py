from time import time
from click import prompt
import requests
import re
import requests


print('-----------\nPersian Word Extractor v0.5\n-----------')

def amountExtracted():
    output = open('output.txt', 'r')
    length = len(set(output.read().split()))
    return (str(length) + ' words extracted')

def timeTaken(t1, t2):
    return str(round(t2 - t1, 2))

def extractor(src):
    src = src.replace('ك','ک').replace('‌',' ')
    src = re.sub("[^اآبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهیؤئء\sًٌٍَُِّ]+", " ", src)

    print('splitting words...')
    splitted = src.split()
    print('done.')

    print('removing duplicates...')
    wordset = set(splitted)
    print('done.')

    rm = []
    print('removing accented words...')
    for x in wordset:
        if len(x) == 1 :
            rm.append(x)
        for z in ['ْ','ٌ','ٍ','ً','ُ','ِ','َ']:
            if z in x:
                rm.append(x)
    rm = set(rm)
    for x in rm:
        wordset.remove(x)
    print('done')

    sortBy = prompt('Sort by:\n1-frequency\n2-alphabetic order\n> (1/2) ')
    if (sortBy == "1"):
        sortHolder = []
        print('counting duplicates...')
        for x in wordset:
            sortHolder.append((x,splitted.count(x)))
        print('done.')

        print('sorting by frequency...')
        def num(e):
            return e[1]
        sortHolder.sort(reverse= True ,key= num)
        print('done.')

        out = []
        for x in sortHolder:
            out.append(x[0])

        return out
        
    elif (sortBy == "2"):
        print('sorting alphabetically...')
        sorted = list(wordset)
        sorted.sort()
        return sorted

    else:
        print('Invalid response. Abort')
        exit()

def listToText(inputlist):
    print('writing to output.txt...')
    output = ''

    n = 0
    for x in inputlist:
        output += ('"' + str(x) + '"' + ";\n")
        n += 1
    print('done.')

    return output

def srcWriter():
    srclist = open('srclist.txt','r').read()
    url = srclist.split()
    open('source.txt','w').close()
    for link in url:
        content = requests.get(link).content
        with open("source.txt", 'ab') as f:
            f.write(content)
        print("Added %s to source.txt"%link)

def srcReader():
    try:
        return open('source.txt' , encoding='UTF-8').read()
    except FileNotFoundError:
        print('source.txt not found, abort.')
        exit()

def verifier(list):
    trash = []
    print('list is:')
    print(list)
    for word in list:
        url = requests.get('https://vajehyab.com/?q=' + word)
        pageContent = url.text
        resultsCount = pageContent.count('<span>جست‌وجوی دقیق</span>')
        if resultsCount == 0:
            print('WRONG WORD:' + word)
            trash.append(word)
        else:
            print(word + 'is correct')
    for word in trash:
        list.remove(word)
    return list

def asker():
    try:
        results = open('output.txt', 'r', encoding='UTF-8')
        if results:
            toErase = input("'output.txt' is not empty, would you like to erase its contents?\n> (y/n) ")
            if toErase == 'y':
                results = open('output.txt','w', encoding='UTF-8')
            elif toErase == 'n':
                print('Refusal to erase output.txt. Abort.')
                exit()
            else:
                print('Invalid response. Abort.')
                exit()
    except FileNotFoundError:
        print('output.txt not found, creating file...')
        results = open('output.txt','w', encoding='UTF-8')
    t1 = time()

    verifyAnswer = input('Do you want to verify the words using vajehyab.com?\n> (y/n) ')
    if verifyAnswer == 'y':
        results.write(listToText(verifier(extractor(srcReader()))))
    elif verifyAnswer == 'n':
        results.write(listToText(extractor(srcReader())))
    else:
        print('Not a valid option. Abort.')
        exit()

    t2 = time()
    print("Operation took " + timeTaken(t1, t2) + " seconds to complete")

asker()
print(amountExtracted())