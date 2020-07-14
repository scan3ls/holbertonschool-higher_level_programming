-- creates mysql user user_0d_1
-- comment 2
DROP USER IF EXISTS 'user_0d_1'@'localhost';
CREATE USER 'jeffrey'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
