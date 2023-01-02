import os
import csv
import argparse

class PageMaker:


    html = """<!DOCTYPE html>
                    <html lang="en">
                    <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>De Niro Movies - [Title]</title>
                    </head>
                    <body>
                    <h1>Film: [Title]</h1>
                    <p>Année de sortie: [Year]</p>
                    <p>Score obtenue: [Score]</p>
                    
                    </body>
                    </html>"""
    
    def __init__(self,fname):

        f = open(fname,"r")
        self.data = csv.reader(f)

        header = []
        header = next(self.data)

    def generate_html(self, repo_path):

        try:
            os.mkdir(repo_path)
            print("dossier créé")
        except FileExistsError as error:
            print("dossier existe deja")  

        année = []
        rows = []
        score = []
        titre = []

        for row in self.data:
            rows.append(row)

        for a in rows:
            année.append(a[0])
            score.append(a[1])
            titre.append(a[2])

        j = 0
        try:
            while j != len(rows):   
                out_file = f"{repo_path}/page{j}.html" 
                with open(out_file, "w") as f:
                    f.write(self.html.replace("[Title]",titre[j]).replace("[Year]",année[j]).replace("[Score]",score[j]))
                    print(f"[+] {repo_path}/page{j}.html")
                    j +=1
        except FileExistsError:  
            print("fichier existe deja")

pm = PageMaker("deniro.csv")
pm.generate_html("tmp") 
print("--- The End ---")

