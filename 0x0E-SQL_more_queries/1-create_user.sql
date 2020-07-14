-- creates mysql user user_0d_1
-- comment 2
CREATE USER IF NOT EXISTS
	'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
