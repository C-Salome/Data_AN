from bs4 import BeautifulSoup
import pandas as pd
import glob
import os

lig = []
col = ["id_indiv","nom", "prenom", "genre", "date_naissance", "dep_naissance", "date_decès", "parlementaire"]

for filename in glob.glob("/Users/salomecolza/desktop/These_Hugo/AMO10_deputes_actifs_mandats_actifs_organes_XVI/acteur/*.xml"):
    with open(os.path.join(os.getcwd(), filename), 'r') as file:
        soup = BeautifulSoup(file,"xml")

        p_id = soup.find("uid")
        pf_id = p_id.get_text()
        print(pf_id)

        p_civ = soup.find("civ")
        pf_civ = p_civ.get_text()

        p_prenom = soup.find("prenom")
        pf_prenom = p_prenom.get_text()

        p_nom = soup.find("nom")
        pf_nom = p_nom.get_text()

        p_date_n = soup.find("dateNais")
        pf_date_n = p_date_n.get_text()

        p_dep_n = soup.find("depNais")
        pf_dep_n = p_dep_n.get_text()

        p_date_d = soup.find("dateDeces")
        pf_date_d = p_date_d.get_text()

        lig.append({"id_indiv": pf_id,  "nom": pf_nom, "prenom": pf_prenom, "genre": pf_civ, "date_naissance": pf_date_n, "dep_naissance": pf_dep_n, "date_decès": pf_date_d, "parlementaire": 1})

        file.close()

out_df = pd.DataFrame(lig, columns = col)
#print(out_df)
out_df.to_csv(r'/Users/salomecolza/desktop/These_Hugo/export_df_XVI.csv', index = False, header=True)

#path = "/Users/salomecolza/desktop/test/*.xml"
#xml_doc = open(path,'r')
#soup = BeautifulSoup(xml_doc,"xml")

# col = ["id_indiv","nom", "prenom", "genre", "date_naissance", "dep_naissance", "date_decès", "parlementaire"]
# lig = []
#
# p_id = soup.find("uid")
# p_civ = soup.find("civ")
# p_prenom = soup.find("prenom")
# p_nom = soup.find("nom")
# p_date_n = soup.find("dateNais")
# p_dep_n = soup.find("depNais")
# p_date_d = soup.find("dateDeces")
#
# lig.append({"id_indiv": p_id,  "nom": p_nom, "prenom": p_prenom, "genre": p_civ, "date_naissance": p_date_n, "dep_naissance": p_dep_n, "date_decès": p_date_d, "parlementaire": "true"})
#
#
# out_df = pd.DataFrame(lig, columns = col)
#
# print(out_df)
#
# xml_doc.close()

#Table individu : (id_indiv, nom_naissance, nom_élu, nom_marital, prénom, genre, date_naissance, dep_naissance, date_decès, parlementaire