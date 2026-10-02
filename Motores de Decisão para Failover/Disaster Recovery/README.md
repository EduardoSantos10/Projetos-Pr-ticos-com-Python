# 🛡️ Motor de Decisão para Failover e Disaster Recovery (HA/DR)

> **Simulação de Tomada de Decisão em Tempo Real para Redes e Infraestrutura de Missão Crítica**

Este projeto implementa um **Motor de Decisão Automatizado em Python** projetado para avaliar métricas de telemetria de infraestrutura (estado do link, latência de rede e lag de replicação de banco de dados) e tomar decisões instantâneas de **Failover** ou **Degradação de Serviço**, visando garantir a contínua **Alta Disponibilidade (HA)** e a estratégia de **Disaster Recovery (DR)** da aplicação.

---

## 🏛️ Contexto e Arquitetura do Sistema

Em ambientes de produção e nuvens corporativas, a falha de um nó primário exige uma resposta automatizada em questão de milissegundos para minimizar o **RTO** e conter perdas de dados alinhadas ao **RPO**.

### 📊 Conceitos Básicos Abrangidos

* **RPO (Recovery Point Objective):** Representado no projeto pelo *lag de replicação do banco de dados*. Determina a tolerância máxima de perda de transações recentes caso ocorra o failover para o nó secundário.
* **RTO (Recovery Time Objective):** Representado pelo tempo de execução do script de chaveamento automatizado, que reduz a indisponibilidade do serviço de horas (intervenção manual) para milissegundos.
* **SLA (Service Level Agreement):** Definição estrita dos limites de tolerância para latência de rede e sincronização de dados antes de declarar o serviço como degradado ou crítico.

---

## ⚙️ Regras de Negócio e Limiares de SLA

As decisões operacionais tomadas pelo motor dependem do cumprimento dos seguintes parâmetros:

| Métrica | Limiar de SLA | Ação / Condição |
| :--- | :--- | :--- |
| **Status do Link Principal** | `UP` | Operação em nó primário. |
| **Latência de Rede (`ping_ms`)** | `≤ 200 ms` | Dentro da margem de desempenho aceitável. |
| **Lag de Replicação BD** | `≤ 5 segundos` | Tolerância máxima para garantia de consistência de dados (RPO). |
| **Status da Contingência** | `READY` | Ambiente secundário/DR apto a assumir o tráfego. |

---

## 🌳 Matriz de Decisão e Lógica de Chaveamento

A árvore de decisão condicional do motor avalia as variáveis em ordem de prioridade estrita:

1. **Estado de Queda Total (`status == "DOWN"`):**
   * Se o ambiente de contingência estiver `READY` $\rightarrow$ **FAILOVER AUTOMÁTICO** (Chaveamento do Load Balancer / DNS).
   * Se a contingência estiver `NOT_READY` $\rightarrow$ **INTERVENÇÃO MANUAL DE EMERGÊNCIA** (Acionamento da equipe N3/SRE).
2. **Estado de Instabilidade / Degradação (`status == "UP"`):**
   * Se `latência > 200ms` **OU** `lag > 5s` $\rightarrow$ **SISTEMA DEGRADADO** (Disparo de alertas de telemetria).
   * Se todas as métricas cumprirem o SLA $\rightarrow$ **SISTEMA OPERACIONAL E SAUDÁVEL**.

+------------------------+
                       |  TELEMETRIA DA REDE   |
                       |  (Status, ms, Lag DB)  |
                       +-----------+------------+
                                   |
                                   v
                       +------------------------+
                       |   MOTOR DE DECISÃO     |
                       |  (Validação de SLA)    |
                       +-----------+------------+
                                   |
       +---------------------------+---------------------------+
       |                           |                           |
       v                           v                           v
[Link Principal OK]        [Queda do Link Principal]    [Métricas Fora do SLA]
+-----------------+        +-----------------------+    +--------------------+
|    SISTEMA      |        |   Failover Automático |    |  Alerta de Sistema |
|   SAUDÁVEL      |        |  ou Intervenção N3    |    |     Degradado      |
+-----------------+        +-----------------------+    +--------------------+

## 🛠️ Estrutura do Código-Fonte

O projeto adota o pilar de **Separação de Responsabilidades (Separation of Concerns)**, dividindo-se em 4 blocos fundamentais:

├── Bloco 01: Telemetria e Coleta de Métricas (Entradas do usuário/sistema)
├── Bloco 02: Configuração de Limiares de SLA (Constantes parametrizadas)
├── Bloco 03: Motor de Decisão (Matriz condicional encadeada em Python)
└── Bloco 04: Painel de Telemetria e Execução (Dashboard no terminal)
   ```bash
   git clone [https://github.com/seu-usuario/motor-decisao-failover.git](https://github.com/seu-usuario/motor-decisao-failover.git)
   cd motor-decisao-failover