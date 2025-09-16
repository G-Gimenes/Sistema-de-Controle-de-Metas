# 🏭 Sistema de Controle de Metas Industriais
Aplicação web desenvolvida com Flask e frontend em HTML/JavaScript/Bootstrap, voltada para o gerenciamento de metas de produção em ambientes industriais. Permite o registro, edição e visualização de metas por unidade e tipo de produção, com integração direta a arquivos Excel.


# 🚀 Funcionalidades
- Interface intuitiva para inserção e edição de metas
- Criação automática do arquivo meta_industria.xlsx caso não exista
- Formulário dinâmico e edição direta na tabela
- Formatação automática:
- Datas no padrão DD/MM/YYYY
- Valores numéricos com duas casas decimais (0,00)
- Ordenação e movimentação de linhas (subir, descer, remover)
- Validação de campos obrigatórios, datas e valores
- Salvamento seguro com thread lock para evitar conflitos de escrita
- Compatível com múltiplos navegadores e responsivo para dispositivos móveis
- 

# 🧰 Tecnologias Utilizadas
| Backend | Python, Flask, Pandas, OpenPyXL | 
| Frontend | HTML5, CSS3, JavaScript, Bootstrap 5 | 
| Extras | Flask-CORS, Threading, Manipulação de Excel | 


# 📁 Estrutura do Projeto
/uploads              # Armazena os arquivos Excel gerados
/static               # Arquivos estáticos (CSS, JS, imagens)
/templates/index.html # Template principal da aplicação
app.py                # Arquivo principal da aplicação Flask


# 🛠️ Como Executar
- Clone o repositório:
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_PROJETO>


- (Opcional) Crie e ative um ambiente virtual:
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


- Instale as dependências:
pip install -r requirements.txt


- Execute a aplicação:
python app.py


- Acesse no navegador:
http://localhost:5000


# 📌 Observações
- O arquivo Excel é salvo automaticamente na pasta /uploads
- A aplicação é responsiva e pode ser usada em dispositivos móveis
- Recomenda-se o uso de navegadores atualizados para melhor compatibilidade
- Login simples incluído: a aplicação conta com uma tela de login básica, que não fornece segurança criptografada. Foi pensado para sistemas internos, onde a principal necessidade é apenas controlar o acesso via
logs
