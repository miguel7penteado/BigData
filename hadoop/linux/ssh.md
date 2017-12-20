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
