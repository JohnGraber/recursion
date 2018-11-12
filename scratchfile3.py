import json, sys
from collections import namedtuple

def read_json(json_filename):
    f = open(json_filename)
    jstr = json.load(f)
    return jstr



def recursive_search_function(data_set, field, search_terms):

    search_terms.append(field)
    print(search_terms)

    for key in data_set:
        print(data_set[key])

        if type(data_set[key]) not in (list, dict):
            print('Dug too deep')
            continue

        elif field in data_set[key]:
            print('       ******   Found it: ' + field)

            return recursive_search_function(data_set, key, search_terms)

        else:
            print("Not in: " + str(list(data_set[key].keys())))
            print("  ** Going Deeper" + "\n")
            recursive_search_function(data_set[key], field, search_terms)



small_cars = read_json('small_cars.json')
specific_car = small_cars["1"]
print(small_cars)

car_terms = []
car_terms2 = []



recursive_search_function(small_cars, 'Horsepower', search_terms = car_terms)
recursive_search_function(small_cars, 'Performance', search_terms = car_terms2)
