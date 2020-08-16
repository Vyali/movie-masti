import csv
import json
data=[]
csv_file = open('generated/keywords.csv','w')
csv_writer = csv.writer(csv_file,quoting=csv.QUOTE_MINIMAL)
row_list=[]
with open('tmdb_5000_movies.csv', newline='') as csvfile:
    movies_reader = csv.reader(csvfile)
    #movies_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
   
    added_val =[]
    i=0
    for row in movies_reader:

        if i==0:
            i=i+1
            continue

        # budget = row[0]
        #genres = json.loads(row[1])
        # homepage = row[2]
        # id = row[3]
        keywords = json.loads(row[4])
        # original_language = row[5]
        # original_title = row[6]
        # overview = row[7]
        # popularity = row[8]
        #production_companies =json.loads(row[9])
        #production_countries = json.loads(row[10])
        # release_date = row[11]
        # revenue = row[12]
        # runtime = row[13]
        # spoken_languages = row[14]
        # status = row[15]
        # tagline = row[16]
        # title = row[17]
        # vote_average = row[18]
        # vote_count = row[19]
        
        # print(keywords)
        # print(type(keywords))
        for row in keywords:
            if row['id'] not in added_val:
                if i==1:
                    i=i+1
                    csv_writer.writerow(row.keys())
                added_val.append(row['id'])
                #row_list.append(company.values())    
                csv_writer.writerow(row.values()) 
        
        
    
csv_file.close()    