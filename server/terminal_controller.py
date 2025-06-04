import paramiko
import subprocess
from config import settings

def exec_command(command: string) -> str:
    key = paramiko.RSAKey.from_private_key_file(settings.shell_key_path)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="retroko-server", username=settings.shell_user, pkey=key)
    stdin, stdout, stderr = ssh.exec_command(command)
    code = stdout.channel.recv_exit_status()
    out = stdout.read().decode() + stderr.read().decode()
    ssh.close()
    if code != 0:
        raise Exception(f"Erreur (code #{code}) : {out}")
    return out