-- map insurance country state table   Q.6
select * from map_insu_country_data; 

--State ,Year , Quarter ,Latitude ,Longitude ,Metric ,District

--State wise total Metric
SELECT "State", SUM("Metric") AS total_insurance_engagement
FROM map_insu_country_data
GROUP BY "State"
ORDER BY total_insurance_engagement DESC;

--Year wise total Metric
SELECT "Year", SUM("Metric") AS total_insurance_engagement
FROM map_insu_country_data
GROUP BY "Year"
ORDER BY total_insurance_engagement DESC;

--Quarter wise total Metric
SELECT "Quarter", SUM("Metric") AS total_insurance_engagement
FROM map_insu_country_data
GROUP BY "Quarter"
ORDER BY total_insurance_engagement DESC;


--District wise total Metric
SELECT "District", SUM("Metric") AS total_insurance_engagement
FROM map_insu_country_data
GROUP BY "District"
ORDER BY total_insurance_engagement DESC;

--Total Insurance Engagement by District
SELECT 
  "State",
  "District",
  "Year",
  SUM("Metric") AS total_insurance_engagement
FROM map_insu_country_data
GROUP BY "State", "District", "Year"
ORDER BY total_insurance_engagement DESC;

--Find Low Performing Districts
SELECT 
  "State",
  "District",
  SUM("Metric") AS total_engagement
FROM map_insu_country_data
GROUP BY "State", "District"
HAVING SUM("Metric") < 20
ORDER BY total_engagement ASC;

--For Geo Mapping (with Latitude & Longitude)
SELECT 
  "State",
  "District",
  "Year",
  "Latitude",
  "Longitude",
  SUM("Metric") AS total_engagement
FROM map_insu_country_data
GROUP BY "State", "District", "Year", "Latitude", "Longitude"
ORDER BY total_engagement DESC;

--******************************************
SELECT 
  "State",
  "District",
  "Quarter",
  "Year",
  SUM("Metric") AS total_engagement,
  COUNT(*) AS metric_count,
  ROUND(AVG("Metric")::numeric, 2) AS average_metric,
  MAX("Metric") AS max_metric,
  MIN("Metric") AS min_metric
FROM map_insu_country_data
GROUP BY "State", "District", "Quarter", "Year";

--********************************************





