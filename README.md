# QR Code Generator

## Sobre

O `<b>`QR Code Generator `</b>` é uma aplicação rápida e simples com interface GUI para gerar QR Code de links, imagens e números.

## Pré-requisitos

É necessário instalar as bibliotecas utilizadas no projeto. Para isto, execute o comando abaixo na raiz do projeto:

`<code>`pip install -r requirements.txt `</code>`

A Biblioteca `<b>`tkinter `</b>` é nativa e já vem com o python. Portanto, basta apenas importar.

## Utilização

Para executar o programa, basta utilizar qualquer IDE que você utiliza, ou pode executar diretamente do terminal.

Para executar do terminal, navegue até a raiz do projeto, e em seguida digite:

* Para Windows: `<code>`python qrcodegenerator.py `</code>`
* Para Linux: `<code>`python3 qrcodegenerator.py.py `</code>`

Após isso, uma janela(form) window é aberta solicitando que você informe o link ou arquivo que deseja gerar o QR Code. A janela será conforme abaixo:

![image](https://user-images.githubusercontent.com/116044972/226730823-c694157c-90a8-4265-820a-54ea6b915b87.png)

Insira o link a qual deseja gerar um QRCode. Após apertar gerar, uma mensagem será exibida (imagem abaixo) pedindo para você confirmar se o link a qual deseja gerar o QRCode está correto. 

![image](https://user-images.githubusercontent.com/116044972/226731644-54073989-0ccc-4baa-9b97-d11e03d48ed1.png)

Após confirmar, uma mensagem será exibida informando que o QR Code foi gerado com sucesso. 
![image](https://user-images.githubusercontent.com/116044972/226732358-ca4fcba4-b6a3-4b6a-a81a-2f06702f9035.png)


O mesmo está salvo no caminho <code>".qrcode/qrcode.png"</code> na pasta raíz do projeto.
Basta apenas agora usar a câmera do celular para testar e escanear o seu QRCode gerado.
