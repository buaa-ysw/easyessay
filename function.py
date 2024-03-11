import os
from init import *

def save(abst, intro, sys_comp, sys_prin, res_ana, inn_poi, mar_pro, conc, bib, name):
    # Check if the folder exists, and create it if it doesn't
    folder_path = output_path + "/" + name
    if os.path.exists(folder_path):
        # Find the next available folder name
        i = 2
        while True:
            folder_path = output_path + "/" + f"{name}_{i}"
            if not os.path.exists(folder_path):
                break
            i += 1
    os.makedirs(folder_path)

    # Save the abst as .txt file
    abst_file_name = f"abst_{name}.txt"
    if os.path.exists(os.path.join(folder_path, abst_file_name)):
        # Find the next available file name
        i = 2
        while True:
            abst_file_name = f"abst_{name}_{i}.txt"
            if not os.path.exists(os.path.join(folder_path, abst_file_name)):
                break
            i += 1
    abst_file_path = os.path.join(folder_path, abst_file_name)
    with open(abst_file_path, "w") as abst_file:
        abst_file.write(abst)
        
    # Save the intro as .txt file
    intro_file_name = f"intro_{name}.txt"
    if os.path.exists(os.path.join(folder_path, intro_file_name)):
        # Find the next available file name
        i = 2
        while True:
            intro_file_name = f"intro_{name}_{i}.txt"
            if not os.path.exists(os.path.join(folder_path, intro_file_name)):
                break
            i += 1
    intro_file_path = os.path.join(folder_path, intro_file_name)
    with open(intro_file_path, "w") as intro_file:
        intro_file.write(intro)
        
    # Save the sys_comp as .txt file
    sys_comp_file_name = f"sys_comp_{name}.txt"
    if os.path.exists(os.path.join(folder_path, sys_comp_file_name)):
        # Find the next available file name
        i = 2
        while True:
            sys_comp_file_name = f"sys_comp_{name}_{i}.txt"
            if not os.path.exists(os.path.join(folder_path, sys_comp_file_name)):
                break
            i += 1
    sys_comp_file_path = os.path.join(folder_path, sys_comp_file_name)
    with open(sys_comp_file_path, "w") as sys_comp_file:
        sys_comp_file.write(sys_comp)
        
    # Save the sys_prin as .txt file
    sys_prin_file_name = f"sys_prin_{name}.txt"
    if os.path.exists(os.path.join(folder_path, sys_prin_file_name)):
        # Find the next available file name
        i = 2
        while True:
            sys_prin_file_name = f"sys_prin_{name}_{i}.txt"
            if not os.path.exists(os.path.join(folder_path, sys_prin_file_name)):
                break
            i += 1
    sys_prin_file_path = os.path.join(folder_path, sys_prin_file_name)
    with open(sys_prin_file_path, "w") as sys_prin_file:
        sys_prin_file.write(sys_prin)
        
    # Save the res_ana as .txt file
    res_ana_file_name = f"res_ana_{name}.txt"
    if os.path.exists(os.path.join(folder_path, res_ana_file_name)):
        # Find the next available file name
        i = 2
        while True:
            res_ana_file_name = f"res_ana_{name}_{i}.txt"
            if not os.path.exists(os.path.join(folder_path, res_ana_file_name)):
                break
            i += 1
    res_ana_file_path = os.path.join(folder_path, res_ana_file_name)
    with open(res_ana_file_path, "w") as res_ana_file:
        res_ana_file.write(res_ana)
        
    # Save the inn_poi as .txt file
    inn_poi_file_name = f"inn_poi_{name}.txt"
    if os.path.exists(os.path.join(folder_path, inn_poi_file_name)):
        # Find the next available file name
        i = 2
        while True:
            inn_poi_file_name = f"inn_poi_{name}_{i}.txt"
            if not os.path.exists(os.path.join(folder_path, inn_poi_file_name)):
                break
            i += 1
    inn_poi_file_path = os.path.join(folder_path, inn_poi_file_name)
    with open(inn_poi_file_path, "w") as inn_poi_file:
        inn_poi_file.write(inn_poi)
    
    # Save the mar_pro as .txt file
    mar_pro_file_name = f"mar_pro_{name}.txt"
    if os.path.exists(os.path.join(folder_path, mar_pro_file_name)):
        # Find the next available file name
        i = 2
        while True:
            mar_pro_file_name = f"mar_pro_{name}_{i}.txt"
            if not os.path.exists(os.path.join(folder_path, mar_pro_file_name)):
                break
            i += 1
    mar_pro_file_path = os.path.join(folder_path, mar_pro_file_name)
    with open(mar_pro_file_path, "w") as mar_pro_file:
        mar_pro_file.write(mar_pro)
    
    # Save the conc as .txt file
    conc_file_name = f"conc_{name}.txt"
    if os.path.exists(os.path.join(folder_path, conc_file_name)):
        # Find the next available file name
        i = 2
        while True:
            conc_file_name = f"conc_{name}_{i}.txt"
            if not os.path.exists(os.path.join(folder_path, conc_file_name)):
                break
            i += 1
    conc_file_path = os.path.join(folder_path, conc_file_name)
    with open(conc_file_path, "w") as conc_file:
        conc_file.write(conc)
        
    # Save the bib as .txt file
    bib_file_name = f"bib_{name}.txt"
    if os.path.exists(os.path.join(folder_path, bib_file_name)):
        # Find the next available file name
        i = 2
        while True:
            bib_file_name = f"bib_{name}_{i}.txt"
            if not os.path.exists(os.path.join(folder_path, bib_file_name)):
                break
            i += 1
    bib_file_path = os.path.join(folder_path, bib_file_name)
    with open(bib_file_path, "w") as bib_file:
        bib_file.write(bib)
