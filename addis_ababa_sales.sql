CREATE DATABASE addis_ababa_sales;
USE addis_ababa_sales;

CREATE TABLE sales_transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    amount DECIMAL(10, 2),
    district VARCHAR(50)
);

INSERT INTO sales_transactions (customer_id, amount, district) VALUES
(201, 150.0, 'Bole'),
(202, 350.0, 'Yeka'),
(203, 75.0, 'Arada'),
(204, 500.0, 'Lideta'),
(205, 200.0, 'Bole'),
(206, 120.0, 'Kirkos'),
(207, 300.0, 'Gullele'),
(208, 450.0, 'Nifas Silk');
