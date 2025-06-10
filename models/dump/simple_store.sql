-- SQL Datenbank, basierend auf README.md
-- Tabelle "Article", mit:
-- ArticleID, ArticleName, ArticleDescription,
-- Amoung, Price, StorageLocation:
CREATE TABLE Article (
    ArticleID INT PRIMARY KEY AUTO_INCREMENT,
    ArticleName VARCHAR(255) NOT NULL,
    ArticleDescription TEXT,
    Amount INT NOT NULL CHECK (Amount >= 0),
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),
    StorageLocation VARCHAR(255)
);
