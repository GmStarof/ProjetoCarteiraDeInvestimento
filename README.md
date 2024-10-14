# Projeto Carteira De Investimento

- Otimização de Sistemas
- Turma: 962 - OTIMIZAÇÃO DE SISTEMAS
- Nome: Guilherme Mateus | matrícula: 2021200570


## Objetivo

Este projeto tem como objetivo otimizar uma carteira de investimentos utilizando uma abordagem adaptada do problema da mochila. A ideia é maximizar o retorno esperado de uma carteira de ativos financeiros, respeitando um limite de risco aceitável. Para isso, utiliza-se a otimização com dados financeiros coletados via API do Yahoo Finanças.

## Descrição do Projeto

O projeto consiste em três etapas principais:

Modelagem Matemática: A formulação do problema é feita utilizando conceitos de otimização. Cada ativo financeiro possui um retorno esperado e um risco associado. O objetivo é maximizar o retorno da carteira respeitando uma capacidade máxima de risco, de forma similar ao problema da mochila.

Implementação em Python: O código foi implementado em Python utilizando bibliotecas como numpy, pandas, scipy.optimize, matplotlib e seaborn. Os dados financeiros dos ativos são coletados usando a biblioteca yfinance.

Visualização dos Resultados: A visualização é uma parte fundamental do projeto, com gráficos gerados para mostrar a fronteira eficiente, a distribuição de ativos, e a evolução do retorno da carteira ao longo do tempo.

## Estrutura do Código

- fetch_data(tickers, start_date, end_date): Função responsável por coletar os dados históricos de preços dos ativos via Yahoo Finanças. Os retornos são calculados a partir dos dados de preços ajustados.

- calculate_portfolio_metrics(weights, returns): Calcula o retorno esperado e o risco da carteira para uma dada distribuição de pesos dos ativos.

- objective_function(weights, returns, target_return): Função objetivo usada na otimização, cujo objetivo é minimizar o risco dado um retorno alvo.

- optimize_portfolio(returns, target_return): Realiza a otimização da carteira utilizando o método SLSQP (Sequential Least Squares Programming) para encontrar a melhor alocação de ativos que minimize o risco para um dado retorno alvo.

- visualize_results(weights, returns): Gera gráficos para ilustrar a fronteira eficiente, a distribuição dos ativos na carteira e a evolução do retorno da carteira ao longo do tempo.

# Visualização dos Resultados

- Fronteira Eficiente: Gráfico que mostra a relação entre risco (desvio padrão) e retorno esperado. Vários pontos são gerados para ilustrar a fronteira eficiente da carteira.

- Distribuição de Ativos: Gráfico de pizza que mostra a distribuição percentual dos ativos na carteira otimizada.

- Evolução do Retorno: Gráfico de linha que mostra o retorno acumulado da carteira ao longo do tempo.

## Como Executar o Projeto

> Pré-requisitos:

1. Python 3.6 ou superior

2. Instalar as dependências utilizando o seguinte comando:

  ```bash
pip install numpy pandas yfinance scipy matplotlib seaborn
  ```
3. Executando o Código:

- Edite a lista de tickers no código para incluir os ativos de interesse.

- Defina o intervalo de datas (start_date e end_date) conforme necessário.

4. Execute o script principal:

- python main.py

Saída:

Gráficos mostrando a fronteira eficiente, a distribuição dos ativos e a evolução do retorno da carteira serão exibidos.
![image](https://github.com/user-attachments/assets/59f08ce7-0e05-405e-95a9-514c471bdcc8)
![image](https://github.com/user-attachments/assets/1e6cd728-cad7-4089-bbed-a2f6860331e8)
![image](https://github.com/user-attachments/assets/412d11d1-6fc1-4fdf-83ad-4d1dade1d760)

## Estrutura do Repositório

- main.py: Arquivo principal contendo a implementação do projeto.

- README.md: Documentação do projeto (este arquivo).

## Considerações Finais

Este projeto visa fornecer uma visão prática de como otimizar uma carteira de investimentos utilizando dados reais de ativos financeiros e técnicas de otimização numérica. A fronteira eficiente ajuda a entender o trade-off entre risco e retorno, possibilitando a escolha de uma carteira que melhor atenda ao perfil de risco do investidor.

Caso tenha dúvidas ou sugestões, sinta-se à vontade para abrir uma issue no repositório. Feliz otimização!
