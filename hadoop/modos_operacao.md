# Modos de Operação
O Hadoop é por natureza um sistema distribuido, portanto, deve possuir um controlador de processos, escalonador e um sistema de arbitragem.

Um cluster hadoop é composto por processos-chave, sendo que cada um é designado para uma tarefa específica.
Estes são os processos-servidores padrão de um cluster hadoop.

* 1. - **NameNode**
* 2. - **DataNode**
* 3. - **JobTracker**
* 4. - **TaskTracker**
* 5. - **ResourceManager** (MRv2)
* 6. - **ApplicationMaster** (MRv2)
* 7. - **NodeManager** (MRv2)
* 8. - **SecondaryNameNode**

## Modos de operação do Hadoop

You can run a Hadoop in one of the 3 supported modes –

* **Modo Local** (Standalone)
* **Modo Pseudo-Distribuido**
* **Modo Distribuido**

## Modo Local (Standalone)

Por padrão, Hadoop é configurado para rodar em um único nó, como um processo java simples. Isto é útil em processos de depuração. Este modo de operação não vai, obviamente, lhe oferecer um ambiente distribuido. O uso deste modo é muito limitado e usualmente utilizado em experimentos.

## Modo Pseudo-Distribuido

Just like the Standalone mode, in Pseudo-Distributed Mode Hadoop is run on a single-node in a pseudo(false) distributed mode. The difference is that each Hadoop daemon runs in a separate Java process in Pseudo-Distributed Mode. Where as in Local mode each Hadoop daemon runs as a single Java process. Again the usage of this mode is very limited and it can be only used for experimentation.

## Modo Distribuido

In fully-distributed mode, all daemons are executed in a separate nodes forming a multi node cluster. This setup offers true distributed computing capability and offers built-in reliability, scalability and fault tolerance. This is the standard mode of operation in DEV, QA, UAT, PREPROD and Production environments.
