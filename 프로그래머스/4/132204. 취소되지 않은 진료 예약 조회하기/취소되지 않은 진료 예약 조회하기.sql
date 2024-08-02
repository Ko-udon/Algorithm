select APNT_NO, PT_NAME, PT_NO, ap.MCDP_CD, DR_NAME, APNT_YMD
from APPOINTMENT as ap

    left join PATIENT as pa using (PT_NO)
    left join DOCTOR as do on do.DR_ID = ap.MDDR_ID
    
where APNT_YMD like '2022-04-13%' and APNT_CNCL_YN = 'N'
order by 6