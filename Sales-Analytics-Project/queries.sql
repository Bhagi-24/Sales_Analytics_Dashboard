CREATE DATABASE sales_project;
USE sales_project;
SHOW TABLES;
SELECT DATABASE();
FROM sales;
SELECT * FROM sales LIMIT 5;
TRUNCATE TABLE sales;
SELECT COUNT(*) FROM sales;
SELECT * FROM sales LIMIT 5;
SELECT SUM(Sales) AS total_sales FROM sales;
SELECT SUM(Profit) AS total_profit FROM sales;
SELECT Category, SUM(Sales)
FROM sales
GROUP BY Category;
SELECT Customer_Name, SUM(Sales) AS total_sales
FROM sales
GROUP BY Customer_Name
ORDER BY total_sales DESC
LIMIT 5;
SELECT Month, SUM(Sales)
FROM sales
GROUP BY Month
ORDER BY Month;
SELECT SUM(Sales) FROM sales;
SELECT SUM(Profit) FROM sales;
SELECT Region, SUM(Sales)
FROM sales
GROUP BY Region;
SELECT Product_Name, SUM(Sales)
FROM sales
GROUP BY Product_Name
ORDER BY SUM(Sales) DESC
LIMIT 5;
SELECT Month, SUM(Sales)
FROM sales
GROUP BY Month;