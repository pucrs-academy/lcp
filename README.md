Uma grande parte dos problemas da área de Computação envolve a obtenção, transformação e análise de dados. O volume de dados muitas vezes é elevado, exigindo um cuidado adicional no seu tratamento e manipulação. A linguagem de programação se torna, então, uma ferramenta essencial para a execução desse tipo de tarefa.

Dessa forma, o projeto da disciplina consiste no desenvolvimento de soluções computacionais capazes de tratar entradas de dados de usuários e vindas de arquivos, bem como realizar análises estatísticas e geração de gráficos para visualização.

O projeto é individual e está organizado em duas fases. Em ambas as fases, você trabalhará com dados meteorológicos. Na primeira fase, você desenvolverá um programa que realiza análises a partir de dados informados pelo usuário. Já na segunda fase, sua implementação receberá como entrada dados vindos de um arquivo.

<h2 align="center"><a href="./projects/01/main.py">Fase 1</a></h2>

```
Implemente um programa que leia, valide e analise dados informados pelo usuário. Os dados são meteorológicos e referem-se aos dados de 2021 (de janeiro a dezembro) registrados em uma cidade. 

 

Toda entrada de dados deve ser validada. No caso de valor inválido, informe ao usuário o erro e permita que ele redigite o dado.

 

Seu programa deve coletar os seguintes dados:


• Mês: use valor numérico de 1 a 12 (janeiro a dezembro) para se referir aos meses do ano.   

Para cada mês do ano, informe:  
• Temperatura máxima do mês: devem estar em Celsius, garanta que estejam dentro de um intervalo válido para temperaturas, tal como: -60 graus à +50 graus.   

A seguir, seu programa deve calcular e exibir:  
• Temperatura média máxima anual: exibe a média das temperaturas máximas informadas.
• Quantidade de meses escaldantes: quantidade de meses com temperaturas máximas acima de 33 graus Celsius.
• Mês mais escaldante do ano: mês que registrou a maior temperatura máxima dentre todos os informados. O mês deve ser escrito na tela por extenso (janeiro a dezembro). 
• Mês menos quente do ano: mês que registrou a menor temperatura máxima dentre todos os informados. O mês deve ser escrito na tela por extenso (janeiro a dezembro).  
```

<h2 align="center"><a href="./projects/02/main.py">Fase 2</a></h2>

```
Novamente vamos trabalhar com dados meteorológicos, mas agora os dados serão de um arquivo texto.  Nesta fase, você trabalhará com um conjunto de dados¹ (formato csv² em anexo disponibilizado no Material Complementar) contendo informações climáticas diárias do município brasileiro de Porto Alegre, entre os anos 1961 e 2016. O arquivo contém 18.564 registros com os campos: data, precipitação (volume de chuva em milímetros por m2), temperatura máxima (em graus celsius), temperatura mínima (em graus celsius), umidade relativa do ar (% entre 0 e 100) e a velocidade do vento (em m/s). 

 

Seu programa deve ser capaz de realizar:

 

• Carga e preparação de dados: trabalhar com arquivos de dados, realizando a sua leitura, filtragem das informações relevantes e armazenamento em estruturas de dados adequadas para consulta. 

• Análise e visualização de dados: análises estatísticas diversas sobre os dados armazenados, por meio da implementação de algoritmos e geração de gráficos para a visualização dos resultados.

 

O código entregue em linguagem Python deve permitir:

 

Leitura do arquivo: os dados do arquivo devem ser carregados para memória e disponibilizados em uma lista de listas/tuplas/dicionário.
   

Observações: 

• É a partir da aula 08 que explicamos como realizar a leitura de arquivo texto e a carga dos dados em listas. No entanto, a manipulação de estruturas de dados está nas aulas anteriores à aula 08. Por isso, é importante você assistir e realizar as práticas na sequência sugerida. Nossos exemplos são todos com arquivo CSV e não há necessidade de uso de bibliotecas específicas, além das abordadas na disciplina. Além das funções de manipulação de arquivo, funções strings, como split, serão essenciais para a carga dos dados em lista/dicionário. No entanto, você pode usar outras bibliotecas se já conhecê-las.

• Crie quantas estruturas de dados (listas, dicionários, ...) que você julgar conveniente e não esqueça de organizar seu código em funções. 

• Comente no seu código decisões tomadas quanto ao tratamento dos dados, mencionando o que você desconsiderou, excluiu ou corrigiu no arquivo. Não use caminhos absolutos para o arquivo .csv, implemente considerando que o arquivo está na mesma pasta do seu programa. Não defina caminhos específicos dentro do seu código para acesso ao arquivo .csv. Se você entregar com caminhos absolutos o trabalho não será avaliado. Considere os exemplos abaixo, caso você não tenha entendido a diferença entre caminho absoluto e caminho relativo. Se mesmo com o exemplo você ainda ficar com dúvida, contate o tutor da disciplina para ele ajudar você. 
          ▫ Caminho relativo: O caminho não é explicitamente especificado, significa que será considerado como caminho aquele em que o programa estiver. 

            Exemplo: arquivo = open('dados.csv', 'r') 

          ▫ Caminho absoluto: O caminho é especificado e o programa só funcionará se esse caminho existir na máquina de quem for executá-lo. 

            Exemplo: arquivo = open('C:\Desktop\PUCRS\dados.csv', 'r') 

• Não modifique o arquivo .csv dado. Seu programa é que deve tratar os dados lidos do arquivo.

 

a) Visualização de intervalo de dados em modo texto: a partir de entradas do usuário, sua implementação deve permitir a visualização dos dados que foram carregados do arquivo. O usuário deve informar o período que quer ver, ou seja, deve indicar o mês e ano iniciais, bem como o mês e ano finais que deseja visualizar os dados. Permita também que o usuário informe se quer ver 1) todos os dados, 2) apenas os de precipitação, 3) apenas os de temperatura, ou 4) apenas os de umidade e vento para o período informado. 

 

Observações: 

• Valide os dados de entrada;

• Você pode escolher a forma de apresentação dos dados, porém não esqueça de incluir um cabeçalho para os dados exibidos.

 

b) Mês mais chuvoso: o mês/ano com maior precipitação, considerando todos os dados do arquivo. Exiba também a maior precipitação na tela juntamente com o mês e o ano. Utilize obrigatoriamente um dicionário e implemente ao menos uma função. Lembre-se de considerar todos os dados do arquivo! 

 

c) Média da temperatura mínima de um determinado mês (auge do inverno) nos últimos 11 anos (2006 a 2016): ano a ano, calcule a temperatura mínima média do mês informado pelo usuário. Implemente esse item, codificando uma função e armazenando os dados em um dicionário. Se o mês informado for agosto, por exemplo, você pode usar como chave o mês combinado com o ano: agosto2006, agosto2007,...; e como valor, você deve apresentar a média da temperatura mínima referente ao mês e ano da chave. Não esqueça de validar a entrada do usuário, o mês deve ser válido.

 

d) Gráfico de barras (vertical ou horizontal) com as médias de temperatura mínima de um determinado mês nos últimos 11 anos. (2006 a 2016). Gere um gráfico com as médias calculadas do mês informado em cada ano do período conforme o item c. Não esqueça de rotular os eixos e usar legendas para deixar o seu gráfico informativo, legível (altere as cores, se necessário) e bem elaborado.

e) Média geral da temperatura mínima de um determinado mês nos últimos 11 anos (2006 a 2016): percorra o dicionário criado no item c, calcule e exiba a média geral da temperatura para o referido mês. 
```