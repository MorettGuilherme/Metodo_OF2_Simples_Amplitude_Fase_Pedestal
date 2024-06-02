# Projeto ATLAS - Reconstrução de sinal - Best Linear Unbiased Estimator (BLUE 1).
# Autor: Guilherme Barroso Morett.
# Data: 01 de junho de 2024.

# Objetivo do código: Aplicação do método Best Linear Unbiased Estimator (BLUE 1).

"""
Organização do código:

Leitura dos dados de entrada de acordo com o janelamento desejado.
Os dados de entrada das ocupações no formato de arquivo texto (txt) contém informações sobre os pulsos de sinais (ADC Count), a amplitude de referência (ADC Count), a fase de referência (ns) e o ruído (ADC Count).
O valor de referência considerado para o pedestal foi de 30 ADC Count.

Funções presentes:

1) Função para a definição do vetor pulso de referência.
Entrada: número de janelamento.
Saída: vetor pulso de referência para cada instante de tempo de acordo com o janelamento.

2) Função para a definição do vetor da derivada temporal do pulso de referência.
Entrada: número de janelamento.
Saída: vetor da derivada temporal do pulso de referência para cada instante de tempo de acordo com o janelamento.

3) Função para o método BLUE 1.
Entrada: parâmetro, matriz com os pulsos de sinais, vetor com o parâmetro de referência, matriz de covariância dos dados de ruídos e o número de janelamento.
Saída: lista com o erro de estimação pelo método BLUE 1

"""

# Importação das bibliotecas.
import numpy as np

# Importação dos arquivos.
from leitura_dados_ocupacao_blue1 import *
from leitura_dados_ruidos_blue1 import *

### ------------------------------------------------- 1) FUNÇÃO PARA O PULSO DE REFERÊNCIA ----------------------------------------------------- ###

# Definição da função para o vetor pulso de referência de acordo com o janelamento.
def pulso_referencia(n_janelamento):
    
    # Criação das variáveis que armazenam os valores dos pulsos de referência para cada cada instante de tempo.
    h_tm225 = 0.0 # t = -225,0 ns
    h_tm200 = 0.0 # t = -220,0 ns
    h_tm175 = 0.0 # t = -175,0 ns
    h_tm150 = 0.0 # t = -150,0 ns
    h_tm125 = 0.0 # t = -125,0 ns
    h_tm100 = 0.0 # t = -100,0 ns
    h_tm75 = 2.304e-05 # t = -75,0 ns
    h_tm50 = 0.0172264 # t = -50,0 ns
    h_tm25 = 0.452445 # t = -25,0 ns
    h_t0 = 1.0 # t = 0,0 ns
    h_tM25 = 0.563307 # t = 25,0 ns
    h_tM50 = 0.149335 # t = 50,0 ns
    h_tM75 = 0.0423598 # t = 75,0 ns
    h_tM100 = 0.00480767 # t = 100,0 ns
    h_tM125 = 0.0 # t = 125,0 ns
    h_tM150 = 0.0 # t = 150,0 ns
    h_tM175 = 0.0 # t = 175,0 ns
    h_tM200 = 0.0 # t = 200,0 ns
    h_tM225 = 0.0 # t = 225,0 ns
       
    # Caso o janelamento seja igual a 7.
    if n_janelamento == 7:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 7 no intervalo de tempo de -75,0 a 75,0 ns.
        vetor_pulso_referencia = np.array([h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75])
        
    # Caso o janelamento seja igual a 9.
    elif n_janelamento == 9:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 9 no intervalo de tempo de -100,0 a 100,0 ns.
        vetor_pulso_referencia = np.array([h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100])
        
    # Caso o janelamento seja igual a 11.
    elif n_janelamento == 11:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 11 no intervalo de tempo de -125,0 a 125,0 ns.
        vetor_pulso_referencia = np.array([h_tm125, h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100, h_tM125])
        
    # Caso o janelamento seja igual a 13.
    elif n_janelamento == 13:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 13 no intervalo de tempo de -150,0 a 150,0 ns.
        vetor_pulso_referencia = np.array([h_tm150, h_tm125, h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100, h_tM125, h_tM150])
        
    # Caso o janelamento seja igual a 15.
    elif n_janelamento == 15:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 15 no intervalo de tempo de -175,0 a 175,0 ns.
        vetor_pulso_referencia = np.array([h_tm175, h_tm150, h_tm125, h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100, h_tM125, h_tM150, h_tM175])   

    # Caso o janelamento seja igual a 17.
    elif n_janelamento == 17:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 17 no intervalo de tempo de -200,0 a 200,0 ns.
        vetor_pulso_referencia = np.array([h_tm200, h_tm175, h_tm150, h_tm125, h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100, h_tM125, h_tM150, h_tM175, h_tM200]) 
        
    # Caso o janelamento seja igual a 19.
    elif n_janelamento == 19:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 19 no intervalo de tempo de -225,0 a 225,0 ns.
        vetor_pulso_referencia = np.array([h_tm225, h_tm200, h_tm175, h_tm150, h_tm125, h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100, h_tM125, h_tM150, h_tM175, h_tM200, h_tM225])     

    # A função retorna o vetor pulso de referência.
    return vetor_pulso_referencia

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ------------------------------------------- 2) FUNÇÃO PARA A DERIVADA DO PULSO DE REFERÊNCIA ----------------------------------------------- ###

# Definição da função para o vetor da derivada do pulso de referência de acordo com o janelamento.
def derivada_pulso_referencia(n_janelamento):
    
    # Criação das variáveis que armazenam os valores das derivadas dos pulsos de referência para cada cada instante de tempo.
    dh_tm225 = 0.0 # t = -225,0 ns
    dh_tm200 = 0.0 # t = -220,0 ns
    dh_tm175 = 0.0 # t = -175,0 ns
    dh_tm150 = 0.0 # t = -150,0 ns
    dh_tm125 = 0.0 # t = -125,0 ns
    dh_tm100 = 0.0 # t = -100,0 ns
    dh_tm75 = 5.472e-05 # t = -75,0 ns
    dh_tm50 = 0.0036703166666666675 # t = -50,0 ns
    dh_tm25 = 0.031080499999999955 # t = -25,0 ns
    dh_t0 = 1.666666668009853e-07 # t = 0,0 ns
    dh_tM25 = -0.024345499999999964 # t = 25,0 ns
    dh_tM50 = -0.008006833333333371 # t = 50,0 ns
    dh_tM75 = -0.0024333666666666635 # t = 75,0 ns
    dh_tM100 = -0.0005361350000000002 # t = 100,0 ns
    dh_tM125 = -0.00215426 # t = 125,0 ns
    dh_tM150 = 0.0 # t = 150,0 ns
    dh_tM175 = 0.0 # t = 175,0 ns
    dh_tM200 = 0.0 # t = 200,0 ns
    dh_tM225 = 0.0 # t = 225,0 ns
    
    # Caso o janelamento seja igual a 7.
    if n_janelamento == 7:
        
        # Definição do vetor da derivada do pulso de referência de acordo com o janelamento 7 no intervalo de tempo de -75,0 a 75,0 ns.
        vetor_derivada_pulso_referencia = np.array([dh_tm75, dh_tm50, dh_tm25, dh_t0, dh_tM25, dh_tM50, dh_tM75])
        
    # Caso o janelamento seja igual a 9.
    elif n_janelamento == 9:
        
        # Definição do vetor da derivada do pulso de referência de acordo com o janelamento 9 no intervalo de tempo de -100,0 a 100,0 ns.
        vetor_derivada_pulso_referencia = np.array([dh_tm100, dh_tm75, dh_tm50, dh_tm25, dh_t0, dh_tM25, dh_tM50, dh_tM75, dh_tM100])
        
    # Caso o janelamento seja igual a 11.
    elif n_janelamento == 11:
        
        # Definição do vetor da derivada do pulso de referência de acordo com o janelamento 11 no intervalo de tempo de -125,0 a 125,0 ns.
        vetor_derivada_pulso_referencia = np.array([dh_tm125, dh_tm100, dh_tm75, dh_tm50, dh_tm25, dh_t0, dh_tM25, dh_tM50, dh_tM75, dh_tM100, dh_tM125])
        
    # Caso o janelamento seja igual a 13.
    elif n_janelamento == 13:
        
        # Definição do vetor da derivada do pulso de referência de acordo com o janelamento 13 no intervalo de tempo de -150,0 a 150,0 ns.
        vetor_derivada_pulso_referencia = np.array([dh_tm150, dh_tm125, dh_tm100, dh_tm75, dh_tm50, dh_tm25, dh_t0, dh_tM25, dh_tM50, dh_tM75, dh_tM100, dh_tM125, dh_tM150])
        
    # Caso o janelamento seja igual a 15.
    elif n_janelamento == 15:
        
        # Definição do vetor da derivada do pulso de referência de acordo com o janelamento 15 no intervalo de tempo de -175,0 a 175,0 ns.
        vetor_derivada_pulso_referencia = np.array([dh_tm175, dh_tm150, dh_tm125, dh_tm100, dh_tm75, dh_tm50, dh_tm25, dh_t0, dh_tM25, dh_tM50, dh_tM75, dh_tM100, dh_tM125, dh_tM150, dh_tM175])   

    # Caso o janelamento seja igual a 17.
    elif n_janelamento == 17:
        
        # Definição do vetor da derivada do pulso de referência de acordo com o janelamento 17 no intervalo de tempo de -200,0 a 200,0 ns.
        vetor_derivada_pulso_referencia = np.array([dh_tm200, dh_tm175, dh_tm150, dh_tm125, dh_tm100, dh_tm75, dh_tm50, dh_tm25, dh_t0, dh_tM25, dh_tM50, dh_tM75, dh_tM100, dh_tM125, dh_tM150, dh_tM175, dh_tM200]) 
        
    # Caso o janelamento seja igual a 19.
    elif n_janelamento == 19:
        
        # Definição do vetor da derivada do pulso de referência de acordo com o janelamento 19 no intervalo de tempo de -225,0 a 225,0 ns.
        vetor_derivada_pulso_referencia = np.array([dh_tm225, dh_tm200, dh_tm175, dh_tm150, dh_tm125, dh_tm100, dh_tm75, dh_tm50, dh_tm25, dh_t0, dh_tM25, dh_tM50, dh_tM75, dh_tM100, dh_tM125, dh_tM150, dh_tM175, dh_tM200, dh_tM225])     

    # A função retorna o vetor pulso de referência.
    return vetor_derivada_pulso_referencia
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ###   

### ----------------------------------------------- 3) FUNÇÃO PARA O MÉTODO BLUE 1 ------------------------------------------------------------- ###

# Definição da função para o método BLUE 1.
def metodo_BLUE1(parametro, Matriz_pulsos_sinais_teste, vetor_parametro_referencia_teste, Matriz_covariancia, n_janelamento):

    # Criação da lista vazia para armazenar os erros calculados para o parâmetro. 
    lista_erro_parametro = []
    
    # A variável vetor_h recebe o retorno da função pulso_referencia.
    vetor_h = pulso_referencia(n_janelamento)
    
    # A variável vetor_dh recebe o retorno da função derivada_pulso_referencia.
    vetor_dh = derivada_pulso_referencia(n_janelamento)
    
    # A variável vetor_unitario é um vetor formato por uns com dimenção igual a quantidade de janelamento.
    vetor_unitario = np.ones(n_janelamento)
    
    # Definição da matriz cujas colunas são respectivamente formadas pelo vetor_h, vetor_dh e o vetor_unitario.
    U = np.column_stack((vetor_h, vetor_dh, vetor_unitario))
        
    # Tenta calcular a inversa da matriz Matriz_covariancia.
    try:
    # Calcula a inversa da matriz Matriz_covariancia usando numpy.linalg.inv.
        Inversa_Matriz_covariancia = np.linalg.inv(Matriz_covariancia)
          
    # Caso a matriz Matriz_Covariancia seja singular ou não invertível.  
    except np.linalg.LinAlgError:
    # Impressão de mensagem de erro
        print("A matriz matriz de covariancia não é invertível.")
        
    # Cálculo da transposta da matriz U.
    Transposta_U = np.transpose(U)
    
    # Cálculo de uma parte do vetor de pesos pelo método BLUE 1.
    parte_vetor_blue1 = np.dot(np.dot(Transposta_U, Inversa_Matriz_covariancia), U)
    
    # Tenta calcular a inversa da parte_vetor_blue1.
    try:
    # Calcula a inversa da matriz parte_vetor_blue1 usando numpy.linalg.inv.
        Inversa_parte_vetor_blue1 = np.linalg.inv(parte_vetor_blue1)
          
    # Caso a matriz parte_vetor_blue1 seja singular ou não invertível.  
    except np.linalg.LinAlgError:
    # Impressão de mensagem de erro
        print("A matriz da parte do vetor de pesos do método BLUE 1 não é invertível.")
    
    
    # Para o índice de zero até o número de linhas da matriz Matriz_pulsos_sinais_treino.
    for indice_linha in range(len(Matriz_pulsos_sinais_teste)):
        
        # O vetor vetor_pulsos_sinais corresponde a linha de índice indice_linha da matriz Matriz_pulsos_sinais_treino.    
        vetor_pulsos_sinais_teste = Matriz_pulsos_sinais_teste[indice_linha]
    
        # A amplitude de referência é o elemento de índice indice_linha do vetor vetor_amplitude_referencia_teste.
        valor_parametro_referencia_teste = vetor_parametro_referencia_teste[indice_linha]
        
        # Cálculo do vetor de pesos pelo método BLUE 1.
        vetor_pesos_blue1 = np.dot(np.dot(Inversa_parte_vetor_blue1, Transposta_U), Inversa_Matriz_covariancia)
        
        # Cálculo do parâmetro estimado pelo método BLUE 1.
        vetor_parametro_estimado = np.dot(vetor_pesos_blue1, vetor_pulsos_sinais_teste)
        
        # Caso a variável parametro seja igual a string "amplitude".
        if parametro == "amplitude":
            
            # A varável parametro_estimado recebe o primeiro elemento do vetor vetor_parametro_estimado.
            parametro_estimado = vetor_parametro_estimado[0]
        
        # Caso a variável parametro seja igual a string "fase".
        elif parametro == "fase":
            
            # A variável amplitude_estimada recebe o primeiro elemento do vetor vetor_parametro_estimado.
            amplitude_estimada = vetor_parametro_estimado[0]
            
            # A variável amolitude_fase_estimada recebe o segundo elemento do vetor vetor_parametro_estimado.
            amplitude_fase_estimada = vetor_parametro_estimado[1]
            
            # A variável parametro_estimado é calculada pela divisão entre os valores da amplitude_fase_estimada pela amplitude_estimada.
            parametro_estimado = amplitude_fase_estimada / amplitude_estimada
        
        # Caso a variável parametro seja igual a string "pedestal".
        elif parametro == "pedestal":
            
            # A variável parametro_estimado recebe o terceiro elemento do vetor vetor_parametro_estimado.
            parametro_estimado = vetor_parametro_estimado[2]
        
        # Cálculo do erro de estimação da amplitude.
        erro_parametro = valor_parametro_referencia_teste-parametro_estimado
    
        # O elemento erro_amplitude é adicionado na lista correspondente.    
        lista_erro_parametro.append(erro_parametro)

    # A função retorna a lista lista_erro_amplitude.
    return lista_erro_parametro
 
### -------------------------------------------------------------------------------------------------------------------------------------------- ###