SELECT A.APNT_NO AS APNTNO, 
       P.PT_NAME AS PTNAME, 
       A.PT_NO AS PTNO, 
       A.MCDP_CD AS MCDPCD, 
       D.DR_NAME AS DRNAME, 
       A.APNT_YMD AS APNTYMD
FROM PATIENT P
JOIN APPOINTMENT A ON P.PT_NO = A.PT_NO
JOIN DOCTOR D ON A.MDDR_ID = D.DR_ID
WHERE TO_CHAR(A.APNT_YMD, 'YYMMDD') = '220413' 
  AND A.APNT_CNCL_YN = 'N' 
  AND A.MCDP_CD = 'CS'
ORDER BY A.APNT_YMD ASC