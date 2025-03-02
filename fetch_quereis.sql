/*What are the top 5 brands by receipts scanned among users 21 and over?*/
/*SELECT products."BRAND", COUNT(*) as receipt_count
FROM transactions 
JOIN products ON transactions."BARCODE" = products."BARCODE"
JOIN users ON transactions."USER_ID" = users."ID"
WHERE EXTRACT(YEAR FROM AGE(users."BIRTH_DATE")) >= 21
GROUP BY products."BRAND"
ORDER BY receipt_count DESC
LIMIT 5;*/


/*UPDATE transactions*/
/*This replaces empty values with 0.00
SET "FINAL_SALE" = '0.00'
WHERE "FINAL_SALE" = '' OR "FINAL_SALE" ~ '[^0-9.]';*/

/*SELECT "USER_ID", 
       COUNT("RECEIPT_ID") AS total_purchases, 
       SUM(COALESCE(NULLIF("FINAL_SALE", ''), '0.00')::NUMERIC) AS total_spent
FROM transactions
GROUP BY "USER_ID"
ORDER BY total_purchases DESC
LIMIT 10;*/



/*What are the top 5 brands by sales among users that have had their account for at least six months?*/

/*SELECT p."BRAND", SUM(CAST(t."FINAL_SALE" AS NUMERIC)) AS total_sales
FROM transactions t
JOIN products p ON t."BARCODE" = p."BARCODE"
JOIN users u ON t."USER_ID" = u."ID"
WHERE u."CREATED_DATE" <= NOW() - INTERVAL '6 months'
GROUP BY p."BRAND"
ORDER BY total_sales DESC
LIMIT 5;*/




/*What is the percentage of sales in the Health & Wellness category by generation?*/
/*SELECT 
    CASE 
        WHEN EXTRACT(YEAR FROM AGE(u."BIRTH_DATE")) >= 58 THEN 'Boomers'
        WHEN EXTRACT(YEAR FROM AGE(u."BIRTH_DATE")) BETWEEN 42 AND 57 THEN 'Gen X'
        WHEN EXTRACT(YEAR FROM AGE(u."BIRTH_DATE")) BETWEEN 26 AND 41 THEN 'Millennials'
        ELSE 'Gen Z'
    END AS generation,
    SUM(CAST(t."FINAL_SALE" AS NUMERIC)) * 100.0 / 
    (SELECT SUM(CAST("FINAL_SALE" AS NUMERIC)) FROM transactions) AS percentage_sales
FROM transactions t
JOIN products p ON t."BARCODE" = p."BARCODE"
JOIN users u ON t."USER_ID" = u."ID"
WHERE p."CATEGORY_1" = 'Health & Wellness'
GROUP BY generation;*/





/*Who are Fetch’s power users?*/
/*Assumptions: Power users are those with high transaction volume and high total spending.*/

/*SELECT u."ID", COUNT(t."RECEIPT_ID") AS total_purchases, 
       SUM(CAST(t."FINAL_SALE" AS NUMERIC)) AS total_spent
FROM transactions t
JOIN users u ON t."USER_ID" = u."ID"
GROUP BY u."ID"
ORDER BY total_purchases DESC, total_spent DESC
LIMIT 10;*/






/*Which is the leading brand in the Dips & Salsa category?*/
/* Assumptions: The leading brand is the one with the highest sales in the "Dips & Salsa" category.*/
/*SELECT p."BRAND", SUM(CAST(t."FINAL_SALE" AS NUMERIC)) AS total_sales
FROM transactions t
JOIN products p ON t."BARCODE" = p."BARCODE"
WHERE p."CATEGORY_2" = 'Dips & Salsa'
GROUP BY p."BRAND"
ORDER BY total_sales DESC
LIMIT 1;*/












