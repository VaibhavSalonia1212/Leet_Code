# Write your MySQL query statement below
Select Distinct author_id as id
From Views
where author_id=viewer_id
Order by id;