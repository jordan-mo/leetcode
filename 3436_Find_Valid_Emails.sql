--- Difficulty: Easy
--- https://leetcode.com/problems/find-valid-emails/description/

--- Write your MySQL query statement below
SELECT 
    user_id,
    email
FROM Users
WHERE REGEXP_LIKE(email, '^[a-zA-Z0-9]*@[a-zA-Z]*[.]com$');