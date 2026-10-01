# ETAPA 01: COLETA E PADRONIZAÇÃO DE MÉTRICAS DA APLICAÇÃO
memoria_ram = float(input("Informe o consumo estimado de memória RAM em Megabytes(MB): "))

process_cpu = int(input("Informe o a quantidade de núcleos de processamento: "))

armazen = int(input("Informe a volumetria de disco em Gigabyte(GB): "))

prioridade = input("Qual é a prioridade do sistema: ").upper()

# Conversão de Hardware (MB para GB):
memoria_ram_GB = memoria_ram / 1024

# CONVERTER GB PARA MB: MULTIPLICAÇÃO *

# CONVERTER MB PARA GB: DIVISÃO /


# ETAPA 02: CÁLCULO DE OVERHEAD DO SISTEMA OPERACIONAL (KERNEL/BUFFER)
margem_RAM = memoria_ram_GB + 1.5

margem_disco = armazen * 1.20


# ETAPA 03: MATRIZ DE DECISÃO E RECOMENDAÇÃO DE INSTÂNCIA EC2
if (prioridade == "COMPUTACAO" or (process_cpu >= 4 and margem_RAM <= 8)):
    familia_ec2 = ("Família c6i (Computed Optimized)")

elif (prioridade == "MEMORIA" or margem_RAM > 16):
    familia_ec2 = ("Família r6i (Memory Optimized)")
    
else:
    familia_ec2 = ("Família t3/m6i (General Purpose)")
    

# ETAPA 04: ESTIMATIVA FINANCEIRA DE NUVEM (FinOps)
custo_hora = (process_cpu * 0.04) + margem_RAM * 0.005

custo_dia = custo_hora * 24

custo_disco = (margem_disco * 0.08) / 30


# SOMA TOTAL DO CUSTO DE OPERAÇÃO DIÁRIA
custo_total_dia = custo_dia + custo_disco


# ETAPA 05: EXIBIÇÃO FORMATADA DO RELATÓRIO
print(f" Os valores foram: Requisitado {memoria_ram_GB} GB vs. Provisionado {margem_RAM} GB")

print(f"A família de instância EC2 recomendada seria {familia_ec2}")

print(f"O custo estimativo diário, seria de US$ {custo_total_dia: .2f}")