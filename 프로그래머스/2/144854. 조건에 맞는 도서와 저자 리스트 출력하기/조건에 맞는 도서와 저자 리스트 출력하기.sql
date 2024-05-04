-- 코드를 입력하세요
SELECT B.BOOK_ID, A.AUTHOR_NAME, DATE_FORMAT(B.PUBLISHED_DATE,'%Y-%m-%d') as PUBLISHED_DATE
from BOOK as B left join AUTHOR as A on A.AUTHOR_ID=B.AUTHOR_ID
where B.CATEGORY='경제'
order by B.PUBLISHED_DATE asc

# SELECT BOOK_ID, AUTHOR_NAME, date_format(PUBLISHED_DATE,'%Y-%m-%d')from BOOK b
# left join AUTHOR a
# on a.AUTHOR_ID = b.AUTHOR_ID
# where CATEGORY = "경제"
# order by PUBLISHED_DATE asc