select round(avg(DAILY_FEE)) as AVERAGE_FEE
from CAR_RENTAL_COMPANY_CAR
group by CAR_TYPE
having CAR_TYPE = 'SUV'


