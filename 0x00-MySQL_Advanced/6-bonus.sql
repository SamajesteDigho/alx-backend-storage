-- For: Create procedure to add new row on table under certain circumstances
DELIMITER $$
CREATE PROCEDURE addBonus(
    user_id INT,
    project_name VARCHAR(255),
    score FLOAT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM projects WHERE name = project_name) THEN
        INSERT INTO projects(name) VALUES (project_name);
    END IF;
    INSERT INTO corrections
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name LIMIT 1), score);
END $$
