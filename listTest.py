# Given a list that contains strings, integers and booleans,
# group all the booleans, integers and strings into separate lists.
# return a dictionary with the keys "booleans", "integers" and "strings"

def group_list(lst: list) -> dict:
    convertToDict: dict[str, list] = {
        "boolean": [],
        "integers" : [],
        "string" : [],
    }
    for perItem in lst:
        if type(perItem) == bool:
            convertToDict['boolean'].append(perItem)
        elif type(perItem) == int:
            convertToDict['integers'].append(perItem)
        else:
            convertToDict['string'].append(perItem)
    return convertToDict

lst = [True, 13, 'Hello', False, 'World', 45, True, 66, 'Ejay','sdfdsfdsfsdfsd', 'aeasdsadas']
print(group_list(lst))
