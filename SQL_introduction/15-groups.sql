-- Group by . list all the numbers with same score and count them
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score;
