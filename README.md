# Projeto para validar senha
<ul>
Regras:
    <li>Nove ou mais caracteres</li>
    <li>Ao menos 1 dígito</li>
    <li>Ao menos 1 letra minúscula</li>
    <li>Ao menos 1 letra maiúscula</li>
    <li>Ao menos 1 caractere especial</li>
    <ul><li>Considere como especial os seguintes caracteres: !@#$%^&*()-+</li></ul>
    <li>Não possuir caracteres repetidos dentro do conjunto</li>
 </ul>


- Para realizar a execução do projeto é necessário ter o docker instalado na máquina
- Após efetuar o clone do projeto é necessario executar os comandas para realizar o build do mesmo
    - docker-compose up --build (esse processo irá baixar as dependencias que o projeto necessita e inicializará o servidor)
    - Servidor inicializar no endereço: http://localhost:8080/api/v1/login
    - Para realizar uma requisição para esse endpoint você precisar enviar o json a baixo.
         - REQUEST
            {
                "senha":"AbTp9!fok"
            }
         - RESPONSE
         {
            "resposta": true
         }

    - Para rodar os testes é ncessário entrar no container.
        - Para iddentificar o container é necessário executar o comando "docker ps"
            - Após essa execução é necessário rodar o "docker exec -it CONTAINER_ID" sh
                - Estando no container é necessário executar o comando: python -m unittest tests/test_api.py, após esse processo irá mostrar se os testes passaram.
- A API foi construida utilizando a linguagem python na versão 3 com o framework Flask
    - Utilizei o Flask por se tratar de um framework que me dar a liberdade de controlar a execução de apenas o que eu preciso para o projeto.
    - Python foi utilizado por se tratar de uma linguagem de fácil entendimento e de alta perfomance, para assim realizar as validações no menor tempo possível 
