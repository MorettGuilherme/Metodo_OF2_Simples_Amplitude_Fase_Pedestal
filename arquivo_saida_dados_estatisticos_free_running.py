# Projeto ATLAS - Reconstrução de sinal - (MÉTODO).
# Autor: Guilherme Barroso Morett.
# Data: 07 de maio de 2024.

# Objetivo do código: geração de arquivos de saída baseados nos dados estatísticos dos hitogramas do erro de estimação pelo método (MÉTODO).

""" Organização do Código:

Importação de arquivos.
Leitura dos dados de ocupação: leitura_dados_ocupacao.py
Método: (ARQUIVO PY DO MÉTODO)
Histograma do erro da estimação pelo método da desconvolução: (NOME DO ARQUIVO PY DO HISTOGRAMA)

Funções presentes:

1) Função para o cálculo dos dados estatístico do erro de estimação (PARÂMETRO).
Entrada: lista com o erro de estimação (PARÂMETRO).
Saída: a média, a variância e o desvio padrão do erro de estimação (PARÂMETRO).

2) Instrução para salvar os dados estatísticos do erro de estimação (PARÂMETRO) para determinada ocupação em uma arquivo de saída.
Entrada: a média, a variância e o desvio padrão do erro de estimação (PARÂMETRO).
Saída: nada.

3) Instrução principal do código.
Entrada: nada.
Saída: nada.

"""
# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import os
from termcolor import colored

# Importação dos arquivos.
from leitura_dados_ocupacao_free_running import *
#from arquivo_metodo import * # (Importação do arquivo que contém o algoritmo do método)

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Geração de arquivos de saída baseados nos dados estatísticos dos histogramas do erro de estimação (PARÂMETRO) pelo método (MÉTODO):\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### ---------------------- 1) FUNÇÃO PARA O CÁLCULO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO (PARÂMETRO) ------------------------------------ ###

# Definição da função para o cálculo dos dados estatísticos do erro de estimação (PARÂMETRO).
def dados_estatisticos_erro_parametro(lista_erro_parametro):
    
    # A lista do erro (PARÂMETRO) é convertida para o tipo numpy array.
    vetor_erro_parametro = np.array(lista_erro_parametro)

    # Cálculo da média do erro de estimação (PARÂMETRO).
    media_erro_parametro = np.mean(vetor_erro_parametro)

    # Cálculo da variância do erro de estimação (PARÂMETRO).
    var_erro_parametro = np.var(vetor_erro_parametro)

    # Cálculo do desvio padrão do erro de estimação (PARÂMETRO).
    desvio_padrao_erro_parametro = np.std(vetor_erro_parametro)
    
    # A função retorna a média, a variância e o desvio padrão dos dados do erro de estimação (PARÂMETRO).
    return media_erro_parametro, var_erro_parametro, desvio_padrao_erro_parametro
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ----------------- 2) FUNÇÃO PARA A IMPRESSÃO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO (PARÂMETRO) EM UM ARQUIVO DE SAÍDA ---------------- ###

def arquivo_saida_dados_estatisticos_erro_parametro(numero_ocupacao, n_janelamento, media_erro_parametro, var_erro_parametro, desvio_padrao_erro_parametro):

    # Definição do título presente no arquivo de saída.
    titulo_arquivo_saida = "Oc, media_erro,var_Erro,desvio_padrao_erro\n"

    # Definição da pasta em que contém o arquivo de saída.
    pasta_saida = "Dados_Estatisticos_Metodo_OC"

    # Caso a pasta não exista.
    if not os.path.exists(pasta_saida):
        # Criação da pasta de saída.
        os.makedirs(pasta_saida)

    # Nome do arquivo de saida.
    arquivo_saida = f"dados_estatisticos_metodo_janelamento_{n_janelamento}.txt"

    # Caminho completo para o arquivo de saída.
    caminho_arquivo_saida = os.path.join(pasta_saida, arquivo_saida)

    # Verifica se o arquivo existe e está vazio
    try:
        with open(caminho_arquivo_saida, 'r') as arquivo_saida_dados_estatisticos:
            primeiro_caractere = arquivo_saida_dados_estatisticos.read(1)
            if not primeiro_caractere:
                # Arquivo está vazio, escreva o título
                with open(caminho_arquivo_saida, 'a') as file:
                    file.write(titulo_arquivo_saida)
    except FileNotFoundError:
        # Se o arquivo não existe, cria e escreve o título
        with open(caminho_arquivo_saida, 'w') as file:
            file.write(titulo_arquivo_saida)

    # Comando para tentar realizar uma operação.
    try:
        # Abre o arquivo de saída no modo de acrescentar (append).
        with open(caminho_arquivo_saida, "a") as arquivo_saida_dados_estatisticos:
            # Escrita dos dados de interesse.
            arquivo_saida_dados_estatisticos.write(f"{numero_ocupacao},{media_erro_parametro},{var_erro_parametro},{desvio_padrao_erro_parametro}\n")
        
    # Excessão.
    except Exception as e:
        # Impressão de mensagem de alerta.
        print("Ocorreu um erro ao atualizar o arquivo de saída dos dados estatísticos:", str(e))

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ---------------------------------------- 3) FUNÇÃO PRINCIPAL do código (MAIN) ------------------------------------------------------------------------ ###

# Definição da função principal (main) para esse código.
def principal_arquivo_saida_dados_estatisticos_metodo():
    
    # A variável ocupacao_inicial armazena o valor inicial da ocupação que é 0.
    ocupacao_inicial = 0
    
    # A variável ocupacao_final armazena o valor final da ocupação que é 10.
    ocupacao_final = 100
    
    # A variável incremento_ocupacao armazena o valor de incremento entre as ocupações.
    incremento_ocupacao = 10
    
    # A variável n_janelamento_inicial armazena o valor inicial do janelamento que é 7.
    n_janelamento_inicial = 7
    
    # A variável n_janelamento_final armazena o valor final do janelamento que é 19.
    n_janelamento_final = 19
    
    # A variável incremento_janelamento aramzena o valor do incremento entre os janelamentos.
    incremento_janelamento = 2
    
    # Para o número de janelamento inicial de 7 até 19 com incremento de 2.
    for n_janelamento in range(n_janelamento_inicial, n_janelamento_final+1, incremento_janelamento):
    
        for numero_ocupacao in range(ocupacao_inicial, ocupacao_final+1, incremento_ocupacao):
    
            # Chamada ordenada das funções.
    
            Matriz_Dados_OC = leitura_dados_ocupacao(numero_ocupacao)
    
            Matriz_Dados_OC_sem_pedestal = retirada_pedestal(Matriz_Dados_OC)
    
            vetor_amostras_pulsos, vetor_amplitude_referencia, _ = amostras_pulsos_e_referencia(Matriz_Dados_OC_sem_pedestal)
    
            Matriz_dados_pulsos, vetor_parametro_referencia = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento)
    
            #lista_erro_amplitude = arquivo_metodo(Matriz_dados_pulsos, vetor_parametro_referencia, n_janelamento)
            
            lista_erro_parametro = []
    
            media_erro_amplitude, var_erro_amplitude, desvio_padrao_erro_amplitude = dados_estatisticos_erro_parametro(lista_erro_parametro)
    
            arquivo_saida_dados_estatisticos_erro_parametro(numero_ocupacao, n_janelamento, media_erro_amplitude, var_erro_amplitude, desvio_padrao_erro_amplitude)
            
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

# Chamada da função principal do código.
principal_arquivo_saida_dados_estatisticos_metodo()

# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")