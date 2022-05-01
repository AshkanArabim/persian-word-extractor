import requests
url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
#just a random link of a dummy file
r = requests.get(url)
#retrieving data from the URL using get method
with open("dummy.pdf", 'wb') as f:
#giving a name and saving it in any required format
#opening the file in write mode
    f.write(r.content) 
#writes the URL contents from the server