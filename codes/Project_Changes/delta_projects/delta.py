
def main(input):
    old_projects = input["old_projects"]
    new_projects=input["new_projects"]
    result = [item for item in new_projects if item not in old_projects]
    return {"new_projects":result}


