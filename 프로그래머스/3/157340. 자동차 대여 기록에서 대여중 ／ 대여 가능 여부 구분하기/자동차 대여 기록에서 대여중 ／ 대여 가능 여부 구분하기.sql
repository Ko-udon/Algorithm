select car_id,
    case when 
    sum(case when '2022-10-16' between start_date and end_date then 1
    else 0 end) =1 then '대여중'
    else '대여 가능'
    end availability
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by 1
order by 1 desc;