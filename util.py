import yaml
import glob

result_dir = "results"

def load_yml(yml_path):
    # Read the YAML file
    with open(yml_path, "r") as file:
        yaml_data = file.read()

    # Split the YAML data into dictionaries based on comments
    yaml_lines = yaml_data.split("\n")

    groups = ["general_params", "filters", "genetic_struct", "treemix", "signs"]
    grouped_dicts = {}
    current_group = None
    i = 0

    for line in yaml_lines:
        if line.startswith("#"):
            current_group = groups[i]
            i += 1
            grouped_dicts[current_group] = []
        elif current_group:
            if not line.strip() or line.strip() == "#":
                continue
            key, value = map(str.strip, line.split(":", 1))
            tmp = {"parameter": key, "value": value}
            grouped_dicts[current_group].append(tmp)
        else:
            continue
    
    for x in grouped_dicts["genetic_struct"]:
        if x["parameter"] == "run_smartpca":
            if x["value"] == "true":
                smartpca = glob.glob(result_dir + "/*_smartpca.html")
                grouped_dicts["smartpca"] = smartpca[0]
        if x["parameter"] == "admixture":
            if x["value"] == "true":
                admixture = glob.glob(result_dir + "/*_admixture.html")
                grouped_dicts["admixture"] = admixture[0]
        if x["parameter"] == "fst_based_nj_tree":
            if x["value"] == "true":
                fst = glob.glob(result_dir + "/*_fst.html")
                grouped_dicts["fst"] = fst[0]
        if x["parameter"] == "est_1_min_ibs_based_nj_tree":
            if x["value"] == "true":
                ibs = glob.glob(result_dir + "/*_ibs.html")
                grouped_dicts["ibs"] = ibs[0]
        
    phylotree = glob.glob(result_dir + "/*_treemix.pdf")
    grouped_dicts["phylotree"] = phylotree[0]
    optm = glob.glob(result_dir + "/*_optM.pdf")
    grouped_dicts["optm"] = optm[0]
    
    for x in grouped_dicts["treemix"]:
        if x["parameter"] == "ending_m_value":
            if int(x["value"]) > 0:
                mig = glob.glob(result_dir + "/*_mig.pdf")
                grouped_dicts["mig"] = mig[0]

    # print(grouped_dicts)
    return grouped_dicts
