src = open('source.txt' , encoding='UTF-8').read()

src = src.replace('ك','ک')
for x in src:
    if x not in {'ا','ب','پ','ت','ث','ج','چ','ح','خ','د','ذ','ر','ز','ژ','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ک','گ','ل','م','ن','و','ه','ی','آ','أ','إ','ؤ','ئ','ء','ْ','ٌ','ٍ','ً','ُ','ِ','ّ','ّ','‌',' '}:
        src = src.replace(x,' ')

splitted = src.split()
wordset = set(splitted)
rm = []
for x in wordset:
    if len(x) == 1:
        rm.append(x)
for x in rm:
    wordset.remove(x)

output = open('output.txt','w', encoding='UTF-8')

out = []
for x in wordset:
    out.append((x,splitted.count(x)))

def num(e):
    return e[1]
out.sort(reverse= True ,key= num)

n = 0
for x in out:
    output.write(str(list(out)[n][0]) + "\n")
    n += 1
