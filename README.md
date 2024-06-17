A segunda versão do método linear Filtro Ótimo (Optimal Filtering - OF2) tem a finalidade de estimar os parâmetros da amplitude, fase e pedestal por meio da resolução de uma equação matricial (Ax = b) que advém do processo de otimização dos multiplicadores de Lagrange.
A matriz dos coeficientes contém em seu interior, a matriz de covariância dos dados de ruídos além dos pulsos de referência e suas derivadas. O vetor de respostas é composto em maioria por zeros,no entanto o único elemento um presente varia de posição de acordo com o parâmetro desejado. O vetor de incógnitas contém os pesos obtidos pelo método OF2 e também os multiplicadores de Lagrange que não são empregados no processo.
Obs.: os resultados demotram que o último janelamento adotado é o idela para a mplitude visto que o valor do desvio padrão não se estabilizou a partir de uma certa quantidade. Por outro lado, novamente a fase não apresentou um comportamento que possa ser padronizado. Em decorrência disso, o termo da amplitude versus a fase também será estimado.

A seguir são listadas as pastas e também os arquivos contidos nesse repositório, assim como suas respectivas funções:

1. Dados_Estatisticos_OF2_amplitude_OC
  * Essa pasta contém arquivos para cada um dos janelamento com os valores das ocupações e médias, variâncias e desvios padrão associados para o erro de estimação da amplitude.

3. Dados_Estatisticos_OF2_fase_OC
  * Essa pasta contém arquivos para cada um dos janelamento com os valores das ocupações e médias, variâncias e desvios padrão associados para o erro de estimação da fase.
  
4. Dados_Estatisticos_OF2_pedestal_OC
  * Essa pasta contém arquivos para cada um dos janelamento com os valores das ocupações e médias, variâncias e desvios padrão associados para o erro de estimação do pedestal.
  
5. Dados_Ocupacoes_Free_Running
  * Essa pasta contém arquivos com os dados para cada uma das ocupações referentes ao pulso de sinal, amplitude de referência, fase de referência e ruído computados a cada 25 ns (perído das colisões no LHC).
  
6. K_Fold_amplitude_DP_Dados_Estatisticos_OF2_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

7. K_Fold_amplitude_media_Dados_Estatisticos_OF2_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

8. K_Fold_amplitude_variancia_Dados_Estatisticos_OF2_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das variâncias dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

9. K_Fold_fase_DP_Dados_Estatisticos_OF2_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação da fase calculados pela técnica de validação cruzada K-Fold.

10. K_Fold_fase_media_Dados_Estatisticos_OF2_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação da fase calculados pela técnica de validação cruzada K-Fold.
  
11. K_Fold_fase_variancia_Dados_Estatisticos_OF2_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação da fase calculados pela técnica de validação cruzada K-Fold.

11. K_Fold_pedestal_DP_Dados_Estatisticos_OF2_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação do pedestal calculados pela técnica de validação cruzada K-Fold.

12.  K_Fold_pedestal_media_Dados_Estatisticos_OF2_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação do pedestal calculados pela técnica de validação cruzada K-Fold.

13. K_Fold_pedestal_variancia_Dados_Estatisticos_OF2_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação do pedestal calculados pela técnica de validação cruzada K-Fold.

14. Resultados_OF2_Amplitude
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação da amplitude pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações.

15. Resultados_OF2_Fase
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação da fase pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações.
   
16. Resultados_OF2_Pedestal
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação do pedestal pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações.
   
17. arquivo arquivo_saida_dados_estatisticos_OF2.py
   * Função para o cálculo dos dados estatísticos do erro de estimação pelo método linear do Filtro Ótimo (OF2).
   * Instrução para salvar os dados estatísticos do erro de estimação da amplitude, fase ou pedestal para determinada ocupação em um arquivo de saída.
   * Instrução principal do código.
   
18. arquivo grafico_dado_estatistico_janelamento_OF2.py
   * Função para a leitura dos dados estatísticos de todas as ocupações para um determinado janelamento.
   * Instrução para o plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento.
   * Instrução principal do código.

19. arquivo grafico_k_fold_OF2.py
   * Função para a leitura dos dados estatísticos da validação cruzada K-Fold.
   * Instrução para a construção do gráfico tipo A da validação cruzada K-Fold.
   * Instrução para a construção do gráfico tipo B da validação cruzada K-Fold.
   * Instrução principal (main) do código.
   
20. arquivo histograma_erro_parametro_OF2.py
   * Função para o cálculo da estatística do erro de estimação da amplitude, fase ou pedestal.
   * Função para o plote do histograma do erro de estimação da amplitude, fase ou pedestal.
   * Função principal.
   
21. arquivo k_fold_OF2.py
   * Instrução para salvar em arquivos os dados estatísticos pela validação cruzada k-Fold.
   * Instrução da validação cruzada K-Fold.
   * Instrução principal do código.
   
22. arquivo leitura_dados_ocupacao_OF2.py
   * Função para a leitura dos dados de ocupação.
   * Função para a retirada do pedestal dos pulsos de sinais.
   * Função para a construção da matriz dos pulsos de sinais e o vetor do parâmetro de referência.
   * Função para separação em dados de treino e teste.

23. arquivo leitura_dados_ruidos_OF2.py
   * Função para a leitura dos dados de ruídos de acordo com a ocupação.
   * Função para a organização dos dados de ruídos de acordo com o janelamento.
   * Função para separação em dados de treino e teste.
   * Função para a construção da matriz de covariância.
   * Função para a construção da matriz de covariância como identidade.

24. arquivo metodo_OF2.py
   * Função para a definição do vetor pulso de referência.
   * Função para a definição do vetor da derivada temporal do pulso de referência.
   * Função para a construção da matriz de coeficientes do método OF2.
   * Vetor de resposta do método OF2.
   * Função para o método OF2.
   
IMPORTANTE: os dados das ocupações foram simulados computacionalmente. As características das distribuições são:

* Distribuição amplitude: exponencial com média 100 ADC Count.
* Distribuição Fase: uniforme com números inteiros no intervalo de -5 a 5 ns.
* Pedestal: 30 ADC Count.
* Nível de deformação: 0,01 ADC Count.
* Número de eventos: 2000000.
* Fold: 100.
