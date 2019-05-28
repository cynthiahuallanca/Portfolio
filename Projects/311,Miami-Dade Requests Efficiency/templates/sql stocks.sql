USE second_international_bank;

SELECT * FROM stocks;

SELECT DATA_TYPE 
FROM INFORMATION_SCHEMA.COLUMNS
WHERE 
     TABLE_NAME = 'stocks' AND 
     COLUMN_NAME = 'price';
