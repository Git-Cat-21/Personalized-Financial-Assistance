CREATE DATABASE IF NOT EXISTS pfa_orange;

USE pfa_orange;
show TABLEs;

CREATE TABLE USER_DETAILS(
    User_ID INT PRIMARY KEY,
    User_name VARCHAR(50),
    Mob long,
    Email_id VARCHAR(30) constraint ck2 check(Email_id like '%_@__%.__%'),
    Dob DATE,
    Pwd VARCHAR(20)
);
-- if you run into an error saying ck1 constraint is violated please run the following commands 

-- SET FOREIGN_KEY_CHECKS = 0;

-- ALTER TABLE user_details DROP CONSTRAINT ck1;

-- SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE ACCOUNT_DETAILS(
    acc_no BIGINT UNIQUE,
    ifsc VARCHAR(20),
    acc_status ENUM('Active','Inactive'),
    acc_type ENUM('Savings','Current'),
    acc_create DATE,
    user_id int,
    Foreign Key (user_id) REFERENCES user_details(User_ID)
    ON DELETE CASCADE
);
ALTER TABLE account_details ADD COLUMN pan CHAR(10) AFTER ifsc;

CREATE TABLE schemes(
    Scheme_ID INT PRIMARY KEY,
    Scheme_Name VARCHAR(40),
    Interest_Rate FLOAT NOT NULL,
    Duration_In_Years FLOAT NOT NULL
);

INSERT INTO schemes (Scheme_ID,Scheme_Name,Interest_Rate, Duration_In_Years) VALUES
(1,'SecureBank FD', 6.5, 1),
(2,'GoldTrust Growth FD', 7.0, 2),
(3,'SafeInvest Future Plan', 7.5, 5),
(4,'TrustCapital Secure FD', 6.8, 3),
(5,'PrimeBank Senior Citizen FD', 8.0, 2),
(6,'GrowthBank Fixed Plan', 8.2, 10),
(7,'HorizonFinance Flexi FD', 5.0, 6),
(8,'FirstChoice Wealth FD', 7.2, 1),
(9,'ValueSafe High Return FD', 6.75, 1),
(10,'CapitalMax Booster FD', 7.1, 3);

-- SET FOREIGN_KEY_CHECKS = 0;

-- UPDATE  schemes set Duration_In_Years=2 WHERE Scheme_id=5;
-- UPDATE  schemes set Duration_In_Years=1 WHERE Scheme_id=8;

-- SET FOREIGN_KEY_CHECKS = 1;

SELECT * FROM schemes;

CREATE TABLE SAVINGS_DETAILS (
    SI_no INT PRIMARY KEY AUTO_INCREMENT,
    User_ID_savings INT NOT NULL,
    Account_Number BIGINT NOT NULL,
    Mobile_Number BIGINT NOT NULL, -- Ensuring it's a 10-digit number
    Amount FLOAT NOT NULL,
    PAN CHAR(10) NOT NULL,
    Maturity_Amount FLOAT,
    Invested_Date DATE NOT NULL,
    Maturity_Date DATE,
    Scheme_ID INT NOT NULL,
    FOREIGN KEY (User_ID_savings) REFERENCES user_details(User_ID),
    FOREIGN KEY (Account_Number) REFERENCES account_details(acc_no),
    FOREIGN KEY (Scheme_ID) REFERENCES schemes(Scheme_ID)
    ON DELETE CASCADE
);

-- ALTER TABLE savings_details ADD COLUMN Scheme_ID INT NOT NULL AFTER Mobile_number;

CREATE TABLE transactions(
    Transaction_ID BIGINT PRIMARY KEY,
    User_ID INT ,
    Credit_Amount FLOAT ,
    Credit_Date DATE ,
    Debit_Amount FLOAT ,
    Debit_Date DATE ,
    FOREIGN KEY (User_ID) REFERENCES USER_DETAILS(User_ID)
    ON DELETE CASCADE
);


desc savings_details;
desc transactions;
DESC user_details;

desc account_details;
SELECT* from account_details;
SELECT* FROM user_details;
SELECT* FROM savings_details;
SELECT* FROM transactions;
DROP TABLE transactions;
DELETE from user_details;
DELETE from account_details;
SHOW TABLES;

DELIMITER //

CREATE FUNCTION calc_int_amt(amount FLOAT, scheme_id INT)
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
    DECLARE mat_amt1 DECIMAL(10, 2);
    DECLARE int_rate FLOAT;
    DECLARE years FLOAT;
    
    -- Add LIMIT 1 to ensure only one row is returned
    SELECT Interest_Rate, Duration_In_Years 
    INTO int_rate, years 
    FROM schemes 
    WHERE Scheme_ID = scheme_id 
    LIMIT 1;

    -- Calculate the maturity amount
    SET mat_amt1 = amount + (amount * int_rate * years / 100);
    
    RETURN mat_amt1;
END//


DELIMITER //

CREATE TRIGGER insert_row 
AFTER INSERT ON transactions 
FOR EACH ROW  
BEGIN
    DECLARE amt FLOAT;
    DECLARE s_id INT;
    DECLARE interest_rate FLOAT;
    DECLARE total_savings FLOAT;

    SELECT sd.Amount, sd.Scheme_ID, sc.Interest_Rate, 
           (SELECT SUM(Amount) FROM SAVINGS_DETAILS WHERE User_ID = NEW.User_ID) AS total_savings
    INTO amt, s_id, interest_rate, total_savings
    FROM SAVINGS_DETAILS sd
    JOIN SCHEME sc ON sd.Scheme_ID = sc.Scheme_ID
    WHERE sd.User_ID = NEW.User_ID
    LIMIT 1;

    UPDATE transactions
    SET Credit_Amount = calc_int_amt(amt, s_id, interest_rate, total_savings)
    WHERE Transaction_ID = NEW.Transaction_ID;
END //

DELIMITER ;



CREATE TABLE admin(
admin_name VARCHAR(10) PRIMARY KEY,
password VARCHAR(20));

-- DUMMY VALUES

INSERT INTO admin (admin_name,password)VALUES
    ('admin1','12345'),
    ('admin2','67890'),
    ('admin3','74125');

SELECT * FROM admin;

DROP TABLE transactions;
DROP TABLE savings_details;
DROP TABLE account_details;

SHOW TABLES;

SELECT * FROM transactions;