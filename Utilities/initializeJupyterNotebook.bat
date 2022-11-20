@echo off
REM : This batch script can initialize jupyter notebook at specific location running a specific virtual enviroment. 
REM : Wrap this batch script with a shortcut and use the short cut to initialize jupyternotebook or just the virtual environment
REM : Activitate a virtual env named jupyter_env (This should be an existing virtual environment). Open notebook at specified path
cmd /k "cd /d C:\Users\Nijil\Python_envs\jupyter_env\Scripts & activate & cd /d C:\Users\Nijil\Workspace\MLProjects & jupyter-notebook"
