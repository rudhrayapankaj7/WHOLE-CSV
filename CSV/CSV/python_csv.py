import csv
NEW_FILE_ONE = r"P:\DJANGO PROGRAMMING\pankaj_library\python with csv\CSV\CSV\country_lang.csv"


with open(NEW_FILE_ONE, 'r') as cf:
    data = csv.reader(cf)  # iterator object
    print(next(data))
    c = 0
    for row in data:
        c += 1
        print(row)
    print(c)


# with open(FILE_PATH, 'r') as cf:
#     data = csv.reader(cf)  # iterator object
#     c = 1
#     for row in data:
        
#         print(f"""
# Country No:- {c}
# CountryCode:-  {row[0]}
# Language:- {row[1]}
# IsOfficial:-  {row[2]}
# Percentage:-  {row[3]}
# --------------------------------------------------
#         """)
#         c += 1

"""

with open(FILE_PATH, 'r') as cf:
    data = csv.reader(cf)  # iterator object
    country_list = []
    c = 1
    for row in data:
        d = {}
        d['Country No'] = c
        d['CountryCode'] = row[0]
        d['Language'] = row[1]
        d['IsOfficial'] = row[2]
        d['Percentage'] = row[3]
        country_list.append(d)
        c += 1
    # print(country_list)

"""

# import csv
# with open(FILE_PATH, 'r') as file:
#     reader = csv.reader(file, delimiter = '\t')  #  "ABW,Dutch,T,5.3"
#     for row in reader:
        # print(row[0].split(','))
        # break



# NEW_FILE_PATH = r"F:\Class\B3-B4\Django\first_csv.csv"

# with open(NEW_FILE_PATH, 'w', newline='') as f:
#     csv_file = csv.writer(f)
#     # csv_file.writerow(['id', 'name', 'age'])
#     # csv_file.writerow([1, "Namrata", 22])
#     # csv_file.writerow([2, "Ranjeet", 25])
#     csv_file.writerows([ ['id', 'name', 'age'], [1, "Ranjeet", 25], [2, "abc", 21], [3, "xyz", 23], [4, "pqr", 26]   ])



# NEW_FILE_ONE = r"P:\DJANGO PROGRAMMING\pankaj_library\python with csv\CSV\CSV\first_csv.csv"

# # with open(NEW_FILE_ONE, 'r') as f:
#     # csv_file = csv.DictReader(f)
#     # for row in csv_file:
#         # print(row)

# d = [{'CountryCode': 'ZWE', 'Language': 'Ndebele', 'IsOfficial': 'F', 'Percentage': '16.2'}, {'CountryCode': 'ZWE', 'Language': 'Nyanja', 'IsOfficial': 'F', 'Percentage': '2.2'}, {'CountryCode': 'ZWE', 'Language': 'Shona', 'IsOfficial': 'F', 'Percentage': '72.1'}]


# NEW_FILE =  r"P:\DJANGO PROGRAMMING\pankaj_library\python with csv\CSV\CSV\first_csv.csv"
# with open(NEW_FILE, 'w', newline='') as f:
#     writer = csv.DictWriter(f=f, fieldnames=["CountryCode", "Language", "IsOfficial", "Percentage"])
#     writer.writeheader()
#     # writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
    # writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
    # writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})
    # writer.writerows(d)