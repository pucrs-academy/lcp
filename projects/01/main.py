def ask_and_validate_temperature(month, months):
  """
  Solicita ao usuário a temperatura de um mês específico e valida a entrada.

  Args:
      month: Número do mês (1 a 12).
      months: Lista de nomes dos meses do ano.

  Returns:
      Temperatura válida (float) para o mês especificado.

  Raises:
      ValueError: Se o valor digitado não for um número válido.
  """
  while True:
    try:
      temperature = float(input(f'{month}º mês({months[month - 1]}): '))
      
      if -60 <= temperature <= 70:
        return temperature
      else:
        print('Valor fora do intervalo válido: -60º a 70º')
        ask_and_validate_temperature(month, months)
      
    except ValueError:
      print('Tipo de valor incorreto, digite uma temperatura válida')
    
def resolve_statistic(months, data):
  """
  Calcula e imprime estatísticas sobre as temperaturas mensais.

  Args:
      meses: Lista de nomes dos meses do ano.
      dados: Dicionário de temperaturas mensais (chave: índice do mês, valor: temperatura).

  Returns:
      None.

  Imprime:
      - Temperatura média máxima anual.
      - Número de meses quentes (temperatura >= 33°C).
      - Mês mais quente do ano (nome e temperatura).
      - Mês mais frio do ano (nome e temperatura).
  """
  average = sum(data.values()) / len(data)
  hottest_months = sum(1 for temperature in data.values() if temperature >= 33)
  hottest_month = max(data, key=data.get)
  coldest_month = min(data, key=data.get)
  
  print(f'Temperatura média máxima anual: {average:.2f}º')
  print(f'Quantidade de mêses escaldantes: {hottest_months}')
  print(f'Mês mais escaldante do ano: {months[hottest_month]} com {data[hottest_month]}º')
  print(f'Mês menos quente do ano: {months[coldest_month]} com {data[coldest_month]}º')

if __name__ == '__main__':
  """
  Programa principal que solicita as temperaturas mensais, as armazena em um dicionário e 
  calcula as estatísticas.
  """
  months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
  data = {}
  
  for month in range(1, 13):
    temperature = ask_and_validate_temperature(month, months)
    data[month - 1] = temperature
    
  resolve_statistic(months, data)