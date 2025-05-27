import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PASTA_DADOS = os.path.join(BASE_DIR, "data")
PASTA_BANCO_DADOS = os.path.join(PASTA_DADOS, "db")
PASTA_RELATORIOS = os.path.join(PASTA_DADOS, "relatorios")

os.makedirs(PASTA_BANCO_DADOS, exist_ok=True)
os.makedirs(PASTA_RELATORIOS, exist_ok=True)
