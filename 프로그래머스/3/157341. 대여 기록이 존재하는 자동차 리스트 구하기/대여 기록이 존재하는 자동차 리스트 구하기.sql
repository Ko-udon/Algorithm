-- 코드를 입력하세요
SELECT DISTINCT CAR_ID 
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where CAR_ID in
(select CAR_ID from CAR_RENTAL_COMPANY_CAR where CAR_TYPE = '세단')
and (START_DATE between '2022-10-01' and '2022-10-31')
order by CAR_ID desc