from sqlalchemy import create_engine


def criar_engine():
    engine = create_engine('postgresql+psycopg2://postgres:noadmin@localhost:5432/dados_validos')
    return engine