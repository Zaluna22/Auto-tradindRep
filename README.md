Automação de Cliques e Mensagens com PyAutoGUI
Este projeto automatiza uma sequência de cliques e o envio de mensagens em uma janela ativa usando a biblioteca pyautogui. A ação é executada a cada 1 hora e 3 minutos.

Pré-requisitos
Python 3.x
Biblioteca pyautogui
Instale o pyautogui com o seguinte comando:

bash:

pip install pyautogui


Descrição do Funcionamento
O programa realiza os seguintes passos:

Move o mouse para uma posição inicial e clica.
Após um breve intervalo, move para outra posição, clica e envia uma mensagem padrão.
Realiza um clique em uma terceira posição.
Usa a combinação de teclas Alt + Esc para minimizar ou alternar a janela.
Essa sequência é repetida em um loop a cada 1 hora e 3 minutos.

Como Usar
Defina as coordenadas das posições desejadas nas variáveis x1, y1, x2, y2, x3 e y3.
Ajuste o texto da mensagem na variável mensagem, se necessário.
Execute o script:

bash:
python nome_do_arquivo.py


Atenção
Desative o FAILSAFE apenas se necessário, pois ele impede que o script seja parado rapidamente movendo o cursor para o canto superior esquerdo da tela.
Certifique-se de que o programa alvo está em uma posição fixa na tela para que o script funcione corretamente.
