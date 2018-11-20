from fuzzywuzzy import fuzz
from fuzzywuzzy import process

db_list = []


def search(string, db_list, limit, accuracy_value):
    result = process.extractBests(string, db_list, limit=limit, score_cutoff=accuracy_value)
    print(result)
    list = []
    for each in result:
        dict = {}
        dict["id"] = each[0][0]
        dict["title"] = each[0][1]
        dict["image"] = each[0][2]
        dict["price"] = each[0][3]
        dict["notes"] = each[0][4]
        dict["status"] = each[0][5]
        dict["mrp"] = each[0][6]
        dict["discount"] = each[0][7]
        dict["subcategory"] = each[0][8]
        list.append(dict)
    return list