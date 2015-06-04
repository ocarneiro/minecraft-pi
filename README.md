# minecraft-pi
Experiências usando minecraft pi (api Python do Minecraft rodando na Raspberry Pi)

O arquivo led_mine.py contém código para permitir a interação do Minecraft com o mundo real. Para isso, devem-se realizar as seguintes conexões:

1) Conectar um LED verde ao pino 22;
2) Conectar um LED vermelho ao pino 18;
3) Conectar um driver de motor ao pino 16.

Quando o usuário ficar de frente para um bloco de ferro, o LED verde se acenderá.

Quando o usuário ficar de frente para um bloco de redstone, o LED vermelho se acenderá.

Quando o usuário ficar de frente para um bloco de diamante, o motor será acionado.

O código cria um "palco" para experimentar esta lógica. Neste palco há uma parede de cada tipo destes materiais.

Bom jogo!
