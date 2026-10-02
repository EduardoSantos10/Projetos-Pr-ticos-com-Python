# ==============================================================================
# BLOCO 01: BASE CENTRALIZADA DE CREDENCIAIS E TELEMETRIA
# ==============================================================================
usuarios = {
    "admin": {
        "senha": "1234",
        "perfil": "ADMINISTRADOR",
        "tentativas": 0,
        "bloqueado": False
    },
    "suporte": {
        "senha": "abcd",
        "perfil": "ANALISTA_N2",
        "tentativas": 0,
        "bloqueado": False
    },
    "auditor": {
        "senha": "xyz",
        "perfil": "AUDITOR",
        "tentativas": 0,
        "bloqueado": False
    }
}

# ==============================================================================
# BLOCO 02: PARÂMETROS DE POLÍTICA DE SEGURANÇA E LIMIARES (SLA / SecOps)
# ==============================================================================
MAX_TENTATIVAS_FALHAS = 3

username = input("Informe o seu nome de usuário: ")
password = input("Informe a sua senha: ")

# Variável de estado para passar o perfil validado ao Bloco 04
perfil_autenticado = None

# ==============================================================================
# BLOCO 03: MOTOR DE AUTENTICAÇÃO E TRIAGEM
# ==============================================================================
if username not in usuarios:
    # Mensagem genérica para evitar User Enumeration
    print("Acesso Negado: Credenciais inválidas.")

else:
    conta = usuarios[username]

    # 1. Verifica se a conta já está bloqueada
    if conta["bloqueado"] or conta["tentativas"] >= MAX_TENTATIVAS_FALHAS:
        conta["bloqueado"] = True
        print("Acesso Negado: Conta Bloqueada por Segurança.")

    # 2. Verifica se a senha está incorreta
    elif password != conta["senha"]:
        conta["tentativas"] += 1
        print(f"Senha Incorreta! Tentativas falhas: {conta['tentativas']}/{MAX_TENTATIVAS_FALHAS}")

        # Avalia se a conta deve ser bloqueada imediatamente
        if conta["tentativas"] >= MAX_TENTATIVAS_FALHAS:
            conta["bloqueado"] = True
            print("Alerta SecOps: Limite de tentativas excedido! Conta bloqueada.")

    # 3. Autenticação bem-sucedida
    else:
        conta["tentativas"] = 0  # Reseta o contador de erros
        perfil_autenticado = conta["perfil"]
        print(f"\n[+] Autenticado com sucesso! Usuário: {username}")

# ==============================================================================
# BLOCO 04: AMBIENTES DE EXECUÇÃO E PAINÉIS DE ACESSO (RBAC)
# ==============================================================================
if perfil_autenticado == "ADMINISTRADOR":
    print("\n--- PAINEL CONTROL CENTER (ROOT / ADMIN) ---")
    print("1. Status dos Servidores e Containers")
    print("2. Gerenciar Regras de Firewall e IAM")
    print("3. Desbloquear Contas de Usuários")
    print("[+] Acesso Total Concedido.")

elif perfil_autenticado == "ANALISTA_N2":
    print("\n--- PAINEL OPERACIONAL (SUPORTE N2) ---")
    print("1. Visualizar Fila de Chamados Críticos")
    print("2. Consultar Logs de Erro da Aplicação")
    print("3. Reiniciar Serviços de Aplicação")
    print("[+] Permissões de Suporte Ativas.")

elif perfil_autenticado == "AUDITOR":
    print("\n--- PAINEL DE CONFORMIDADE E AUDITORIA (GRC) ---")
    print("1. Exportar Logs de Autenticação (Read-Only)")
    print("2. Relatório de Conformidade LGPD/ISO 27001")
    print("[+] Acesso Restrito em Modo Leitura.")