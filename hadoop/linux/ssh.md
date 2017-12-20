# Configurando o servidor de protocolo **SSH** para o **Hadoop**

O servidor de `SSH` deve permitir autenticação sem senha para o usuário do `HADDOP`. Considerando que seu usário do `HADOOP`
se chama **usuario_hadoop**, é possível faze-lo autenticar sem senha nos nós `HADOOP` utilizando a famosa **autenticação por
chave pública**, que o servidor **OpenSSH** suporta.

## 1. Instalando o servidor SSH em sua distribuição.
Não quero me limitar a uma distribuição específica, mas vou exemplificar a mais simples e genérica de todas, atualmente, que é o Linux **Debian** versão stretch (ou Linux **Devuan** versão ascii).

### 1.1 Instalando o servidor SSH - Debian
```bash
# atualize a lista de novos pacotes
sudo apt-get update -y
# instale o servidor SSH
sudo apt-get install openssh-server -y
#instale o cliente SSH
sudo apt-get install openssh-client -y
#instale o servidor de ftp seguro (sftp)
sudo apt-get install openssh-sftp-server -y
```
## 2. Habilitando a autenticação "sem senha" no servidor OpenSSH
A autenticação sem senha para o usuário do `hadoop` que nós criamos anteriormente, **usuario_hadoop**, é na verdade uma
**autenticação por chave pública**. Essa autenticação usa uma chave pública apresentada ao servidor como sua "senha".
Por aí já sabemos que, conceitualmente, cada nó deve ter a chave pública de todos os nós participantes.

### 2.1 - Habiltando a autenticação de Chave Pública no arquivo de configuração do servidor `sshd_config`
Vamos ter que dizer ao servidor SSH que o mesmo deve aceitar a autenticação por Chave Pública, inclusive.
Edite o arquivo **sshd_config**. No debian, ele está no diretório **/etc/ssh**:
```bash
# opcional - instale o editor VIM
sudo apt-get install vim -y
# agora abra o arquivo ssh_config para edição
sudo vim /etc/ssh/sshd_config
# por fim deixe esta linha como está abaixo:
Set PubkeyAuthentication to Yes
# salve o arquivo.
# carregue as novas configurações no servidor ssh
sudo /etc/init.d/ssh reload
```

