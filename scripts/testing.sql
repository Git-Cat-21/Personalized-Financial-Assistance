USE pfa_orange;

-- if you run into an error saying ck1 constraint is violated please run the following commands 

-- SET FOREIGN_KEY_CHECKS = 0;

-- ALTER TABLE user_details DROP CONSTRAINT ck1;

-- SET FOREIGN_KEY_CHECKS = 1;

-- ALTER TABLE SAVINGS_DETAILS MODIFY COLUMN Maturity_Amount FLOAT;

-- DESC savings_details;
-- ALTER TABLE SAVINGS_DETAILS MODIFY COLUMN Maturity_Date DATE;

-- ALTER TABLE savings_details ADD COLUMN Scheme_ID INT NOT NULL AFTER Mobile_number;

-- ALTER TABLE savings_details MODIFY COLUMN Mobile_Number AFTER User_ID_savings;


desc savings_details;
desc account_details;
DESC user_details;

desc transactions;
SELECT* from account_details;
SELECT* FROM user_details;
SELECT* FROM savings_details;
SELECT* FROM transactions;
DROP TABLE transactions;
DELETE from user_details;
SHOW TABLES;