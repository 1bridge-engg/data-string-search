from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def search(string, db_list, limit, score_cutoff):
    result = process.extractBests(string, db_list, limit=limit, score_cutoff=score_cutoff)
    list = []
    for each in result:
        dict = {}
        dict["id"] = each[0][0]
        dict["name"] = each[0][1]
        dict["img_url"] = each[0][2]
        list.append(dict)
    return list
