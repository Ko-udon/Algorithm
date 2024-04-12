-- 코드를 입력하세요
SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME 
from ANIMAL_INS I, ANIMAL_OUTS O
where I.ANIMAL_ID = O.ANIMAL_ID and I.SEX_UPON_INTAKE LIKE "Intact%" and o.SEX_UPON_OUTCOME in ("Spayed Female","Neutered Male")