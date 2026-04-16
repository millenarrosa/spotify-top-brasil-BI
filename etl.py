import pandas as pd

def executar_etl(caminho_arquivo):
    # 1. EXTRAÇÃO (Extract)
    print("Iniciando extração dos dados...")
    df = pd.read_csv(caminho_arquivo)
    
    # 2. TRANSFORMAÇÃO (Transform)
    print("Transformando os dados...")
    
    # A. Limpeza de strings (remover espaços extras)
    df['musica'] = df['musica'].str.strip()
    df['artista'] = df['artista'].str.strip()
    
    # B. Tratamento da Data de Coleta
    # Como a data está em português ("terça-feira, 17 de fevereiro..."), 
    # Aqui, vamos extrair apenas a parte da data (DD de MM de AAAA)
    def limpar_data(texto):
        try:
            # Remove o dia da semana e limpa espaços
            data_limpa = texto.split(',')[1].strip()
            return data_limpa
        except:
            return texto

    df['data_simplificada'] = df['data_coleta'].apply(limpar_data)
    
    # C. Criação de Novas Métricas (Enriquecimento)
    # KPI: Média de plays por dia que a música está na lista
    df['plays_por_dia'] = (df['total_plays'] / df['dias_na_lista']).round(2)
    
    # D. Tipagem de Dados
    df['total_plays'] = df['total_plays'].astype(int)
    df['dias_na_lista'] = df['dias_na_lista'].astype(int)

    # 3. CARREGAMENTO (Load)
    # Salvando o arquivo pronto para o BI (Power BI, Tableau, etc)
    nome_saida = "spotify_top50_ready.csv"
    df.to_csv(nome_saida, index=False, encoding='utf-8-sig')
    
    print(f"ETL concluído com sucesso! Arquivo gerado: {nome_saida}")
    return df

# Executar o processo
df_final = executar_etl('dados.csv')
print(df_final.head())