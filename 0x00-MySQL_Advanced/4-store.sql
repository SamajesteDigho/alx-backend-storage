-- For: Creating and applying a trigger
DELIMITER $$
CREATE
TRIGGER `decrease_qty_AINS`
AFTER INSERT ON `orders`
FOR EACH ROW
BEGIN 
    UPDATE `items`
    SET `quantity` = `quantity` - New.number
    WHERE `name` = NEW.item_name;
END$$