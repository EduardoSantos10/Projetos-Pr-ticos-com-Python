# 🛡️ Scanner e Audit de Risco de Infraestrutura em Python

Unidade de Auditoria de Segurança de Infraestrutura desenvolvida como parte da formação prática em **Tecnologia da Informação**, cobrindo fundamentos de **Lógica de Programação**, **Redes de Computadores** e **Cibersegurança (DevSecOps)**.

O objetivo do projeto é avaliar a postura de segurança de um ativo de rede (servidor/hostname), correlacionando portas abertas, regras de firewall e proteções da camada de aplicação web para calcular um índice de risco qualificado.

---

## 🎯 Funcionalidades e Regras de Negócio

O motor de avaliação analisa o ativo através de 4 blocos estruturados:

1. **Telemetria de Entrada:** Coleta dados do ativo, portas TCP abertas, política do Firewall de borda e presença de cabeçalhos de proteção web.
2. **Auditoria de Criptografia (Camada 7):** Identifica o uso de protocolos em texto claro (HTTP/80, FTP/21, Telnet/23) e penaliza a falta de cifragem de dados em trânsito.
3. **Auditoria de Exposição Administrativa (Camadas 3/4 + Firewall):** Identifica se portas de gestão remota (SSH/22) estão expostas para a Internet pública (`0.0.0.0/0`) via Firewall permissivo.
4. **Hardening Web:** Verifica a presença de cabeçalhos HTTP de segurança (`Strict-Transport-Security` e `Content-Security-Policy`) em servidores com serviços web ativos.
5. **Relatório Executivo e Classificação de Risco:** Traduz a pontuação quantitativa em uma matriz de risco qualitativa baseada nos princípios do **CVSS** e da **ISO/IEC 27001**:
   - **0 a 20 pontos:** Risco Baixo (Verde)
   - **21 a 50 pontos:** Risco Médio (Amarelo)
   - **Acima de 50 pontos:** Risco Crítico / Alto (Vermelho)

---

## 🛠️ Tecnologias e Conceitos Aplicados

* **Linguagem:** Python 3.x
* **Lógica de Programação:** Estruturas condicionais (`if / elif / else`), operadores lógicos (`and`, `or`, `in`), manipuladores de strings, listas e dicionários.
* **Redes de Computadores:** Mapeamento de portas TCP/IP (21, 22, 23, 80, 443), protocolos de aplicação e regras de filtragem de pacotes em Firewalls.
* **Cibersegurança:** Análise de vulnerabilidades, matriz de riscos, princípios da Tríade CID (Confidencialidade, Integridade e Disponibilidade) e Hardening de sistemas.

---

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado em sua máquina.