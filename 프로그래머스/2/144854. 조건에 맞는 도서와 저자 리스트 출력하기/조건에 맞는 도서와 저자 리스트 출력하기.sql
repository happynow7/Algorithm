SELECT b.BOOK_ID as BOOK_ID, a.AUTHOR_NAME as AUTHOR_NAME, TO_CHAR(b.PUBLISHED_DATE, 'YYYY-MM-DD') AS PUBLISHED_DATE
FROM AUTHOR a JOIN BOOK b ON b.AUTHOR_ID = a.AUTHOR_ID
WHERE b.CATEGORY = '경제'
ORDER BY PUBLISHED_DATE ASC