id,budget,genre_list,homepage,keywords_list,original_language,original_title,overview,popularity,companies,countries,release_date,revenue,runtime,spoken_lang_list,status,vote_average,vote_count,tagline,title


create table dev_schema.movies(
    id INT,
    budget NUMBER
    genre_list VARCHAR(1024)
    homepage VARCHAR(1024)
    keywords_list VARCHAR(1024)
    original_language VARCHAR(1024)
    original_title VARCHAR(1024)
    overview VARCHAR(1024)
    popularity VARCHAR(1024)
    companies VARCHAR(1024)
    countries VARCHAR(1024)
    release_date VARCHAR(1024)
    revenue VARCHAR(1024)
    runtime VARCHAR(1024)
    spoken_lang_list VARCHAR(1024)
    status VARCHAR(240)
    vote_average VARCHAR(240)
    vote_count VARCHAR(240)
    tagline VARCHAR(640)
    title VARCHAR(240)
    

    
    PRIMARY KEY (id)
)