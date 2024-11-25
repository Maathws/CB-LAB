Este projeto tem como objetivo extrair dados de um arquivo ERP.json ou de APIs externas que fornecem informações sobre as operações das lojas de uma rede de restaurantes. O pipeline processa essas informações e armazena no MySQL para análise posterior e em um Data Lake na AWS S3 para arquivamento e acesso organizado.

**Estrutura do projeto**
O projeto é composto pelos seguintes arquivos principais:

retornaDicionarioErp.py: Recupera o arquivo ERP.json de uma URL ou local e retorna os dados como um dicionário Python.
dataBase.py: Gerencia a conexão com o banco de dados MySQL, criação do banco de dados/tabelas e inserção de dados.
desafio.py: Arquivo principal que orquestra o processo de conexão com o banco, criação das tabelas e inserção dos dados obtidos do ERP.
uploadToS3.py: Faz o upload dos dados processados para um Data Lake na AWS S3, organizando os arquivos por endpoint e data.

**Bibliotecas:**
requests - Para fazer requisições HTTP.
mysql-connector - Para interação com o banco de dados MySQL.
python-dotenv - Para carregar variáveis de ambiente.
boto3: Para integração com o AWS S3 e envio dos dados ao Data Lake.


**Clone o repositório:**

No terminal: 
- git clone https://github.com/Maathws/CB-LAB


**Instale as dependências:**
No terminal via arquivo requirements.txt:
- pip install -r requirements.txt

No terminal via pip:
- pip install requests mysql-connector-python python-dotenv boto3


**Configuração do Banco de Dados e Amazon S3:**

Crie um arquivo .env na raiz do projeto com as variáveis de ambiente para as credenciais do banco de dados e AWS S3:

.env:
DATABASE_HOST=...
DATABASE_PORT=...
DATABASE_USER=...
DATABASE_PASSWORD=...
AWS_S3_REGION_NAME=...
AWS_S3_ACESS_KEY_ID=...
AWS_S3_SECRET_KEY=...



O arquivo dataBase.py contém a lógica para criar o banco de dados e as tabelas necessárias. Certifique-se de que o banco de dados MySQL está rodando e que as credenciais estão configuradas corretamente.

**Execução do Projeto**
Rodar o processo:

Para executar o pipeline completo, basta rodar o arquivo desafio.py, que irá:

Conectar-se ao banco de dados.
Criar o banco de dados e as tabelas necessárias.
Recuperar o arquivo ERP.json e processá-lo.
Inserir os dados no banco de dados.


No terminal, execute o seguinte comando:
- python desafio.py

E em seguida o arquivo desafio2.py, que irá:
Conectar ao S3 da AWS.
Fazer upload do json já filtrado para cada endpoint específico.


**Estrutura do Banco de Dados:**

O banco de dados criado é o restauranteasanorte e contém as seguintes tabelas:

guest_checks: Contém informações gerais sobre os pedidos.
menu_item: Contém detalhes sobre os itens do menu consumidos no pedido.
taxes: Contém informações sobre as taxas aplicadas aos pedidos.
detail_lines: Contém detalhes sobre as linhas do pedido, como os itens específicos e seus totais.


**Funções Principais**
retornaDicionarioErpUsandoRequests: Faz uma requisição HTTP para obter o arquivo ERP.json da URL especificada e retorna os dados em formato de dicionário.
retornaDicionarioErp: Abre o arquivo local ERP.json e retorna os dados em formato de dicionário.
conectarDataBaseGeral: Conecta ao banco de dados MySQL usando as credenciais configuradas no arquivo .env.
criarDataBaseRestaurantesETabelas: Cria o banco de dados restauranteasanorte e as tabelas necessárias para armazenar os dados dos pedidos e itens de menu.
inserirDataBaseRestaurantesETabelas: Insere os dados dos pedidos no banco de dados.
uploadJsonS3: Realiza o upload dos dados processados em formato JSON para o AWS S3, organizando os arquivos por API e data.


**Considerações Finais**
Este projeto foi desenvolvido para processar e organizar dados de pedidos das lojas de forma eficiente, armazenando-os em um banco de dados MySQL para análises rápidas e estruturadas, além de integrar com um Data Lake na AWS S3, onde arquivos JSON filtrados são organizados por endpoint, garantindo acessibilidade e suporte às demandas de inteligência de dados. Modular e escalável, o projeto pode ser facilmente expandido para incorporar novos endpoints e se adaptar às necessidades do negócio, tornando-se uma solução flexível e robusta para gestão e análise de dados.