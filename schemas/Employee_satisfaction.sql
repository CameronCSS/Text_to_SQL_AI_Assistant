CREATE TABLE CDDtest.dbo.Employee_satisfaction (
	employee_id int NULL,
	Education nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	EnvironmentSatisfaction nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	JobInvolvement nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	JobSatisfaction nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	PerformanceRating int NULL,
	RelationshipSatisfaction nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	WorkLifeBalance nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);