--- https://leetcode.com/problems/combine-two-tables/description/
--- Easy
--- Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Person
LEFT JOIN Address ON Person.personId = Address.personId;