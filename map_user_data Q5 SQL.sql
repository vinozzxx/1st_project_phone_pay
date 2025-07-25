-- map user state table Q.5
select * from map_user_data;


SELECT 
    "State",
    "Year",
    "Quarter",
    SUM("Users") AS total_registered_users,
    SUM("App_opens") AS total_app_opens,
    ROUND(SUM("App_opens")::NUMERIC / NULLIF(SUM("Users"), 0), 2) AS avg_app_opens_per_user
FROM map_user_data
GROUP BY "State", "Year", "Quarter"
ORDER BY total_registered_users DESC;

SELECT
    "State",
    "Year",
    "Quarter",
    SUM("Users") AS total_registered_users,
    SUM("App_opens") AS total_app_opens,
    ROUND(SUM("App_opens")::NUMERIC / NULLIF(SUM("Users"), 0), 2) AS avg_app_opens_per_user,
    MAX("Users") AS max_users_in_a_district,
    MAX("App_opens") AS max_app_opens_in_a_district,
    MIN("Users") AS min_users_in_a_district,
    MIN("App_opens") AS min_app_opens_in_a_district
FROM map_user_data
GROUP BY "State", "Year", "Quarter"
ORDER BY total_registered_users DESC;
