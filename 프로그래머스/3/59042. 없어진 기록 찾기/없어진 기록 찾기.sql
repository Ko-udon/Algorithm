-- 코드를 입력하세요
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS as I RIGHT JOIN ANIMAL_OUTS as O USING(ANIMAL_ID) 
WHERE INTAKE_CONDITION IS NULL
ORDER BY ANIMAL_ID, NAME
