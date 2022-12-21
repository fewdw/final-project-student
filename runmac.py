import subprocess

subprocess.run(["cd", "flask-api"])
subprocess.Popen(["flask", "run", "--port", "5001"], shell=True)
subprocess.run(["cd", ".."])
subprocess.run(["cd", "flask-frontend"])
subprocess.Popen(["flask", "run"], shell=True)
