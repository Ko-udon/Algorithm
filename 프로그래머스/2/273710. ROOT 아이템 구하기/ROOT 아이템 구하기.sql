-- 코드를 작성해주세요
select T.ITEM_ID, I.ITEM_NAME
from ITEM_TREE T join ITEM_INFO I on T.ITEM_ID=I.ITEM_ID
where T.PARENT_ITEM_ID is NULL
order by ITEM_ID asc