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
