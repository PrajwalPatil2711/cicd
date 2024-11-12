from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from jobs.data_transformation import transform_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

dag = DAG('data_pipeline_dag', default_args=default_args, schedule_interval='@daily')

start = PythonOperator(
    task_id='start',
    python_callable=lambda: print("Starting the DAG"),
    dag=dag
)

transform = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag
)

end = PythonOperator(
    task_id='end',
    python_callable=lambda: print("Ending the DAG"),
    dag=dag
)

start >> transform >> end
