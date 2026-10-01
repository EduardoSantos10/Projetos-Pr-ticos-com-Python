# BLOCO 01: COLETA DE DADOS (ENTRADAS)
endereco_comp = input("Informe seu IP ou Hostname: ")

portas = input("Informe a lista de portas abertas: ")

regras = input("A regra de Firewall permite acesso global (S/N): ").upper()

cabecalhos = input("A aplicação web possui os cabeçalhos HSTS e CSP (S/N): ").upper()


# BLOCO 02: ESTRUTURA DE REGRAS DE NEGÓCIO E PONTUAÇÃO
score_risco = 0

vulnerab_detectadas = []

recomend_acao = []

portas_sem_cripto = {
    21: "FTP - Transferência de Arquivos em Texto Claro",
    23: "Telnet - Acesso Remoto Inseguro",
    80: "HTTP - Tráfego Web Sem SSL/TLS"
}

portas_adm = {
    22: "SSH - Acesso Remoto via Terminal",
    3389: "RDP - Área de Trabalho Remota (Windows Server)",
    3306: "MySQL - Banco de Dados Relacional",
    5432: "PostgreSQL - Banco de Dados Relacional"
}


# BLOCO 03: PROCESSAMENTO E ESTRUTURAS CONDICIONAIS
if "80" in portas:
    score_risco = score_risco + 30
    vulnerab_detectadas.append(portas_sem_cripto[80])
    recomend_acao.append("HTTP - Tráfego Web Sem SSL/TLS(443).")
    
if "21" in portas:
    score_risco = score_risco + 30
    vulnerab_detectadas.append(portas_sem_cripto[21])
    recomend_acao.append("Migrar o tráfego FTP para SFTP")
    
if "23" in portas:
    score_risco = score_risco + 30
    vulnerab_detectadas.append(portas_sem_cripto[23])
    recomend_acao.append("Migrar o tráfego Telnet para SSH")
    
# CHECAGEM DE EXPOSIÇÃO ADMINISTRATIVA (SSH NA PORTA 22):
if ("22" in portas) and (regras == "S"):
    score_risco = score_risco + 25
    vulnerab_detectadas.append("SSH (Porta 22) exposto para a Internet pública (0.0.0.0/0).")
    recomend_acao.append("Restringir o acesso à porta 22 apenas para IPs da VPN/Bastion.")
        
# CHECAGEM DE HARDENING WEB (CONDICIONAL ANINHADA CORRIGIDA)
if ("80" in portas) or ("443" in portas):
    if cabecalhos == "N":
        score_risco = score_risco + 20
        vulnerab_detectadas.append("Ausência de cabeçalhos de segurança web (HSTS/CSP).")
        recomend_acao.append("Configurar Strict-Transport-Security e Content-Security-Policy na aplicação.")
        

# BLOCO 04: CLASSIFICAÇÃO E RELATÓRIO
if score_risco <= 20:
    nivel_risco = "BAIXO (VERDE)"
    
elif score_risco <= 50:
    nivel_risco = "MÉDIO (AMARELO)"
    
else:
    nivel_risco = "CRÍTICO (VERMELHO)"
    
print(f"Pontuação Total de Risco: {score_risco} pontos")
print(f"Nível Geral de Risco:    {nivel_risco}")

print("VULNERABILIDADES DETECTADAS:")
if vulnerab_detectadas:
    print(vulnerab_detectadas)
else:
    print("Nenhuma vulnerabilidade detectada nas regras auditadas.")

print("PLANO DE AÇÃO E RECOMENDAÇÕES DE MITIGAÇÃO:")
if recomend_acao:
    print(recomend_acao)
else:
    print("Nenhuma ação de mitigação necessária no momento.")