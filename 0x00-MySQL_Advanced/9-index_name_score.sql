-- For: Creating indexing on name and score fields
CREATE
INDEX idx_name_first_score
ON names (name(1), score)
