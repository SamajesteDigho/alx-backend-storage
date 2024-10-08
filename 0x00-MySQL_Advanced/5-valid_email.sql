-- For: Trigger for email validation
DELIMITER $$
CREATE
TRIGGER `validate_email_AINS`
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$
