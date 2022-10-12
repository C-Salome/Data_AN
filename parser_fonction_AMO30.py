from bs4 import BeautifulSoup
import pandas as pd
import glob
import os
import re

col = ["id_indiv",'id_instance','id_fonction','date_deb','date_fin']
res = []
lib = []
id_f = []

for filename in glob.glob('/Users/salomecolza/desktop/These_Hugo/AMO30_tous_acteurs_tous_mandats_tous_organes_historique/acteur/*.xml'):
    with open(os.path.join(os.getcwd(), filename), 'r') as file:
        soup = BeautifulSoup(file,"xml")

        mandat = soup.find_all("mandat")

        for i in mandat:

            ref = i.find("organeRef")
            id_instance = ref.get_text()

            if id_instance != 'PO230434' and id_instance != 'PO384266' and id_instance != 'PO644420' and id_instance != 'PO717460' :

                ref = i.find("codeQualite")
                id_fonction = ref.get_text()

                if not id_fonction:
                    ref = i.find("libQualite")
                    id_fonction = ref.get_text()
                    if id_fonction not in lib:
                        lib.append(id_fonction)

                match = re.search('Rapporteur pour avis au nom de la commission', id_fonction)
                if match:
                    id_fonction = 69
                elif id_fonction == 'Membre':
                    id_fonction = 1
                elif id_fonction == 'Titulaire':
                    id_fonction = 2
                elif id_fonction == "Vice-Président":
                    id_fonction = 3
                elif id_fonction == "Secrétaire":
                    id_fonction = 4
                elif id_fonction == "Député non-inscrit":
                    id_fonction = 5
                elif id_fonction == "Suppléant":
                    id_fonction = 6
                elif id_fonction == "Ministre":
                    id_fonction = 7
                elif id_fonction == "Membre de droit du Bureau":
                    id_fonction = 8
                elif id_fonction == "Rapporteur":
                    id_fonction = 9
                elif id_fonction == "Président":
                    id_fonction = 10
                elif id_fonction == "Co-Président":
                    id_fonction = 11
                elif id_fonction == "Co-rapporteur":
                    id_fonction = 12
                elif id_fonction == "en mission":
                    id_fonction = 13
                elif id_fonction == "Sénateur":
                    id_fonction = 14
                elif id_fonction == "Membre rattaché":
                    id_fonction = 15
                elif id_fonction == "Membre de droit":
                    id_fonction = 16
                elif id_fonction == "Rapporteur thématique":
                    id_fonction = 17
                elif id_fonction == "Ministre délégué":
                    id_fonction = 18
                elif id_fonction == "Membre apparenté":
                    id_fonction = 19
                elif id_fonction == "Juge suppléant":
                    id_fonction = 20
                elif id_fonction == "Premier ministre":
                    id_fonction = 21
                elif id_fonction == "Autre membre du Bureau":
                    id_fonction = 22
                elif id_fonction == "Secrétaire d'État":
                    id_fonction = 23
                elif id_fonction == "Vice-Président délégué":
                    id_fonction = 24
                elif id_fonction == "Président délégué":
                    id_fonction = 25
                elif id_fonction == "Premier Vice-Président":
                    id_fonction = 26
                elif id_fonction == "Garde des sceaux":
                    id_fonction = 27
                elif id_fonction == "Rapporteur spécial":
                    id_fonction = 28
                elif id_fonction == "Trésorier adjoint":
                    id_fonction = 29
                elif id_fonction == "Juge titulaire":
                    id_fonction = 30
                elif id_fonction == "Questeur":
                    id_fonction = 31
                elif id_fonction == "Membre de droit (Président de la commission des lois)":
                    id_fonction = 32
                elif id_fonction == "Co-président":
                    id_fonction = 11
                elif id_fonction == "Président de droit  ":
                    id_fonction = 34
                elif id_fonction == "Rapporteur général":
                    id_fonction = 35
                elif id_fonction == "Deuxième Vice-Président":
                    id_fonction = 36
                elif id_fonction == "Membre nommé par le Président du Sénat":
                    id_fonction = 37
                elif id_fonction == "Premier vice-président":
                    id_fonction = 26
                elif id_fonction == "Membre de droit (Président de la commission de la défense)":
                    id_fonction = 39
                elif id_fonction == "Vice-président, co-rapporteur":
                    id_fonction = 40
                elif id_fonction == "Membre désigné par les groupes":
                    id_fonction = 41
                elif id_fonction == "Rapporteur suppléant":
                    id_fonction = 42
                elif id_fonction == "Membre de droit (Président de la commission des affaires étrangères)":
                    id_fonction = 43
                elif id_fonction == "Trésorier":
                    id_fonction = 44
                elif id_fonction == "Président-rapporteur":
                    id_fonction = 45
                elif id_fonction == "Secrétaire general-adjoint":
                    id_fonction = 46
                elif id_fonction == "Rapporteur-spécial":
                    id_fonction = 28
                elif id_fonction == "Président de groupe":
                    id_fonction = 48
                elif id_fonction == "Membre nommé par le Président de l'Assemblée nationale":
                    id_fonction = 49
                elif id_fonction == "Ministre d'État":
                    id_fonction = 50
                elif id_fonction == "Rapporteur general ":
                    id_fonction = 35
                elif id_fonction == "Secrétaire général":
                    id_fonction = 52
                elif id_fonction == "Représentant du president de groupe":
                    id_fonction = 53
                elif id_fonction == "Membre de droit (Représentant de la commission des affaires étrangères)":
                    id_fonction = 54
                elif id_fonction == "Membre de droit (Président de la commission des affaires culturelles)":
                    id_fonction = 55
                elif id_fonction == "Président exécutif":
                    id_fonction = 56
                elif id_fonction == "Membre associé":
                    id_fonction = 57
                elif id_fonction == "Président délégué pour l'UEO":
                    id_fonction = 58
                elif id_fonction == "Membre de droit (Représentant de la commission des finances)":
                    id_fonction = 59
                elif id_fonction == "Chef de la delegation de l'Assemblée nationale":
                    id_fonction = 60
                elif id_fonction == "Membre de droit (Rapporteur du projet de loi de financement de la séc. sociale)":
                    id_fonction = 61
                elif id_fonction == "Membre de droit (Représentant de la commission de la défense)":
                    id_fonction = 62
                elif id_fonction == "Membre de droit (Représentant de la commission des lois)":
                    id_fonction = 63
                elif id_fonction == "Membre de droit (Représentant de la commission des affaires économiques)":
                    id_fonction = 64
                elif id_fonction == "Membre de droit (Représentante de la commission des affaires culturelles)":
                    id_fonction = 65
                elif id_fonction == "Président de la République":
                    id_fonction = 66
                elif id_fonction == "Membre de droit (Président de la commission des affaires sociales)":
                    id_fonction = 67
                elif id_fonction == "Membre de droit (Représentant de la commission des affaires sociales)":
                    id_fonction = 68
                elif id_fonction == "membre":
                    id_fonction = 1
                elif id_fonction == "Vice-président":
                    id_fonction = 3
                elif id_fonction == "Délégué":
                    id_fonction = 70

                ref = i.find("acteurRef")
                id_indiv = ref.get_text()

                ref = i.find("dateDebut")
                date_deb = ref.get_text()

                ref = i.find("dateFin")
                date_fin = ref.get_text()

                #test

                if id_fonction not in id_f:
                    id_f.append(id_fonction)
                    print(id_fonction)

                res.append({"id_indiv" : id_indiv,'id_instance' : id_instance ,'date_deb' : date_deb,'date_fin' : date_fin, 'id_fonction' : id_fonction})

    file.close()

df = pd.DataFrame(lib)
df.to_csv('/Users/salomecolza/desktop/These_Hugo/export_dataframe_mandats_AMO30_libQualite.csv')

out_df = pd.DataFrame(res, columns = col)
out_df.to_excel('/Users/salomecolza/desktop/These_Hugo/export_dataframe_mandats_AMO30_sans_dep.xlsx', index = False, header=True)

print(len(res))