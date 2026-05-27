import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Set highly professional publication styles
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['figure.titlesize'] = 14
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['axes.labelsize'] = 11.5
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11
plt.rcParams['legend.fontsize'] = 11

out_dir = r"c:\Users\Renato\Documents\Synergia - GP\assets"
if not os.path.exists(out_dir): 
    os.makedirs(out_dir)

def save_dashboard_chart(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, f"{name}.png"), bbox_inches='tight', dpi=180)
    plt.close(fig)

# ==============================================================================
# --- GRUPO 2: TRANSPORTE PÚBLICO E MOBILIDADE ---
# ==============================================================================
g2_primary = '#2563eb' # Blue
g2_accent = '#1d4ed8'
g2_light = '#3b82f6'

# 1. Evolução da Frota Operacional (Bar chart)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
anos = ['2020', '2021', '2022', '2023', '2024']
frota = [250, 280, 310, 350, 385]
bars = ax.bar(anos, frota, color='#2563eb', edgecolor='white', width=0.6)
ax.set_ylabel('Número de Veículos Operacionais', weight='bold', size=11, color="#0f172a")
ax.set_title('1. Evolução da Frota Operacional do Transporte Coletivo\nFonte: Relatório de Gestão Semob / MTU Cuiabá 2025', weight='bold', pad=15, color="#0f172a")
ax.set_ylim(0, 450)
ax.set_xticks(range(len(anos)))
ax.set_xticklabels(anos, size=11, color="#0f172a", weight="bold")
ax.bar_label(bars, padding=3, weight='bold', size=11, color='#1e3a8a')
save_dashboard_chart(fig, 'g2_c1')

# 2. Índice de Reclamações (SAC) (Line chart)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai']
reclamacoes = [450, 420, 580, 510, 490]
ax.plot(meses, reclamacoes, marker='o', color='#ef4444', linewidth=4, markersize=10, markerfacecolor='#ef4444', markeredgecolor='white', markeredgewidth=2)
ax.fill_between(meses, reclamacoes, color='#ef4444', alpha=0.12)
ax.set_ylabel('Chamados Registrados no SAC', weight='bold', size=11, color="#0f172a")
ax.set_title('2. Índice Mensal de Reclamações de Usuários (SAC)\nFonte: Ouvidoria Municipal e Agência Reguladora (ARSEC)', weight='bold', pad=15, color="#0f172a")
ax.set_ylim(0, 700)
ax.set_xticks(range(len(meses)))
ax.set_xticklabels(meses, weight='bold', size=11, color='#0f172a')
for i, val in enumerate(reclamacoes):
    ax.text(i, val + 20, str(val), ha='center', weight='bold', color='#991b1b', size=11)
save_dashboard_chart(fig, 'g2_c2')

# 3. Pavimentação Periférica (Donut chart)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
sizes = [35, 65]
labels = ['Pavimentadas (35%)', 'Não Pavimentadas / Solo Natural (65%)']
colors = ['#2563eb', '#cbd5e1']
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=90, 
                                  colors=colors, textprops=dict(color="#0f172a", weight="bold", size=11),
                                  wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2.5))
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_size(12)
    autotext.set_weight('bold')
ax.set_title('3. Estado das Vias nos Eixos Periféricos de Ônibus\nFonte: Plano Diretor de Pavimentação e Infraestrutura Urbana', weight='bold', pad=15, color="#0f172a")
save_dashboard_chart(fig, 'g2_c3')

# 4. Cumprimento de Horário (Bar Chart)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
categorias = ['Linhas Tronco (Eixo Principal)', 'Linhas Alimentadoras (Bairros)']
pontualidade = [82, 45]
bars = ax.bar(categorias, pontualidade, color=['#2563eb', '#60a5fa'], edgecolor='white', width=0.55)
ax.set_ylabel('Índice de Pontualidade (%)', weight='bold', size=11, color="#0f172a")
ax.set_title('4. Cumprimento de Horários por Categoria de Linha\nFonte: Auditoria Operacional por GPS (Semob Cuiabá 2025)', weight='bold', pad=15, color="#0f172a")
ax.set_ylim(0, 100)
ax.set_xticks(range(len(categorias)))
ax.set_xticklabels(categorias, size=11, color="#0f172a", weight="bold")
ax.bar_label(bars, padding=3, weight='bold', size=11, color='#1e3a8a', fmt='%d%%')
save_dashboard_chart(fig, 'g2_c4')

# 5. Custo por KM (Stacked Bar)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
anos_custo = ['2022', '2023', '2024']
combustivel = [2.1, 2.3, 2.4]
manutencao = [1.1, 1.2, 1.4]
b1 = ax.bar(anos_custo, combustivel, label='Combustível e Lubrificantes', color='#1e293b', width=0.5)
b2 = ax.bar(anos_custo, manutencao, bottom=combustivel, label='Manutenção, Peças e Pessoal', color='#3b82f6', width=0.5)
ax.set_ylabel('Custo Operacional Total por KM (R$)', weight='bold', size=11, color="#0f172a")
ax.set_title('5. Evolução dos Custos de Operação por Quilômetro\nFonte: Planilha de Custos Regulatórios homologada pela ARSEC', weight='bold', pad=15, color="#0f172a")
ax.set_ylim(0, 5.0)
ax.set_xticks(range(len(anos_custo)))
ax.set_xticklabels(anos_custo, size=11, color="#0f172a", weight="bold")
ax.legend(frameon=True, facecolor='white', edgecolor='none')
# Labels on stack
for i in range(len(anos_custo)):
    total = combustivel[i] + manutencao[i]
    ax.text(i, total + 0.1, f"R$ {total:.2f}", ha='center', weight='bold', color='#0f172a', size=11)
save_dashboard_chart(fig, 'g2_c5')


# ==============================================================================
# --- GRUPO 4: INVISIBILIDADE DE DADOS E GEORREFERENCIAMENTO ---
# ==============================================================================
g4_primary = '#f59e0b' # Amber/Orange
g4_accent = '#d97706'
g4_light = '#fbbf24'

# 1. Gap Cadastro (Bar chart)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
bases = ['Oficial (Prefeitura)', 'Realidade de Campo (Censo IBGE)']
registros = [185, 231]
bars = ax.bar(bases, registros, color=['#94a3b8', '#f59e0b'], edgecolor='white', width=0.55)
ax.set_ylabel('Imóveis Cadastrados (Milhares)', weight='bold', size=11, color="#0f172a")
ax.set_title('1. Divergência entre Cadastro Municipal e Censo IBGE\nFonte: Censo Demográfico IBGE 2022 vs Cadastro IPTU Municipal', weight='bold', pad=15, color="#0f172a")
ax.set_ylim(0, 300)
ax.set_xticks(range(len(bases)))
ax.set_xticklabels(bases, size=11, color="#0f172a", weight="bold")
ax.bar_label(bars, padding=3, weight='bold', size=11, color='#7c2d12')
save_dashboard_chart(fig, 'g4_c1')

# 2. Inadimplência IPTU por Regional (Bar chart)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
regionais = ['Norte', 'Sul', 'Leste', 'Oeste']
inadimplencia = [15, 42, 18, 35]
bars = ax.bar(regionais, inadimplencia, color=['#fde68a', '#f59e0b', '#d97706', '#b45309'], edgecolor='white', width=0.6)
ax.set_ylabel('Inadimplência de IPTU (%)', weight='bold', size=11, color="#0f172a")
ax.set_title('2. Taxa de Inadimplência por Região Geográfica\nFonte: Relatório Fiscal da Secretaria de Fazenda de Cuiabá', weight='bold', pad=15, color="#0f172a")
ax.set_ylim(0, 60)
ax.set_xticks(range(len(regionais)))
ax.set_xticklabels(regionais, size=11, color="#0f172a", weight="bold")
ax.bar_label(bars, padding=3, weight='bold', size=11, color='#7c2d12', fmt='%d%%')
save_dashboard_chart(fig, 'g4_c2')

# 3. Solicitações LAI (Line chart)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
anos_lai = ['2021', '2022', '2023', '2024']
pedidos = [120, 250, 480, 890]
ax.plot(anos_lai, pedidos, marker='s', color='#f59e0b', linewidth=4, markersize=10, markerfacecolor='#f59e0b', markeredgecolor='white', markeredgewidth=2)
ax.fill_between(anos_lai, pedidos, color='#f59e0b', alpha=0.12)
ax.set_ylabel('Quantidade de Chamados via LAI', weight='bold', size=11, color="#0f172a")
ax.set_title('3. Histórico de Pedidos de Acesso à Informação (LAI)\nFonte: Controladoria Geral do Município / Ouvidoria LAI', weight='bold', pad=15, color="#0f172a")
ax.set_ylim(0, 1100)
ax.set_xticks(range(len(anos_lai)))
ax.set_xticklabels(anos_lai, weight='bold', size=11, color='#0f172a')
for i, val in enumerate(pedidos):
    ax.text(i, val + 35, str(val), ha='center', weight='bold', color='#7c2d12', size=11)
save_dashboard_chart(fig, 'g4_c3')

# 4. Dados Digitais (Donut chart)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
sizes_dados = [20, 80]
labels_dados = ['Digitalizado / SIG Ativo (20%)', 'Formato Físico / Papel / Desatualizado (80%)']
colors_dados = ['#f59e0b', '#e2e8f0']
wedges, texts, autotexts = ax.pie(sizes_dados, labels=labels_dados, autopct='%1.0f%%', startangle=140, 
                                  colors=colors_dados, textprops=dict(color="#0f172a", weight="bold", size=11),
                                  wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2.5))
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_size(12)
    autotext.set_weight('bold')
ax.set_title('4. Nível de Digitalização e Integração do Acervo Fundiário\nFonte: Diagnóstico Interno de TIC da Prefeitura Municipal', weight='bold', pad=15, color="#0f172a")
save_dashboard_chart(fig, 'g4_c4')

# 5. Tempo de Resposta Cidadão (Bar Chart)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
departamentos = ['Saúde e Assistência', 'Fazenda e IPTU', 'Habitação e Urbanismo']
dias = [10, 18, 45]
bars = ax.bar(departamentos, dias, color=['#fbbf24', '#f59e0b', '#b45309'], edgecolor='white', width=0.55)
ax.set_ylabel('Tempo Médio de Resposta (Dias Úteis)', weight='bold', size=11, color="#0f172a")
ax.set_title('5. Tempo Médio de Resposta aos Pedidos dos Cidadãos\nFonte: Ouvidoria Municipal e Relatórios CGU de Transparência', weight='bold', pad=15, color="#0f172a")
ax.set_ylim(0, 60)
ax.set_xticks(range(len(departamentos)))
ax.set_xticklabels(departamentos, size=11, color="#0f172a", weight="bold")
ax.bar_label(bars, padding=3, weight='bold', size=11, color='#7c2d12', fmt='%d dias')
save_dashboard_chart(fig, 'g4_c5')


# ==============================================================================
# --- GRUPO 6: SANEAMENTO E JUSTIÇA AMBIENTAL ---
# ==============================================================================
g6_primary = '#10b981' # Emerald/Green
g6_accent = '#059669'
g6_light = '#34d399'

# 1. Coleta Esgoto (Bar chart)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
anos_esg = ['2017 (Início Concessão)', '2024 (Diagnóstico Recente)']
coleta = [35, 82]
bars = ax.bar(anos_esg, coleta, color=['#cbd5e1', '#10b981'], edgecolor='white', width=0.5)
ax.set_ylabel('Cobertura de Coleta de Esgoto (%)', weight='bold', size=11, color="#0f172a")
ax.set_title('1. Evolução da Cobertura de Coleta de Esgoto Sanitário\nFonte: Painel de Indicadores de Saneamento do SNIS / ARSEC', weight='bold', pad=15, color="#0f172a")
ax.set_ylim(0, 100)
ax.set_xticks(range(len(anos_esg)))
ax.set_xticklabels(anos_esg, size=11, color="#0f172a", weight="bold")
ax.bar_label(bars, padding=3, weight='bold', size=11, color='#047857', fmt='%d%%')
save_dashboard_chart(fig, 'g6_c1')

# 2. Qualidade Água (Line chart)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
meses_agua = ['Jan', 'Mar', 'Mai', 'Jul', 'Set']
potabilidade = [99.1, 99.4, 98.9, 99.8, 99.9]
ax.plot(meses_agua, potabilidade, marker='o', color='#10b981', linewidth=4, markersize=10, markerfacecolor='#10b981', markeredgecolor='white', markeredgewidth=2)
ax.set_ylabel('Amostras em Conformidade (%)', weight='bold', size=11, color="#0f172a")
ax.set_title('2. Índice de Potabilidade e Conformidade Física da Água\nFonte: Laudos Laboratoriais Mensais Auditados pela ARSEC', weight='bold', pad=15, color="#0f172a")
ax.set_ylim(95, 100.5)
ax.set_xticks(range(len(meses_agua)))
ax.set_xticklabels(meses_agua, weight='bold', size=11, color='#065f46')
for i, val in enumerate(potabilidade):
    ax.text(i, val + 0.1, f"{val:.1f}%", ha='center', weight='bold', color='#065f46', size=11)
save_dashboard_chart(fig, 'g6_c2')

# 3. Investimento PPP (Bar chart)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
fontes_invest = ['Parceiro Privado (PPP)', 'Setor Público (Orçamento Direto)']
valores_invest = [1200, 150]
bars = ax.bar(fontes_invest, valores_invest, color=['#059669', '#1e293b'], edgecolor='white', width=0.5)
ax.set_ylabel('Investimento Acumulado (Milhões de R$)', weight='bold', size=11, color="#0f172a")
ax.set_title('3. Investimentos no Sistema de Água e Esgoto (2017-2024)\nFonte: Relatório de Investimentos da Concessionária e ARSEC', weight='bold', pad=15, color="#0f172a")
ax.set_ylim(0, 1500)
ax.set_xticks(range(len(fontes_invest)))
ax.set_xticklabels(fontes_invest, size=11, color="#0f172a", weight="bold")
ax.bar_label(bars, padding=3, weight='bold', size=11, color='#111827', fmt='R$ %dM')
save_dashboard_chart(fig, 'g6_c3')

# 4. Perdas Rede (Donut chart)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
sizes_perdas = [35, 65]
labels_perdas = ['Água Perdida / Vazamentos / Fraude (35%)', 'Água Faturada e Consumida (65%)']
colors_perdas = ['#ef4444', '#10b981']
wedges, texts, autotexts = ax.pie(sizes_perdas, labels=labels_perdas, autopct='%1.0f%%', startangle=140, 
                                  colors=colors_perdas, textprops=dict(color="#0f172a", weight="bold", size=11),
                                  wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2.5))
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_size(12)
    autotext.set_weight('bold')
ax.set_title('4. Índice de Perdas Físicas e Comerciais na Rede\nFonte: Sistema Nacional de Informações sobre Saneamento (SNIS)', weight='bold', pad=15, color="#0f172a")
save_dashboard_chart(fig, 'g6_c4')

# 5. Internações x Saneamento (Regression/Scatter plot)
fig, ax = plt.subplots(figsize=(7.5, 5.2))
x_cobertura = np.array([40, 50, 60, 70, 80])
y_internacoes = np.array([500, 450, 380, 310, 250])
sns.regplot(x=x_cobertura, y=y_internacoes, color='#10b981', ax=ax,
            scatter_kws={"s": 150, "alpha": 0.85, "edgecolors": "white", "linewidths": 2},
            line_kws={"linewidth": 3, "color": "#059669"})
ax.set_xlabel('Cobertura de Rede de Esgoto no Bairro (%)', weight='bold', size=11, color="#0f172a")
ax.set_ylabel('Internações SUS por Doenças Hídricas', weight='bold', size=11, color="#0f172a")
ax.set_title('5. Impacto do Saneamento nas Internações de Saúde (SUS)\nFonte: DATASUS / Secretaria Municipal de Saúde de Cuiabá', weight='bold', pad=15, color="#0f172a")
ax.set_xlim(35, 85)
ax.set_ylim(200, 600)
ax.set_xticks(x_cobertura)
ax.set_xticklabels([f"{val}%" for val in x_cobertura], size=11, color="#0f172a", weight="bold")
# Add exact coordinates labels
for i in range(len(x_cobertura)):
    ax.text(x_cobertura[i], y_internacoes[i] + 15, f"{y_internacoes[i]} ob.", ha='center', weight='bold', color='#065f46', size=10)
save_dashboard_chart(fig, 'g6_c5')

print("All GP dashboards generated successfully with publication style!")
