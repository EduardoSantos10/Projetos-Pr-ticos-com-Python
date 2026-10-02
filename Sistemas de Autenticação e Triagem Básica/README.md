 🛡️ Projeto 04: Motor de Autenticação, Autorização e Triagem de Acesso (IAM / RBAC / SecOps)

> **Implementação em Python de um motor de gestão de identidades, controle de acesso baseado em funções (RBAC), mitigações contra força bruta e segregação de privilégios.**


📌 Visão GeralO Projeto 04 consiste na construção de um Motor de IAM (Identity and Access Management) e RBAC (Role-Based Access Control). O objetivo principal é demonstrar a transição de um script condicional simples para uma arquitetura de software defensiva e modular, aplicando conceitos práticos de segurança da informação e governança de TI.

O sistema simula a autenticação de usuários contra uma base centralizada, gerencia o estado de bloqueio individual por conta (lockout policy), evita falhas de enumeração de usuários (User Enumeration) e direciona a navegação para ambientes de execução específicos com base no perfil do usuário (Role-Based Access Control).

🏗️ Arquitetura do Sistema (Estrutura em 4 Blocos)A solução foi desenvolvida seguindo o padrão modular em 4 blocos funcionais:
                            Plaintext
  ┌────────────────────────────────────────────────────────┐
  │ [BLOCO 01] Base Centralizada de Credenciais (AD/LDAP)  │
  └───────────────────────────┬────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │ [BLOCO 02] Políticas de Segurança e Parâmetros (SLA)   │
  └───────────────────────────┬────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │ [BLOCO 03] Motor de Autenticação e Triagem (AuthN)     │
  └───────────────────────────┬────────────────────────────┘
                              │
                              ▼
  ┌────────────────────────────────────────────────────────┐
  │[BLOCO 04] Painéis de Execução e Permissões (AuthZ/RBAC)│
  └───────────────────────────┴────────────────────────────┘



🧱 Detalhamento dos Blocos1. 

Bloco 01 — Base Centralizada de Credenciais e TelemetriaConceito: Representa o repositório centralizado de identidades da organização (análogo a um Active Directory, LDAP ou banco de dados de contas).

Implementação: Utilização de dicionários aninhados em Python. Cada conta possui como chave o username e armazena um sub-dicionário contendo:senha: Credencial de acesso.perfil: Nível de acesso atrelado (ADMINISTRADOR, ANALISTA_N2, AUDITOR).

tentativas: Contador individual de falhas consecutivas de autenticação.bloqueado: Flag booleana (True/False) que define o estado da conta.2.

Bloco 02 — Políticas de Segurança e Limiares (SecOps)Conceito: Centraliza os parâmetros globais de SLA, regras e limites operacionais de segurança da informação.Implementação: Definição da constante MAX_TENTATIVAS_FALHAS = 3, determinando a tolerância do sistema antes do acionamento da política de lockout automatizada.

Bloco 03 — Motor de Autenticação e Triagem (AuthN)Conceito: Pipeline de decisão e verificação de identidade (Authentication), responsável por validar entradas e gerenciar estados.

Fluxo Operacional de Decisão:Validação de Existência: Checa se o nome de usuário consta na base.

Mitigação SecOps: Retorna uma mensagem genérica de erro ("Credenciais inválidas") caso o usuário não exista, prevenindo a vulnerabilidade de User Enumeration.

Verificação de Estado (Lockout): Checa o atributo bloqueado. Se True, recusa a execução imediatamente sem avaliar a senha.Validação de Credencial: Compara a senha digitada com a armazenada na base.

Falha: Incrementa o contador individual (tentativas += 1). Se tentativas >= MAX_TENTATIVAS_FALHAS, altera o estado para bloqueado = True.

Sucesso: Zera o contador (tentativas = 0) e encaminha a requisição autorizada para o Bloco 04.4. Bloco 04 — Ambientes de Execução e Permissões (AuthZ / RBAC)Conceito: Aplicação do Princípio do Menor Privilégio (Least Privilege) e da Segregação de Funções (SoD - Segregation of Duties).

Perfis de Acesso Configurados:👑 ADMINISTRADOR: Acesso completo à infraestrutura, alteração de regras de firewall e gerenciamento de contas.🛠️ ANALISTA_N2: Acesso operacional a filas de chamados, visualização de logs de aplicação e reinício de serviços.

🔍 AUDITOR: Acesso restrito em modo leitura (Read-Only) para extração de relatórios de conformidade e auditoria de logs.


🔄 Fluxograma do Pipeline do Motor (Bloco 03)Plaintext                     

                    [ENTRADA DE CREDENCIAIS]
                                │
                 ¿ Usuário existe na base ?
                                │
             ┌──────────────────┴──────────────────┐
          [ NÃO ]                               [ SIM ]
             │                                     │
      Erro Genérico                        ¿ Conta Bloqueada ?
  ("Credenciais Inválidas")                        │
                                        ┌──────────┴──────────┐
                                     [ SIM ]               [ NÃO ]
                                        │                     │
                                Mensagem de Erro      ¿ Senha Correta ?
                               ("Conta Bloqueada")            │
                                                   ┌──────────┴──────────┐
                                                [ NÃO ]               [ SIM ]
                                                   │                     │
                                         Incrementa Tentativas    Reseta Tentativas (0)
                                            ¿ Alcançou Max ?             │
                                           (Se SIM -> Bloqueia)  Redireciona para o
                                                                 Painel do Perfil (RBAC)


🛠️ Tecnologias e Conceitos AplicadosCategoriaConceitos AplicadosLinguagemPython 3.xEstruturas de DadosDicionários Aninhados, Manipulação de Estado em MemóriaIdentity & Access (IAM)Autenticação (AuthN), Autorização (AuthZ), RBAC, Política de LockoutCibersegurança (SecOps)Prevenção contra User Enumeration, Mitigação de Brute Force, Princípio do Menor PrivilégioEngenharia de SoftwareArquitetura Modular em 4 Blocos, Segregação de Responsabilidades (SoD)