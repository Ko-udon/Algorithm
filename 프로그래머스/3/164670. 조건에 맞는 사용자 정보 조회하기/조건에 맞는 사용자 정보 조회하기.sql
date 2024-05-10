-- 코드를 입력하세요
SELECT G.USER_ID, G.NICKNAME, 
concat(G.CITY, ' ', G.STREET_ADDRESS1, ' ',G.STREET_ADDRESS2) as '전체주소', 
concat(substr(G.TLNO,1,3),'-',substr(G.TLNO,4,4), '-',substr(G.TLNO,8,4))
as '전화번호'
from USED_GOODS_USER as G join USED_GOODS_BOARD as B on G.USER_ID = B.WRITER_ID
group by B.WRITER_ID
having count(B.WRITER_ID) >= 3
order by B.WRITER_ID desc