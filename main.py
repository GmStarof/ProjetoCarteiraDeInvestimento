import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import seaborn as sns
import time

# Coleta de Dados
def fetch_data(tickers, start_date, end_date):
    all_data = []
    valid_tickers = []
    for ticker in tickers:
        try:
            data = yf.download(ticker, start=start_date, end=end_date)['Adj Close']
            if not data.empty:
                all_data.append(data)
                valid_tickers.append(ticker)
        except Exception as e:
            print(f"Erro ao baixar dados do ativo {ticker}: {e}. Pulando este ativo...")
            continue
        time.sleep(1)  # Intervalo entre as requisições
    if not all_data:
        raise ValueError("Nenhum dado foi baixado. Verifique os tickers ou a conexão com a internet.")
    data = pd.concat(all_data, axis=1)
    data.columns = valid_tickers
    data = data.dropna(how='any')  # Remove linhas com valores NaN
    returns = data.pct_change(fill_method=None).dropna()
    return returns

# Função para calcular o retorno esperado e risco
def calculate_portfolio_metrics(weights, returns):
    expected_return = np.dot(weights, returns.mean())
    risk = np.sqrt(np.dot(weights.T, np.dot(returns.cov(), weights)))
    return expected_return, risk

# Função objetivo para otimização (minimização do risco para um dado retorno)
def objective_function(weights, returns, target_return):
    _, risk = calculate_portfolio_metrics(weights, returns)
    return risk

# Restrições da otimização
def constraint(weights):
    return np.sum(weights) - 1

# Otimização da carteira
def optimize_portfolio(returns, target_return):
    n = returns.shape[1]
    initial_weights = np.ones(n) / n
    bounds = tuple((0, 1) for _ in range(n))
    constraints = ({
        'type': 'eq',
        'fun': constraint
    })

    result = minimize(objective_function, initial_weights, args=(returns, target_return), method='SLSQP', bounds=bounds, constraints=constraints)
    return result.x

# Visualização dos resultados
def visualize_results(weights, returns):
    # Fronteira eficiente
    risks = []
    returns_list = []
    for target_return in np.linspace(returns.mean().min(), returns.mean().max(), 100):
        optimal_weights = optimize_portfolio(returns, target_return)
        expected_return, risk = calculate_portfolio_metrics(optimal_weights, returns)
        risks.append(risk)
        returns_list.append(expected_return)
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=risks, y=returns_list, marker='o')
    plt.title("Fronteira Eficiente")
    plt.xlabel("Risco (Desvio Padrão)")
    plt.ylabel("Retorno Esperado")
    plt.grid(True)
    plt.show()

    # Distribuição de Ativos
    plt.figure(figsize=(10, 6))
    plt.pie(weights, labels=returns.columns, autopct='%1.1f%%', startangle=140)
    plt.title("Distribuição de Ativos")
    plt.show()

    # Evolução do Retorno e Risco
    cumulative_returns = (returns + 1).cumprod()
    cumulative_returns.plot(figsize=(10, 6))
    plt.title("Evolução do Retorno da Carteira")
    plt.xlabel("Data")
    plt.ylabel("Retorno Acumulado")
    plt.grid(True)
    plt.show()

# Principal
if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'META', 'TSLA', 'NVDA', 'JPM', 'V', 'JNJ',
               'PG', 'DIS', 'MA', 'NFLX', 'ADBE', 'PYPL', 'PFE', 'KO', 'MRK', 'PEP']
    start_date = '2020-01-01'
    end_date = '2024-01-01'
    target_return = 0.02  # Retorno alvo desejado

    try:
        returns = fetch_data(tickers, start_date, end_date)
        optimal_weights = optimize_portfolio(returns, target_return)
        visualize_results(optimal_weights, returns)
    except ValueError as e:
        print(e)
