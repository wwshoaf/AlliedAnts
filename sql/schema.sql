/*
Write all DDL CREATE TABLE scripts
sql/schema.sql · Person, Teacher, Customer, Class, Sale, PersonClass
*/
DROP TABLE IF EXISTS Sale;
DROP TABLE IF EXISTS PersonClass;
DROP TABLE IF EXISTS Class;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Teacher;
DROP TABLE IF EXISTS Person;

CREATE TABLE Person (
   name VARCHAR(100) NOT NULL,
   phone VARCHAR(11) NOT NULL, 
   email VARCHAR(50) NOT NULL,
   PRIMARY KEY (name, phone)
);

CREATE TABLE Teacher (
   name VARCHAR(25) NOT NULL,
   phone VARCHAR(11) NOT NULL, 
   number_of_classes_taught INT DEFAULT 0,
   PRIMARY KEY (name, phone),
   FOREIGN KEY (name, phone) REFERENCES Person(name, phone) ON DELETE CASCADE
);

CREATE TABLE Customer (
    name VARCHAR(25) NOT NULL,
    phone VARCHAR(11) NOT NULL, 
    payment_method VARCHAR(50),
    PRIMARY KEY (name, phone),
    FOREIGN KEY (name, phone) REFERENCES Person(name, phone) ON DELETE CASCADE
);

CREATE TABLE Class (
    class_date DATE NOT NULL,
    class_time TIME NOT NULL,
    class_type VARCHAR(50) NOT NULL,
    duration INT,
    attendance INT NOT NULL DEFAULT 0,
    PRIMARY KEY (class_date, class_time)
);

CREATE TABLE PersonClass (
    name VARCHAR(25) NOT NULL,
    phone VARCHAR(11) NOT NULL, 
    pc_date DATE NOT NULL,
    pc_time TIME NOT NULL,
    PRIMARY KEY (name, phone, pc_date, pc_time),
    FOREIGN KEY (name, phone) REFERENCES Person(name, phone) ON DELETE CASCADE,
    FOREIGN KEY (pc_date, pc_time) REFERENCES Class(class_date, class_time) ON DELETE CASCADE
);

CREATE TABLE Sale (
    transaction_id INT AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,
    phone VARCHAR(11) NOT NULL, 
    sale_date DATE,
    sale_time TIME,
    price DECIMAL(10, 2),
    payment_method VARCHAR(50),
    buyer VARCHAR(25),
    type VARCHAR(50),
    PRIMARY KEY (transaction_id),
    FOREIGN KEY (name, phone) REFERENCES Customer(name, phone)
);


