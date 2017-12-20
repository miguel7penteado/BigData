# Hadoop - Configuração no Linux

## 1. O Ambiente Linux suas ferramentas nativas
O ambiente Hadoop nasceu em ambiente Unix/Linux/Posix escrito em `JAVA`, prevendo já sua portabilidade.
O suporte do Linux a `JAVA` e `SSH` é nativo, portanto é bem fácil fazer a configuração do `hadoop` neste ambiente,
seja qual for sua distribuição. De um `DEBIAN` a um `SLACKWARE`.
O interpretador de comandos normalmente é o `BASH`, mas se vocẽ quer aventuras, basta rescrever alguns scripts e fácilmente você 
poderá utilizar shells como `Korn`, `ZSH` e `CSH`. Afinal, até o `cmd` do windows roda o `HADOOP` pelo `JAVA`.

### 1.1 SSH (servidor e Cliente)
Você obviamente vai ter que instalar o servidor SSH (claro, servidor e cliente) em sua distribuição `Linux`. Isso normalmente eh feito com uma linha de comando hoje em dia.

### 1.2 JAVA (JRE)
O ambiente `JAVA` também é bem simples de se instalar e se suportar no Linux, seja qual for sua distribuição. Recomendo que vocẽ use o framework `JAVA` da `oracle`, mas fique livre para testar o framework OpenJDK, se quiser.
