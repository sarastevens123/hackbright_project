
CREATE TABLE users(
    user_id INTEGER PRIMARY KEY,
    fname VARCHAR(25) NOT NULL,
    lname VARCHAR(25) NOT NULL,
    user_password VARCHAR(10) NOT NULL
    email VARCHAR(25) NOT NULL,
    birth_date DATE NOT NULL,
    city VARCHAR(25) NOT NULL,
    user_since TIMESTAMP NOT NULL,
    review_count INTEGER,
    score INTEGER 
);

CREATE TABLE restaurants(
    restaurant_id INTEGER PRIMARY KEY,
    external_id INTEGER,
    restaurant_name VARCHAR(25) NOT NULL,
    email VARCHAR(25) NOT NULL,
    restaurant_password VARCHAR(10) NOT NULL,
    restaurant_address VARCHAR(25) NOT NULL,
    restaurant_state VARCHAR(25) NOT NULL,
    city VARCHAR(25) NOT NULL,
    zip_code INTEGER NOT NULL,
    review_count INTEGER,
    score INTEGER 
);

CREATE TABLE restaurant_ratings(
    rating_id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES user,
    restaurant_id INTEGER REFERENCES restaurants,
    rating_score INTEGER NOT NULL,
    rating_text TEXT
);

CREATE TABLE user_ratings(
    rating_id INTEGER PRIMARY KEY,
    restaurant_id INTEGER REFERENCES restaurants,
    user_id INTEGER REFERENCES users,
    user_rating_score INTEGER NOT NULL,
    user_rating_text TEXT NOT NULL
)