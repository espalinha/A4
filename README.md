# A4 — Mobile AR Docking

Protótipo em three.js/WebXR. Publique os três arquivos `index.html`, `app.js` e `design-draft.md` em um servidor HTTPS (por exemplo GitHub Pages) e abra no Chrome Android com ARCore. Toque em Iniciar AR, autorize a câmera, aponte para uma superfície e toque para posicionar. Escolha a cor correspondente; arraste e torça com dois dedos, ou selecione para carregar, mova e gire o celular apontando para a superfície e toque em Fixar. O encaixe exige até 2 cm e 10 graus. Encerre a sessão AR para preparar outra tentativa e exportar o CSV.

O CSV fica no armazenamento local do navegador até ser exportado. Registre fadiga 1–5 após cada técnica, superfície, iluminação, ordem e observações separadamente. Faça 2 participantes × 2 técnicas × 3 tentativas, invertendo a ordem entre participantes. Grave uma tentativa de cada técnica (até 1 minuto no total). Os dados, resultados, gravações e discussão devem vir do estudo real. Confira no telefone o suporte a WebXR, os gestos, o overlay e o rastreamento antes da coleta.

`tracking_lost` conta transições para ausência de pose ou de hit-test após posicionamento; `touch_count` conta contatos iniciados na tela e nos controles. O cronômetro começa na seleção correta e erros são medidos no primeiro instante em que ambas as tolerâncias são satisfeitas.
