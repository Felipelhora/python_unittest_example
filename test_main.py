import subprocess
import os
import time


local_path = os.getcwd()
comando = f"python -m unittest {local_path}/src/TestCalculadoraDiferente.py"
saida = subprocess.check_output(comando, shell=True)


print(saida.decode('utf-8'))

time.sleep(3)
