from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from data_utils import download_data

default_args = {
    "owner": "ivoryRabbit",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}
with DAG(
    dag_id="dbt_dag",
    default_args=default_args,
    description="An Airflow DAG to invoke simple dbt commands",
    schedule_interval=timedelta(days=1),
    catchup=False,
):
    load_data = PythonOperator(
        task_id="load_data",
        python_callable=download_data,
        op_kwargs={"dir": "/opt/airflow/dbts/seeds"},
    )

    dbt_seed = BashOperator(
        task_id="dbt_seed",
        env={"DBT_PROFILES_DIR": "/opt/airflow/dbts"},
        append_env=True,
        bash_command="dbt seed",
        cwd="/opt/airflow/dbts",
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        env={"DBT_PROFILES_DIR": "/opt/airflow/dbts"},
        append_env=True,
        bash_command="dbt run",
        cwd="/opt/airflow/dbts",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        env={"DBT_PROFILES_DIR": "/opt/airflow/dbts"},
        append_env=True,
        bash_command="dbt test",
        cwd="/opt/airflow/dbts",
    )

    load_data >> dbt_seed >> dbt_run >> dbt_test