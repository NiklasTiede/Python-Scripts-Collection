# a list of all FDA-approved drugs (downloaded from fda.gov) is extracted
# and used for scraping their InChI-strings from the web:
# collecting the data within another .csv-file
import csv

import requests  # type: ignore

with open('preprocessed_compilation.csv') as csv_file:
    spamreader = csv.reader(csv_file, delimiter=',')
    for num, row in enumerate(spamreader):
        print(num)
        if num <= 421:
            continue
        prop_name, ingredient = row
        for name1 in prop_name.split(' '):
            name1 = name1.strip(',').strip(';')
            res = requests.get(f"https://cactus.nci.nih.gov/chemical/structure/{name1}/stdinchi")
            if 'InChI' in res.text:
                request = res.text
                break
            else:
                for name2 in ingredient.split(' '):
                    name2 = name2.strip('"').strip("'").strip('\n').strip(',').strip(';')
                    res = requests.get(f"https://cactus.nci.nih.gov/chemical/structure/{name2}/stdinchi")
                    if 'InChI' in res.text:
                        request = res.text
                        break
                    else:
                        request = 'bad request'
        with open('fda_drugs_inchi.csv', 'a') as file:
            file.write(f'{prop_name},"{ingredient}","{request}"\n')

print('script finished!')

# the scraping took about 5 h for me!
