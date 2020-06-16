# BIG DATA
## Uma aplicação prática de BIG DATA tomando como exemplo os microdados 
## do CENSO 2010 do IBGE
[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/miguel-penteado-760486a9/)
&nbsp;
[![GitHub](https://i.stack.imgur.com/tskMh.png) GitHub](https://github.com/miguel7penteado)

# Documentação do projeto

Site está em [!http://miguel7penteado.github.io/BigData](http://miguel7penteado.github.io/BigData)

## Criando Documentação
```bash
# Clone o repositório remoto
git clone <endereço_repositorio_github>

# Adicione o ramo de páginas do projeto
# no github o nome padrão é gh-pages
git checkout --orphan gh-pages

# apague a cópia dos arquivos que existe nesse ramo (rascunho)
git rm -rf .

# apague o arquivo de ignorações
rm '.gitignore'

# Crie seus arquivos
gitbook init

# edite os modelos

# Gere a estrutura html
gitbook install && gitbook build

# Apagando temporários
git clean -fx node_modules
git clean -fx _book

# adicione tudo que você criou
git add -A

# Dê o nome para sua atualização
git commit -a -m "Publicação Inicial"

# Mande o ramo de volta para o repositório github
git push -u origin gh-pages

# volte para o tronco principal (ramo master)
git checkout master
```
## Atualizando a Documentação

```bash
# Clone o repositório remoto
git clone <endereço_repositorio_github>

# entre no ramo gh-pages para atualizar a documentação
git checkout gh-pages

# faça suas atualizações

# Gere a estrutura html
gitbook install && gitbook build

# Apagar arquivos temporários
git clean -fx node_modules
git clean -fx _book

# adicione tudo que você criou
git add -A

# Dê o nome para sua atualização
git commit -a -m "Publicação Inicial"

# Mande o ramo de volta para o repositório github
git push -u origin gh-pages

```
