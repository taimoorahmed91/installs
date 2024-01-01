import subprocess

def run_script(script_name):
    output_file = script_name.replace('.py', '.txt')
    try:
        with open(output_file, 'a') as file:  # 'a' mode for appending to the file
            completed_process = subprocess.run(['python3', script_name], check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            file.write(completed_process.stdout)
    except subprocess.CalledProcessError as e:
        with open(output_file, 'a') as file:
            file.write(f"Error running {script_name}:\n{e.output}")

scripts = ['europkr.py', 'europln.py', 'plnpkr.py', 'usdpkr.py' ,'usdpln.py']

for script in scripts:
    run_script(script)
