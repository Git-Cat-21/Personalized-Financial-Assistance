CREATE DATABASE IF NOT EXISTS pfa_orange;

USE pfa_orange;

CREATE TABLE schemes(
    Scheme_Name VARCHAR(30) PRIMARY KEY,
    Interest_Rate FLOAT NOT NULL,
    Duration VARCHAR(10) NOT NULL
);
ALTER TABLE schemes
MODIFY COLUMN Scheme_Name VARCHAR(40)


DELETE FROM schemes;
INSERT INTO schemes (Scheme_Name,Interest_Rate, Duration) VALUES
('SecureBank FD', 6.5, '1 year'),
('GoldTrust Growth FD', 7.0, '2 years'),
('SafeInvest Future Plan', 7.5, '5 years'),
('TrustCapital Secure FD', 6.8, '3 years'),
('PrimeBank Senior Citizen FD', 8.0, '1.5 years'),
('GrowthBank Fixed Plan', 8.2, '10 years'),
('HorizonFinance Flexi FD', 5.0, '6 months'),
('FirstChoice Wealth FD', 7.2, '4 years'),
('ValueSafe High Return FD', 6.75, '1 year'),
('CapitalMax Booster FD', 7.1, '3 years');


SELECT * FROM schemes;