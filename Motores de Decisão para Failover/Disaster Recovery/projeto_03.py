# BLOCO 01: TELEMETRIA E COLETA DE MÉTRICAS (ENTRADAS)
status = input("Qual o status do link principal (UP/DOWN): ")

ms = int(input("Qual a latência da rede principal em ms: "))

lag = int(input("Qual o lag de replicação do BD secundário (em segundos): "))

status_contingencia = input("Qual o status de contingência (READY/NOT_READY): ")


# BLOCO 02: PARÂMETROS DE SLA E LIMIARES TOLERÁVEIS (REGRAS DE NEGÓCIO)
MAX_LATENCY_MS = 200

MAX_DB_LAG_SEC = 5


# BLOCO 03: MOTOR DE DECISÃO E MATRIZ DE CHAVEAMENTO (LÓGICA CONDICIONAIS)
if status == "DOWN":
    if status_contingencia == "READY":
        print("FAILOVER AUTOMATICO")
    else:
        print("INTERVENÇÃO MANUAL")

elif status == "UP":
    if ms > MAX_LATENCY_MS or lag > MAX_DB_LAG_SEC:
        print("SISTEMA DEGRADADO")
    else:
        print("SISTEMA OPERACIONAL E SAUDÁVEL")

    
# BLOCO 04: EXECUÇÃO E APRESENTAÇÃO
print(f"Status do Link Principal: {status}")
print(f"Latência Atual: {ms} ms (Limite SLA: {MAX_LATENCY_MS})")
print(f"Lag Replicação BD: {lag} s (Limite SLA: {MAX_DB_LAG_SEC} s)")
print(f"Status Contingência: {status_contingencia}")