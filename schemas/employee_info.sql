CREATE TABLE CDDtest.dbo.employee_info (
	employee_id int NOT NULL,
	First_name nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	Last_name nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	Salary int NOT NULL,
	Job_title nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
);