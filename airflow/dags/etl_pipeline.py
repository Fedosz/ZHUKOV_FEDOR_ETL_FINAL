from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="etl_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval=None,
    catchup=False
) as dag:

    generate_data = BashOperator(
        task_id="generate_data",
        bash_command="python /opt/airflow/scripts/generate_data.py"
    )

    mongo_to_postgres = BashOperator(
        task_id="mongo_to_postgres",
        bash_command="python /opt/airflow/scripts/mongo_to_postgres.py"
    )

    build_marts = BashOperator(
        task_id="build_marts",
        bash_command="""
        export PGPASSWORD=etl_password

        psql -h postgres -U etl_user -d etl_warehouse -c "
        delete from mart.user_activity;
        insert into mart.user_activity
        select user_id,count(*),count(*)
        from staging.event_logs
        group by user_id;

        delete from mart.support_stats;
        insert into mart.support_stats
        select issue_type,count(*)
        from staging.support_tickets
        group by issue_type;
        "
        """
    )

    generate_data >> mongo_to_postgres >> build_marts