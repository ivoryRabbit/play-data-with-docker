from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import datetime
from airflow.utils.dates import timedelta

default_args = {
    "owner": "astronomer",
    "depends_on_past": False,
    "start_date": datetime(2023, 12, 23),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}
with DAG(
    "dbt_dag",
    default_args=default_args,
    description="An Airflow DAG to invoke simple dbt commands",
    schedule_interval=timedelta(days=1),
    catchup=False,
):
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

    dbt_seed >> dbt_run >> dbt_test