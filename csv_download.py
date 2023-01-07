import requests
from bs4 import BeautifulSoup

def Download_csv():

    l = []
    url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html'
    url2 = 'https://people.sc.fsu.edu/~jburkardt/data/csv/'

    ##Hitting the URL to get the Response
    req = requests.get(url)
    print("Response - ",req.status_code)
    
    ##Parsing the HTML content Response from hitting the URL
    soup = BeautifulSoup(req.text, 'html.parser')

    ##Extracting all the CSV files
    for h in soup.find_all('a'):
        #print(h.get('href'))
        b = h.get('href')
        if ".csv" in b:
            #print(b)
            l.append(b)
    
    ##Printing all the CSV File Names
    print('Below are all the CSV files present in the Website - \n')
    for i in range(len(l)):
        print(l[i])
    
    ##Downloading all the CSV files
    for d in l:
        r = requests.get('{}{}'.format(url2,d))
        print("\nDownload Response for {} - {}".format(d,r.status_code))

        with open("{}".format(d),"wb") as f:
            f.write(r.content)

    print("\nSuccessful End of Program\n")

Download_csv()

