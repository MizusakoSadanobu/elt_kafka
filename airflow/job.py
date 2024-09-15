# import the libraries
from datetime import timedelta, datetime

# The DAG object
from airflow.models import DAG

# Operators
from airflow.operators.python import PythonOperator

def days_ago(n, hour=0, minute=0, second=0, microsecond=0):
    """
    Get a datetime object representing `n` days ago. By default the time is
    set to midnight.
    """
    today = datetime.today()
    return today - timedelta(days=n)

#defining DAG arguments
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'My name',
    'start_date': days_ago(0),
    'email': ['myemail@somemail.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def fun1():
    return 2

def fun2(x):
    return x * 3

def fun3(x):
    return x / 3

# define the DAG
dag = DAG(
    dag_id='unique_id_for_DAG',
    default_args=default_args,
    description='A simple description of what the DAG does',
    schedule=timedelta(days=1),
)

# define the tasks
task1 = PythonOperator(
    task_id='fun1',
    python_callable=fun1,
    dag=dag,
)

task2 = PythonOperator(
    task_id='fun2',
    python_callable=fun2,
    dag=dag,
)

task3 = PythonOperator(
    task_id='fun3',
    python_callable=fun3,
    dag=dag,
)

# task pipeline
task1 >> task2 >> task3