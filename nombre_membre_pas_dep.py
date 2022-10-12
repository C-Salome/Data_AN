from bs4 import BeautifulSoup
import pandas as pd
import glob
import os

col = ["id_indiv",'id_legis','id_mandat','id_inves','id_incomp','remporte','date_deb','date_fin']
res = []

for filename in glob.glob('/Users/salomecolza/desktop/These_Hugo/AMO30_tous_acteurs_tous_mandats_tous_organes_historique/acteur/*.xml'):
    with open(os.path.join(os.getcwd(), filename), 'r') as file:
        soup = BeautifulSoup(file,"xml")

        mandat = soup.find_all("mandat")
        for i in mandat:

            ref = i.find("codeQualite")
            id_fonction = ref.get_text()

            if not id_fonction:
                ref = i.find("libQualite")
                id_fonction = ref.get_text()

            ref = i.find("organeRef")
            id_instance = ref.get_text()

            if id_fonction == "membre" and (id_instance != 'PO230434' or id_instance != 'PO384266' or id_instance != 'PO644420' or id_instance != 'PO717460' ):

                ref = i.find("acteurRef")
                id_indiv = ref.get_text()
                print(id_indiv)

                ref = i.find("legislature")
                id_legis = ref.get_text()

                ref = i.find("dateDebut")
                date_deb = ref.get_text()

                ref = i.find("dateFin")
                date_fin = ref.get_text()

                res.append({"id_indiv" : id_indiv, 'id_legis' : id_legis, 'id_mandat' : 1, 'id_inves' : None , 'id_incomp' : None, 'remporte' : 'true', 'date_deb' : date_deb,'date_fin' : date_fin})

    file.close()

out_df = pd.DataFrame(res, columns = col)
out_df.to_csv('/Users/salomecolza/desktop/These_Hugo/export_dataframe_membre_non_dep_AMO30.csv', index = False, header=True)

print(len(res))