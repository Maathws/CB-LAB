Este projeto tem como objetivo extrair dados de um arquivo ERP.json ou de uma API externa que forneça informações sobre as operações das lojas de uma rede de restaurantes. O pipeline processa essas informações e armazena em um banco de dados MySQL para análise posterior.

Estrutura do Projeto
O projeto é composto por três arquivos principais:

retornaDicionarioErp.py: Responsável por recuperar o arquivo ERP.json de uma URL ou de um arquivo local e retornar os dados como um dicionário Python.

dataBase.py: Responsável pela conexão com o banco de dados MySQL, criação do banco de dados e tabelas, e inserção dos dados no banco.

desafio.py: Arquivo principal que orquestra o processo de conexão com o banco, criação das tabelas e inserção dos dados obtidos do ERP.

Bibliotecas:
requests - Para fazer requisições HTTP.
mysql-connector - Para interação com o banco de dados MySQL.
python-dotenv - Para carregar variáveis de ambiente.


Clone o repositório:

No terminal: 
- git clone https://github.com/usuario/repositorio.git
- cd repositorio


Instale as dependências:
No terminal via arquivo requirements.txt:
- pip install -r requirements.txt

No terminal via arquivo requirements.txt:
- pip install requests mysql-connector-python python-dotenv


Configuração do Banco de Dados:

Crie um arquivo .env na raiz do projeto com as variáveis de ambiente para as credenciais do banco de dados:

.env:

DATABASE_HOST=
DATABASE_PORT=
DATABASE_USER=
DATABASE_PASSWORD=

O arquivo dataBase.py contém a lógica para criar o banco de dados e as tabelas necessárias. Certifique-se de que o banco de dados MySQL está rodando e que as credenciais estão configuradas corretamente.

Execução do Projeto
Rodar o processo:

Para executar o pipeline completo, basta rodar o arquivo desafio.py, que irá:

Conectar-se ao banco de dados.
Criar o banco de dados e as tabelas necessárias.
Recuperar o arquivo ERP.json e processá-lo.
Inserir os dados no banco de dados.


No terminal, execute o seguinte comando:
- python desafio.py


Estrutura do Banco de Dados:

O banco de dados criado é o restauranteasanorte e contém as seguintes tabelas:

guest_checks: Contém informações gerais sobre os pedidos.
menu_item: Contém detalhes sobre os itens do menu consumidos no pedido.
taxes: Contém informações sobre as taxas aplicadas aos pedidos.
detail_lines: Contém detalhes sobre as linhas do pedido, como os itens específicos e seus totais.


Funções Principais
retornaDicionarioErpUsandoRequests: Faz uma requisição HTTP para obter o arquivo ERP.json da URL especificada e retorna os dados em formato de dicionário.
retornaDicionarioErp: Abre o arquivo local ERP.json e retorna os dados em formato de dicionário.
conectarDataBaseGeral: Conecta ao banco de dados MySQL usando as credenciais configuradas no arquivo .env.
criarDataBaseRestaurantesETabelas: Cria o banco de dados restauranteasanorte e as tabelas necessárias para armazenar os dados dos pedidos e itens de menu.
inserirDataBaseRestaurantesETabelas: Insere os dados dos pedidos no banco de dados.


Considerações Finais
Este projeto tem como objetivo processar os dados dos pedidos das lojas de forma eficiente, armazenando-os em um banco de dados MySQL para posterior análise. Ele pode ser expandido para suportar novas APIs ou adaptado conforme as necessidades do negócio.