-- creates the MySQL server user user_0d_1
SELECT EXISTS (
    SELECT 1
    FROM mysql.user
    WHERE user = 'user_0d_1'
) INTO @user_exists;

-- If user doesn't exist, create the user
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%';
    FLUSH PRIVILEGES;
    SELECT 'User user_0d_1 created successfully.';
ELSE
    SELECT 'User user_0d_1 already exists.';
END IF;
