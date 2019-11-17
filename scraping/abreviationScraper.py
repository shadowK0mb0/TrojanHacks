from bs4 import BeautifulSoup
import urllib.request

def getSchools():
    with urllib.request.urlopen('https://classes.usc.edu/term-20201/') as source:
        soup = BeautifulSoup(source, 'html.parser')

    abreviations = soup.find(id="sortable-classes").contents
    schools = []
    for i in range(len(abreviations)):
        if (not isinstance(abreviations[i], str)) and abreviations[i]["data-type"] == "department":
            schools.append(abreviations[i]["data-code"])
    return(schools)


