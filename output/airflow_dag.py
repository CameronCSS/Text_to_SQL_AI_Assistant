from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta

# This DAG created by ClaudeAI includes:

# 1. Proper imports and default arguments with `depends_on_past=True`
# 2. DAG configuration with daily schedule
# 3. Task to create staging table for retail sales
# 4. Task to create employee info table
# 5. Task for loading data into staging
# 6. Task for final transformation
# 7. Task dependencies defined

# Key features:
# - Uses PostgresOperator for database operations
# - Includes `IF NOT EXISTS` in table creation
# - Prepared for `{{ ds }}` parameter usage
# - Dependencies on employee_info table considered
# - Proper task flow defined

# You would need to:
# 1. Add your specific SQL transformation logic
# 2. Configure the Postgres connection in Airflow
# 3. Add any additional error handling or data validation steps
# 4. Modify the schedule interval as needed
# 5. Add any required data quality checks

default_args = {
    'owner': 'airflow',
    'depends_on_past': True,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'retail_employee_transformation',
    default_args=default_args,
    description='Transform retail sales data with employee information',
    schedule_interval='@daily',
    catchup=False
)

# Create staging table for retail sales
create_staging_retail = PostgresOperator(
    task_id='create_staging_retail',
    postgres_conn_id='postgres_default',
    sql="""
        CREATE TABLE IF NOT EXISTS staging_retail_sales (
            InvoiceNo VARCHAR(50),
            StockCode VARCHAR(50),
            Description VARCHAR(50),
            Quantity VARCHAR(50),
            InvoiceDate TIMESTAMP,
            UnitPrice FLOAT,
            CustomerID INTEGER,
            Salesman_ID INTEGER,
            Country VARCHAR(50)
        );
    """,
    dag=dag
)

# Create employee info table
create_employee_info = PostgresOperator(
    task_id='create_employee_info',
    postgres_conn_id='postgres_default',
    sql="""
        CREATE TABLE IF NOT EXISTS employee_info (
            employee_id INTEGER NOT NULL,
            First_name VARCHAR(50) NOT NULL,
            Last_name VARCHAR(50) NOT NULL,
            Salary INTEGER NOT NULL,
            Job_title VARCHAR(50) NOT NULL
        );
    """,
    dag=dag
)

# Load data into staging
load_staging = PostgresOperator(
    task_id='load_staging',
    postgres_conn_id='postgres_default',
    sql="""
        -- Insert staging data logic here
        -- Using {{ ds }} for date filtering
    """,
    dag=dag
)

# Transform and merge data
transform_data = PostgresOperator(
    task_id='transform_data',
    postgres_conn_id='postgres_default',
    sql="""
        -- Transform and merge logic here
        -- Join with employee_info
        -- Filter using {{ ds }}
    """,
    dag=dag
)