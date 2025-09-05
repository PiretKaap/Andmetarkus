-- Leia müügisummad toodete kaupa
select  product_id, round(sum(quantity*unit_price*(1-discount)):: numeric,0) as sales_sum
from salestable 
group by product_id
order by product_id ;

--Leia müügisummad klientide kaupa
select  customer_id , round(sum(quantity*unit_price*(1-discount)):: numeric,0) as sales_sum
from salestable 
group by customer_id
order by sales_sum desc ;

--Leia müügisummad müügiesindajate kaupa
select  sales_rep_id , round(sum(quantity*unit_price*(1-discount)):: numeric,0) as sales_sum
from salestable 
group by sales_rep_id
order by sales_rep_id asc ;

--Leia müügisummad aastate kaupa
select to_char(sale_date, 'YYYY') as year, round(sum(quantity*unit_price*(1-discount)):: numeric,0)
from salestable 
group by to_char(sale_date, 'YYYY')
order by to_char(sale_date, 'YYYY') asc;

-- II variant
SELECT EXTRACT (YEAR FROM sale_date) AS "year", round(sum(sales_sum),0)
from salestable
GROUP BY "year"
ORDER BY "year";

-- Lisa müükidele müügisumma kategooriad
--Large Sale > 500
--Medium Sale <= 500 and >= 250
--Small Sale < 250

select sales_sum,
case
    when sales_sum  > 500 then 'Large Sale'
    when sales_sum <= 500 and sales_sum >= 250 then 'Medium Sale'
    else 'Small Sale'
end as sales_category
from salestable;

--Leia müükide arv ja müügisumma müügisumma kategooriate kaupa
WITH 
sales_with_categories AS (select sales_sum
    FROM salestable)
SELECT
    CASE
        WHEN sales_sum > 500 THEN 'Large Sale'
        WHEN sales_sum >= 250 THEN 'Medium Sale'
        ELSE 'Small Sale'
    END AS sales_category,
    COUNT(*) as number_of_sales ,
    round(SUM(sales_sum),0) as sales_sum
FROM sales_with_categories
GROUP BY sales_category
order by sales_category desc;

select 
case 
	when sales_sum > 500 then 'Large Sale'
	when sales_sum >= 250 then 'Medium Sale'
	else 'Small Sale' end as sales_category,
	count(*) as number_of_sales,
	round(sum(sales_sum),0) as sales_sum
	from salestable
	group by sales_category
	order by sales_category desc;

-- Mida veel võiks leida?
