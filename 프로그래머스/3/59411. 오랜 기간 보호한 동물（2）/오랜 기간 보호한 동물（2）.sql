select animal_id, name
from (
    SELECT I.ANIMAL_ID, I.NAME
    from ANIMAL_INS I
    join ANIMAL_OUTS O
    on I.ANIMAL_ID = O.ANIMAL_ID
    order by O.DATETIME - I.DATETIME DESC
)
where rownum <= 2