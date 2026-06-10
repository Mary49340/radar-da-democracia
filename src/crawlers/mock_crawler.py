# Criação do arquivo: src/crawlers/mock_crawler.py
# Projeto: Radar da Democracia (ADS 2026)

import time
import random
from datetime import datetime

def simular_requisicao_portal():
    """Simula uma requisição HTTP GET para um portal de Diário Oficial."""
    portais = [
        "https://diariooficial.go.gov.br/licitacoes",
        "https://www.diariooficial.df.gov.br/saude",
        "https://www.imprensanacional.gov.br/dou"
    ]
    portal_alvo = random.choice(portais)
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [INFO] [CRAWLER] Conectando ao endpoint: {portal_alvo}...")
    time.sleep(1.5) # Simula a latência real de rede
    
    # Simulação de códigos de status HTTP comuns no backend
    status_code = random.choice([200, 200, 200, 404, 500]) 
    
    if status_code == 200:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [SUCCESS] [CRAWLER] HTTP 200: Conexão estabelecida com sucesso.")
        return True
    elif status_code == 404:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [ERROR] [CRAWLER] HTTP 404: Página do portal não encontrada.")
        return False
    else:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [CRITICAL] [CRAWLER] HTTP 500: Instabilidade no servidor governamental.")
        return False

def executar_varredura_rotina():
    """Executa a rotina de varredura mapeando elementos simulados do HTML."""
    print("=" * 70)
    print("        INICIANDO ROTINA DE RASPAGEM AUTOMATIZADA (WEB CRAWLER)")
    print("=" * 70)
    
    if not simular_requisicao_portal():
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [WARNING] [CRAWLER] Falha na conexão. Agendando nova tentativa em 60s.")
        print("=" * 70)
        return None

    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [INFO] [CRAWLER] Parseando árvore HTML (BeautifulSoup)...")
    time.sleep(1)
    
    # Simulação do metadado capturado na varredura do DOM da página
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [SUCCESS] [CRAWLER] Novo documento binário (PDF) identificado na árvore HTML!")
    
    dados_capturados = {
        "fonte_url": "https://diariooficial.go.gov.br/licitacoes/download/ato_042.pdf",
        "detectado_em": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "tamanho_bytes": 46284
    }
    
    print(f"-> URL do Arquivo: {dados_capturados['fonte_url']}")
    print(f"-> Tamanho do Stream: {dados_capturados['tamanho_bytes'] / 1024:.2f} KB")
    print("=" * 70)
    
    return dados_capturados

if _name_ == "_main_":
    # Executa o robô de testes localmente se o arquivo for chamado direto
    executar_varredura_rotina()
