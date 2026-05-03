# guilherme_tonello_ag11_DS_I
Este código é uma simulação de um painel de controle para monitoramento de reservatórios
Ele divide o volume de água em 5 níveis, indo do "Crítico" (Nível 1) ao "Muito Alto" (Nível 5).
O código inclui uma verificação (if 0 <= indice < len(situacoes)) para garantir que, se o sistema receber um número inesperado (como nível 10 ou -1), ele não quebre e avise que o dado é inválido.
