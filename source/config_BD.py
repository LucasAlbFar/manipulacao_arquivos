from sqlalchemy import create_engine


def criar_engine():
    engine = create_engine('postgresql+psycopg2://username:password@localhost:5432/database')
    return engine