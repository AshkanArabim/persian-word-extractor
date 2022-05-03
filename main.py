from time import time
from unittest import result
import chardet
import requests
import re

#to do :
#Add crawler function

print('-----------\nPersian Word Extractor v.1.4\n-----------')

def timeTaken(t1, t2):
    return str(round(t2 - t1, 2))

# def crawler():
#     srclist = open('./srclist.txt','r')
#     l1 = srclist.read().split()
#     for link in l1:
#         content = requests.get(link).content
#         newLinks = re.findall(b"https://fa\.wikipedia\.org/.*\"", content)
#         for newLink in newLinks:
#             print(newLink.encode('utf8'))

# crawler()

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
