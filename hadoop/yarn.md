# Yarn - Yet Another Resource Negotiator

O negociador de recursos do Hadoop, Yarn, consiste em 3 peças arquiteturais:
*. - Gerenciador de Recursos ou **ResourceManager** (um por cluster)
*. - Arbitro de Aplicação ou **ApplicationMaster** (um por aplicação)
*. - Gerenciador de Nós ou **NodeManagers** (um por nó)

No contexto do yarn temos de ter cuidado com alguns termos:
>>> **Resource Container** (RC) representa uma coleção de recursos físicos. Máquinas, HDs, memórias.
>>> **Aplicação** no contexto do yarn significa um job.


## 1. Gerenciador de Recursos - ResourceManager:
O `Gerenciador de Recursos` é responsável por inventariar recursos disponíveis e manter serviços-chave, cujo mais importante de todos é o `escalonador de recursos` ou **Scheduler**.

### 1.1 Escalonador ou Scheduler de recursos
O componente `escalonador de recursos` do `Gerenciador de Recursos` do YARN aloca *recursos* para rodar Aplicações (jobs). Ele é um "escalonador puro" no fato de que ele não monitora ou segue o status do job ou seu progresso. E como ele não as monitora, ele não pode garantir que o job reinicie caso ele falhe.

Na versão Hadoop 2.7.2, YARN suporta *politicas de escalonamento* : 
>>> * 1. O CapacityScheduler, 
>>> * 2. O FairScheduler, 
>>> * 3. O FIFO (first in first out) Scheduler. 
O escalonador padrão varia nas distribuições Hadoop, mas não importa a política usada, o escalonador aloca recursos associando containers (conjunto de recursos físicos) à requisição do `Arbitro de Aplicação` ou ApplicationMaster.

## 2 Arbitro de Aplicação ou ApplicationMaster

Cada job rodando no HADOOP tem sua própria instância de `Arbitro de Aplicação` ou **ApplicationMaster**. Esta instância "vive" em seu próprio container separado em um dos nós do cluster. Os ApplicationMaster de cada job mandam periodicamente mensagens "Batida-de-Coração" ao **Gerenciador de Recursos** ou ResourceManager, bem como requisitam recursos adicionais se necessário. Recursos adicionais são garantidos pelo ResourceManager através de arrendamentos do Container de Recursos, que servem como reservas para os containers nos **Gerenciadores de Nós** ou NodeManager.

The ApplicationMaster oversees the execution of an application over its full lifespan, from requesting additional containers from the ResourceManger, to submitting container release requests to the NodeManager.

## 3 Gerenciadores de Nós ou NodeManagers

O `Gerenciador de Nós` ou **NodeManager** é um agente que está presente em cada nó. Sua missão é cuidar dos containers de recursos durante seu ciclo de vida, ou seja, monitorar uso de recursos do container e monitorar a periodicidade de comunicação com o `Gerenciador de Recursos` ou **ResourceManager**. Conceitualmente, o `Gerenciador de Nós` ou **NodeManager** é muito mais parecido com um Rastreador de Tarefas nas primeiras versões do HADOOP. 


## Ciclo de Vida

* 1. - A aplicação-cliente submente uma aplicação MapReduce ao `Gerenciador de Recursos`, junto com a informação para executar o `arbitro de aplicação` específico.
* 2. - O `gerenciador de recursos` um container para o `arbitro de aplicação` e executa o `arbitro de aplicação`.
* 3. - `Arbitro de aplicação` inicializa e se registra no `gerenciador de recursos`, permitindo a aplicação-cliente interfacear diretamente com o `arbitro da aplicação`.
* 4. - `Arbitro da aplicação` negocia recursos (container de recursos) para a aplicação-cliente.
* 5. - `Arbitro da aplicação` da a especificação de execução de container para o `Gerenciador de Nós`, que executa um container para a aplicação.
* 6. - Durante a execução, a aplicação-cliente varre o `Arbitro da Aplicação` consultando o status da aplicação e seu progresso.
* 7. - Após completar, `Arbitro da aplicação` se desregistra do `Gerenciador de Recursos` e se desliga, retornando seu container a pilha de recursos.
