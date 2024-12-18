
-- Create database
USE cse5720;
/*
-- User Table
CREATE TABLE User (
    u_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

-- Service Table
CREATE TABLE Service (
    s_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    s_date DATE NOT NULL,
    u_id INT,
    FOREIGN KEY (u_id) REFERENCES User(u_id)
);



-- Address Table
CREATE TABLE Address (
    a_id INT AUTO_INCREMENT PRIMARY KEY,
    street VARCHAR(150),
    city VARCHAR(100),
    state VARCHAR(100)
);

-- Deposit Table
CREATE TABLE Deposit (
    d_id INT AUTO_INCREMENT PRIMARY KEY,
    method VARCHAR(50) NOT NULL,user
    amount DECIMAL(10, 2) NOT NULL,
    u_id INT,
    a_id INT,
    FOREIGN KEY (u_id) REFERENCES User(u_id),
    FOREIGN KEY (a_id) REFERENCES Address(a_id)
);

-- Tracking Detail Table
CREATE TABLE Tracking_Detail (
    t_id INT AUTO_INCREMENT PRIMARY KEY,
    status VARCHAR(50) NOT NULL,
    s_id INT,
    FOREIGN KEY (s_id) REFERENCES Service(s_id)
);

-- Service Category Table
CREATE TABLE Service_Category (
    c_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Order-Service (M:M relationship between Service and Category)
CREATE TABLE Order_Service (
    order_no INT AUTO_INCREMENT PRIMARY KEY,
    s_id INT,
    c_id INT,
    FOREIGN KEY (s_id) REFERENCES Service(s_id),
    FOREIGN KEY (c_id) REFERENCES Service_Category(c_id)
);

SET GLOBAL sql_mode = 'ALLOW_INVALID_DATES';
*/