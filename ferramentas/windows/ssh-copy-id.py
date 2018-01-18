"""ssh-copy-id for Windows.

Exemplo de uso: python ssh-copy-id.py fulano@maquinaremota

este programa precisa do scp e do cliente ssh no PATH para funcionar.
Por conveniencia voce tambem pode tentar utilizar o http://bliker.github.io/cmder/.
"""

import argparse, os
from subprocess import call

def winToPosix(parametro_caminho_windows):
	"""Coverte a nomenclatura de sistemas de arquivos windows para o formato POSIX para entrega-las aos clientes scp e ssh.

	Exemplo:
	parametro_caminho_windows: C:\\home\\user
	caminho_posix: /c/home/user
	"""
	caminho_posix = parametro_caminho_windows.replace('\\', '/')
	return "/" + caminho_posix.replace(':', '', 1)

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--identity_file", help="identity file, default to ~\\.ssh\\idrsa.pub", default=os.environ['HOME']+"\\.ssh\\id_rsa.pub")
parser.add_argument("-d", "--dry", help="run in the dry run mode and display the running commands.", action="store_true")
parser.add_argument("remote", metavar="user@machine")
argumentos_comando_original = parser.parse_args()

chave_publica_local = winToPosix(argumentos_comando_original.identity_file)
chave_publica_remota = "~/temp_id_rsa.pub"

# Copia a chave publica sobre a remota temporariamente 
linha_comando_scp = "scp {} {}:{}".format(chave_publica_local, argumentos_comando_original.remote, chave_publica_remota)
print(linha_comando_scp)
if not argumentos_comando_original.dry:
	call(linha_comando_scp)

# Insere a chave publica copiada temporariamente no arquivo authorized_key e em seguida remove a chave temporaria.
linha_comando_ssh = ("ssh {} "
	             "mkdir ~/.ssh;"
	             "touch ~/.ssh/authorized_keys;"
	             "cat {} >> ~/.ssh/authorized_keys;"
	             "rm {};").format(argumentos_comando_original.remote, chave_publica_remota, chave_publica_remota)
print(linha_comando_ssh)
if not argumentos_comando_original.dry:
	call(linha_comando_ssh)
