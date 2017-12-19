# Map Reduce

A operação de **map-reduce** permite enviar para vários nós o processamento computacional. 
A operação de reduzir (somar, totalizar) é executada em cada nó **paralelamente**.

## Operações
* 1. - Ler (arquivos) de entrada
* 2. - Carregar linhas dos arquivos em instâncias individuais do mapeador.
* 3. - Separar ocorrências, mapear-las e atribuir uma chave a cada valor.
* 4. - Agrupar pares chave-valor e ordena-los.
* 5. - Reduzir (somar, totalizar) os grupos chave-valor em um único resultado chave-valor.
* 6. - Consolidar os grupos resultantes em uma saída.

### Exemplo clássico: contador de palavras.
