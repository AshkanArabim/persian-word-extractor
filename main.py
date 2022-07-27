from time import time
from urllib import response
from click import prompt
import requests
import re
import copy

print('-----------\nPersian Word Extractor v0.5\n-----------')

def amountExtracted():
    output = open('output.txt', 'r')
    length = len(set(output.read().split()))
    return (str(length) + ' words extracted')

def timeTaken(t1, t2):
    return str(round(t2 - t1, 2))

def crawler(n):
    n = int(n)
    srclist = open('./srclist.txt','r')
    l1 = srclist.read().split()
    l2 = copy.copy(l1)
    l3 = []
    srclist.close()
    print("srclist.txt has " + str(len(l1)) + " links initially")

    while(len(l1) <= n):
        while(len(l2) > 0):
            content = requests.get(l2[0]).text
            l3 += re.findall("(?<=\")https:\/\/fa\.wikipedia\.org\/wiki\/[^\"]*", content)
            l2.pop(0)
        
        print("length of old l1 is: " + str(l1))        
        l1 += l3
        l2 = copy.copy(l3)

    l1 = set(l1)

    srclist = open('./srclist.txt','w')
    for link in l1:
        srclist.write(link + "\n")

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
        print(sortHolder)
        print('done.')

        out = []
        for x in sortHolder:
            # fix this error
            print(str(sortHolder[x])) 
            out.append(sortHolder[x][0])

        return out
        
    elif (sortBy == "2"):
        print('sorting alphabetically...')
        splitted.sort()
        print('done')
        return splitted

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

def asker():
    try:
        results = open('output.txt', 'r', encoding='UTF-8')
        if results:
            toErase = input("'output.txt' is not empty, would you like to erase its contents?\n> (yes/no) ")
            if toErase == 'yes':
                results = open('output.txt','w', encoding='UTF-8')
            elif toErase == 'no':
                print('Refusal to erase output.txt. Abort.')
                exit()
            else:
                print('Invalid response. Abort.')
                exit()
    except FileNotFoundError:
        print('output.txt not found, creating file...')
        results = open('output.txt','w', encoding='UTF-8')


    srcAnswer = input('Choose source origin: \n  online (builds a link-tree from initial fa.wikipedia.org link) \n  offline (source.txt file in root directory) \n> ')
    t1 = time()
    if srcAnswer == 'online':
        linkAmount = prompt("Minimum number of generated links: \n> ")
        crawler(linkAmount)
        srcWriter()
        results.write(listToText(extractor(srcReader())))
    elif srcAnswer == 'offline':
        results.write(listToText(extractor(srcReader())))
    else:
        print('Invalid response. Abort.')
        exit()
    t2 = time()
    print("Operation took " + timeTaken(t1, t2) + " seconds to complete")

asker()
print(amountExtracted())