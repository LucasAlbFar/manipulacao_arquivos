[<img src="https://img.shields.io/badge/author-Lucas Faria-yellow?style=flat-square"/>](https://github.com/LucasAlbFar)

# Serviço de Manipulação de Dados

Realizar a insereção de registros em BD PostgreSQL, recuperados através de arquivo TXT ou CSV. 

## Configurações e Funcionamento:
* Instalar os pacotes identificados no arquivo [requirements.txt](https://github.com/LucasAlbFar/manipulacao_arquivos/blob/main/source/requirements.txt), contendo as bibliotecas necessárias para a execução da aplicação;
* Iniciar banco de Dados PostgreSQL, alterando dados de username, password e database conforme arquitetura local, no arquivo [code/config_db.py](https://github.com/LucasAlbFar/manipulacao_arquivos/blob/main/source/config_BD.py);
* Mover arquivo à ser persistido em diretório raiz [code/dados](https://github.com/LucasAlbFar/manipulacao_arquivos/tree/main/source/dados);
* Executar o programa [code/main.py](https://github.com/LucasAlbFar/manipulacao_arquivos/blob/main/source/main.py);
* Validar a mensagem de retorno final e, caso existam registros rejeitados, localiza-los na diretório [code/dados/rejeitados](https://github.com/LucasAlbFar/manipulacao_arquivos/tree/main/source/dados/rejeitados);
  * O nome do arquivo rejeitado sequirá a seguinte regra:
    * 'rejeitados_' + nome do arquivo inicial
* Validar os dados gravados no BD PostgreSQL na table 'dados_validos', criada em processo de execução da aplicação;

## Funcionalidades da aplicação:
Ao iniciar a aplicação, os dados de PERSON TYPE e MEDIA TYPE serão automaticamente carregados com alguns valores defaut, sendo que o client poderá incluir novas categorias na tabela PERSON TYPE através do comando POST.
Com o sistema carregado, será possível registrar uma nova pessoa no sistema, informando o NAME, CPF, COMPANY e PERSON TYPE como dados obrigatórios e PHONE como dado opcional. 
Após o cadastro é possível visualizar o registro de auditoria no '/audit/' ou '/listaudit/<int:pk>/' através do ID da tabela PERSON, todas as pessoas registradas através da '/person/' ou listar somente os dados de uma pessoa através do '/listperson/<int:cpf>/', informando o CPF desejado. 
Através do comando PACTH, será possível atualizar os dados do registro de uma pessoa. Caso haja atualização do CPF, o mesmo será registrado na auditoria, ou quando houver uma atualização com o registro da pessoa, a base de dado de auditoria também será atualizada.
Com o cadastro de um indivíduo finalizado, será possível incluir uma mídia de identificação (foto ou biometria). O uploada se realiza através da URL '/media/', informando para qual pessoa cadastrada será vinculada a imagem e a aplicação converterá a imagem para a base64. A consulta das mídias poderá ser realizada pela '/listmedia/<int:pk>/' informando o ID da tabela PERSON.

## Informações de ambiente:
[requirements.txt](https://github.com/LucasAlbFar/manipulacao_arquivos/blob/main/source/requirements.txt)

## Contato:
[<img src="https://img.shields.io/badge/LucasFaria-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/lucasalbfar/)
[<img src="https://img.shields.io/badge/lucasalbfar@gmail.com-EA4335?style=flat-square&logo=Gmail&logoColor=white" />](mailto:lucasalbfarw@gmail.com)
