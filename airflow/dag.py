# import the libraries
from datetime import timedelta, datetime
from airflow.models import DAG # The DAG object
from airflow.operators.python import PythonOperator # Python Operators
from airflow.operators.bash import BashOperator # Bash Operators

# defining DAG arguments
default_args = {
    'owner': 'My name',
    'start_date': datetime.today(),
    'email': ['myemail@somemail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# define the DAG
dag = DAG(
    dag_id='ETL_toll_data',
    schedule=timedelta(days=1),
    default_args=default_args,
    description='Apache Airflow Final Assignment',
)

# task: unzip_data
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xzf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment/',
    dag=dag,
)

# task: extract_data_from_csv
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -d"," -f1-4 /home/project/airflow/dags/finalassignment/vehicle-data.csv'\
    ' > /home/project/airflow/dags/finalassignment/csv_data.csv',
    dag=dag,
)

# task: extract_data_from_tsv
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command="cut -d$'\t' -f5-7 /home/project/airflow/dags/finalassignment/tollplaza-data.tsv"\
    " | sed 's/\t/,/g' > /home/project/airflow/dags/finalassignment/tsv_data.csv",
    dag=dag,
)

# task: extract_data_from_fixed_width 
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command="cut -c1-10,51-60 /home/project/airflow/dags/finalassignment/payment-data.txt"\
    " | awk '{print $1 "," $2}' > /home/project/airflow/dags/finalassignment/fixed_width_data.csv",
    dag=dag,
)

# task: consolidate_data 
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command="paste -d ',' /home/project/airflow/dags/finalassignment/csv_data.csv"\
    " /home/project/airflow/dags/finalassignment/tsv_data.csv"\
    " | paste -d /home/project/airflow/dags/finalassignment/fixed_width_data.csv"\
    " > /home/project/airflow/dags/finalassignment/extracted_data.csv",
    dag=dag,
)

# task: transform_data
transform_data = BashOperator(
    task_id='transform_data ',
    bash_command="""awk -F',' '{print $1 "," $2 "," $3 "," toupper($4) "," $5 "," $6 "," $7}' """\
    "/home/project/airflow/dags/finalassignment/extracted_data.csv"\
    " > /home/project/airflow/dags/finalassignment/transformed_data.csv",
    dag=dag,
)

# task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> \
extract_data_from_fixed_width >> consolidate_data >> transform_data