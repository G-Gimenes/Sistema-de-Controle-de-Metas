# 🏭 Sistema de Controle de Metas Industriais

Aplicação web desenvolvida com **Flask** no backend e frontend em **HTML/JavaScript/Bootstrap**, voltada para o gerenciamento de metas de produção em ambientes industriais. Permite o registro, edição e visualização de metas por unidade e tipo de produção, com integração direta a arquivos Excel.
Agora inclui **autenticação via Firebase**, garantindo um login seguro com validação de token no backend.

---

# 🚀 Funcionalidades

* Login moderno utilizando **Firebase Authentication** (email/senha)
* Interface intuitiva para inserção e edição de metas
* Criação automática do arquivo `meta_industria.xlsx` caso não exista
* Formulário dinâmico e edição direta na tabela
* Formatação automática:

  * Datas no padrão **DD/MM/YYYY**
  * Valores numéricos com duas casas decimais (0,00)
* Ordenação e movimentação de linhas (subir, descer, remover)
* Validação de campos obrigatórios, datas e valores
* Salvamento seguro com **thread lock** para evitar conflitos de escrita
* Compatível com múltiplos navegadores e responsivo para dispositivos móveis
* Logs de acesso registrados automaticamente

---

# 🧰 Tecnologias Utilizadas

* **Backend:** Python, Flask, Pandas, OpenPyXL
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
* **Extras:** Flask-CORS, Threading, Firebase Admin SDK, Manipulação de Excel

---

# 📁 Estrutura do Projeto

```
/uploads              # Armazena os arquivos Excel gerados
/static               # Arquivos estáticos (CSS, JS, imagens)
/templates/index.html # Template principal da aplicação
/templates/login_index.html # Tela de login com Firebase
app.py                # Arquivo principal da aplicação Flask
serviceAccountKey.json # Credenciais do Firebase Admin SDK
/logs                 # Armazena logs de acessos
```

---

# 🛠️ Como Executar

1. Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_PROJETO>
```

2. (Opcional) Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure o **Firebase Admin SDK**:

* Gere o arquivo **Service Account** no Firebase Console
* Salve o arquivo como `serviceAccountKey.json` na raiz do projeto
* No `app.py`, ajuste o caminho:

```python
cred = credentials.Certificate(os.path.join(BASE_DIR, 'serviceAccountKey.json'))
firebase_admin.initialize_app(cred)
```

5. Execute a aplicação:

```bash
python app.py
```

6. Acesse no navegador:

```
http://localhost:5000
```

---

# 📌 Observações

* O arquivo Excel é salvo automaticamente na pasta `/uploads`
* A aplicação é responsiva e pode ser usada em dispositivos móveis
* Recomenda-se o uso de navegadores atualizados para melhor compatibilidade
* O login utiliza **Firebase Authentication** para segurança real de credenciais
* Logs de acessos são salvos automaticamente em `/logs/acessos.log`
* A autenticação via token garante que apenas usuários válidos possam acessar o dashboard

