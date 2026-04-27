import os
from datetime import datetime

# Dados para o relatório
nome_arquivo = "relatorio_final.txt"
data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

conteudo = f"""
====================================
RELATÓRIO DE CONFIGURAÇÃO - WSL
====================================
Usuário: Osvaldo
Data de Execução: {data_atual}
Status: Ambiente configurado com sucesso!

Ferramentas validadas:
- WSL2 (Linux)
- Python 3
- Git & GitHub
- VS Code Integration

Este arquivo foi gerado automaticamente por um script Python.
====================================
"""

# Criando e escrevendo no arquivo
with open(nome_arquivo, "w") as arquivo:
    arquivo.write(conteudo)

print(f"✅ Sucesso! O arquivo '{nome_arquivo}' foi criado na sua pasta.")
