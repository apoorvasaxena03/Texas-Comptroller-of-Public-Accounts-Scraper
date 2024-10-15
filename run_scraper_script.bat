@echo off
REM Activate the conda environment
CALL C:\Users\Apoorva.Saxena\AppData\Local\miniconda3\envs\venv_test

REM Navigate to the directory where your Python script is located (optional)
cd C:\path\to\your\script

REM Run the Python script
python run_notebook.py

REM Deactivate the environment after running the script
CALL conda deactivate