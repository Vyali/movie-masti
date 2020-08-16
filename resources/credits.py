import csv
import json
data=[]
csv_file = open('generated/credits.csv','w')
csv_writer = csv.writer(csv_file,quoting=csv.QUOTE_MINIMAL)
row_list=[]
with open('tmdb_5000_credits.csv', newline='') as csvfile:
    credit_reader = csv.reader(csvfile)
    #movies_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
   
    added_val =[]
    i=0
    for row in credit_reader:

        if i==0:
            i=i+1
            continue

        movie_id=row[0]
        title=row[1]
        cast=json.loads(row[2])
        crew=json.loads(row[3])
        
        cast_list=[]
        for row in cast:
            cast_list.append(row['id'])  
        crew_list=[]
        for row in cast:
            crew_list.append(row['id'])  
        row = [movie_id,title,cast_list,crew_list]
        csv_writer.writerow(row)        

    
csv_file.close()    