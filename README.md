[<img src="https://img.shields.io/badge/author-Lucas Faria-yellow?style=flat-square"/>](https://github.com/LucasAlbFar)

# Serviço de Manipulação de Dados

Serviço para recebimento arquivo TXT (base_teste.txt), contendo dados das compras realizadas na loja franqueada. Dados serão persistidos antes de se realizar o insert no banco de dados relacional (Postgres). Caso algum registro do arquivo esteja em desacordo com as validações iniciais, o mesmo não será inserido no banco de dados, podendo ser localizado no diretório 'dados/rejeitados'.

## Configurações e Funcionamento:
* Instalar os pacotes identificados no arquivo [requirements.txt](https://github.com/LucasAlbFar/manipulacao_arquivos/blob/main/source/requirements.txt), contendo as bibliotecas necessárias para a execução da aplicação;
* Iniciar banco de Dados PostgreSQL, alterando dados de username, password e database conforme arquitetura local, no arquivo [code/config_db.py](https://github.com/LucasAlbFar/manipulacao_arquivos/blob/main/source/config_BD.py);
* Mover arquivo à ser persistido em diretório raiz [code/dados](https://github.com/LucasAlbFar/manipulacao_arquivos/tree/main/source/dados);
* Executar o programa [code/main.py](https://github.com/LucasAlbFar/manipulacao_arquivos/blob/main/source/main.py);
* Validar a mensagem de retorno final e, caso existam registros rejeitados, localiza-los na diretório [code/dados/rejeitados](https://github.com/LucasAlbFar/manipulacao_arquivos/tree/main/source/dados/rejeitados);
  * O nome do arquivo rejeitado sequirá a regra:
    * 'rejeitados_' + nome do arquivo inicial
* Validar os dados gravados no BD PostgreSQL na table 'dados_validos', criada em processo de execução da aplicação;

## Informações de ambiente:
[requirements.txt](https://github.com/LucasAlbFar/manipulacao_arquivos/blob/main/source/requirements.txt)

## Contato:
[<img src="https://img.shields.io/badge/LucasFaria-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/lucasalbfar/)
[<img src="https://img.shields.io/badge/lucasalbfar@gmail.com-EA4335?style=flat-square&logo=Gmail&logoColor=white" />](mailto:lucasalbfarw@gmail.com)
