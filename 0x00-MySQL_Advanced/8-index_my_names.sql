-- For: Indexing the name field so as to make it rapidly searcheable
CREATE INDEX idx_name_first ON names (name(1));
