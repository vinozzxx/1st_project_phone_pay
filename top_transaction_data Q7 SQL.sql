select * from top_transaction_data; -- top transaction state table Q.7

--Top 10 districts by transaction amount (Latest Quarter)
SELECT 
    "State",
    "Year",
    "Quarter",
    "Entity_Name" AS District,
    SUM("Transaction_Count") AS total_transactions,
    SUM("Transaction_Amount") AS total_amount
FROM top_transaction_data
WHERE "Entity_Type" = 'districts'
GROUP BY "State", "Year", "Quarter", "Entity_Name"
ORDER BY total_amount DESC
LIMIT 10;

--Top 10 pincodes by insurance activity
SELECT 
    "State",
    "Year",
    "Quarter",
    "Entity_Name" AS Pincode,
    SUM("Transaction_Count") AS total_transactions,
    SUM("Transaction_Amount") AS total_amount
FROM top_transaction_data
WHERE "Entity_Type" = 'pincodes'
GROUP BY "State", "Year", "Quarter", "Entity_Name"
ORDER BY total_amount DESC
LIMIT 10;

--State-wise total insurance transaction summary
SELECT 
    "State",
    SUM("Transaction_Count") AS total_transactions,
    SUM("Transaction_Amount") AS total_amount
FROM top_transaction_data
GROUP BY "State"
ORDER BY total_amount DESC;

--
SELECT
    "State",
    "Year",
    "Quarter",
    "Entity_Type",
    "Entity_Name",
    SUM("Transaction_Count") AS Transaction_Count,
    SUM("Transaction_Amount") AS Transaction_Amount
FROM top_transaction_data
GROUP BY "State","Year","Quarter","Entity_Type","Entity_Name"
ORDER BY Transaction_Count DESC;

SELECT
    "State",
    "Year",
    "Quarter",
    "Entity_Type",
    "Entity_Name",
    SUM("Transaction_Count") AS Total_Transactions,
    SUM("Transaction_Amount") AS Total_Amount
FROM top_transaction_data
WHERE "Year" = '2020' AND "Quarter" = '3'  -- You can change year and quarter here
GROUP BY "State", "Year", "Quarter", "Entity_Type", "Entity_Name"
ORDER BY Total_Transactions DESC;


SELECT
    "State",
    "Year",
    "Quarter",
	"Entity_Type",
	"Entity_Name",
    SUM("Transaction_Count") AS total_transactions,
    ROUND(SUM("Transaction_Amount")::numeric, 2) AS total_amount,
    ROUND(AVG("Transaction_Count")::numeric, 2) AS avg_transactions_per_entry,
    ROUND(AVG("Transaction_Amount")::numeric, 2) AS avg_amount_per_entry,
    MAX("Transaction_Count") AS max_transactions,
    MAX("Transaction_Amount") AS max_amount,
    MIN("Transaction_Count") AS min_transactions,
    MIN("Transaction_Amount") AS min_amount
FROM top_transaction_data
GROUP BY "State","Year", "Quarter","Entity_Type","Entity_Name"
ORDER BY total_transactions DESC;
