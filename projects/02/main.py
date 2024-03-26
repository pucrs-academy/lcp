import csv

def load_data(file_name):
  """Carrega os dados do arquivo CSV e armazena em uma lista de tuplas.

  Args:
      file_name: Caminho do arquivo CSV.

  Returns:
      list: Lista de tuplas contendo os dados climáticos.
  """

  data = []

  with open(file_name, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader, None)  # Ignorando o cabeçalho

    for line in reader:
      # Convertendo os campos para os tipos de dados apropriados
      date, precip, temp_max, temp_min, horas_insol, temp_media, um_relativa, vel_vento = line
      precip = float(precip)
      temp_max = float(temp_max)
      temp_min = float(temp_min)
      horas_insol = float(horas_insol) if horas_insol else 0.0
      temp_media = float(temp_media) if temp_media else 0.0
      um_relativa = float(um_relativa) if um_relativa else 0.0
      vel_vento = float(vel_vento) if vel_vento else 0.0

      # Armazenando os dados como uma tupla
      data.append((date, precip, temp_max, temp_min, horas_insol, temp_media, um_relativa, vel_vento))

  return data

def visualize_data(date, start_date, final_date, datatype):
  """
  Função que permite a visualização dos dados em modo texto, filtrando por período e tipo de dado.

  Args:
      date: Lista de tuplas contendo os dados climáticos.
      start_date: Data inicial no formato DD/MM/AAAA.
      final_date: Data final no formato DD/MM/AAAA.
      datatype: Tipo de dado a ser visualizado:
          1 - Todos os dados
          2 - Precipitação
          3 - Temperatura (máxima e mínima)
          4 - Umidade e velocidade do vento
  """

  # Validando as datas de entrada
  dates = [date[0] for date in date]

  if start_date not in dates or final_date not in dates:
    print('Datas de entrada inválidas!')

    return

  # Convertendo as datas para índices para facilitar a iteração
  start_index = dates.index(start_date)
  final_index = dates.index(final_date)

  if datatype == 1:
    print('{:<12} {:<12} {:<12} {:<12} {:<15} {:<12} {:<15} {:<12}'.format(
      'Data', 'Precipitação', 'Temp. Máxima', 'Temp. Mínima', 'Horas Insolação', 'Temp. Média', 'Um. Relativa', 'Vel. Vento'
    ))
  elif datatype == 2:
    print('{:<12} {:<12}'.format('Data', 'Precipitação'))
  elif datatype == 3:
    print('{:<12} {:<12} {:<12}'.format('Data', 'Temp. Máxima', 'Temp. Mínima'))
  elif datatype == 4:
    print('{:<12} {:<15} {:<12}'.format('Data', 'Um. Relativa', 'Vel. Vento'))
  else:
    print('Tipo de dados inválido!')

    return

  # Imprimindo os dados dentro do intervalo especificado
  for i in range(start_index, final_index + 1):
    date, precip, temp_max, temp_min, horas_insol, temp_media, um_relativa, vel_vento = data[i]
    if datatype == 1:
      print(
        '{:<12} {:<12.2f} {:<12.2f} {:<12.2f} {:<15.2f} {:<12.2f} {:<15.2f} {:<12.2f}'.format(
          date, precip, temp_max, temp_min, horas_insol, temp_media, um_relativa, vel_vento
        )
      )
    elif datatype == 2:
      print('{:<12} {:<12.2f}'.format(date, precip))
    elif datatype == 3:
      print('{:<12} {:<12.2f} {:<12.2f}'.format(date, temp_max, temp_min))
    elif datatype == 4:
      print('{:<12} {:<15.2f} {:<12.2f}'.format(date, um_relativa, vel_vento))

if __name__ == '__main__':
  """
  Função principal que carrega os dados, exibe o menu e chama as funções de acordo com a escolha do usuário.
  """
  data = load_data('resources\\02\\Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv')

  if data:
    while True:
      start_month = int(input('Digite o mês inicial (MM): '))
      start_year = int(input('Digite o ano inicial (AAAA): '))
      final_month = int(input('Digite o mês final (MM): '))
      final_year = int(input('Digite o ano final (AAAA): '))

      if not (1 <= start_month <= 12 and 1961 <= start_year <= final_year <= 2016):
        print('Mês ou ano inicial/final inválido(s).')
        continue

      option = int(input('Digite 1 para todos os dados, 2 para precipitação, 3 para temperatura, 4 para umidade e vento: '))

      if option not in [1, 2, 3, 4]:
        print('Opção inválida. Digite um número entre 1 e 4.')
        continue

      start_date = f'01/{start_month:02d}/{start_year}'
      final_date = f'01/{final_month:02d}/{final_year}'

      print(f'Dados de Porto Alegre no período de {start_date} à {final_date}')

      visualize_data(data, start_date, final_date, option)

      break