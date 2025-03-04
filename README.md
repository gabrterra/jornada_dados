# jornada_dados

## instalar git

- Baixar git

1)  No Power shell digitar: winget install --id Git.Git -e --source winget

2) Seguir [documentação](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) para gerar chave ssh e conectar ao repositório


# pyenv + venv

Como garantir que o projeto não sofra com atualizações?

- Usar o pyenv para "travar" as versões de pacotes e bibliotecas

1) instalar versoes específicas do python:

pyenv install 3.12.1

pyenv install 3.11.5

2) Setar versão global (versão mais recente):

pyenv global 3.12.1

3) E para cada diretório (projeto), setar a versao do python local:

pyenv local 3.11.5

![arquivo .python-version](image.png)

![versão atribuída](image-1.png)



## Limpar piplist

pip list -> listar todas as bibliotecas instaladas
pip freeze | grep -v "^-e" | xargs pip uninstall -y -> limpar todas as bibliotecas listadas na etapa anterior


Entrar no ambiente do projeto
cd ....

Instalar o venv
$ python -m venv .venv

Ativar o venv
source .venv/Scripts/activate

Baixar as bibliotecas
pip install ...

Desativa a venv
deactivate


## PIPX
O pipx é uma ferramenta recomendada para instalar e gerenciar aplicativos Python globalmente de forma isolada, sem bagunçar seu ambiente de desenvolvimento. Ele é útil principalmente para instalar ferramentas CLI (Command Line Interface) que você usaria em qualquer projeto, como dbt, black, pre-commit, poetry, etc.

## Poetry
O Poetry é um gerenciador de dependências e pacotes para projetos Python que traz várias vantagens em relação a outras ferramentas como pip e virtualenv
