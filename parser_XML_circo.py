#uid
#codeType
#libelle
#numero
#region/libelle
#departement/code
#dateDebut
#dateFin

from bs4 import BeautifulSoup
import pandas as pd
import glob
import os

lig = []
col = ["id_territoire","type_territoire", "libelle_territoire","num_circo","num_departement", "libelle_region", "date_deb", "date_fin"]

for filename in glob.glob("/Users/salomecolza/desktop/These_Hugo/xml2/organe/*.xml"):
    with open(os.path.join(os.getcwd(), filename), 'r') as file:
        soup = BeautifulSoup(file,"xml")

        p_id = soup.find("uid")
        pf_id = p_id.get_text()


        p_type = soup.find("codeType")
        pf_type = p_type.get_text()


        if pf_type == "CIRCONSCRIPTION":

            p_libel_terr = soup.find("libelle")
            pf_libel_terr = p_libel_terr.get_text()
            print(pf_libel_terr)

            p_numcirco = soup.find("numero")
            pf_numcirco = p_numcirco.get_text()

            p_numdep = soup.find("code")
            pf_numdep = p_numdep.get_text()

            p1_libel_reg = soup.find("region")
            p2_libel_reg = p1_libel_reg.find("libelle")
            pf_libel_reg = p2_libel_reg.get_text()


            p_date_d = soup.find("dateDebut")
            pf_date_d = p_date_d.get_text()

            p_date_f = soup.find("dateFin")
            pf_date_f = p_date_f.get_text()

            lig.append({"id_territoire": pf_id,"type_territoire":pf_type, "libelle_territoire": pf_libel_terr,"num_circo": pf_numcirco,"num_departement": pf_numdep, "libelle_region": pf_libel_reg, "date_deb": pf_date_d, "date_fin": pf_date_f})

        file.close()

out_df = pd.DataFrame(lig, columns = col)
#print(out_df)
out_df.to_csv(r'/Users/salomecolza/desktop/These_Hugo/export_dataframe_circo.csv', index = False, header=True)

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