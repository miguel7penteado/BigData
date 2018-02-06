# Instalação do ssh-copy-id.py

1. Tenha o python instalado e suas variáves de ambiente configuradas.
2. Tenha o SSH for windows instalado e suas variáveis de ambiente configuradas.
3. Salve este script no diretório de instalação do seu SSH for windows.

## Fazendo um programa .py ficar executável no windows

Associe arquivos com terminação *.py com o seu python local.

Rode os seguintes comando no shell prompt:

```cmd
assoc .py=PythonScript
ftype PythonScript=C:\bin\python.exe "%1" %*
```
Substitua, claro, o `C:\Python\bin\python.exe` pelo caminho da sua instalação de python. Isso ira te permitir rodar myscript.py 
ao invés de etr que digitar `python myscript.py` o tempo todo.

Adicione `.py` a sua variável de ambiente `PATHEXT`:

Isto vai fazer o windows considerar arquivos *.py executáveis quando os mesmos fore procurados nos caminhos dentro de 
sua variáves de ambiente PATH. Com isto, para você rodar o comando você so tem que digitar `myscript` em vez de `myscript.py` .

Fazendo isso para a sessão atual:

```cmd
set PATHEXT=%PATHEXT%;.PY
```

Fazendo isso ficar permanente ( Windows Vista em diante):

```cmd
setx PATHEXT %PATHEXT%;.PY
```

# Instalação do JAVA puro ( sem instalador ):

## 1. Descompacte o Java
## 2. Defina a variável JAVA_HOME
## 3. Descompacte os arquivos compactados

```cmd
cd %JAVA_HOME%

for /R %f in (.\*.pack) do @"%cd%\bin\unpack200" -r -v -l "" "%f" "%~pf%~nf.jar"
```




