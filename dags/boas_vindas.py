from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

with DAG(
    "02_boas_vindas",
    start_date=days_ago(1),
    schedule_interval='@daily'
) as dag:

    def cumprimentos():
        print("Boas-vindas ao Airflow!")

    tarefa = PythonOperator(
        task_id='cumprimentos',
        python_callable=cumprimentos
    )