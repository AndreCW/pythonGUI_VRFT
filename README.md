# pythonGUI_VRFT
GUI para o método VRFT

## Descrição
Aplicação que cria uma interface gráfica para aplicar o método VRFT no
contexto de conversores CC-CC. Esta ferramenta implementa o VRFT através
de um conjunto de dados de uma planta e certas informações relevantes.

## Como utilizar
Baixar o arquivo 'EasyVRFT.exe'. Este é o arquivo executável da aplicação
que permite que qualquer usuário possa utilizar esta sem precisar configurar
todo o ambiente em Python necessário para executar os códigos aqui fornecidos.

### Exemplo de uso

Para a primeira aba, deve ser selecionado o botão correspondente ao 
conversor da planta, por exemplo o 'Buck'. Após isso, informar os seguintes 
valores nos campos de texto ao lado:

* Ciclo de Trabalho(D): 0.6
* Tensão de Saída(Vo): 150

Selecionar 'Gerar Ganho Proporcional Máximo' irá mostrar na caixa de texto 
abaixo o ganho estático máximo para a coleta dos dados para o projeto do
controlador.

* Ganho estático máximo: 0.004 [V<sup> -1</sup>]

Na pasta 'Datasets' tem dois arquivos, contendo um conjunto de dados em cada.
Com a aplicação aberta, na segunda aba pode ser adicionado o primeiro desses
conjuntos, 'exemploProjeto', que corresponde a um ensaio feito para coletar
os dados para projetar um controlador. 

Selecionar a opção 'Padrão de primeira ordem' na parte da escolha
do modelo de referência e informar os seguintes valores:

* Tempo de Acomodação: 18.6
* x% mais rápido: 20
* Freq. de Amostragem: 50000

Selecionar a opção 'PID' na parte de escolha da classe do controlador.

Selecionar a opção 'Filtro Padrão L=Td(1-Td)' na parte de escolha do filtro.

Selecionar o botão 'Projetar Controlador'.

Na caixa de saída foi exibido os parâmetros gerados para o controlador PID 
selecionado:

* Kp = 0.008972759677321657
* Ki = 4.198094126666305e-05
* Kd = 0.025150970643255662

Na terceira aba, pode ser adicionado o outro conjunto fornecido, 'exemploValidacao'.
Este corresponde a um ensaio feito para coletar os dados para validar o
controlador projetado anteriormente.

Com o conjunto carregado para a ferramenta, pode ser vista a comparação gráfica
entre o sinal coletado da malha fechada com o sinal simulado do modelo de 
referência selecionando a opção 'Gerar Gráfico T(z)'.

Selecionar a opção 'Calcular Custo J(VR)' irá mostrar o valor do erro médio
quadrático entre o sinal coletado da malha fechada e o sinal simulado do
modelo de referência:

* Estimativa do custo minimizado: 0.3601159395178259

Selecionar a opção 'Estimar Função de Sensibilidade' irá mostrar a função
de sensibilidade do sistema simulado.
