import yaml


def load_yml(yml_path):
    # Read the YAML file
    with open(yml_path, "r") as file:
        yaml_data = file.read()

    # Split the YAML data into dictionaries based on comments
    yaml_lines = yaml_data.split("\n")

    groups = ["general_params", "filters", "gene3", "gene4", "gene5"]
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

    # print(grouped_dicts)
    return grouped_dicts
