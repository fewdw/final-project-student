import os
import subprocess

os.chdir("flask-api")
subprocess.Popen(["flask", "run", "--port", "5001"], shell=True)
os.chdir("..")
os.chdir("flask-frontend")
subprocess.Popen(["flask", "run"], shell=True)