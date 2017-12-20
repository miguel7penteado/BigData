# Hadoop - Configuração em Windows

## 1. O Ambiente Windows e as ferramentas nativas
O ambiente Hadoop nasceu em ambiente Unix/Linux/Posix escrito em `JAVA`, prevendo já sua portabilidade. Como os criadores 
vieram da fundação APACHE, era de se esperar que adotassem ferramentas e protocolos OpenSource para fazer funcionar aquilo
que estava fora do alcance do `JAVA` puro. Podemos citar por exemplo a ausencia do suporte a nativo a `SSH`.
Já o suporte do Windows ao `JAVA` (Hadoop é escrito em `JAVA`) é bem maduro.

### 1.1 SSH (servidor e Cliente)
Até bem pouco tempo atrás, o windows não tinha suporte nativo ao protocolo SSH, fazendo com que o usuário tivesse que lançar mão
do uso de um ambiente "linux" para windows instalando o CygWin por exemplo.
Uma vez que temos um SSH server rodando em Windows, as coisas se simplificam bastante.

### 1.2 JAVA (JRE)
O windows precisa instalar o framework `JAVA` para poder rodar o `Hadoop`. No momento em que este tutorial foi escrito, estava trabalhando com o **HADOOP** versão 2.7.5 e usava o **JAVA** versão **8**. Também é necessário que o sistema operacional consiga executar o java a partir da linha de comando, sendo necessário a criaçãodefinição das `VARIÁVEIS DE AMBIENTE`, tanto as padrões do `JAVA`, quanto as do `HADOOP`.



