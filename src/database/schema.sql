-- Criação da tabela principal de armazenamento de editais e atos oficiais
CREATE TABLE IF NOT EXISTS tb_editais_radar (
    id_ato VARCHAR(50) NOT NULL,
    orgao_emissor VARCHAR(150) NOT NULL,
    tipo_publicacao VARCHAR(100) NOT NULL,
    objeto TEXT NOT NULL,
    valor_previsto_reais DECIMAL(15, 2),
    data_abertura DATE,
    prazo_limite_propostas DATE,
    resumo_executivo_ia TEXT NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Definição da Chave Primária (Garante que não haverá duplicidade de atos no sistema)
    CONSTRAINT pk_tb_editais_radar PRIMARY KEY (id_ato)
);

-- Índices para otimização de performance nas buscas do Dashboard da Maria Eduarda
CREATE INDEX IF NOT EXISTS idx_orgao_emissor ON tb_editais_radar(orgao_emissor);
CREATE INDEX IF NOT EXISTS idx_data_abertura ON tb_editais_radar(data_abertura);
