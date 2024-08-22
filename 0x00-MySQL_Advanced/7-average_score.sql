-- For: Procedure for computing the Average score for a user
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
    UPDATE `users`
    SET `average_score` = ( SELECT AVG(`score`) FROM `corrections` WHERE `user_id` = user_id )
    WHERE `id` = user_id;
END $$
