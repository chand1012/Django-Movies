import os
from tqdm import tqdm
import csv

ids = []

with open('new_movies.tsv', mode = 'w', encoding= "utf-8") as new_file:
    with open('movies.tsv', mode ='r', encoding= "utf-8") as file:
        # reading the CSV file
        csv_reader = csv.reader(file, delimiter= "\t")
        for line in tqdm(csv_reader, total=9376980):
            if line[1] != 'movie':
                continue
            
            new_file.write('\t'.join(line) + '\n')
            # remove the tt from the id
            ids.append(line[0])

ids_as_str = ','.join(ids)

with open('new_actors.tsv', mode = 'w', encoding= "utf-8") as new_file:
    with open('actors.tsv', mode ='r', encoding= "utf-8") as file:
        # reading the CSV file
        csv_reader = csv.reader(file, delimiter= "\t")
        for line in tqdm(csv_reader, total=12081797):
            if os.path.commonprefix([line[5], ids_as_str]) == '':
                continue
            new_file.write('\t'.join(line) + '\n')
