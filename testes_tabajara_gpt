import importlib
import io
import os
import random
import shutil
import tempfile
from contextlib import redirect_stdout

import pytest

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

class CliRunner:
    """Feed a sequence of answers to built‑in input() and capture stdout."""

    def __init__(self, answers):
        self.answers = list(map(str, answers))
        self._gen = (a for a in self.answers)

    def __call__(self, _prompt=""):
        try:
            return next(self._gen)
        except StopIteration as exc:
            raise AssertionError("CLI pediu mais entradas do que as fornecidas.") from exc


# ---------------------------------------------------------------------------
# Pytest fixtures – cada teste roda em ambiente isolado de arquivos
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def _isolar_dados(monkeypatch):
    """Cria diretório temporário para data/db e data/relatorios e remapeia Caminhos."""
    tmp_root = tempfile.mkdtemp()
    db_dir = os.path.join(tmp_root, "db"); os.makedirs(db_dir)
    rel_dir = os.path.join(tmp_root, "rel"); os.makedirs(rel_dir)

    # patch Caminhos antes de recarregar dependências
    import config.Caminhos as caminhos
    monkeypatch.setattr(caminhos, "PASTA_DADOS", tmp_root, raising=False)
    monkeypatch.setattr(caminhos, "PASTA_BANCO_DADOS", db_dir, raising=False)
    monkeypatch.setattr(caminhos, "PASTA_RELATORIOS", rel_dir, raising=False)

    # recarrega módulos que seguram caminhos
    for mod in [
        "repository.PessoaRepository",
        "repository.ReservaRepository",
        "service.RelatorioService",
        "service.PessoaService",
        "service.ReservaService",
        "cli.ReservaCLI",
        "cli.PessoaCLI",
        "cli.MenuPrincipal",
    ]:
        if mod in importlib.sys.modules:
            importlib.reload(importlib.import_module(mod))

    yield
    shutil.rmtree(tmp_root, ignore_errors=True)


# ---------------------------------------------------------------------------
# Utilidades de teste CLI
# ---------------------------------------------------------------------------

from cli import MenuPrincipal as menu_cli


def _novo_cpf():
    return "".join(str(random.randint(0, 9)) for _ in range(11))


def _run_cli(answers):
    runner = CliRunner(answers)
    backup_input = __builtins__["input"]
    __builtins__["input"] = runner
    buf = io.StringIO()
    try:
        with redirect_stdout(buf):
            try:
                menu_cli.MenuPrincipal.exibir_menu()
            except SystemExit:
                pass  # saída normal
    finally:
        __builtins__["input"] = backup_input
    return buf.getvalue()


# ---------------------------------------------------------------------------
# 20 TESTES END‑TO‑END 100 % CLI
# ---------------------------------------------------------------------------

# 1  fluxo completo básico

def test_cli_fluxo_completo():
    cpf = _novo_cpf()
    out = _run_cli([
        "1", cpf, "Fulano", "1", "1", "S",  # cria
        "2", cpf, "1",                           # check‑in
        "3", cpf, "1",                           # check‑out
        "6"
    ])
    assert "Reserva criada" in out
    assert "Check-in concluído." in out
    assert "Check-out concluído." in out


# 2 cancelar reserva e listar relatório C

def test_cli_cancelar_reserva():
    cpf = _novo_cpf()
    out = _run_cli([
        "1", cpf, "Teste", "1", "1", "S",
        "4", cpf, "1", "C",  # cancela
        "5", "2",              # relatório C
        "6"
    ])
    assert "Reserva cancelada" in out
    assert "Arquivo gerado" in out


# 3 alterar reserva (pessoas/diárias/quarto)

def test_cli_alterar_reserva():
    cpf = _novo_cpf()
    out = _run_cli([
        "1", cpf, "Teste", "1", "1", "S",
        "4", cpf, "1", "E", "2", "3", "P",
        "6"
    ])
    assert "Reserva atualizada." in out


# 4 total recebido após finalizar

def test_cli_total_recebido():
    cpf = _novo_cpf()
    out = _run_cli([
        "1", cpf, "Teste", "1", "1", "D",
        "2", cpf, "1",
        "3", cpf, "1",
        "5", "5",
        "6"
    ])
    assert "Total recebido" in out
    assert "200.00" in out  # Deluxe


# 5 menu principal repete em opção inválida

def test_cli_menu_invalido():
    out = _run_cli(["9", "x", "6"])
    assert out.count("Opção inválida") >= 2


# 6 criar duas reservas e IDs incrementam

def test_cli_ids_incrementam():
    cpf = _novo_cpf()
    out = _run_cli([
        "1", cpf, "T1", "1", "1", "S",
        "1", cpf,              "1", "1", "S",
        "6"
    ])
    assert "identificador=2" in out  # segunda reserva deve ser id 2


# 7 tentativa check‑in sem reservas

def test_cli_checkin_sem_reserva():
    cpf = _novo_cpf()
    out = _run_cli([
        "2", cpf,               # check‑in
        "6"
    ])
    assert "Nenhuma reserva aguardando check-in" in out


# 8 tentativa check‑out sem ativo

def test_cli_checkout_sem_ativo():
    cpf = _novo_cpf()
    out = _run_cli([
        "1", cpf, "Teste", "1", "1", "S",
        "3", cpf,            # checkout sem ativo
        "6"
    ])
    assert "Nenhuma reserva em hospedagem" in out


# 9 relatorio reservas R

def test_cli_relatorio_status_r():
    cpf = _novo_cpf()
    out = _run_cli([
        "1", cpf, "Teste", "1", "1", "S",
        "5", "1",            # relatório R
        "6"
    ])
    assert "Arquivo gerado" in out


# 10 relatorio por titular

def test_cli_relatorio_por_titular():
    cpf = _novo_cpf()
    out = _run_cli([
        "1", cpf, "Teste", "1", "1", "S",
        "5", "6", cpf,       # relatório por titular
        "6"
    ])
    assert "Arquivo gerado" in out


# 11 tipo de quarto código minúsculo + correção

def test_cli_quarto_minusculo():
    cpf = _novo_cpf()
    out = _run_cli([
        "1", cpf, "Fulano", "1", "1", "x", "p",  # x errado, depois p
        "6"
    ])
    assert out.count("Inválido") >= 1
    assert "Reserva criada" in out


# 12 CPF inexistente no check‑in

def test_cli_cpf_nao_encontrado():
    cpf = _novo_cpf()
    out = _run_cli([
        "2", cpf,      # nenhum cadastro
        "6"
    ])
    assert "CPF não encontrado" in out


# 13 usar ID numérico no check‑in/out

def test_cli_usar_id_numerico():
    cpf = _novo_cpf()
    out = _run_cli([
        "1", cpf, "A", "1", "1", "S",
        "2", "1", "1",  # ID do titular (1)
        "3", "1", "1",
        "6"
    ])
    assert "Check-out concluído" in out


# 14 cancelamento depois de alteração gera erro

def test_cli_alterar_depois_checkin_erro():
    cpf = _novo_cpf()
    out = _run_cli([
        "1", cpf, "T", "1", "1", "S",
        "2", cpf, "1",            # checkin ativo
        "4", cpf, "1", "E",      # tentar alterar após checkin (deve falhar)
        "6"
    ])
    assert "apenas reservas com status R".lower() in out.lower()


# 15 geração de total recebido com várias reservas

def test_cli_total_recebido_varios():
    cpf = _novo_cpf()
    out = _run_cli([
        "1", cpf, "T", "1", "1", "D",
        "2", cpf, "1",
        "1", cpf,       "1", "1", "P",
        "2", cpf, "2",
        "3", cpf, "1",
        "3", cpf, "2",
        "5", "5",
        "6"
    ])
    assert "Total recebido" in out
    assert "500.00" in out  # 200 + 300


# 16 fluxo de cancelamento após alteração aceitável

def test_cli_cancelamento_pos_alteracao():
    cpf = _novo_cpf()
    out = _run_cli([
        "1", cpf, "X", "1", "1", "S",
        "4", cpf, "1", "E", "2", "2", "D",
        "4", cpf, "1", "C",
        "5", "2",
        "6"
    ])
    assert "Reserva cancelada" in out


# 17 opção relatorio inválida pede de novo titular

def test_cli_relatorio_invalido_pede_titular():
    cpf = _novo_cpf()
    out = _run_cli([
        "1", cpf, "Y", "1", "1", "S",
        "5", "9", "6"
    ])
    assert "Opção" in out  # o menu reaparece


# 18 sair com opção 6 exibe Saindo...

def test_cli_sair_mostra_msg():
    out = _run_cli(["6"])
    assert "Saindo" in out


# 19 tentar mudar status inválido (R -> F) via CLI programa

def test_cli_transicao_invalida():
    cpf = _novo_cpf()
    out = _run_cli([
        "1", cpf, "Z", "1", "1", "S",
        "3", cpf, "1",   # tenta checkout direto
        "6"
    ])
    assert "Transição" in out or "nenhuma" in out.lower()


# 20 menu relatório mostra texto

def test_cli_menu_relatorio_texto():
    out = _run_cli(["5", "6"])
    assert "Relatórios disponíveis" in out
