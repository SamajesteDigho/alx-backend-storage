-- For: Procedure for computing the Average score for a user
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    UPDATE users u
    JOIN(
        SELECT AVG(score) as mark
        FROM corrections
        WHERE user_id = user_id
    ) m ON u.id = user_id
    SET u.average_score = m.mark;
END $$
