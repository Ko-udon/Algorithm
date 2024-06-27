select
    d.ID, 
    d.EMAIL, 
    d.FIRST_NAME, 
    d.LAST_NAME 
from 
    DEVELOPERS d
where exists (
    select 1
    from SKILLCODES s
    where (d.SKILL_CODE & s.CODE) != 0 
    and (s.NAME = 'Python' or s.NAME = 'C#')
)
ORDER BY d.ID;