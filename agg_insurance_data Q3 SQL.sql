-----aggregated insurance state table Q.3
SELECT * FROM agg_insurance_data;

--SQL Query: Total Insurance Transactions by State and Year
SELECT 
  "State",
  "Year",
  SUM("Transaction_count") AS total_transactions,
  SUM("Transaction_amount") AS total_amount
FROM agg_insurance_data
GROUP BY "State", "Year"
ORDER BY "Year", total_transactions DESC;

--state wise total transaction amount sum top 10 list
SELECT "State", sum("Transaction_amount") as total_amount 
from agg_insurance_data
GROUP BY "State" 
ORDER BY total_amount DESC
LIMIT 10;

--state wise total transaction count sum top 10 list
SELECT "State", sum("Transaction_count") as total_transaction 
from agg_insurance_data
GROUP BY "State" 
ORDER BY total_transaction DESC;

--Year wise total transaction amount (there are 5 types years only)
SELECT "Year", SUM("Transaction_amount") AS total_amount
FROM agg_insurance_data
GROUP BY "Year"
ORDER BY total_amount DESC;

--Quater wise total transaction amount (4 types only)
SELECT "Quarter", SUM("Transaction_amount") AS total_amount
FROM agg_insurance_data
GROUP BY "Quarter"
ORDER BY total_amount DESC;

--top amount - quarter - state
SELECT "State","Quarter","Transaction_type", SUM ("Transaction_amount") as total_amount
FROM agg_insurance_data
GROUP BY "State","Quarter","Transaction_type"
ORDER BY total_amount DESC;

--just order (state , quarter) wise amount
SELECT "State","Quarter","Transaction_type", SUM ("Transaction_amount") as total_amount
FROM agg_insurance_data
GROUP BY "State","Quarter","Transaction_type"
ORDER BY "State","Quarter";

--compare total_amount to past quarter to present (1,2,3,4) with mention [NULL]
SELECT 
"State",
"Quarter",
"Transaction_type",
SUM("Transaction_amount") AS total_amount,
LAG(SUM("Transaction_amount")) OVER(PARTITION BY "State","Transaction_type" ORDER BY "Quarter") AS pervious_quarter_amount
FROM agg_insurance_data
GROUP BY "State","Quarter","Transaction_type"
ORDER BY "State","Quarter","Transaction_type";

--compare to past quarter then find (growth or decline) in state wise order
SELECT 
"State",
"Quarter",
"Transaction_type",
SUM("Transaction_amount") AS total_amount,
LAG(SUM("Transaction_amount")) OVER(PARTITION BY "State","Transaction_type" ORDER BY "Quarter") AS pervious_quarter_amount,
SUM("Transaction_amount")-LAG(SUM("Transaction_amount")) OVER(PARTITION BY "State","Transaction_type" ORDER BY "Quarter") AS growth_or_decline
FROM agg_insurance_data
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
FROM agg_insurance_data
GROUP BY "State","Quarter","Transaction_type"
ORDER BY growth_or_decline DESC;

--**********************************************
SELECT 
  "State",
  "Quarter",
  "Year",
  SUM("Transaction_amount") AS total_amount,
  COUNT(*) AS total_amount_count,
  ROUND(AVG("Transaction_amount")::numeric, 2) AS average_amount,
  MAX("Transaction_amount") AS max_amount,
  MIN("Transaction_amount") AS min_amount
FROM agg_insurance_data
GROUP BY "State", "Quarter", "Year"
ORDER BY total_amount DESC;



