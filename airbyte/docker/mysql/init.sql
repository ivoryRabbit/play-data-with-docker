USE dev;

CREATE TABLE IF NOT EXISTS category (
    id INT NOT NULL AUTO_INCREMENT,
    category_name VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO category (category_name) VALUES 
    ('apparel'),
    ('food'),
    ('furniture'),
    ('grocery'),
    ('etc')
;