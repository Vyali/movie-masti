import csv
import json
data=[]
csv_file = open('generated/prod-companies.csv','w')
csv_writer = csv.writer(csv_file,quoting=csv.QUOTE_MINIMAL)
row_list=[]
with open('tmdb_5000_movies.csv', newline='') as csvfile:
    movies_reader = csv.reader(csvfile)
    #movies_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
    added_val=[]
        
    i=0
    for row in movies_reader:

        if i==0:
            i=i+1
            continue

        # budget = row[0]
        # genres = row[1]
        # homepage = row[2]
        # id = row[3]
        # keywords = row[4]
        # original_language = row[5]
        # original_title = row[6]
        # overview = row[7]
        # popularity = row[8]
        production_companies =json.loads(row[9])
        # production_countries = row[10]
        # release_date = row[11]
        # revenue = row[12]
        # runtime = row[13]
        # spoken_languages = row[14]
        # status = row[15]
        # tagline = row[16]
        # title = row[17]
        # vote_average = row[18]
        # vote_count = row[19]
        
        # print(type(production_companies))
        
        #print(production_companies)
        for company in production_companies:
            if company['id'] not in added_val:
               
                added_val.append(company['id'])
                #row_list.append(company.values())    
                csv_writer.writerow(company.values())   
        
        
# for row in row_list:
#     csv_writer.writerow(row)            
csv_file.close()    