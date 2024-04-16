-- 코드를 입력하세요
SELECT b.USER_ID, b.NICKNAME, sum(a.PRICE) as TOTAL_SALES
from USED_GOODS_BOARD as a join USED_GOODS_USER as b on a.WRITER_ID = b.USER_ID
where a.STATUS = 'DONE'
group by a.WRITER_ID
having TOTAL_SALES >= 700000
order by TOTAL_SALES asc