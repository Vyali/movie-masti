import csv
import json
data=[]
csv_file = open('generated/crew.csv','w')
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

        # movie_id=row[0]
        # title=row[1]
        # cast=json.loads(row[2])
        crew=json.loads(row[3])
        
        # print(crew)
        # print(type(crew))
        for row in crew:
            if row['id'] not in added_val:
                if i==1:
                    i=i+1
                    csv_writer.writerow(row.keys())
                added_val.append(row['id'])
                #row_list.append(company.values())    
                csv_writer.writerow(row.values()) 
        
            
    
csv_file.close()    