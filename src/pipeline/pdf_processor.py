# Criação do arquivo: src/pipeline/pdf_processor.py
# Projeto: Radar da Democracia (ADS 2026)

import re
from datetime import datetime

def extrair_texto_bruto_pdf(caminho_arquivo):
    """
    Simula a extração de stream de texto de um arquivo PDF binário
    (Equivalente ao uso de bibliotecas como PyPDF2 ou pdfplumber).
    """
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [INFO] [PIPELINE] Abrindo stream binário do ficheiro: {caminho_arquivo}")
    
    # Simulação de um bloco de texto com ruídos textuais comuns em PDFs (múltiplos espaços, quebras de linha erradas)
    texto_sujo = """
    ESTADO DE GOIÁS   -   SECRETARIA DE ESTADO DA EDUCAÇÃO\n\n
    AVISO DE ABERTURA DE PROCESSO LICITATÓRIO     Nº 004/2026\n
    O ÓRGÃO INFORMA QUE REALIZARÁ LICITAÇÃO NA MODALIDADE PREGÃO ELETRÔNICO.\n
    VALOR ESTIMADO:    R$ 2.450.000,00.   DATA DE ABERTURA DA SESSÃO PÚBLICA:\n
    18 DE JUNHO DE 2026 ÀS 09:00 HORAS. OBJETO: AQUISIÇÃO DE TABLETS.
    """
    return texto_sujo

def limpar_texto_com_regex(texto_bruto):
    """
    Aplica técnicas de ETL (Extract, Transform, Load) e Expressões Regulares (Regex)
    para padronizar e limpar a string para o motor de IA.
    """
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [INFO] [REGEX] Iniciando sanitização de string e normalização...")
    
    # 1. Substitui quebras de linha (\n) e tabulações (\t) por espaços simples
    texto_limpo = re.sub(r'[\n\t\r]+', ' ', texto_bruto)
    
    # 2. Remove espaços em branco duplicados ou múltiplos colados
    texto_limpo = re.sub(r'\s+', ' ', texto_limpo)
    
    # 3. Remove espaços vazios no início e fim do bloco de texto
    texto_limpo = texto_limpo.strip()
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [SUCCESS] [REGEX] Filtro concluído. Redução de caracteres de ruído efetuada.")
    return texto_limpo

def executar_pipeline_transformacao(meta_dados_crawler):
    """Coordena a captura do arquivo e a transformação do dado bruto."""
    print("=" * 70)
    print("        PROCESSAMENTO E SANEAMENTO DE DADOS TEXTUAIS (PIPELINE ETL)")
    print("=" * 70)
    
    if not meta_dados_crawler:
        print("[ERROR] [PIPELINE] Nenhum metadado de arquivo válido foi fornecido.")
        return None
        
    url_ficheiro = meta_dados_crawler.get("fonte_url")
    texto_extraido = extrair_texto_bruto_pdf(url_ficheiro)
    
    print("\n--- [PRE-VIEW] Texto Bruto do PDF (Sujo): ---")
    print(texto_extraido.replace("\n", "[\\n]"))
    print("-" * 50)
    
    texto_final_sanitizado = limpar_texto_com_regex(texto_extraido)
    
    print("\n--- [PRE-VIEW] Texto Pronto para API (Sanitizado via Regex): ---")
    print(texto_final_sanitizado)
    print("=" * 70)
    
    return texto_final_sanitizado

if _name_ == "_main_":
    # Teste isolado do componente de pipeline
    mock_meta = {"fonte_url": "https://diariooficial.go.gov.br/licitacoes/download/ato_042.pdf"}
    executar_pipeline_transformacao(mock_meta)
