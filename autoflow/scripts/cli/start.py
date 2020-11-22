import os
import json
import subprocess
import click
from autoflow.env import projectsDir, slash
from autoflow.scripts.shell import runCommand, proc

@click.command()
@click.argument('dir',type=click.STRING)
def start(dir):
    project = projectsDir + slash + dir
    if os.path.isdir(project):
        os.chdir(project)
        #checks if af-config exists
        isFile = os.path.isfile('af-config.json')
        if isFile:
            with open('af-config.json') as file:
                data = json.load(file)
                file.close()
                runCommand(f'cd {project}\n')
                runCommand('code .\n')
                if 'command' in data.keys():
                    command = data['command']
                    if 'python' in data['type']:
                        runCommand('. ./env/bin/activate\n')
                        runCommand(f'{command}\n')
                        for line in iter(proc.stdout.readline, ''):
                            print(line)
                    else:
                        subprocess.run([command],shell=True)
        else:
            click.echo('🤦 af-config.json doesn\'t exists')
    else:
        click.echo('😅 Project doesn\'t exists')