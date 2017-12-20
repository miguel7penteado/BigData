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

Neste modo Hadoop também roda em um único nó. A diferença é que cada Hadoop processo-chave roda em um processo java separado, ao invés de rodarem todos em um mesmo processo como no modo anterior. Novamente O uso deste modo é muito limitado e usualmente utilizado em experimentos.

## Modo Distribuido

No modo distribuido, cada processo-chave roda em nós distintos, criando ai sim, um cluster. Esta configuração possibilita a computação distribuida e permite confiabilidade, escalabilidade e tolerança a falhas. Este é o modo de operação padrão em ambientes DEV, QA, UAT, PREPROD e Produção.

Neste modo os nós se comunicam por SSH, utilizando uma `autenticação por Chave Pública`, isto é, uma autenticação SSH sem senha.


