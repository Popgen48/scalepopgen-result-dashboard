from jinja2 import Environment, FileSystemLoader
import yaml
import sys
from util import load_yml


def render(yml_path):
    # Define the Jinja2 environment
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("template.html")

    # Define the data to be used in the template
    context = load_yml(yml_path)

    # Render the template with the data
    with open("results.html", mode="w", encoding="utf-8") as results:
        results.write(template.render(context))
        print(f"... wrote to results.html")


if __name__ == "__main__":
    render(sys.argv[1])
