# Google Cloud SDK

Processo de instalação do SDK do google Cloud a partir do Linux Debian ou Linux Devuan (versão 9 do debian ou versão ascii do devuan) para acessar a Google Cloud via linha de comando.

```bash

# veja qual versão de Debian ou Devuan você tem
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"

# gere o arquivo de repositorio no /etc/apt/sources.list.d/
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

# Baixe a chave do repositório
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

# instale os SDKs
apt-get install                     \
google-cloud-sdk                    \
python-crcmod                       \
google-cloud-sdk-app-engine-java    \
google-cloud-sdk-app-engine-python  \
google-cloud-sdk-pubsub-emulator    \
google-cloud-sdk-bigtable-emulator  \
google-cloud-sdk-datastore-emulator \
kubectl
```

Inicializando
```bash
gcloud init
```
