CREATE TABLE CDDtest.dbo.Retail_sales (
	InvoiceNo nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	StockCode nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	Description nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	Quantity nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	InvoiceDate datetime2 NULL,
	UnitPrice float NULL,
	CustomerID int NULL,
	Salesman_ID int NULL,
	Country nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);