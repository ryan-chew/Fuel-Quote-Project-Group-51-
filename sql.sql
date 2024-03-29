DROP TABLE User;
DROP TABLE Profile;
DROP TABLE Quote;
 
CREATE TABLE User(
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password STRING(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
); 
CREATE TABLE Profile(
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    address1 VARCHAR(255) NOT NULL,
    address2 VARCHAR(255) NOT NULL,)
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    zipcode INT NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    FOREIGN KEY(user_id) REFERENCE User(id)
); 
CREATE TABLE Quote(
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    date INT NOT NULL,
    gallons_requested VARCHAR(255)
    suggest_price VARCHAR(255)
    total_price VARCHAR(255)
    delivery_address VARCHAR(255)
    user_id VARCHAR(255) NOT NULL,
    FOREIGN KEY(user_id) REFERENCE User(id)
);