# SELECT CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS
SELECT ROUND(AVG(DAILY_FEE)) AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV'