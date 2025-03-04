# 📊 jornada_dados  

## 🛠 Instalar Git  

### 🔹 Passo 1: Baixar o Git  
No PowerShell, execute o seguinte comando para instalar o Git:  

```bash
winget install --id Git.Git -e --source winget
```

### 🔹 Passo 2: Configurar SSH  
Siga a [documentação oficial](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) para gerar uma chave SSH e conectar ao repositório.  

---

# 🐍 pyenv + venv  

## ✅ Como garantir que o projeto não sofra com atualizações?  
Utilize o `pyenv` para "travar" as versões do Python e garantir a compatibilidade do projeto.  

### 🔹 Passo 1: Instalar versões específicas do Python  
```bash
pyenv install 3.12.1
pyenv install 3.11.5
```

### 🔹 Passo 2: Definir versão global (versão mais recente)  
```bash
pyenv global 3.12.1
```

### 🔹 Passo 3: Definir versão local por projeto  
```bash
pyenv local 3.11.5
```

📌 **Exemplo do arquivo `.python-version`**  
![arquivo .python-version](readme/arquivo_python_version.png)  

📌 **Exemplo da versão atribuída**  
![versão atribuída](readme/versão_atribuída.png)  

---

## 🧹 Limpar `pip list`  

### 🔹 Passo 1: Listar todas as bibliotecas instaladas  
```bash
pip list
```

### 🔹 Passo 2: Remover todas as bibliotecas instaladas  
```bash
pip freeze | grep -v "^-e" | xargs pip uninstall -y
```

### 🔹 Passo 3: Criar e ativar um ambiente virtual  

1️⃣ **Entrar no diretório do projeto**  
```bash
cd nome_do_projeto
```

2️⃣ **Criar um ambiente virtual (`venv`)**  
```bash
python -m venv .venv
```

3️⃣ **Ativar o ambiente virtual**  
- No Linux/macOS:  
  ```bash
  source .venv/bin/activate
  ```
- No Windows (cmd/Powershell):  
  ```bash
  source .venv/Scripts/activate
  ```

4️⃣ **Instalar bibliotecas necessárias**  
```bash
pip install -r requirements.txt
```

5️⃣ **Desativar o ambiente virtual**  
```bash
deactivate
```

📌 **O `pip list` deve ficar assim após a limpeza:**  
```bash
$ pip list
Package      Version
------------ -------
argcomplete  3.5.3
click        8.1.8
colorama     0.4.6
packaging    24.2
pip          23.2.1
pipx         1.7.1
platformdirs 4.3.6
userpath     1.9.2
```

---

## ⚙️ PIPX  
O `pipx` é uma ferramenta recomendada para instalar e gerenciar aplicativos Python globalmente de forma isolada, sem bagunçar seu ambiente de desenvolvimento.  

📌 **Ele é útil para instalar ferramentas CLI como:**  
- `dbt`  
- `black`  
- `pre-commit`  
- `poetry`  

---

## 📦 Poetry  
O `Poetry` é um gerenciador de dependências e pacotes para projetos Python que traz diversas vantagens em relação ao `pip` e `virtualenv`.  

💡 **Vantagens do Poetry:**  
- Gerenciamento eficiente de dependências  
- Arquivo `pyproject.toml` para configuração padronizada  
- Melhor controle de versões  

```bash
# Instalar o Poetry
pipx install poetry

# Criar um novo projeto com Poetry
poetry new meu_projeto

# Instalar dependências de um projeto existente
poetry install
```

---