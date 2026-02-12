import subprocess
from thistlethwaite.offline.pruning_table_generator import main as generate_tables
def run_on_robot():
    subprocess.run(["pybricksdev", "run", "ble", "main.py"], check=True)


generate_tables()
run_on_robot()
