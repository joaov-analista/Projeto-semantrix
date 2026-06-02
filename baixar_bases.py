"""
Script: Juntar arquivos de despesas do Portal da Transparencia

Como usar:
1. Coloque este script na mesma pasta onde estao os CSVs
2. Rode: python juntar_despesas.py
"""

import os
import glob
import pandas as pd

# CONFIGURACOES

PASTA_ARQUIVOS = "C:\\Users\\jv001\\Downloads\\Python\\.venv311\\arquivos_despesa"           
ARQUIVO_FINAL  = "gastos_consolidado.csv"

# JUNTANDO OS ARQUIVOS

def main():
    print("\n" + "=" * 55)
    print("  Consolidador de Despesas do Governo Federal")
    print("=" * 55 + "\n")

    # Busca todos os CSVs com o padrao do portal (ex: 202401_Despesas.csv)
    arquivos = sorted(glob.glob(os.path.join(PASTA_ARQUIVOS, "*_Despesas.csv")))

    # se nao encontrar nenhum arquivo
    if not arquivos:
        print("Nenhum arquivo encontrado!")
        print("Verifique se os CSVs estao na mesma pasta que este script.")
        print("Os arquivos devem ter o formato: 202401_Despesas.csv")
        return

    print(f"{len(arquivos)} arquivo(s) encontrado(s):\n")
    # juntando cada arquivo
    for a in arquivos:
        print(f"{os.path.basename(a)}")

    print("\nLendo e juntando...\n")
    # df para armazenar todos os arquivos
    dfs = []

    for arquivo in arquivos:
        nome = os.path.basename(arquivo)
        try:
            df = pd.read_csv(
                arquivo,
                sep=";",
                encoding="latin-1",
                dtype=str,
                low_memory=False
            )
            dfs.append(df)
            print(f"    OK  {nome}  ({len(df):,} linhas)")

        except Exception as e:
            print(f"    ERRO em {nome}: {e}")

    if not dfs:
        print("\n  Nenhum arquivo foi lido com sucesso.")
        return

    # Junta tudo em um unico DataFrame
    df_final = pd.concat(dfs, ignore_index=True)

    # Salva o arquivo consolidado
    df_final.to_csv(ARQUIVO_FINAL, index=False, encoding="utf-8-sig", sep=";")

    print("\n" + "=" * 55)
    print(f"  Arquivo salvo: {ARQUIVO_FINAL}")
    print(f"  Total de linhas: {len(df_final):,}")
    print(f"  Total de colunas: {len(df_final.columns)}")
    print(f"  Colunas: {list(df_final.columns)}")
    print("=" * 55)
    print("\n  Pronto! Importe o arquivo consolidado no seu dashboard.")

if __name__ == "__main__":
    main()
