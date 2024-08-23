-- For: Procedure to calculate the weighted average directly for all the students
DELIMITER $$
CREATE
PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
    JOIN (
        SELECT res.id, SUM(res.score * res.weight)/SUM(res.weight) as aws
        FROM (
            SELECT users.id, projects.id as project_id, projects.weight as weight, corrections.user_id as user_id, corrections.score
            FROM users
            INNER JOIN corrections, projects
            WHERE projects.id = corrections.project_id AND users.id = corrections.user_id
        ) res
        GROUP BY res.id
    ) ans
    SET average_score = ans.aws
    WHERE users.id = ans.id;
END $$
