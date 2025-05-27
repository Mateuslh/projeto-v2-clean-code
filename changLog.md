
---

## [1.0.0] – 27/05/2025
### ✨ Adicionado
- **Camada Service**
  - `PessoaService`, `ReservaService`, `RelatorioService` organizam as regras de negócios e orquestram chamadas ao repositório.
- **Camada CLI**
  - `MenuPrincipal` com `match/case` (Python 3.10+).
  - `PessoaCLI` e `ReservaCLI` para entrada de dados e exibição de resultados.
- **Módulo de Relatórios**
  - `RelatorioService` gera CSV por status, por titular e TXT com o total recebido.
  - Arquivos criados automaticamente em `data/relatorios`.
- **Bootstrap de Infraestrutura**
  - Criação automática das pastas `data/db` e `data/relatorios` na primeira execução.
- **Helpers de UI**
  - Função `_linha(*valores)` para tabelas alinhadas no terminal.
  - Mensagens de feedback com `time.sleep()` ajustadas para UX.

### 🔄 Alterado
- **Persistência**  
  - Migração de arquivos texto sem formatação para **CSV** com cabeçalho e separador padrão, reduzindo riscos de parsing incorreto.
- **Cálculo de Valor de Reserva**  
  - Centralizado em `ReservaBuilder.calcular_valor`, removendo duplicações.
- **Validação de Entrada**  
  - Reuso de métodos helpers em vez de `while` duplicados por menu.

### 🗑️ Removido
- Arquivos temporários `*2.txt` gerados nas etapas de relatórios/check‑in/out.
- Concatenações manuais com vírgulas no código legado.
- Blocos repetidos de `try/except` engolindo exceções.

### 🛠️ Corrigido
- Geração de **ID** agora funciona quando o arquivo está vazio (antes gerava string vazia).
- Cálculo de **total recebido** usa `sum()` sobre `float`, evitando erros de conversão de string.

### 🔐 Segurança / Integridade
- `ReservaSpecification.validar_transicao_status` impede transições inválidas (ex.: `RESERVADO → FINALIZADO`).
- Criação de diretórios idempotente com `exist_ok=True`, evitando falhas de I/O.

---

## [0.1.0] – 14/05/2025
### ✨ Adicionado
- **Camada Model**  
  - Entidades `Pessoa` e `Reserva` com `__slots__` para otimizar memória.  
  - `Enum` de domínio:  
    - `StatusReserva` (`RESERVADO`, `ATIVO`, `FINALIZADO`, `CANCELADO`).  
    - `TipoQuarto` (`STANDARD`, `DELUXE`, `PREMIUM`) com propriedade `tarifa`.
- **Camada Repository**  
  - `PessoaRepository` e `ReservaRepository` persistindo em CSV dentro de `data/db`.  
  - Funções `_proximo_id`, `_linha_valida` e parsing robusto via `csv`‑module.
- **Builder Pattern**  
  - `AbstractBuilder`: implementação genérica.  
  - `PessoaBuilder`, `ReservaBuilder` com **Interface Fluente** (`.nome().cpf().build()`).
- **Specification Pattern**  
  - Validações centralizadas (`PessoaSpecification`, `ReservaSpecification`), incluindo regras de integridade e transições de status.

### ℹ️ Notas
- Primeira versão **extraída** do script monolítico original, definindo as bases de uma arquitetura limpa (DDD).  
- Garantiu isolamento de dados e regras, possibilitando testes unitários e evolução incremental.

