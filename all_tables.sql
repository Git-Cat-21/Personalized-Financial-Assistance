CREATE DATABASE IF NOT EXISTS pfa_orange;

USE pfa_orange;

CREATE TABLE USER_DETAILS(
    User_ID INT PRIMARY KEY,
    User_name VARCHAR(50),
    Mob long constraint ck1 check(Mob like '[0-9]{10}'),
    Email_id VARCHAR(30) constraint ck2 check(Email_id like '%_@__%.__%'),
    Dob DATE,
    Pwd VARCHAR(20)
);
CREATE TABLE ACCOUNT_DETAILS(
    acc_no BIGINT PRIMARY KEY,
    ifsc VARCHAR(20),
    acc_status ENUM('Active','Inactive'),
    acc_type ENUM('Savings','Current'),
    acc_create DATE,
    user_id int,
    Foreign Key (user_id) REFERENCES user_details(User_ID)
);
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
(5,'PrimeBank Senior Citizen FD', 8.0, 1.5),
(6,'GrowthBank Fixed Plan', 8.2, 10),
(7,'HorizonFinance Flexi FD', 5.0, 6),
(8,'FirstChoice Wealth FD', 7.2, 0.5),
(9,'ValueSafe High Return FD', 6.75, 1),
(10,'CapitalMax Booster FD', 7.1, 3);
SELECT * FROM schemes;

CREATE TABLE SAVINGS_DETAILS (
    User_ID_savings INT NOT NULL,
    Account_Number BIGINT UNIQUE NOT NULL,
    Mobile_Number BIGINT UNIQUE NOT NULL, -- Ensuring it's a 10-digit number
    Amount FLOAT NOT NULL,
    PAN CHAR(10) UNIQUE NOT NULL,
    Maturity_Amount FLOAT NOT NULL,
    Invested_Date DATE NOT NULL,
    Maturity_Date DATE NOT NULL,
    PRIMARY KEY (User_ID_savings, Account_Number),
    FOREIGN KEY (User_ID_savings) REFERENCES user_details(User_ID),
    FOREIGN KEY (Account_Number) REFERENCES account_details(acc_no)
);

SHOW TABLES;

SELECT * from users;
CREATE TABLE transactions(
    Transaction_ID INT PRIMARY KEY,
    User_ID INT ,
    Credited_Amount FLOAT NOT NULL,
    Credited_Date DATE NOT NULL,
    Debited_Amount FLOAT NOT NULL,
    Debited_Date DATE NOT NULL,
    FOREIGN KEY (User_ID) REFERENCES USER_DETAILS(User_ID)
);