select E.DEPT_ID, D.DEPT_NAME_EN, round(avg(E.SAL), 0) as AVG_SAL
from HR_EMPLOYEES as E join HR_DEPARTMENT as D on E.DEPT_ID = D.DEPT_ID
group by DEPT_ID
order by avg(E.SAL) desc