# ☁️ Cloud Sizing & Instance Matcher CLI (AWS EC2 & FinOps)

Uma ferramenta em linha de comando (CLI) desenvolvida em Python para dimensionamento automatizado de infraestrutura em nuvem (AWS EC2) e estimativa de custos operacionais (FinOps), considerando overhead de sistema operacional, prioridade de workload e regras de dimensionamento de hardware.

---

## 📌 Visão Geral do Projeto

O objetivo do projeto é simular o processo de arquitetura de nuvem ao receber requisitos de uma aplicação (RAM, vCPUs, Armazenamento e Perfil de Carga) e automatizar:
1. **Dimensionamento com Overhead de Kernel:** Inclusão de margens de segurança para RAM (evitando *OOM-Killer*) e armazenamento (prevenindo exaustão de *inodes* e logs).
2. **Recomendação de Família EC2:** Seleção inteligente da família de instâncias AWS (`c6i`, `r6i` ou `t3/m6i`).
3. **Análise Financeira (FinOps):** Cálculo do custo estimado de operação diária (computação + armazenamento EBS).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Conceitos de TI Aplicados:**
  - **Hardware & Arquitetura:** Aritmética de memória (binário vs. decimal, paginação).
  - **Sistemas Operacionais:** Gerenciamento de processos, mitigação de OOM-Killer, taxas de E/S de disco (`ext4`/`xfs`).
  - **Cloud Computing & Virtualização:** AWS EC2 (Hypervisor Nitro, famílias Computação/Memória/General Purpose).
  - **FinOps:** Modelagem de custos em nuvem (OpEx, modelo *pay-as-you-go*).

---

## ⚙️ Funcionalidades e Regras de Negócio

- **Entrada de Dados:** Coleta interativa de parâmetros da aplicação via CLI.
- **Cálculo de Overhead de Sistema:**
  - $\text{RAM Provisionada} = \text{RAM Requisitada (GB)} + 1.5\text{ GB}$ (reserva para Kernel e daemons do SO).
  - $\text{Disco Provisionado} = \text{Disco Requisitado} \times 1.20$ (margem de 20% para logs e metadados).
- **Matriz de Decisão de Instância:**
  - `c6i (Compute Optimized)`: Prioridade `COMPUTACAO` ou ($\ge 4\text{ vCPUs}$ e $\le 8\text{ GB RAM}$).
  - `r6i (Memory Optimized)`: Prioridade `MEMORIA` ou $\text{RAM} > 16\text{ GB}$.
  - `t3/m6i (General Purpose)`: Casos gerais e cargas de trabalho equilibradas.
- **Estimativa de Custos:**
  - Cálculo de custo por hora/dia para vCPUs e RAM.
  - Projeção diária do volume de disco EBS.

---

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo `.py`.
3. No terminal, execute o script:

```bash
python3 main.py