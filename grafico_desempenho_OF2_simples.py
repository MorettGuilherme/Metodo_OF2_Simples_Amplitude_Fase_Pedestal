# EXPERIMENTO ATLAS - Reconstrução de sinal - Método do Filtro Ótimo Simples (Optimal Filtering - OF2 Simples).
# Autor: Guilherme Barroso Morett.
# Data: 02 de setembro de 2024.

# Objetivo do código: gráfico do desempenho (EME, MSE, MAE, SNR E DP) ao longo das ocupações de acordo com o janelamento ideal para o método OF2 simples para a estimação da amplitude, fase ou pedestal.

""" 
Organização do Código:

Leitura dos dados estatísticos de todas as ocupações para um determinado janelamento.

Funções presentes:

1) Função para a leitura dos dados do desempenho do método OF2 simples de todas as ocupações para o janelamento ideal.
Entrada: parâmetro estimado, número do janelamento ideal, opção de avaliação do desempenho.
Saída: matriz com os dados de entrada organizados de acordo com a coluna (número da ocupação, média, variância e desvio padrão do desempenho do método OF2 simples).

2) Instrução para o plote do gráfico do desempenho do método OF2 simples ao longo das ocupações para o janelamento ideal.
Entrada: matriz dos dados de desempenho do método OF2 simples.
Saída: nada.

3) Instrução principal do código.
Entrada: nada.
Saída: nada.
"""

# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
import os
from termcolor import colored

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Plote do gráfico do desempenho (EME, MSE, MAE, SNR ou DP) ao longo das ocupações de acordo com o janelamento ideal para o método Optimal Filtering (OF2 Simples):\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### ------------------------- 1) FUNÇÃO PARA A LEITURA DOS DADOS ESTATÍSTICOS DO DESEMPENHO DO MÉTODO OF2 SIMPLES ------------------------------ ###

# Definição da função para a leitura dos dados estatísticos do desempenho do método OF2 simples.
def leitura_dados_estatisticos_desempenho_OF2_simples(parametro, n_janelamento_ideal, opcao_avaliacao_desempenho):

    # Nome da pasta em que se encontra o arquivo de entrada dos dados estatísticos do desempenho de acordo com o janelamento ideal.
    pasta_dados_estatisticos_desempenho = f"K_Fold_{parametro}_{opcao_avaliacao_desempenho}_Desempenho_OF2_Simples_OC"

    # Nome do arquivo de entrada dos dados estatísticos do desempenho de acordo com o janelamento ideal.
    arquivo_dados_estatisticos_desempenho = f"k_fold_{parametro}_{opcao_avaliacao_desempenho}_desempenho_OF2_simples_J_{n_janelamento_ideal}.txt"

    # O caminho para esse arquivo de entrada.
    caminho_arquivo_dados_estatisticos_desempenho = os.path.join(pasta_dados_estatisticos_desempenho, arquivo_dados_estatisticos_desempenho)

    # Caso o caminho especificado exista.
    if os.path.exists(caminho_arquivo_dados_estatisticos_desempenho):
    
        # Abre o aquivo de entrada no modo leitura.
        with open(caminho_arquivo_dados_estatisticos_desempenho, "r") as arquivo_entrada_dados_estatisticos_desempenho:
        
            # Armazena os dados na variável Matriz_Dados_Desempenho.
            Matriz_Dados_Desempenho = np.array(np.loadtxt(arquivo_entrada_dados_estatisticos_desempenho, skiprows = 1, dtype = 'double', delimiter = ','))
 
    # Caso contrário.       
    else:
    
        # Impressão de mensagem que o arquivo de entrada não existe.
        print(f"O arquivo {arquivo_dados_estatisticos_desempenho} não existe na pasta {pasta_dados_estatisticos_desempenho}.")

    # Obs.: da forma que o programa está escrito, os arquivos de entrada devem estar na mesma pasta em que está o código do programa.
    # Caso deseja-se alterar isso basta mudar o endereço do arquivo.
    
    # A função retorna a matriz Matriz_Dados_Desempenho.
    return Matriz_Dados_Desempenho

### ---------------------------------------------------------------------------------------------------------------------------------------------- ###

### --- 2) INSTRUÇÃO PARA O PLOTE DO GRÁFICO DO DADO ESTATÍSTICO DO DESEMPENHO AO LONGO DAS OCUPAÇÕES PARA O JANELAMENTO IDEAL PELO MÉTODO OF2 SIMPLES -- ###

# Definição da instrução para o plote do gráfico do dado estatístico do desempenho ao longo das ocupações para o janelamento ideal pelo método OF2 simples.
def grafico_dado_estatistico_desempenho_OF2_simples(parametro, opcao_avaliacao_desempenho, Matriz_Dados_Desempenho):
    
    # Definição da variável indice_coluna_ocupacoes que armazena o valor do índice da coluna das ocupações.
    indice_coluna_ocupacoes = 0
    
    # Definição da variável indice_coluna_media que armazena o valor do índice da coluna das médias.
    indice_coluna_media = 1
    
    # Definição da variável indice_coluna_var que armazena o valor do índice da coluna das variâncias.
    indice_coluna_var = 2
    
    # Definição da variável indice_coluna_DP que armazena o valor do índice da coluna dos desvios padrão.
    indice_coluna_DP = 3
    
    # Definição do eixo das abscissas.
    vetor_ocupacoes = Matriz_Dados_Desempenho[: , indice_coluna_ocupacoes]
    
    # Definição do eixo das ordenadas.
    vetor_dados = Matriz_Dados_Desempenho[:, indice_coluna_media]
    
    # Definição da lista com os valores das barras de erro.
    vetor_barras_erro = Matriz_Dados_Desempenho[:, indice_coluna_DP]
    
    # Comando para o nome do eixo das abscissas.
    plt.xlabel("Ocupação (OC.)", fontsize = 18)
    plt.xticks(fontsize = 16)
    
    # Caso a variável opcao_avaliacao_desempenho seja 1.
    if opcao_avaliacao_desempenho == 1:
              
        # Comando para o nome do eixo das ordenadas de acordo com o erro médio de estimação.
        plt.ylabel("Média do erro médio de estimação (ADC Count)", fontsize = 18)
        
        # Caso a variável parametro seja a igual a "fase_amplitude_estimada" ou "fase_amplitude_referencia".
        if parametro == "fase_amplitude_estimada" or parametro == "fase_amplitude_referencia":
           
           # Comando para o nome do eixo das ordenadas de acordo com o erro médio de estimação para a fase.
           plt.ylabel("Média do erro médio de estimação (ns)", fontsize = 18) 
            
    # Caso a variável opcao_avaliacao_desempenho seja 2.
    if opcao_avaliacao_desempenho == 2:
              
        # Comando para o nome do eixo das ordenadas de acordo com o erro médio quadrático.
        plt.ylabel(r"Média do erro médio quadrático (ADC Count)$^2$", fontsize = 18)
        
        # Caso a variável parametro seja a igual a "fase_amplitude_estimada" ou "fase_amplitude_referencia".
        if parametro == "fase_amplitude_estimada" or parametro == "fase_amplitude_referencia":
           
           # Comando para o nome do eixo das ordenadas de acordo com o erro médio quadrático para a fase.
           plt.ylabel(r"Média do erro médio quadrático (ns)$^2$", fontsize = 18) 
              
    # Caso a variável opcao_avaliacao_desempenho seja 3.
    elif opcao_avaliacao_desempenho == 3:
            
        # Comando para o nome do eixo das ordenadas de acordo com o erro médio absoluto.
        plt.ylabel("Média do erro médio absoluto (ADC Count)", fontsize = 18)
        
        # Caso a variável parametro seja a igual a "fase_amplitude_estimada" ou "fase_amplitude_referencia".
        if parametro == "fase_amplitude_estimada" or parametro == "fase_amplitude_referencia":
           
           # Comando para o nome do eixo das ordenadas de acordo com o erro médio absoluto para a fase.
           plt.ylabel("Média do erro médio absoluto (ns)", fontsize = 18) 
        
    # Caso a variável opcao_avaliacao_desempenho seja 4.
    elif opcao_avaliacao_desempenho == 4:
        
        # Comando para o nome do eixo das ordenadas de acordo com a relação Sinal-Ruído (Signal-to-Noise Ratio - SNR).
        plt.ylabel("Média da relação Sinal-Ruído", fontsize = 18)
        
    # Caso a variável opcao_avaliacao_desempenho seja 5.
    elif opcao_avaliacao_desempenho == 5:
        
        # Comando para o nome do eixo das ordenadas de acordo com a média do desvio padrão.
        plt.ylabel("Média do desvio padrão (ADC Count)", fontsize = 18)
        
        # Caso a variável parametro seja a igual a "fase_amplitude_estimada" ou "fase_amplitude_referencia".
        if parametro == "fase_amplitude_estimada" or parametro == "fase_amplitude_referencia":
           
           # Comando para o nome do eixo das ordenadas de acordo com a média do desvio padrão para a fase.
           plt.ylabel("Média do desvio padrão (ns)", fontsize = 18)
        
    # Comando que define o tamanho dos números do eixo das ordenadas.
    plt.yticks(fontsize = 16)
    
    # Comando para o plote do gráfico.
    plt.errorbar(vetor_ocupacoes, vetor_dados, vetor_barras_erro, color = 'blue', linestyle = '--', marker = 'o')
    
    # Comando para o grid.
    plt.grid()
    
    # Comando para o plote.
    plt.show()
        
### -------------------------------------------------------------------------------------------------------------------------------------------- ###        
        
### ---------------------------------------------------- 3) INSTRUÇÃO PRINCIPAL DO CÓDIGO ------------------------------------------------------ ###

# Definição da instrução principal (main) do código.
def principal_grafico_dado_estatistico_desempenho_OF2_simples():
    
    # Impressão de mensagem no terminal.
    print("Opções de parâmetros:\nAmplitude: 1\nFase pela amplitude estimada: 2\nFase pela amplitude de referência: 3\nPedestal: 4\n")
    
    # A variável parametro armazena o número do tipo inteiro digitado pelo usuário via terminal.
    parametro = int(input("Digite o número do parâmetro desejado: "))
    
    # A variável lista_valores_parametros armazena os valroes válidos para parametro.
    lista_valores_parametro = list(range(1,5,1))
    
    # Caso o valor digitado armazenado na variável parametro não estiver presente na lista lista_valores_parametro.
    if parametro not in lista_valores_parametro:
    
        # Exibição de uma mensagem de alerta de que a opção solicitada é inválida.
        print("Essa opção é inválida!")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
    
    # Impressão de mensagem no terminal.
    print("Opções de avaliações de desempenho do método:\nErro Médio Estimação (EME) - 1\nErro Médio Quadrático (Mean Squared Error - MSE) - 2\nErro Médio Absoluto (Mean Absolute Erro - MAE) - 3\nRelação Sinal-Ruído (Signal-to-Noise Ratio - SNR) - 4\nDesvio Padrão (DP) - 5")

    # A variável opcao_avaliacao_desempenho armazena o número do tipo inteiro digitado pelo usuário via terminal.
    opcao_avaliacao_desempenho = int(input("Digite o número da opção desejada: "))

    # A variável valores_avaliacoes_desempenho é uma lista com os valores aceitáveis para opcao_avaliacao_desempenho.
    valores_avaliacoes_desempenho = list(range(1,6,1))
    
    # Caso o valor digitado armazenado na variável opcao_avaliacao_desempenho não estiver presente na lista valores_avaliacoes_desempenho.
    if opcao_avaliacao_desempenho not in valores_avaliacoes_desempenho:
    
        # Exibição de uma mensagem de alerta de que a opção solicitada é inválida.
        print("Essa opção é inválida!")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
    
    # Caso a variável opcao_avaliacao_desempenho seja igual a 1.
    if opcao_avaliacao_desempenho == 1:
            
        # A variável mecanismo_desempenho recebe a string "EME".
        mecanismo_desempenho = "EME"
    
    # Caso a variável opcao_avaliacao_desempenho seja igual a 2.
    if opcao_avaliacao_desempenho == 2:
            
        # A variável mecanismo_desempenho recebe a string "MSE".
        mecanismo_desempenho = "MSE"
            
    # Caso a variável opcao_avaliacao_desempenho seja igual a 3.
    elif opcao_avaliacao_desempenho == 3:
          
        # A variável mecanismo_desempenho recebe a string "MAE".  
        mecanismo_desempenho = "MAE"    
            
    # Caso a variável opcao_avaliacao_desempenho seja igual a 4.
    elif opcao_avaliacao_desempenho == 4:
           
        # A variável mecanismo_desempenho recebe a string "SNR".
        mecanismo_desempenho = "SNR"  
        
    # Caso a variável opcao_avaliacao_desempenho seja igual a 5.
    elif opcao_avaliacao_desempenho == 5:
           
        # A variável mecanismo_desempenho recebe a string "DP".
        mecanismo_desempenho = "DP"
          
    # Caso a variável parametro seja igual a 1.
    if parametro == 1:
        
        # A variável parametro recebe a string "amplitude".
        parametro = "amplitude"
        
    # Caso a variável parametro seja igual a 2.
    elif parametro == 2:
    
        # A variável parametro recebe a string "fase_amplitude_estimada".
        parametro = "fase_amplitude_estimada"
        
    # Caso a variável parametro seja igual a 3.
    elif parametro == 3:
        
        # A variável parametro recebe a string "fase_amplitude_referencia".
        parametro = "fase_amplitude_referencia"
        
    # Caso a variável parametro seja igual a 4.
    elif parametro == 4:
        
        # A variável parametro recebe a string "pedestal".
        parametro = "pedestal"
    
    # A variável n_janelamento_ideal recebe o valor do janelamento ideal do método OF2 simples.
    # Obs.: essa análise deve ser realizada previamento pela interpretação dos gráficos gerados pelo K-Fold (grafico_k_fold_OF2_simples).
    n_janelamento_ideal = int(input("Digite o número do janelamento ideal para o parâmetro estimado desejado: "))
        
    # Chamada ordenada das funções.
    
    Matriz_Dados_Desempenho = leitura_dados_estatisticos_desempenho_OF2_simples(parametro, n_janelamento_ideal, mecanismo_desempenho)
    grafico_dado_estatistico_desempenho_OF2_simples(parametro, opcao_avaliacao_desempenho, Matriz_Dados_Desempenho)

### -------------------------------------------------------------------------------------------------------------------------------------------- ###
    
# Chamada da instrução principal do código.
principal_grafico_dado_estatistico_desempenho_OF2_simples()

# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")
    
    
            
    
    
    
    