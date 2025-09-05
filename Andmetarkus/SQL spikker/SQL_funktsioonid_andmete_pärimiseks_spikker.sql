-- VALIMINE
-- Valime esimesed 10 rida tabeliga tutvumiseks - LIMIT
SELECT * 
FROM salestable
LIMIT 10; 

-- Valime konkreetsed tulbad - tulba nimed eraldada komadega
SELECT 
	sale_date, 
    product_id, 
    quantity
FROM 
	salestable
LIMIT 10; 

-- Valime unikaalsed väärtused - DISTINCT käsk
SELECT DISTINCT
	product_id
FROM 
	salestable; 

-- FILTREERIMINE - kindlate ridade valimine

-- FILTREERIMINE - KINDEL VÄÄRTUS: Valime kindla toote müügid - WHERE käsk tekstilise välja puhul
SELECT *
FROM 
	salestable
WHERE 
	product_id = 'P001';
    
-- FILTREERIMINE - VÄLISTAMINE: Välistame kindla toote müügid - WHERE käsk tekstilise välja puhul
SELECT *
FROM 
	salestable
WHERE 
	product_id != 'P001';
    
-- FILTREERIMINE - NUMBRLISE VÄÄRTUSE VÕRDLEMINE: Valime ainult müügid, kus kogus on suurem viiest - WHERE käsk numbrilise välja puhul (teised võrdlused: <, <= , >=)
SELECT *
FROM 
	salestable
WHERE 
	quantity > 5;  
    
-- FILTREERIMINE MITME TUNNUSE ALUSEL: Valime kindla toote müügid kindlale kliendile - WHERE ning AND
SELECT *
FROM 
	salestable
WHERE 
	product_id = 'P001' 
    AND customer_id = 'C002';    

-- FILTREERIMINE MITME TUNNUSE ALUSEL: Valime kindla toote müügid VÕI kindla kliendi müügid - WHERE ning OR
SELECT *
FROM 
	salestable
WHERE 
	product_id = 'P001' 
    OR customer_id = 'C002';
    
-- FILTREERIMINE VAHEMIKU ALUSEL: Valime ainult müügid, kus kogus on 5 ja 8 vahepeal - BETWEEN
SELECT *
FROM 
	salestable
WHERE 
	quantity BETWEEN 5 AND 8;  
    
-- FILTREERIMINE - VALIME MITU VÄÄRTUST: Valime mitme kindla toote müügid - IN
SELECT *
FROM 
	salestable
WHERE 
	product_id in ('P001', 'P002', 'P004');
    
-- FILTREERIMINE OSALISE TEKSTI alusel: Valime kõik tooted, mille ID algab 'P00' - LIKE ja % 
SELECT *
FROM 
	salestable
WHERE 
	product_id like 'P00%';

-- FILTREERIMINE - TÕSTUTUNDLIKKUSE EEMALDAMINE: Valime kõik tooted, mille ID algab 'P00' või 'p000' - LOWER või UPPER käsk
SELECT *
FROM 
	salestable
WHERE 
	UPPER(product_id) like 'P00%'; 
    
-- FILTREERIMINE - MITME TINGIMUSE KOMBINEERIMINE: Valime müügid, mis esimese toote puhul on kogusega 2 ja teise toote puhul on kogusega 5 - SULGUDE KASUTAMINE
SELECT *
FROM 
	salestable
WHERE 
	(product_id = 'P001' AND quantity = 2)
	OR (product_id = 'P002' AND quantity = 5);    
    
-- SORTEERIMINE: Sorteerime suurema toote hinnaga müügid ette poole - ORDER BY
SELECT *
FROM 
	salestable
ORDER BY
	unit_price DESC;
    
-- ALIAS - TULBALE UUS NIMI VÄLJUNDIS: Date tulbast SalesDate tulp väljundis - AS
SELECT sale_date AS SalesDate
FROM 
	salestable;  

/* 
Mitmerealise kommentaari lisamine: 
kui tahad mitu rida kommentaari kirjutada, siis alusta / ja * ning lõpeta * ja /
*/ 
SELECT *
FROM 
	salestable
WHERE 
	quantity > 5;
    
-- ARVUTUSED - võimalik teha aritmeetilisi tehteid (+, -, /, *) tulpade loomiseks, filtreerimiseks ja sorteerimiseks
-- ARVUTUS - Leia müügisummad, kus müügisumma on suurem kui 500 ja järjesta müügisumma alusel kasvavalt
SELECT 
	quantity, 
    unit_price, 
    discount, 
    quantity * unit_price * (1 - discount) AS sales_sum
FROM 
	salestable
WHERE
	sales_sum > 500
ORDER BY 
	sales_sum ASC;
    
-- AGREGEERIMINE

-- LOENDAMINE: Kui palju müügitehinguid on tehtud? - COUNT
SELECT COUNT (sale_id) AS tehinguid
FROM 
	salestable;
    
-- UNIKAALSETE VÄÄRTUSTE LOENDAMINE: Kui palju eri tooteid on müüdud? - COUNT (DISTINCT)
SELECT 
	COUNT (DISTINCT product_id) as "Erinevaid tooteid:"
FROM 
	salestable;
    
-- SUMMERIMINE: Kui palju on tooteid müüdud? - SUM
SELECT 
	SUM (quantity) AS "Tooteid müüdud:"
FROM 
	salestable;
    
-- KESKMINE, MIINIMUM, MAKSIMUM: Mis on toodete keskmine, minimaalne ja maksimaalne hind? - AVG, MIN, MAX
SELECT 
	AVG(unit_price) AS average_price, 
    MIN(unit_price) AS minimum_price, 
    MAX(unit_price) AS maximum_price
FROM 
	salestable;
    
-- GRUPEERIMINE: Mis on toodete keskmine, minimaalne ja maksimaalne hind toodete kaupa? - GROUP BY
SELECT 
	product_id,
	AVG(unit_price) AS average_price, 
    MIN(unit_price) AS minimum_price, 
    MAX(unit_price) AS maximum_price
FROM 
	salestable
GROUP BY product_id;

-- AGREGEERTITUD VÄÄRTUSE ALUSEL FILTREERIMINE: Näita ainult tooteid, mille keskmine hind on suurem kui 54.50. - HAVING
SELECT 
	product_id,
	AVG(unit_price) AS average_price, 
    MIN(unit_price) AS minimum_price, 
    MAX(unit_price) AS maximum_price
FROM 
	salestable
GROUP BY product_id
HAVING AVG(unit_price) > 54.5;

-- TÜHI VÄÄRTUS: Näita tooteridu, kus kogus on tühi väärtus - IS NULL või IS NOT NULL
SELECT 
quantity
FROM 
	salestable
WHERE quantity IS NULL;

-- TÜHI VÄÄRTUS: Näita tooteridu, kus kogus ei ole tühi väärtus - IS NOT NULL
SELECT 
quantity
FROM 
	salestable
WHERE quantity IS NOT NULL;

-- VÄÄRTUSE MUUTMINE: Grupeeri tooted kategooriatesse - CASE WHEN 
SELECT 
product_id, 
CASE WHEN product_id = 'P001' THEN 'Category1' 
	 WHEN product_id = 'P002' THEN 'Category2' 
     ELSE 'Category3' END AS product_category
FROM 
	salestable;

-- TABELITE ÜHENDAMINE
-- Kõik read esimesest tabelist ja seotud read teisest tabelist: Kõik eelarveread, seotud müügiesindajad. - LEFT JOIN 
SELECT
budget.sales_rep_id AS budget_sales_rep_id,
budget.budget_sum, 
sales_rep.sales_rep_name, 
sales_rep.sales_rep_id
FROM 
	budgettable AS budget
LEFT JOIN
	salesreptable AS sales_rep
ON budget.sales_rep_id = sales_rep.sales_rep_id;
-- Tulemusena NULL väärtusega müügiesindajate tabelist ID näitab, et müügiesindajate tabelis ei ole antud ID-ga müügiesindajat

-- Kõik read teisest tabelist ja seotud read esimesest tabelist: Kõigi müügiesindajate tabelis olevate müügiesindajate eelarveread - RIGHT JOIN
-- NB! Parem praktika loetavuse mõttes on vahetada tabelite asukohad ja kasutada LEFT JOIN, aga siin demome RIGHT JOIN olemasolu.
SELECT
budget.sales_rep_id AS budget_sales_rep_id,
budget.budget_sum, 
sales_rep.sales_rep_name, 
sales_rep.sales_rep_id
FROM 
	budgettable AS budget
RIGHT JOIN
	salesreptable AS sales_rep
ON budget.sales_rep_id = sales_rep.sales_rep_id;
-- Tulemusena NULL väärtusega eelarvetabelist ID näitab, et eelarvetabelis ei ole antud müügiesindajale rida.


-- Read, mis on olemas mõlemas tabelis: Näita ainult ridu, millel on müügiesindaja nii eelarve tabelis kui ka väärtus müügiesindajate tabelis. - INNER JOIN 
SELECT
budget.sales_rep_id AS budget_sales_rep_id,
budget.budget_sum, 
sales_rep.sales_rep_name, 
sales_rep.sales_rep_id
FROM 
	budgettable AS budget
INNER JOIN
	salesreptable AS sales_rep
ON budget.sales_rep_id = sales_rep.sales_rep_id;
-- Tulemusena ainult üks rida näitab, et ainult ühel müügiesindajal on olemas eelarve ja müügiesindajate tabelis väärtus.

-- Read, mis on olemas ühes või teises tabelis: Näita kõiki eelarveridu ja kõiki müügiesindajate ridu. - FULL OUTER JOIN 
SELECT
budget.sales_rep_id AS budget_sales_rep_id,
budget.budget_sum, 
sales_rep.sales_rep_name, 
sales_rep.sales_rep_id
FROM 
	budgettable AS budget
FULL OUTER JOIN
	salesreptable AS sales_rep
ON budget.sales_rep_id = sales_rep.sales_rep_id;
-- Tulemusena neli rida näitab, et kokku on kahe tabeli peale ära kirjeldatud nelja erineva müügiesindaja ID-d.

-- Read, mis on olemas esimeses tabelis ja teises ei ole: Näita eelarveridu, millele pole müügiesindaja tabelis müügiesindajat kirjeldatud - LEFT JOIN ja IS NULL
SELECT
budget.sales_rep_id AS budget_sales_rep_id,
budget.budget_sum, 
sales_rep.sales_rep_name, 
sales_rep.sales_rep_id
FROM 
	budgettable AS budget
LEFT JOIN
	salesreptable AS sales_rep
ON budget.sales_rep_id = sales_rep.sales_rep_id
WHERE 
	sales_rep.sales_rep_id IS NULL;
-- Saame ühe müügiesindajaID, kes on eelarve tabelis, aga müügiesindajate tabelis pole.

-- Read, mida pole esimeses tabelis, aga on teises tabelis: Näita eelarveridu, millele pole müügiesindaja tabelis müügiesindajat kirjeldatud - RIGHT JOIN ja IS NULL
-- NB! Parem praktika loetavuse mõttes on vahetada tabelite asukohad ja kasutada LEFT JOIN, aga siin demome RIGHT JOIN olemasolu.
SELECT
budget.sales_rep_id AS budget_sales_rep_id,
budget.budget_sum, 
sales_rep.sales_rep_name, 
sales_rep.sales_rep_id
FROM 
	budgettable AS budget
RIGHT JOIN
	salesreptable AS sales_rep
ON budget.sales_rep_id = sales_rep.sales_rep_id
WHERE 
	budget.sales_rep_id IS NULL;
-- Saame kaks müügiesindajat, kellel pole eelarveridu.
   
-- Read, mis on puudu ühest või teisest tabelis: Näita müügiesindajaid, kellel on puudu eelarve või müügiesindaja tabelist rida. - FULL OUTER JOIN, IS NULL ja OR 
SELECT
budget.sales_rep_id AS budget_sales_rep_id,
budget.budget_sum, 
sales_rep.sales_rep_name, 
sales_rep.sales_rep_id
FROM 
	budgettable AS budget
FULL OUTER JOIN
	salesreptable AS sales_rep
ON budget.sales_rep_id = sales_rep.sales_rep_id
WHERE 
	budget.sales_rep_id IS NULL OR sales_rep.sales_rep_id IS NULL;
-- Tulemusena kolm rida näitab, et ühest või teisest tabelist on puudu kolmel real andmed. NULL väärtuste järgi näeb, kummast tabelist info puudu on.

-- Rohkem kui kahe tabeli ühendamine: Näita müüke, millel on olemas müügiesindaja eelarve ja müügiesindaja tabelis. - INNER JOIN iga seotava tabeli vahele
SELECT
sales.sale_id,
budget.sales_rep_id AS budget_sales_rep_id,
sales_rep.sales_rep_name AS SalesRep, 
sales_rep.sales_rep_id
FROM 
	salestable AS sales
INNER JOIN 
	budgettable AS budget
ON sales.sales_rep_id = budget.sales_rep_id
INNER JOIN
	salesreptable AS sales_rep
ON sales.sales_rep_id = sales_rep.sales_rep_id;
-- Tulemusena 3964 müügirida näitab, et vaid 3964 müügireal on olemas sales_rep_id vaste nii eelarve kui ka müügiesindaja tabelis.


-- ALAMPÄRINGUD - viide teisele päringule: Millised töötajad on keskmiselt andnud allahindlust üle 7,5%?
SELECT 
	sales_rep.sales_rep_name
FROM 
	salesreptable AS sales_rep
WHERE sales_rep.sales_rep_id IN ( 
   SELECT sales.sales_rep_id
   FROM 
		salestable AS sales
   GROUP BY 
   	sales.sales_rep_id
   HAVING
   	AVG(sales.discount) > 0.075); 



-- AJUTISED PÄRINGUTULEMUSED (Common Table Expressions - CTEs): : Millised töötajad on keskmiselt andnud allahindlust üle 7,5% ja kui suur on keskmine antud allahindlus?
WITH sales_rep_discount AS (
	SELECT 
  	 	sales.sales_rep_id, 
  	 	AVG(sales.discount) AS average_discount
	FROM 
		salestable AS sales
	GROUP BY 
   	sales.sales_rep_id
	HAVING
   	AVG(sales.discount) > 0.075)
SELECT 
	sales_rep.sales_rep_name, 
    sales_rep_discount.average_discount
FROM 
	salesreptable as sales_rep
INNER JOIN
	sales_rep_discount on sales_rep.sales_rep_id = sales_rep_discount.sales_rep_id;
    
-- TABELITE KOMBINEERIMINE
-- Leia tabelite pealt unikaalsed väärtused: Leia kliendid, kellel oli müüke 2025. aastal või enne 2021. aastat -- UNION
-- UNION jaoks on vaja valida sama palju ja sama tüüpi tulbad tabelitest.
SELECT customer_id
FROM salestable
WHERE sale_date >= '2025-01-01'
UNION
SELECT customer_id
FROM salestable
WHERE sale_date < '2021-01-01';


-- Leia kõik väärtused mitmest tabelist: Leia kõik müügid 2025. aastal või enne 2021. aastat -- UNION ALL
-- UNION ALL jaoks on vaja valida sama palju ja sama tüüpi tulbad tabelitest.
-- Sama saaks saavutada WHERE ja OR käskude abil, aga siin tahame demoda UNION ALL funktsiooni.
SELECT sale_id, customer_id
FROM salestable
WHERE sale_date >= '2025-01-01'
UNION
SELECT sale_id, customer_id
FROM salestable
WHERE sale_date < '2021-01-01';

-- Rohkem funktsioone ja SQL keelte eripärad leiad: https://www.w3schools.com/sql/
    

       
    