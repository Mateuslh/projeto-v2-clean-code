# Reservation Management CLI

> **TL;DR**  
> A modular *Command‑Line* application that manages hotel reservations (create, check‑in, check‑out, reports) using a clean architecture (CLI → Service → Repository → Model). It replaces the original monolithic script with testable, extensible and **fluent‑interface** driven code.

---

## 📦 Descrição do Software & Funcionalidades Principais

| Camada        | Responsabilidade-chave                                   |
|---------------|----------------------------------------------------------|
| **CLI**       | Interação com o usuário (`MenuPrincipal`, `PessoaCLI`, `ReservaCLI`) |
| **Service**   | Regras de negócio (`PessoaService`, `ReservaService`, `RelatorioService`) |
| **Repository**| Persistência em arquivos CSV (subpasta `data/db`)        |
| **Model**     | Entidades (`Pessoa`, `Reserva`) + `Enum`s (`StatusReserva`, `TipoQuarto`) |

Funcionalidades destacadas:

* Cadastro de reservas com cálculo automático de valor (`tarifa × pessoas × diárias`).
* Check‑in / Check‑out controlados por transições de status.
* Alteração ou cancelamento de reservas pendentes.
* Geração de relatórios CSV (por status, por titular, total recebido).
* Persistência leve via CSV sem dependências externas.

---

## 🔍 Análise dos Principais Problemas Detectados (pré‑refatoração)

1. **Código monolítico** com *business logic* misturado a I/O.
2. **Repetição massiva** de validações e `while` loops.
3. **Tratamentos de exceção genéricos** que escondiam falhas.
4. **Baixa testabilidade**: funções dependentes de `input()/print()`.
5. **Persistência frágil** em `.txt` sem cabeçalhos, propensa a corrupção.
6. **Regra de negócios dispersa**, dificultando manutenção.

---

## 🛠️ Estratégia de Refatoração

| Passo | Ação | Resultado |
|-------|------|-----------|
| 1 | Introduzir **camadas claras** (CLI, Service, Repository, Model). | Separação de responsabilidades. |
| 2 | Implementar **Builder Pattern** com **Fluent Interface** | Construção segura e legível de entidades. |
| 3 | Criar **Specifications** de validação | Centralização das regras de negócio. |
| 4 | Migrar arquivos `.txt` → **CSV estruturado** | Dados auto‑descritivos, parsing robusto. |
| 5 | Substituir `try/except` genéricos por erros semânticos | Falhas transparentes para o desenvolvedor. |
| 6 | Adicionar **RelatorioService** | DRY para geração de relatórios. |
| 7 | Preparar ambiente para **pytest** | Base para testes automatizados. |

---

## 📑 ChangeLog

O histórico completo de modificações encontra‑se em [`CHANGELOG.md`](CHANGELOG.md).

---

## 🚀 Interface Fluente (Fluent Interface)

Exemplo de uso do `ReservaBuilder`:

```python
from model.reserva.TipoQuarto import TipoQuarto
from model.reserva.ReservaBuilder import ReservaBuilder

nova_reserva = (
    ReservaBuilder()
    .titular_identificador(1)
    .quantidade_pessoas(2)
    .numero_diarias(3)
    .tipo_quarto_e_valor(TipoQuarto.DELUXE)
    .build()
)
```

*Cada método retorna `self`, permitindo **method chaining** intuitivo e imutabilidade controlada.*

---

## 🏗️ Instalação

```bash
git clone https://github.com/Mateuslh/projeto-v2-clean-code.git
cd projeto-v2-clean-code
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # (somente pytest para dev)
```

> **Prerequisites**: Python **3.10+** (uso de `match/case`).

---

## ▶️ Execução

```bash
python3 main.py
```

Os dados serão criados automaticamente em `data/db` e os relatórios em `data/relatorios`.
Aproveite o projeto! 🎉
