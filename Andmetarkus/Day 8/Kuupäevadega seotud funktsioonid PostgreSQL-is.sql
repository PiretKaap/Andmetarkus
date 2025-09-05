-- Kuupäevadega seotud funktsioonid PostgreSQL-is

-- 1.1. Leia müügikogused kuude lõikes -- TO_CHAR funktsionaalsus
select to_char(sale_date, 'YYYY-MM') as yearmonth, sum(quantity) -- to_char - teeb tulemuse tekstiks (to_char -ainult iseloomulik PostgreSQL´ile)
from salestable 
group by to_char(sale_date, 'YYYY-MM')
order by to_char(sale_date, 'YYYY-MM') asc;

--  1.2. HARJUTAMISEKS: Leia müügikogused aastate lõikes
select to_char(sale_date, 'YYYY') as year, sum(quantity)
from salestable 
group by to_char(sale_date, 'YYYY')
order by to_char(sale_date, 'YYYY') asc;

-- 1.3. Kui palju on viimasest müügist möödas?
-- 1.3.1. I võimalus: age funktsioon, annab tekstilise tulemuse
select age(max (sale_date)) -- palju tänaseks on möödas selleks kuupäevaks ehk tänane päev miinus viimane kuupev. (age - ainult iseloomulik PostgreSQL´ile)
from salestable 

-- 1.3.2. II võimalus: current_date ja lahutustehe - annab päevade arvu numbrilise väärtusena
select current_date, max(sale_date), current_date - max(sale_date) as age_in_day
from salestable;

-- 1.4. HARJUTAMISEKS: Kui palju aega on esimesest müügist möödas?
select age(min (sale_date)), current_date - min(sale_date) as age_in_day, min(sale_date)
from salestable;

-- 1.5. Kui palju on tegelikud müügid, eelarve ja nende võrdlus kuude kaupa?
--Loome eelarvetabeli kuude kaupa.
with -- üks kord päringu kohta st., et s ette ei ole with enam vaja.
b as (select to_char(budget_date, 'YYYY-MM') as yearmonth,
sum(budget_sum) as budget_sum
from budget_monthly_salesrep
group by to_char(budget_date, 'YYYY-MM')),  
--Loome müügitabeli kuude kaupa
s as (select to_char(sale_date, 'YYYY-MM') as yearmonth, 
round(sum(quantity*unit_price*(1-discount)):: numeric,0) as sales_sum --
from salestable as s
group by to_char(sale_date, 'YYYY-MM'))	
-- Ühendame loodud tabelid
select b.yearmonth, b.budget_sum, s.sales_sum, s.sales_sum - b.budget_sum as diff_from_budget
from b
left join s on b.yearmonth = s.yearmonth
order by b.yearmonth asc;

--Lisame tulba sales_sum jaoks
ALTER TABLE salestable 						-- millist tabelit muudame.
ADD sales_sum numeric 						-- add=lisame, uue tulba nimi ja formaat
generated always as 						-- alati arvutab välja teiste tulpade põhjal
(quantity*unit_price*(1-discount)) stored;  -- arvutus, tabelisse salvestatud

-- 1.6. HARJUTAMISEKS: Kui palju on tegelikud müügid, eelarve ja nende võrdlus kuude ja müügiesindaja kaupa?
--Loome eelarvetabeli kuude ja müügiesindaja kaupa.
with 
b as (select to_char(budget_date, 'YYYY-MM') as yearmonth,sales_rep_id,
sum(budget_sum) as budget_sum
from budget_monthly_salesrep
group by to_char(budget_date, 'YYYY-MM'), sales_rep_id ),  
--Loome müügitabeli kuude kaupa ja müügiesindaja kaupa.
s as (select to_char(sale_date, 'YYYY-MM') as yearmonth, sales_rep_id,
round(sum(quantity*unit_price*(1-discount)):: numeric,0) as sales_sum 
from salestable as s
group by to_char(sale_date, 'YYYY-MM'),sales_rep_id)	
-- Ühendame loodud tabelid
select b.yearmonth,b.sales_rep_id, b.budget_sum, s.sales_sum, s.sales_sum - b.budget_sum as diff_from_budget
from b
left join s on b.yearmonth = s.yearmonth and b.sales_rep_id = s.sales_rep_id 
order by b.yearmonth asc, b.sales_rep_id asc;


