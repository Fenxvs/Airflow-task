from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator 


def print_number():
    for i in range (10):
        print(i)    
    


with DAG (
    dag_id = "dag2",
    start_date = datetime(2025, 9, 29),
    schedule_interval = timedelta(minutes= 1),
    catchup = False
) as dag :
    task1 = PythonOperator(
        task_id = "Python_task",
        python_callable = print_number
    )