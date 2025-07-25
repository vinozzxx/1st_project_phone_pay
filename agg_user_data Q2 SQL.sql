-----aggregated user state table Q.2  
SELECT * FROM agg_user_data;


--Brand wise total transaction user_count sum top 
SELECT "Device_Brand", sum("User_Count") as total_user_count 
from agg_user_data
GROUP BY "Device_Brand" 
ORDER BY total_user_count DESC;

--state wise total transaction count sum top 
SELECT "State", sum("User_Count") as total_user_count 
from agg_user_data
GROUP BY "State" 
ORDER BY total_user_count DESC;

--Year wise total transaction amount (5 types only)
SELECT "Year", SUM("User_Count") AS total_user_count
FROM agg_user_data
GROUP BY "Year"
ORDER BY total_user_count DESC;

--Quarter wise total transaction amount (4 types only)
SELECT "Quarter", SUM("User_Count") AS total_user_count
FROM agg_user_data
GROUP BY "Quarter"
ORDER BY total_user_count DESC;

--Registered users wise total transaction count 
SELECT "State","Year","Registered_Users", SUM("User_Count") AS total_user_count
FROM agg_user_data
GROUP BY "State","Year","Registered_Users"
ORDER BY total_user_count DESC;

--state-year-brand user count
SELECT 
  "State",
  "Year",
  "Device_Brand",
  SUM("User_Count") AS total_user_count
FROM agg_user_data
GROUP BY "State", "Year", "Device_Brand"
ORDER BY  total_user_count DESC;


--compare total_user_count to past quarter to present (1,2,3,4)
SELECT 
"State",
"Quarter",
"Device_Brand",
SUM("User_Count") AS total_amount,
LAG(SUM("User_Count")) OVER(PARTITION BY "State","Device_Brand" ORDER BY "Quarter") AS pervious_quarter_user_count
FROM agg_user_data
GROUP BY "State","Quarter","Device_Brand"
ORDER BY "State","Quarter","Device_Brand";

----state-year-quarter  compare total_count to past quarter to present (1,2,3,4) show profit or loss 
SELECT 
"State",
"Quarter",
"Device_Brand",
SUM("User_Count") AS total_amount,
LAG(SUM("User_Count")) OVER(PARTITION BY "State","Device_Brand" ORDER BY "Quarter") AS pervious_quarter_user_count,
SUM("User_Count")-LAG(SUM("User_Count")) OVER(PARTITION BY "State","Device_Brand" ORDER BY "Quarter") AS growth_or_decline
FROM agg_user_data
GROUP BY "State","Quarter","Device_Brand"
ORDER BY "State","Quarter","Device_Brand";

--high compare total_count to past quarter to present (1,2,3,4) show profit or loss 
SELECT 
"State",
"Quarter",
"Transaction_type",
SUM("Transaction_amount") AS total_amount,
LAG(SUM("Transaction_amount")) OVER(PARTITION BY "State","Transaction_type" ORDER BY "Quarter") AS pervious_quarter_amount,
SUM("Transaction_amount")-LAG(SUM("Transaction_amount")) OVER(PARTITION BY "State","Transaction_type" ORDER BY "Quarter") AS growth_or_decline
FROM agg_transaction_data
GROUP BY "State","Quarter","Transaction_type"
ORDER BY growth_or_decline DESC;


--Bonus (Filter by Year or State)
SELECT 
  "State",
  "Year",
  "Device_Brand",
  SUM("User_Count") AS total_user_count
FROM agg_user_data
WHERE "Year" = '2021'
GROUP BY "State", "Year", "Device_Brand"
ORDER BY "State", total_user_count DESC;

--find engagement rate
SELECT 
  "State",
  "Year",
  "Quarter",
  "Device_Brand",
  SUM("Registered_Users") AS total_registered,
  SUM("App_Opens") AS total_opens,
  ROUND(SUM("App_Opens") * 100.0 / NULLIF(SUM("Registered_Users"), 0), 2) AS engagement_rate
FROM agg_user_data
GROUP BY "State", "Year", "Device_Brand","Quarter"
ORDER BY "State","Quarter", "Year", engagement_rate;

--***********************************************************
SELECT
     "State", 
	 "Quarter",
	 "Year",
	 "Device_Brand",
	SUM("User_Count") AS total_user,
    COUNT(*) AS list_count,
    ROUND(AVG("User_Count")::numeric, 2) AS average_user,
    MAX("User_Count") AS max_user,
    MIN("User_Count") AS min_user
FROM agg_user_data
GROUP BY "State", "Quarter", "Year","Device_Brand"
ORDER BY total_user DESC;



