# HDFS

Uma das partes integrantes do Hadoop, eh um sistema de arquivos distribuido. Seu principal objetivo eh poder armazenar arquivos 
muito grandes. Provavelmente grandes demais para ser armazenado em uma única máquina.

# Cliente HDFS
 É uma interface de gravação e leitura dos arquivos armazenados no servidor de arquivos HDFS.
 
## Servidor HDFS (Namenode(s) + Datanodes)
* - *NameNode* - Possui o índice de localização de todos os pedaços de arquivos.
* - *Datanodes* - São vários nós. Os nós possuem os pedaços dos arquivos inseridos no sistema de arquivo HDFS.
