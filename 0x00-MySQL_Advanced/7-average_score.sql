-- For: Procedure for computing the Average score for a user
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    UPDATE users
    JOIN(
        SELECT AVG(corrections.score) as mark
        FROM corrections
        WHERE corrections.user_id = user_id
    ) m ON id = user_id
    SET average_score = m.mark
    WHERE id = user_id;
END $$
