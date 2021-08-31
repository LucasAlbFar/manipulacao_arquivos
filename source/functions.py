import glob
import pandas as pd
from validate_docbr import CPF, CNPJ
from config_BD import criar_engine


def recuperar_arquivos_em_diretorio():
    """
      Recuperar os arquivos que estejam contidos no diretório 'dados' a serem processados
      Retorno: Lista com todos os arquivos do diretório
    """
    arquivos = []
    for arquivo in glob.glob("dados/*.txt"):
        arquivos.append(arquivo[6:])

    return arquivos


def carregar_dados(nome_arquivo: str):
    """
      Carregar arquivo contendo os dados a serem persistidos em banco de dados
      Retorno: Pandas DataFrame
    """
    diretorio = 'dados/' + nome_arquivo
    df = pd.read_csv(diretorio, delim_whitespace=True, encoding="ISO-8859-1", skiprows=1)
    df.columns = ['CPF', 'PRIVATE', 'INCOMPLETO', 'DATA_ULTIMA_COMPRA', 'TICKET_MEDIO', 'TICKET_ULTIMA_COMPRA',
                  'LOJA_MAIS_FREQUENTE', 'LOJA_ULTIMA_COMPRA']

    return df


def converter_campo_para_tipo_float(df: pd.DataFrame):
    """
      Realizar chamada de funções para conversão de tipo de dados
    """
    df['TICKET_MEDIO'] = converter_para_float(df['TICKET_MEDIO'])
    df['TICKET_ULTIMA_COMPRA'] = converter_para_float(df['TICKET_ULTIMA_COMPRA'])


def limpar_campo_cpf_e_cnpj(df: pd.DataFrame):
    """
      Realizar chamada de funções para realizar a limpeza de campos cpf e cpnj
    """
    df['CPF'] = limpar_campo_doc(df['CPF'])
    df['LOJA_MAIS_FREQUENTE'] = limpar_campo_doc(df['LOJA_MAIS_FREQUENTE'])
    df['LOJA_ULTIMA_COMPRA'] = limpar_campo_doc(df['LOJA_ULTIMA_COMPRA'])


def converter_campo_para_datatime(df: pd.DataFrame):
    """
      Realizar chamada de função para conversão de campo para tipo datetime
    """
    df['DATA_ULTIMA_COMPRA'] = pd.to_datetime(df['DATA_ULTIMA_COMPRA'])


def substituir_campos_nan(df: pd.DataFrame):
    """
      Realizar a conversão de dados NaN para valores '0'
    """
    return df.fillna('0')


def validar_cpf_e_cnpj(df: pd.DataFrame):
    """
      Realizar chamada de função para validar campos CPF e CNPJ, criando colunas dummy identificando os documentos
      válidos e inválidos
    """
    df['CPF_VALIDO'] = [cpf_valido(cpf) for cpf in df['CPF']]
    df['CNPJ_LOJA_MAIS_FREQUENTE_VALIDO'] = [cnpj_valido(cnpj) for cnpj in df['LOJA_MAIS_FREQUENTE']]
    df['CNPJ_LOJA_ULTIMA_COMPRA_VALIDO'] = [cnpj_valido(cnpj) for cnpj in df['LOJA_ULTIMA_COMPRA']]


def selecionar_dados_validos(df: pd.DataFrame):
    """
      Realizar chamada de função para selecionar dados que contém CPF e CNPJ válidos
    """
    selecao = ((df['CPF_VALIDO'] == True) & (df['CNPJ_LOJA_MAIS_FREQUENTE_VALIDO'] == True) &
               (df['CNPJ_LOJA_ULTIMA_COMPRA_VALIDO'] == True))

    return realizar_selecao(selecao, df)


def selecionar_dados_invalidos(df: pd.DataFrame):
    """
      Realizar chamada de função para selecionar dados que contém CPF e CNPJ inválidos
    """
    selecao = ((df['CPF_VALIDO'] == False) | (df['CNPJ_LOJA_MAIS_FREQUENTE_VALIDO'] == False) |
                         (df['CNPJ_LOJA_ULTIMA_COMPRA_VALIDO'] == False))

    return realizar_selecao(selecao, df)


def salvar_arquivo_rejeitados(dados_invalidos: pd.DataFrame, nome_arquivo: str):
    """
      Salvar Pandas DataFrames gerados na execução da rotina em arquivos CSV
    """
    if dados_invalidos.shape[0] > 0:
        diretorio = 'dados/rejeitados/dados_invalidos_' + nome_arquivo + '.csv'
        dados_invalidos.to_csv(diretorio, index=False)


def gravar_em_banco_dados(df: pd.DataFrame):
    """
      Gravar dados válidos em banco de dados PostgreSQL
    """
    if df.shape[0] > 0:
        engine = criar_engine()
        df.to_sql('dados', engine, if_exists='replace', index=False)
        # df.to_sql('dados', engine, if_exists='append', index=False)


def mensagem_final(dados_validos: pd.DataFrame, dados_invalidos: pd.DataFrame, nome_arquivo: str):
    """
      Exibir mensagem final
    """
    print(f'Gravado(s) {dados_validos.shape[0]} registro(s) e descartado(s) '
          f'{dados_invalidos.shape[0]} registro(s), do arquivo {nome_arquivo}.')


def converter_para_float(dados: pd.DataFrame):
    """
      Converter para tipo float a coluna  de dados recebida via parâmetro, alterando o separado ',' para '.'
      Parâmetro: Dados da coluna do dataframe a ter seus dados convertidos para float
      Retorno: Dados convertidos para float
    """
    dados = dados.str.replace(',', '.').astype(float)

    return dados


def limpar_campo_doc(coluna_documento: pd.DataFrame):
    """
      Realizar a limpeza de campo documento, removendo caracteres não-numéricos
      Parâmetro: Coluna que contém os dados de documento a ser higienizado
                 Identificador de coluna que contém campo CNPJ
      Retorno: Coluna com dados higienizados
    """
    coluna_documento = coluna_documento.str.replace('.', '')
    coluna_documento = coluna_documento.str.replace('-', '')

    if len(coluna_documento) > 11:
        coluna_documento = coluna_documento.str.replace('/', '')

    return coluna_documento


def cpf_valido(num_cpf: str):
    """
      Validar campo CPF
      Parâmetro: num_cpf a ser validado
      Retorno: Indicador TRUE or FALSE para o campo CPF
    """
    cpf = CPF()

    return cpf.validate(num_cpf)


def cnpj_valido(num_cnpj: str):
    """
      Validar campo CNPJ
      Parâmetro: num_cnpj a ser validado
      Retorno: Indicador TRUE or FALSE para o campo CNPJ
    """
    cnpj = CNPJ()

    if num_cnpj == '0':
        return True
    else:
        return cnpj.validate(num_cnpj)


def realizar_selecao(selecao: pd.Series, df_base: pd.DataFrame):
    """
      Selecionar os registros em 'df_base', à partir de cláusula contida na series 'seleção'
      Parâmetro: selecao contendo os dados recuperados
                  df_base contendo o pandas DataFrame a ser realizado a busca pelos dados
      Retorno: Pandas DataFrame contendo os dados selecionados, excluído colunas fora do escopo da persistência em banco de dados
    """

    df_retorno = df_base[selecao]
    df_retorno = df_retorno.drop(['CPF_VALIDO', 'CNPJ_LOJA_MAIS_FREQUENTE_VALIDO',
                                  'CNPJ_LOJA_ULTIMA_COMPRA_VALIDO'], axis=1)

    return df_retorno



