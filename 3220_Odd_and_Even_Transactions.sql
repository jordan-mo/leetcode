--- https://leetcode.com/problems/odd-and-even-transactions/description/
--- Medium
--- Write your MySQL query statement below
SELECT
    a.transaction_date,
    IFNULL((SELECT SUM(b.amount) FROM transactions b WHERE b.amount % 2 != 0 AND b.transaction_date  = a.transaction_date),0) AS odd_sum,
    IFNULL((SELECT SUM(b.amount) FROM transactions b WHERE b.amount % 2 = 0 AND b.transaction_date  = a.transaction_date),0) AS even_sum
FROM transactions a
GROUP BY a.transaction_date
ORDER BY a.transaction_date;