# receive_resize_image


É um aplicativo cuja função é receber um arquivo de imagem como parâmetro de entrada, essa imagem será processada e enviada para uma fila rabbitmq. Posteriormente, esses dados armazenados, serão consumidos e uma nova imagem será gerada com um novo redimensionamento.

Para utilizar o aplicativo, basta executar o comando:

```shell
$ docker-compose up
```

Será carregado 3 contêiner:

**- receive_image**: Um Rest Api (Flask) que receberá uma imagem como parâmetro de entrada e enviará para uma fila (rabbitmq);

**- resizing_image**: Um aplicativo que vai consumir os dados das imagens na fila, e vai criar uma nova imagem com tamanho 384x384 (redimensionado);

**- rabbitmq**: armazenará as imagens e informações como nome da imagem e parâmetros de largura e altura ("width", "height") utilizados para processamento.

Existem duas opções para enviar as imagens ao aplicativo, uma delas é através do endereço:

http://127.0.0.1:5000/

e a outra é através do comando:
 
```shell
$ curl -X POST http://127.0.0.1:5000 -F file=@'nome_da_imagem’
```

exemplo:

```shell
$ curl -X POST http://127.0.0.1:5000 -F file=@imagem.jpeg
```

Depois que esses dados forem processado, uma nova imagem será gerado e salvo dentro do contêiner ‘resizing_image’, na área de trabalho ‘/home/resizing_image’ com o nome, exemplo: ‘imagem_resize.jpeg’.

É possível acessar a nova imagem gerada via ‘volumes’, para isso, descomente a linhas do arquivo “docker-compose.yml”

```shell
#    volumes:
#      - resizing_image:/home/resizing_image
```

e

```shell
#volumes:
#  resizing_image:
#    external: true
```

E execute o comando para criar o volume:

```shell
$ docker volume create  resizing_image
```

para verificar os detalhes do volume criado, execute:

```shell
$ docker volume inspect resizing_image
```

Dessa forma, sera possível visualizar a imagem resultante gerada.
