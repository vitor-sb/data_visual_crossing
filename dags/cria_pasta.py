from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.operators.empty import EmptyOperator


with DAG(
  '01_cria_pasta',
  start_date=days_ago(2),
  schedule_interval='@daily',
) as dag:

   tarefa_1 = EmptyOperator(task_id='tarefa_1')
   tarefa_2 = EmptyOperator(task_id='tarefa_2')
   tarefa_3 = EmptyOperator(task_id='tarefa_3')

   tarefa_4 = BashOperator(
        task_id = 'cria_pasta',
        # bash_command = 'mkdir -p "/opt/airflow/data/pasta={{ data_interval }}"'
        bash_command = 'mkdir -p "/opt/airflow/data/pasta={{ ds }}"'
      )

   tarefa_1 >> [tarefa_2, tarefa_3]
   tarefa_3 >> tarefa_4