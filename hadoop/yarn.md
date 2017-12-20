# Yarn

## Ciclo de Vida

* 1. - A aplicação-cliente submente uma aplicação MapReduce ao `Gerenciador de Recursos`, junto com a informação para executar o `arbitro de aplicação` específico.
* 2. - O `gerenciador de recursos` um container para o `arbitro de aplicação` e executa o `arbitro de aplicação`.
* 3. - `Arbitro de aplicação` inicializa e se registra no `gerenciador de recursos`, permitindo a aplicação-cliente interfacear diretamente com o `arbitro da aplicação`.
* 4. - `Arbitro da aplicação` negocia recursos (container de recursos) para a aplicação-cliente.
* 5. - `Arbitro da aplicação` da a especificação de execução de container para o `Gerenciador de Nós`, que executa um container para a aplicação.
* 6. - Durante a execução, a aplicação-cliente varre o `Arbitro da Aplicação` consultando o status da aplicação e seu progresso.
* 7. - Após completar, `Arbitro da aplicação` se desregistra do `Gerenciador de Recursos` e se desliga, retornando seu container a pilha de recursos.
