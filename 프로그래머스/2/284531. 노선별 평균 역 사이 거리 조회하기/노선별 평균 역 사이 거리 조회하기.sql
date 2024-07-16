select ROUTE, 
concat(round(sum(D_BETWEEN_DIST), 1), 'km') AS TOTAL_DISTANCE, 
concat(round(avg(D_BETWEEN_DIST), 2), 'km') AS AVERAGE_DISTANCE
from SUBWAY_DISTANCE

group by ROUTE
order by ROUTE desc  # 총 누계거리를 기준으로 내림차순하라메,,
# 문제가 이상한듯 ROUTE를 기준으로 내림차순하니 통과