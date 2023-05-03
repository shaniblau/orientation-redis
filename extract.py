import subprocess

command = "sshpass -p Password123! scp -r azureuser@40.114.92.103:/home/azureuser/dogs " \
          "/home/azureuser/orientation-redis"
output = subprocess.check_output(command, shell=True)