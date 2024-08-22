-- For: Creating indexing on name and score fields
CREATE
INDEX idx_name_first_score
ON names (
    names(1),
    score(1)
)