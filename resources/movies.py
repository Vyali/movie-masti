import csv
import json
csv_file = open('generated/movies.csv','w')
csv_writer = csv.writer(csv_file,quoting=csv.QUOTE_MINIMAL)

with open('tmdb_5000_movies.csv', newline='') as csvfile:
    movies_reader = csv.reader(csvfile)
    #movies_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    i=0
    for row in movies_reader:

        if i==0:
            i=i+1
            continue

        budget = row[0]
        genres = json.loads(row[1])
        homepage = row[2]
        id = row[3]
        keywords = json.loads(row[4])
        original_language = row[5]
        original_title = row[6]
        overview = row[7]
        popularity = row[8]
        production_companies = json.loads(row[9])
        production_countries = json.loads(row[10])
        release_date = row[11]
        revenue = row[12]
        runtime = row[13]
        spoken_languages = json.loads(row[14])
        status = row[15]
        tagline = row[16]
        title = row[17]
        vote_average = row[18]
        vote_count = row[19]
        
        countries=[]
        for row in production_countries:
            countries.append(row['iso_3166_1'])
        companies=[]
        for row in production_companies:
            companies.append(row['id'])
        genre_list=[]
        for row in genres:
            genre_list.append(row['id'])

        spoken_lang_list=[]
        for row in spoken_languages:
            spoken_lang_list.append(row['iso_639_1'])         

        keywords_list=[]
        for row in keywords:
            keywords_list.append(row['id'])         
        row=[id,budget,genre_list,homepage,keywords_list,original_language,original_title,overview,popularity,companies,countries,release_date,revenue,runtime,spoken_lang_list,status,vote_average,vote_count,tagline,title]
        csv_writer.writerow(row)               
        
        #print(budget,genres,homepage)
csv_file.close()        