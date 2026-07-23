import yaml


def load_assignment(path):
    """
    Load an assignment.yml file and return a Python dictionary.
    """

    with open(path, "r", encoding="utf-8") as file:
        assignment = yaml.safe_load(file)

    return assignment