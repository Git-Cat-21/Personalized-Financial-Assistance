CREATE DATABASE IF NOT EXISTS pfa_orange;

USE pfa_orange;

CREATE TABLE schemes(
    Scheme_Name VARCHAR(30) PRIMARY KEY,
    Interest_Rate FLOAT NOT NULL,
    Duration VARCHAR(10) NOT NULL
);
ALTER TABLE schemes
MODIFY COLUMN Scheme_Name VARCHAR(40)

INSERT INTO schemes (Scheme_Name,Interest_Rate, Duration) VALUES
('SecureBank 1-Year FD', 6.5, '1 year'),
('GoldTrust 2-Year Growth FD', 7.0, '2 years'),
('SafeInvest 5-Year Future Plan', 7.5, '5 years'),
('TrustCapital 3-Year Secure FD', 6.8, '3 years'),
('PrimeBank Senior Citizen FD', 8.0, '1.5 years'),
('GrowthBank 10-Year Fixed Plan', 8.2, '10 years'),
('HorizonFinance 6-Month Flexi FD', 5.0, '6 months'),
('FirstChoice 4-Year Wealth FD', 7.2, '4 years'),
('ValueSafe 1-Year High Return FD', 6.75, '1 year'),
('CapitalMax 3-Year Booster FD', 7.1, '3 years');


SELECT * FROM schemes;