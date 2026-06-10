import json
from datetime import datetime

def obter_instrucoes_sistema():
    """Retorna o prompt de sistema que molda o comportamento do modelo de IA."""
    prompt_sistema = (
        "Você é um extrator de dados focado em análise governamental. Seu trabalho é ler textos "
        "brutos de Diários Oficiais e extrair APENAS as variáveis solicitadas, estruturando a "
        "saída estritamente em formato JSON. Remova termos jurídicos redundantes e crie um "
        "resumo executivo direto e em português claro. Se alguma variável não for encontrada, "
        "retorne null."
    )
    return prompt_sistema

def simular_chamada_api_ia(texto_sanitizado):
    """
    Simula o envio do payload para a API de IA Generativa e valida se a
    resposta retornada segue a estrutura de chaves exigida pelo sistema.
    """
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [INFO] [AI_ENGINE] Carregando Prompt de Sistema do Felipe...")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [INFO] [AI_ENGINE] Despachando token e payload para a infraestrutura da API...")
    
    # Simulação da resposta estruturada pura que o modelo devolve quando o JSON Mode está ativo
    json_mock_retorno = """
    {
      "id_ato": "SEDUC-GO-2026-004",
      "orgao_emissor": "Secretaria de Estado da Educação - GO",
      "tipo_publicacao": "PREGÃO ELETRÔNICO",
      "objeto": "Aquisição de equipamentos de informática (notebooks e tablets) para atender as unidades escolares da rede estadual.",
      "valor_previsto_reais": 2450000.00,
      "data_abertura": "2026-06-18",
      "prazo_limite_propostas": "2026-06-17",
      "resumo_executivo_ia": "Abertura de pregão eletrônico para compra de notebooks e tablets escolares com orçamento estimado em R$ 2,45 milhões."
    }
    """
    return json_mock_retorno

def processar_extracao_inteligente(texto_limpo):
    """Gere o ciclo de vida da chamada de IA e faz o parsing gramatical do JSON."""
    print("=" * 70)
    print("        CAMADA DE INTELIGÊNCIA ARTIFICIAL E ENGENHARIA DE PROMPT")
    print("=" * 70)
    
    prompt_base = obter_instrucoes_sistema()
    resposta_bruta_api = simular_chamada_api_ia(texto_limpo)
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [INFO] [AI_ENGINE] Resposta recebida. Iniciando validação sintática do objeto...")
    
    try:
        # Tenta converter a string recebida pela IA num dicionário Python (validação de JSON)
        objeto_json_validado = json.loads(resposta_bruta_api)
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [SUCCESS] [AI_ENGINE] Objeto JSON validado com sucesso na arquitetura.")
        
        print("\n--- [RESULTADO] JSON Estruturado Pronto para o Banco SQL: ---")
        print(json.dumps(objeto_json_validado, indent=2, ensure_ascii=False))
        print("=" * 70)
        
        return objeto_json_validado
        
    except json.JSONDecodeError as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [CRITICAL] [AI_ENGINE] Falha crítica de parsing: A IA alucinou e quebrou a sintaxe do JSON.")
        print(f"Detalhes do erro: {e}")
        print("=" * 70)
        return None

if __name__ == "__main__":
    # Teste isolado do motor de IA
    texto_teste = "ESTADO DE GOIÁS - AVISO DE LICITAÇÃO Nº 004/2026. VALOR: R$ 2.450.000,00."
    processar_extracao_inteligente(texto_teste)
