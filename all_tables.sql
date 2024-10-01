CREATE DATABASE IF NOT EXISTS pfa_orange;

USE pfa_orange;

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
