## **Resolução do desafio técnico da Foco**
O desafio consiste em prever os resultados para os próximos 12 meses (jan/2025 a dez/2025) com base nos dados históricos dos contratos realizados entre jan/2023 e dez/2024.

Deve-se utilizar a base histórica fictícia fornecida para projetar os seguintes indicadores por loja e por mês:
1. Diárias Locadas
2. Diária Média

**Sobre a base de dados:**\
A base fornecida contém registros simulados de contratos de locação com as seguintes colunas:

- id_contrato
- data_inicio_locacao
- duracao_locacao (dias)
- id_loja
- dias_antecedencia (entre reserva e início locação)
- diaria_media
- valor_total_locacao (diaria_media x duração_locacao)

---

**Como executar este notebook:**

 Clone o repositório do desafio. https://github.com/getrolucas/desafio-tecnico-foco.git
- Usando `uv` [Recomendado]: Se não tiver, instale `uv` para gerenciar o ambiente virtual. Disponível em: (https://docs.astral.sh/uv/getting-started/installation/). Na pasta do projeto, execute o seguinte comando no cmd: `uv sync`.
- Usando `pip`: Execute os seguintes comandos: `python -m venv` para criar um ambiente virtual. Em seguida `pip install -r requirements.txt` para instalar os pacotes.
