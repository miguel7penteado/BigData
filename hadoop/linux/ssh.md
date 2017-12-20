# Configurando o servidor de protocolo **SSH** para o **Hadoop**

O servidor de `SSH` deve permitir autenticação sem senha para o usuário do `HADDOP`. Considerando que seu usário do `HADOOP`
se chama **usuario_hadoop**, é possível faze-lo autenticar sem senha nos nós `HADOOP` utilizando a famosa **autenticação por
chave pública**, que o servidor **OpenSSH** suporta.
