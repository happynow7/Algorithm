SELECT TRUNC(PRICE, -4) AS PRICE_GROUP,
       COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY TRUNC(PRICE, -4)
ORDER BY PRICE_GROUP;