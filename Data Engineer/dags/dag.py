from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'gugun',
    'depends_on_past': False,
    'start_date': datetime(2026, 6, 1),
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'stock_daily_update',
    default_args=default_args,
    description='Pipeline harian update data saham',
    schedule_interval='@daily', # Berjalan setiap hari secara otomatis
    catchup=False
) as dag:

    # Task untuk menjalankan update_data.py
    run_update = BashOperator(
        task_id='run_update_data',
        # Menambahkan '2>&1' agar pesan error Python muncul di log Airflow
        bash_command='python /opt/airflow/scripts/update_data.py 2>&1'
    )
    
    # Task berikutnya (misalnya untuk prediksi) bisa ditambahkan di sini
    # run_prediction = ... 

    run_update