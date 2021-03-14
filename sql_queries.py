# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL PRIMARY KEY,
        start_time TIMESTAMPTZ,
        user_id INT NOT NULL,
        level VARCHAR,
        song_id VARCHAR NULL,
        artist_id VARCHAR NULL,
        session_id NUMERIC NOT NULL,
        location VARCHAR,
        user_agent VARCHAR,
        CONSTRAINT artists_fkey
            FOREIGN KEY(artist_id)
                REFERENCES artists(artist_id),
        CONSTRAINT song_fkey
            FOREIGN KEY(song_id)
                REFERENCES songs(song_id),
        CONSTRAINT users_fkey
            FOREIGN KEY(user_id)
                REFERENCES users(user_id)
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT NOT NULL PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        gender VARCHAR,
        level VARCHAR
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR NOT NULL PRIMARY KEY,
        title VARCHAR,
        artist_id VARCHAR,
        year INT,
        duration NUMERIC(9,5)
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR NOT NULL PRIMARY KEY,
        name VARCHAR,
        location VARCHAR,
        latitude NUMERIC(8,6),
        longitude NUMERIC(9,6)
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMPTZ NOT NULL PRIMARY KEY,
        hour INT,
        day INT,
        week INT,
        month INT,
        year INT,
        weekday VARCHAR
    );
""")

# INSERT RECORDS %s

songplay_table_insert = ("""
    INSERT INTO songplays
        (start_time, user_id, level, song_id, \
        artist_id, session_id, location, user_agent)
    VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT ON CONSTRAINT songplays_pkey
        DO NOTHING;
""")

user_table_insert = ("""
    INSERT INTO users VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id)
        DO UPDATE
        SET level = EXCLUDED.level;
""")

song_table_insert = ("""
    INSERT INTO songs VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT ON CONSTRAINT songs_pkey
            DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT ON CONSTRAINT artists_pkey
            DO NOTHING;
""")

time_table_insert = ("""
    INSERT INTO time VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT ON CONSTRAINT time_pkey
            DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT songs.song_id,
           songs.artist_id
    FROM   songs
    JOIN   artists
    ON     artists.artist_id = songs.artist_id
    WHERE  songs.title = %s
    AND    artists.name = %s
    AND    songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [song_table_create, artist_table_create,
                        time_table_create, user_table_create,
                        songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop,
                      artist_table_drop, time_table_drop]
