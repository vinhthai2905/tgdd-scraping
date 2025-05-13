
CREATE DATABASE productDB;
USE productDB;

CREATE TABLE brand (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE product (
    id VARCHAR(50) PRIMARY KEY,
    brandId VARCHAR(50) REFERENCES brand(id),
    name VARCHAR(255) NOT NULL,
    lastPrice INTEGER NOT NULL,
    description TEXT,
    discount INTEGER DEFAULT 0,
    quantity INTEGER NOT NULL,
    sold INTEGER DEFAULT 0
);

CREATE TABLE productImage (
    id SERIAL PRIMARY KEY,
    productId VARCHAR(50) REFERENCES product(id),
    url VARCHAR(255) NOT NULL
);
