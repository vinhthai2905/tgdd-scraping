CREATE TABLE brand (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE product (
    id VARCHAR(50) PRIMARY KEY,
    brandid VARCHAR(50) REFERENCES brand(id) ON DELETE SET NULL,
    name VARCHAR(255) NOT NULL,
    lastprice INTEGER NOT NULL CHECK (lastprice >= 0),
    description TEXT,
    discount INTEGER DEFAULT 0 CHECK (discount >= 0),
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    sold INTEGER DEFAULT 0 CHECK (sold >= 0)
);

CREATE TABLE productimage (
    id SERIAL PRIMARY KEY,
    productid VARCHAR(50) REFERENCES product(id) ON DELETE CASCADE,
    url VARCHAR(255) NOT NULL
);