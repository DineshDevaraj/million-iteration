
CREATE TABLE `five` (
  `id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `ten` (
  `id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `hundred` (
  `id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `thousand` (
  `id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE DEFINER=`root`@`%` PROCEDURE `fill_table`(tableName varchar(8), maxVal INT)
BEGIN
    
    set @counter := 1;
	set @sqlText := concat("INSERT INTO learning.", tableName, " VALUES (?)");
	prepare sqlStmt from @sqlText;    
    
    WHILE @counter <= maxVal DO
		execute sqlStmt using @counter;
        SET @counter = @counter + 1;
    END WHILE;

END

call fill_table("five", 5);
call fill_table("ten", 10);
call fill_table("hundred`", 100);
call fill_table("thousand", 1000);
