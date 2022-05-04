from time import time
import requests
import re
import copy

print('-----------\nPersian Word Extractor v.1.4\n-----------')

def timeTaken(t1, t2):
    return str(round(t2 - t1, 2))

def crawler(n):
    n = int(n)
    srclist = open('./srclist.txt','r')
    l1 = srclist.read().split()
    l2 = copy.copy(l1)
    srclist.close()
    print("length of initial l1 is: " + str(len(l1)))

    while(len(l1) <= n):
        l3 = []

        while(len(l2) > 0):
            content = requests.get(l2[0]).text
            l3 += re.findall("https:\/\/fa\.wikipedia\.org\/.*?\"", content)
            l2.pop(0)
        
        print("length of old l1 is: " + str(len(l1)))        
        l1 += l3
        l2 = copy.copy(l3)

    print("length of l3 is: " + str(len(l3)))
    print("length of l1 is: " + str(len(l1)))
    for link in l1:
        link = link.replace('"', '')
        print(link)

    l1 = set(l1)

    srclist = open('./srclist.txt','w')
    for link in l1:
        srclist.write(link + "\n")

def extractor(src):
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

def srcWriter():
    srclist = open('srclist.txt','r').read()
    url = srclist.split()
    open('source.txt','w').close()
    for link in url:
        content = requests.get(link).content
        with open("source.txt", 'wb') as f:
            f.write(content)
        print("Added %s to source.txt"%link)

def srcReader():
    return open('source.txt' , encoding='UTF-8').read()

results = open('output.txt','w', encoding='UTF-8')

def asker():
    srcAnswer = input('Choose source origin: \n  online (from links in srclist.txt) \n  offline (source.txt file in root directory) \n>> ')
    t1 = time()
    if srcAnswer == 'online':
        srcWriter()
        results.write(extractor(srcReader()))
    elif srcAnswer == 'offline':
        results.write(extractor(srcReader()))
    else:
        print('That is not a valid option. Abort.')
        exit()

    print('Words extracted successfully. Check output.txt')
    t2 = time()
    print("Operation took " + timeTaken(t1, t2) + " seconds to complete")

# asker()
