/*
Write all DDL CREATE TABLE scripts
sql/schema.sql · Person, Teacher, Customer, Class, Sale, PersonClass
*/
CREATE TABLE Person (
   name VARCHAR(25) NOT NULL,
   phone VARCHAR(11) NOT NULL, 
   email VARCHAR(50) NOT NULL,
   PRIMARY KEY (name, phone)
);

CREATE TABLE Teacher (
   name VARCHAR(25) NOT NULL,
   phone VARCHAR(11) NOT NULL, 
   number_of_classes_taught INT DEFAULT 0,
   PRIMARY KEY (name, phone),
   FOREIGN KEY (name, phone) REFERENCES Person(name, phone)
);

CREATE TABLE Customer (
    name VARCHAR(25) NOT NULL,
    phone VARCHAR(11) NOT NULL, 
    payment_method VARCHAR(50),
    PRIMARY KEY (name, phone),
    FOREIGN KEY (name, phone) REFERENCES Person(name, phone)
)

CREATE TABLE Class (
    date DATE NOT NULL,
    time TIME NOT NULL,
    class_type VARCHAR(50) NOT NULL,
    duration INT,
    attendance INT NOT NULL,
    PRIMARY KEY (date, time)
);

CREATE TABLE PersonClass (
    name VARCHAR(25) NOT NULL,
    phone VARCHAR(11) NOT NULL, 
    date DATE NOT NULL,
    time TIME NOT NULL,
    PRIMARY KEY (name, phone, date, time),
    FOREIGN KEY (name, phone) REFERENCES Person(name, phone),
    FOREIGN KEY (date, time) REFERENCES Class(date, time)
);

CREATE TABLE Sale (
    transaction_id INT,
    name VARCHAR(25) NOT NULL,
    phone VARCHAR(11) NOT NULL, 
    date DATE,
    time TIME,
    price DECIMAL(10, 2),
    PRIMARY KEY (name, phone),
    FOREIGN KEY (name, phone) REFERENCES Customer(name, phone)
);
