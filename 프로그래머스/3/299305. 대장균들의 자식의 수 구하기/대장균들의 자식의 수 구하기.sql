-- 코드를 작성해주세요
select P.ID, count(C.ID) as CHILD_COUNT
from ECOLI_DATA as P
LEFT OUTER JOIN ECOLI_DATA AS C ON P.ID = C.PARENT_ID
GROUP BY P.ID
ORDER BY P.ID