CREATE TABLE brand (
    id VARCHAR(50) PRIMARY KEY,
    brandName VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE product (
    id VARCHAR(50) PRIMARY KEY,
    brandID VARCHAR(50) REFERENCES brand(id) ON DELETE SET NULL,
    productName VARCHAR(255) NOT NULL,
    price INTEGER NOT NULL CHECK(price >= 0)
    lastPrice INTEGER NOT NULL CHECK (lastprice >= 0),
    productDescription TEXT,
    discount INTEGER DEFAULT 0 CHECK (discount >= 0),
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    sold INTEGER DEFAULT 0 CHECK (sold >= 0)
);

CREATE TABLE product_image (
    id SERIAL PRIMARY KEY,
    productID VARCHAR(50) REFERENCES product(id) ON DELETE CASCADE,
    imageURL VARCHAR(255) NOT NULL
);