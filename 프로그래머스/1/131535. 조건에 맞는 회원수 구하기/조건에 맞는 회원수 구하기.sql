SELECT COUNT(user_id) as users
FROM user_info
where  age between 20 and 29 and joined between to_date('2021-01-01', 'yyyy-mm-dd') and to_date('2021-12-31', 'yyyy-mm-dd')