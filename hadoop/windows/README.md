# Hadoop - Configuração em Windows

O ambiente Hadoop nasceu em ambiente Unix/Linux/Posix escrito em `JAVA`, prevendo já sua portabilidade. Como os criadores 
vieram da fundação APACHE, era de se esperar que adotassem ferramentas e protocolos OpenSource para fazer funcionar aquilo
que estava fora do alcance do JAVA puro. Portando, levemos em consideração o Protocolo SSH.
Até bem pouco tempo atrás, o windows não tinha suporte nativo ao protocolo SSH, fazendo com que o usuário tivesse que lançar mão
do uso de um ambiente "linux" para windows instalando o CygWin por exemplo.
Uma vez que temos um SSH server rodando em Windows, as coisas se simplificam bastante.
