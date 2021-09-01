[<img src="https://img.shields.io/badge/author-Lucas Faria-yellow?style=flat-square"/>](https://github.com/LucasAlbFar)

# Serviço de Manipulação de Dados

Realizar a insereção de registros em BD PostgreSQL, recuperados através de arquivo TXT ou CSV. 

## Configurações e Funcionamento:
* Instalar os pacotes identificados no arquivo [requirements.txt](https://github.com/LucasAlbFar/manipulacao_arquivos/blob/main/source/requirements.txt), contendo as bibliotecas necessárias para a execução da aplicação;
* Iniciar banco de Dados PostgreSQL, com database 'dados_validos', alterando dados de username e password conforme arquitetura local, no arquivo 'config_db.py' localizado no na pasta [code](https://github.com/LucasAlbFar/manipulacao_arquivos/blob/main/source/config_BD.py);
* Mover arquivo à ser persistido em diretório raiz [dados](https://github.com/LucasAlbFar/manipulacao_arquivos/tree/main/source/dados);
* Executar o programa [main.py](https://github.com/LucasAlbFar/manipulacao_arquivos/blob/main/source/main.py);
* Validar a mensagem de retorno final e, caso exista registros rejeitados, localiza-los na diretório [dados/rejeitados](https://github.com/LucasAlbFar/manipulacao_arquivos/tree/main/source/dados/rejeitados);
  * O nome do arquivo rejeitado sequirá a seguinte regra:
    * 'rejeitados_' + nome do arquivo inicial


## Funcionamento:
Ao iniciar a aplicação, os dados de PERSON TYPE e MEDIA TYPE serão automaticamente carregados com alguns valores defaut, sendo que o client poderá incluir novas categorias na tabela PERSON TYPE através do comando POST.
Com o sistema carregado, será possível registrar uma nova pessoa no sistema, informando o NAME, CPF, COMPANY e PERSON TYPE como dados obrigatórios e PHONE como dado opcional. 
Após o cadastro é possível visualizar o registro de auditoria no '/audit/' ou '/listaudit/<int:pk>/' através do ID da tabela PERSON, todas as pessoas registradas através da '/person/' ou listar somente os dados de uma pessoa através do '/listperson/<int:cpf>/', informando o CPF desejado. 
Através do comando PACTH, será possível atualizar os dados do registro de uma pessoa. Caso haja atualização do CPF, o mesmo será registrado na auditoria, ou quando houver uma atualização com o registro da pessoa, a base de dado de auditoria também será atualizada.
Com o cadastro de um indivíduo finalizado, será possível incluir uma mídia de identificação (foto ou biometria). O uploada se realiza através da URL '/media/', informando para qual pessoa cadastrada será vinculada a imagem e a aplicação converterá a imagem para a base64. A consulta das mídias poderá ser realizada pela '/listmedia/<int:pk>/' informando o ID da tabela PERSON.

## Estratégias:
* Por motivo de usabilidade, a própria aplicação realiza a conversão para um arquivo de 256kb;
* Para limitar o número de tipos de mídia (MEDIA TYPE), não foi disponibilizado um endpoint para realizar o POST nesta tabela;

## Informações de ambiente:
[requirements.txt](https://github.com/LucasAlbFar/manipulacao_arquivos/blob/main/source/requirements.txt)

## Contato:
[<img src="https://img.shields.io/badge/LucasFaria-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/lucasalbfar/)
[<img src="https://img.shields.io/badge/lucasalbfar@gmail.com-EA4335?style=flat-square&logo=Gmail&logoColor=white" />](mailto:lucasalbfarw@gmail.com)
