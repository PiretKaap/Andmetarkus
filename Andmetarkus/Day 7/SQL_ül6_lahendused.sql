-- 11. ALAMPÄRINGUD - viide teisele päringule:
-- Millised töötajad on keskmiselt andnud allahindlust üle 7,5%?
select sales_rep_name			-- 2. Töötaja nimi, kes on müügiesindajate tabelis
from salesreptable 
where sales_rep_id in (			-- 3. Kontrollib, kas töötaja nimele vastav id on alapäringus. 
	select sales_rep_id 		-- 1. Alampäring ehk töötaja id, kelle keskmine allahindlus on üle 7.5%
	from salestable 
	group by sales_rep_id 
	having avg (discount) >0.075);

-- 12. AJUTISED PÄRINGUTULEMUSED (Common Table Expressions - CTEs): 
--: Millised töötajad on keskmiselt andnud allahindlust üle 7,5% ja kui suur on keskmine antud allahindlus?
with salesrepdiscount as (
	select sales_rep_id, avg (discount) as avg_discount
	from salestable 
	group by sales_rep_id 
	having avg(discount) >0.075)
select salesreptable.sales_rep_id, salesrepdiscount.avg_discount, salesrepdiscount.sales_rep_id 
from salesrepdiscount
left join salesreptable on salesrepdiscount.sales_rep_id = salesreptable.sales_rep_id;

--Harjutamiseks: Tegelikud müügid vs eelarve müügiesindaja kaupa.
with realsale as (
	select sales_rep_id, round(sum(unit_price *quantity*(1-discount)) :: numeric, 0) as sales
	from salestable 
	group by sales_rep_id )
select realsale.sales_rep_id, budgettable.budget_sum , realsale.sales, budgettable.sales_rep_id   
from realsale 
full outer join budgettable  on realsale.sales_rep_id = budgettable.sales_rep_id;


-- 13. TABELITE KOMBINEERIMINE
-- 13.1. Leia tabelite pealt unikaalsed väärtused: 
--Leia kliendid, kellel oli müüke 2025. aastal või enne 2021. aastat -- UNION
select customer_id, product_id, sum(quantity )
from salestable 
where sale_date >='2025-01-01'
group by customer_id , product_id 
union 
select customer_id, product_id, sum(quantity )
from salestable
where sale_date <'2021-12-31'
group by customer_id , product_id ;

-- 13.2. Leia kõik väärtused mitmest tabelist: 
--Leia kõik müügid 2025. aastal või enne 2021. aastat -- UNION ALL
select *
from salestable 
where sale_date >='2025-01-01'
union all
select *
from salestable
where sale_date <'2021-12-31';
