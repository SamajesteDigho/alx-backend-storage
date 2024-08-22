-- For: Select sting that contins and make some date operations
SELECT `band_name`, (IFNULL(`split`, 2022) - formed) as lifespan
FROM metal_bands
WHERE `style` LIKE '%Glam rock%'
ORDER BY lifespan DESC;
