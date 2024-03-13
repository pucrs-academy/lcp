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