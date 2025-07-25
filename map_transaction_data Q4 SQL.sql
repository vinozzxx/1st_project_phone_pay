-- map transaction state table Q.4
SELECT * FROM map_transaction_data; 

--state wise total transaction amount sum top 10 list
SELECT "State", sum("Transaction_amount") as total_amount 
from map_transaction_data
GROUP BY "State" 
ORDER BY total_amount ASC;

--state wise total transaction count sum top 10 list
SELECT "State", sum("Transaction_count") as total_count 
from map_transaction_data
GROUP BY "State" 
ORDER BY total_count ASC;

--Year wise total transaction amount (7 types only)
SELECT "Year", SUM("Transaction_amount") AS total_amount
FROM map_transaction_data
GROUP BY "Year"
ORDER BY total_amount DESC;

--Quater wise total transaction amount (4 types only)
SELECT "Quarter", SUM("Transaction_amount") AS total_amount
FROM map_transaction_data
GROUP BY "Quarter"
ORDER BY total_amount DESC;

--Transaction type wise total transaction amount (5 types only)
SELECT "Transaction_type", SUM("Transaction_amount") AS total_amount
FROM map_transaction_data
GROUP BY "Transaction_type"
ORDER BY total_amount DESC;

--
SELECT "State","Quarter","Transaction_type", SUM ("Transaction_amount") as total_amount
FROM map_transaction_data
GROUP BY "State","Quarter","Transaction_type"
ORDER BY total_amount DESC;

--
SELECT "State","Quarter","Transaction_type", SUM ("Transaction_amount") as total_amount
FROM map_transaction_data
GROUP BY "State","Quarter","Transaction_type"
ORDER BY "State","Quarter";

--compare total_amount to past quarter to present (1,2,3,4)
SELECT 
"State",
"Quarter",
"Transaction_type",
SUM("Transaction_amount") AS total_amount,
LAG(SUM("Transaction_amount")) OVER(PARTITION BY "State","Transaction_type" ORDER BY "Quarter") AS pervious_quarter_amount
FROM map_transaction_data
GROUP BY "State","Quarter","Transaction_type"
ORDER BY "State","Quarter","Transaction_type";


SELECT 
"State",
"Quarter",
"Transaction_type",
SUM("Transaction_amount") AS total_amount,
LAG(SUM("Transaction_amount")) OVER(PARTITION BY "State","Transaction_type" ORDER BY "Quarter") AS pervious_quarter_amount,
SUM("Transaction_amount")-LAG(SUM("Transaction_amount")) OVER(PARTITION BY "State","Transaction_type" ORDER BY "Quarter") AS growth_or_decline
FROM map_transaction_data
GROUP BY "State","Quarter","Transaction_type"
ORDER BY "State","Quarter","Transaction_type";

--compare total_amount to past quarter to present (1,2,3,4) show profit or loss 
SELECT 
"State",
"Quarter",
"Transaction_type",
SUM("Transaction_amount") AS total_amount,
LAG(SUM("Transaction_amount")) OVER(PARTITION BY "State","Transaction_type" ORDER BY "Quarter") AS pervious_quarter_amount,
SUM("Transaction_amount")-LAG(SUM("Transaction_amount")) OVER(PARTITION BY "State","Transaction_type" ORDER BY "Quarter") AS growth_or_decline
FROM map_transaction_data
GROUP BY "State","Quarter","Transaction_type"
ORDER BY growth_or_decline DESC;

--state,qtr,trn_type wise  total transaction amount 
SELECT "State","Quarter","Transaction_type" ,SUM("Transaction_amount") AS total_amount
FROM map_transaction_data
GROUP BY "State","Quarter","Transaction_type"
ORDER BY "State","Quarter","Transaction_type";

--**********************************************************
SELECT 
  "State",
  "Quarter",
  "Year",
  SUM("Transaction_amount") AS total_amount,
  COUNT(*) AS total_amount_count,
  ROUND(AVG("Transaction_amount")::numeric, 2) AS average_amount,
  MAX("Transaction_amount") AS max_amount,
  MIN("Transaction_amount") AS min_amount
FROM map_transaction_data
GROUP BY "State", "Quarter", "Year"
ORDER BY total_amount DESC;

