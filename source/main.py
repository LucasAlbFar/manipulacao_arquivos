from functions import *


def run():
    lista_arquivos = recuperar_arquivos_em_diretorio()

    for arquivo in lista_arquivos:
        dados = carregar_dados(arquivo)
        converter_campo_para_tipo_float(dados)
        limpar_campo_cpf_e_cnpj(dados)
        converter_campo_para_datatime(dados)
        dados = substituir_campos_nan(dados)
        validar_cpf_e_cnpj(dados)
        dados_validos = selecionar_dados_validos(dados)
        dados_invalidos = selecionar_dados_invalidos(dados)
        salvar_arquivo_invalido_csv(dados_invalidos, arquivo)
        gravar_em_banco_dados(dados_validos)
        mensagem_final(dados_validos, dados_invalidos, arquivo)


if __name__ == '__main__':
    run()
