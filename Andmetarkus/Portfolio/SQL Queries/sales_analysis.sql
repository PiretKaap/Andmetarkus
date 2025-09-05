-- This SQL query is for exploring sales data and comparing it to budget data.

-- 1. Using LIMIT to check the first 10 rows of the tables to get an overall understanding of:
-- 1.1 SalesTable
SELECT * 
FROM SalesTable 
LIMIT 10;
-- 1.2 SalesRepTable
SELECT *
FROM SalesRepTable
LIMIT 10;
-- 1.3 BudgetSalesRep
SELECT *
FROM BudgetSalesRep
LIMIT 10;

-- 2. Finding total sales by each sales year.
SELECT EXTRACT(YEAR FROM sale_date) AS sales_year, 
       ROUND(SUM(unit_price * quantity * (1 - discount))::numeric, 0) AS total_sales
FROM SalesTable
GROUP BY sales_year
ORDER BY sales_year asc;

--3. Coparing total sales by each sales year to the total budgeted sales eash year.
with b as(
    SELECT EXTRACT(YEAR FROM sale_date) AS budget_year, 
           ROUND(SUM(budget_sum_eur)::numeric, 0) AS total_budget
           FROM budget_table
              GROUP BY budget_year)