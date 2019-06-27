CREATE DATABASE WT;
GO

USE WT;

	-- Create the Order, Orderline, Doctor, Customer, Cashier, Prescription, Supplier, Product, and ProductCategory tables

	CREATE TABLE IF NOT EXISTS conditions(
	  condition_ID bigint NOT NULL PRIMARY KEY,
	  condition_name varchar(50) NOT NULL,
	  condition_category_id bigint NOT NULL, 
	  description text NULL);

	CREATE TABLE IF NOT EXISTS cond_treat(
	  cond_treat_ID bigint NOT NULL PRIMARY KEY,
	  cond_treat_name varchar(50) NOT NULL,
	  condition_ID bigint NOT NULL,
	  treatment_ID bigint NOT NULL);

	CREATE TABLE IF NOT EXISTS treatments(
	  treatment_ID bigint NOT NULL PRIMARY KEY,
	  treatment_name varchar(50) NOT NULL,
	  treatment_category_id bigint NOT NULL, 
	  description text NULL);

	CREATE TABLE IF NOT EXISTS treatment_category(
	  treatment_category_ID bigint NOT NULL PRIMARY KEY,
	  treatment_category_name varchar(50) NOT NULL,
	  description varchar(50) NULL); 
	
	CREATE TABLE IF NOT EXISTS condition_category(
	  condition_category_ID bigint NOT NULL PRIMARY KEY,
	  condition_category_name varchar(50) NOT NULL,
	  description varchar(50) NULL); 
	  
	-- Create the relationships: 
		-- conditions
	ALTER TABLE conditions ADD CONSTRAINT FK_conditions_category_ID 
	FOREIGN KEY (condition_category_ID) REFERENCES condition_category(condition_category_ID);
		-- cond_treat
	ALTER TABLE cond_treat ADD CONSTRAINT FK_condition_ID 
	FOREIGN KEY (condition_ID) REFERENCES conditions(condition_ID);

	ALTER TABLE cond_treat ADD CONSTRAINT FK_treatment_ID
	FOREIGN KEY (treatment_ID) REFERENCES treatments(treatment_ID);
		
		-- treatments
	ALTER TABLE treatments ADD CONSTRAINT FK_treatment_category_ID 
	FOREIGN KEY (treatment_category_ID) REFERENCES treatment_category(treatment_category_ID);

