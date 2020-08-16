movie_id,title,cast_list,crew_list
create table dev_schema.credits(
    movie_id INT,
    title VARCHAR(240),
    cast_list VARCHAR(640),
    crew_list VARCHAR(1024),
    PRIMARY KEY(movie_id)
)