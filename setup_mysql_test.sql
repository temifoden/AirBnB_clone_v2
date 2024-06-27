-- Drop the user if it exists
DROP USER IF EXISTS 'hbnb_test'@'localhost';

-- Create the database hbnb_dev_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user hbnb_dev if it doesn't exits
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all priviledges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT Privilege on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush priviledges to ensure that all changes take effect
FLUSH PRIVILEGES;
