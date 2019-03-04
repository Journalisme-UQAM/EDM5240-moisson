# coding  utf-8

import csv
import requests
from bs4 import BeautifulSoup 

fichier = "avertissements_voyages.csv"

url = "https://voyage.gc.ca/voyager/avertissements"

entetes = {
	"User-Agent":"Camille Payant - requête dans le cadre d'un cours de journalisme de données ",
	"From":"camille.payant@hotmail.com"
}

contenu = requests.get(url,headers=entetes)

page = BeautifulSoup(contenu.text,"html.parser")

payss = page.find_all("tr", class_="gradeX")

for pays in payss: 
	if not pays.find("span", class_="wb-invisible"):
		href = pays.find("a")["href"]
		url = "https://voyage.gc.ca" + href
		nom = pays.find("a").text
		avertissement = pays.find_all("td")[2].text
		heure = pays.find_all("td")[3].text
	
		infos = [url,nom,avertissement,heure]
		print(infos)

		diables = open(fichier, "a")
		rouges = csv.writer(diables)
		rouges.writerow(infos)