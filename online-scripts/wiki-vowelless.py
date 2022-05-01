import requests
url = "https://fa.wikipedia.org/wiki/%D8%AC%D9%86%DA%AF_%D8%BA%D8%B2%D9%87_(%DB%B2%DB%B0%DB%B0%DB%B8%E2%80%93%DB%B2%DB%B0%DB%B0%DB%B9)"
#link to a test wikipedia article
r = requests.get(url)
#retrieving data from the URL using get method
with open("./sources/dummy.html", 'wb') as f:
#giving a name and saving it in any required format
#opening the file in write mode
    f.write(r.content) 
#writes the URL contents from the server

src = r.content


src.find()