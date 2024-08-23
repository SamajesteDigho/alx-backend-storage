-- For: Procedure to calculate the weighted average directly
DELIMITER $$
CREATE
PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
    UPDATE users
    JOIN(
        SELECT SUM(pro.score * pro.weight)/SUM(pro.weight) as aws
        FROM (
            SELECT projects.id, projects.weight, corrections.user_id, corrections.score
            FROM projects
            INNER JOIN corrections
            WHERE projects.id =  corrections.project_id
        ) pro
        WHERE pro.user_id = user_id
    ) res
    SET average_score = res.aws
    WHERE id = user_id;
END $$
