-- 10. TABELITE ÜHENDAMINE
-- 10.1. Kõik eelarveread eelarve tabelist ja nendega seotud müügiesindaja nimi müügiesindajate tabelist.
SELECT *
FROM salesreptable  
RIGHT JOIN budgettable  
ON salesreptable.sales_rep_id 
= budgettable.sales_rep_id ;

-- 10.3. Kõik müügiesindajad müügiesindajate tabelist ja nendega seotud eelarveread eelarve tabelist.
SELECT * 
FROM salesreptable  
LEFT JOIN budgettable  
ON salesreptable.sales_rep_id 
= budgettable.sales_rep_id ;

-- 10.4. Näita ainult ridu, millel on müügiesindaja nii eelarve tabelis kui ka väärtus müügiesindajate tabelis.
SELECT * 
FROM salesreptable  
inner JOIN budgettable  
ON salesreptable.sales_rep_id 
= budgettable.sales_rep_id ;

-- 10.5. Näita kõiki ridu eelarve tabelist ja kõiki ridu müügiesindaja tabelist.
SELECT * 
FROM salesreptable  
full outer JOIN budgettable  
ON salesreptable.sales_rep_id 
= budgettable.sales_rep_id ;

-- 10.6. Näita ridu eelarve tabelist, millele pole müügiesindaja tabelis müügiesindajat kirjeldatud.
SELECT * 
FROM salesreptable  
Right JOIN budgettable  
ON salesreptable.sales_rep_id 
= budgettable.sales_rep_id 
where salesreptable.sales_rep_id is NULL;

-- 10.7. Näita ridu müügiesindaja tabelist, millele pole kirjeldatud ridu eelarve tabelis.
SELECT * 
FROM salesreptable  
Left JOIN budgettable  
ON salesreptable.sales_rep_id 
= budgettable.sales_rep_id 
where budgettable.sales_rep_id is NULL;

-- 10.8. Näita müügiesindajaid, kellel on puudu eelarve või müügiesindaja tabelist rida.
SELECT * 
FROM salesreptable  
full outer JOIN budgettable  
ON salesreptable.sales_rep_id 
= budgettable.sales_rep_id 
where budgettable.sales_rep_id is null
or salesreptable.sales_rep_id is NULL;

-- 10.9. Näita ridu müügitabelist, millel on olemas müügiesindaja info eelarve ja müügiesindaja tabelis.
SELECT *
FROM salestable s
Inner JOIN budgettable b ON s.sales_rep_id = b.sales_rep_id 
Inner JOIN salesreptable c ON s.sales_rep_id = c.sales_rep_id;
