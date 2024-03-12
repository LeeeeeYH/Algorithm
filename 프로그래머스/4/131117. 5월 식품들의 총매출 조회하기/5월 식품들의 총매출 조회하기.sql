SELECT P.PRODUCT_ID, P.PRODUCT_NAME, P.PRICE * SUM(O.AMOUNT) TOTAL_SALES
FROM FOOD_PRODUCT P
JOIN FOOD_ORDER O
ON P.PRODUCT_ID = O.PRODUCT_ID
WHERE O.PRODUCE_DATE LIKE "2022-05%"
GROUP BY O.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, P.PRODUCT_ID