select * from top_user_data; -- top user state table Q.8

SELECT
    "State",
    "Year",
    "Quarter",
    "Entity_Type",
    "Entity_Name",
    SUM("Registered_Users") AS total_registered_users,
    ROUND(AVG("Registered_Users")::numeric, 2) AS avg_registered_users_per_entry,
    MAX("Registered_Users") AS max_registered_users,
    MIN("Registered_Users") AS min_registered_users
FROM top_user_data
GROUP BY "State", "Year", "Quarter", "Entity_Type", "Entity_Name"
ORDER BY total_registered_users DESC;


SELECT 
"State",
"Quarter",
"Entity_Type",
"Entity_Name",
SUM("Registered_Users") AS total_amount,
LAG(SUM("Registered_Users")) OVER(PARTITION BY "State","Entity_Type","Entity_Name" ORDER BY "Quarter") AS pervious_quarter_user,
SUM("Registered_Users")-LAG(SUM("Registered_Users")) OVER(PARTITION BY "State","Entity_Type","Entity_Name" ORDER BY "Quarter") AS growth_or_decline
FROM top_user_data
GROUP BY "State","Quarter","Entity_Type","Entity_Name"
ORDER BY growth_or_decline DESC;


