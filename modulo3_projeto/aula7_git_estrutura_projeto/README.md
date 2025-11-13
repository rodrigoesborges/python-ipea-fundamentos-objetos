## Passo-a-passo Git 

a. Criar repositórios
B. Clonar repositórios (copiar)
C. Versionar arquivos e entender o básico do Git.

---

### 1. Criar conta no GitHub
Acesse [github.com](https://github.com) e crie uma conta (se ainda não tiver).

---

### 2. Instalar Git e configurar
- Baixe e instale o Git: [https://git-scm.com/downloads](https://git-scm.com/downloads)  
- Após a instalação, abra o VS Code e confirme que o Git foi reconhecido:  
  - Menu: **View → Terminal**
  - Digite:
    ```bash
    git --version
    ```
  - Se aparecer a versão, está tudo certo.  
- **Configure seu nome e e-mail (usado nos commits)**:
  ```bash
  git config --global user.name "Seu Nome"
  git config --global user.email "seu@email"

---
### A. Criar repositório no GitHub e vincular diretório
1. No GitHub, clique em + → New repository.

Escolha um nome, mantenha público (por enquanto) 

2. Clique em Create repository.

3. Copie a URL HTTPS do repositório.

Será algo com:
    **`https://github.com/BAFurtado/meu_primeiro_repo.git`**

4. No Terminal digite;
`git init`  # Isso vai iniciar um projeto versionado no seu diretório

5. Depois digite:
`git remote add origin https://github.com/BAFurtado/meu_primeiro_repo.git`
Você está informando para o git onde está o remoto (na nuvem), que se chama origin

6. Pronto, o folder está vinculado. Quando criar um arquivo, o Source Contrl do VSCODE vai acusar mudanças. 

7. A partir daí proceda com **+** quando adicionar mudanças, dê `commit` salvo localmente no repositório git e `push' -> sincroniza com a origem-

---
### B. Clonar repositório no VS Code
1. Você pode clonar pelo próprio VS Code, sem usar terminal:

2. Abra o VS Code.

3. Pressione Ctrl+Shift+P → digite Git: Clone → pressione Enter.

4. Cole a URL do repositório do GitHub (exemplo):

`https://github.com/BAFurtado/python-ipea-fundamentos-objetos.git`

5. Escolha uma pasta local para salvar.

6. Após o clone, o VS Code perguntará se deseja abrir o projeto clonado — clique em Open.

### C. Git basics--entendimento geral dos processos

1. **`git init`** -- transforma o diretório corrente em um diretório versionado do tipo git. Na prática, cria um arquivo `.git'
2. **commit** -- salva as mudanças locais para o arquivo git. 
3. **push** -- empurra as mudanças locais para a origin (o repositório externo)
4. **pull** -- puxa as mudanas do repositório externo, a `origin`, para o seu computador. 
5. **`git status`** -- te conta em qual branch você está...

6. **branch** -- ramo distinto para testes de código que deixo o ramo principal intocado (usualmente chamado main ou master). Quando a feature, o desenvolvimento, está completo, usa-se **merge** para juntar o branch com o tronco principal. 

---
7. **Fluxo de trabalho típico (VS Code)**
    Abrir o projeto no VS Code.

    Fazer mudanças em um ou mais arquivos.

    Ctrl+Shift+G → + (Stage) para preparar os arquivos.

    Escrever mensagem de commit e clicar em ✓.

    Sync Changes (ou Push) para enviar ao GitHub.

    Pull se houver mudanças remotas antes de começar um novo trabalho.

---
8. **Dicas rápidas**
    Use mensagens de commit curtas e descritivas (ex.: Adiciona função de leitura de CSV).

    Sempre faça pull antes de começar o trabalho para evitar conflitos.

    Evite versionar arquivos grandes, de dados ou ambientes (.csv, .env, venv/).

    Para ver o histórico:

    Clique com o botão direito sobre o arquivo → Open Timeline.

    Ou use a extensão “GitLens” para visualização avançada.

    Se algo der errado, você pode:

    Clicar nos três pontinhos (⋯) → Undo Last Commit.

    Ou restaurar arquivo individual via menu de contexto no Source Control


---
 ## D. GitHub Actions--AUTOMAÇÃO
### Rodar python direto, na web, sem custos, para execução de rotinas: (a) busca de dados, (b) geração relatórios

### GitHub Actions: Panorama Básico
1. O que é GitHub Actions?
GitHub Actions é uma plataforma de CI/CD (Integração Contínua/Entrega Contínua) que automatiza workflows diretamente no seu repositório GitHub.

2. Workflow
Arquivo YAML que define o processo de automação
Fica na pasta **.github/workflows/**
Pode ser acionado por eventos (schedule, push, pull request, etc.)

```yaml
on:  
  # Agendamento (cron)
  schedule:
    - cron: '0 8 * * *'  # Todo dia às 8h UTC

```

3. Event (Evento)
Gatilho que inicia o workflow
Exemplos: **schedule**, workflow_dispatch, push, pull_request

4. Job (Tarefa)
Conjunto de steps que executa em um mesmo runner: uma função **`main()`**
Jobs podem ser executados em paralelo ou sequencialmente

5. Step (Passo)
Unidade individual de execução

6. Action (Ação)
Comando reutilizável que pode ser compartilhado entre workflows

7. Runner (Executor)
Servidor que executa os workflows
GitHub fornece runners ou você pode usar seus próprios

### Exemplo mínimo configuração
- coletor-diario.ym
- Tarefa: construir `coletor_ipea.py`

### Exemplo concreto
- https://github.com/BAFurtado/ipea_dou_bot
