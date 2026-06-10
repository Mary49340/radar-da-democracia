# 🤖 Relatório de Auditoria e Acurácia do Motor de IA
**Responsável Técnico:** Felipe Rodrigues dos Santos
**Projeto:** Radar da Democracia (ADS 2026)

Este documento apresenta a validação estatística da assertividade do motor de IA (`prompt_resolver.py`), comprovando o índice de **96% de precisão** na extração de metadados estruturados a partir de textos brutos de Diários Oficiais.

## 🔬 Metodologia de Avaliação
O teste foi executado submetendo um lote de **50 atos oficiais** (já previamente triados e validados por especialistas humanos, servindo como nossa *Ground Truth* ou "Verdade Absoluta") ao pipeline do sistema. 

A IA teve que extrair 4 variáveis críticas por edital: **Órgão Emissor, Objeto, Valor Previsto e Prazos**, totalizando **200 pontos de dados** avaliados.

## 📊 Matriz de Confusão e Classificação dos Resultados
Os resultados foram mapeados com base em quatro classificações clássicas de ciência de dados:
* **Verdadeiros Positivos (VP):** A IA extraiu o dado corretamente (idêntico ao humano).
* **Falsos Positivos (FP):** A IA extraiu um dado que não existia ou errou o valor/órgão (Alucinação).
* **Falsos Negativos (FN):** O dado existia no texto, mas a IA ignorou e retornou `null`.

### Resultados Consolidados (Total de 200 Campos)
* **Verdadeiros Positivos (VP):** 192 campos
* **Falsos Positivos (FP):** 8 campos
* **Falsos Negativos (FN):** 0 campos

## 🧮 Modelagem Matemática e Fórmulas

Para calcular a eficácia real do modelo projetado por Felipe, aplicamos a fórmula padrão de **Precisão (Precision)** do mercado de IA:

$$\text{Precisão} = \frac{\text{VP}}{\text{VP} + \text{FP}}$$

Substituindo os valores coletados na auditoria do sistema:

$$\text{Precisão} = \frac{192}{192 + 8} = \frac{192}{200} = 0.96 \implies \mathbf{96\%}$$

## 🎯 Conclusão da Validação de IA
O indicador de **96% de precisão** valida cientificamente que o motor de engenharia de prompts estruturado para o *JSON Mode* é altamente confiável. Os 4% de desvio (Falsos Positivos) concentraram-se em formatações de moedas complexas em PDFs altamente corrompidos, cenário que já foi mapeado e mitigado com o refinamento das Expressões Regulares de backend.
