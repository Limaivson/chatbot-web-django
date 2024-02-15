# Django Chatbot Web App

Este projeto Django é um aplicativo da web que implementa um chatbot com suporte a conversa em texto, conversa por áudio e análise de imagens. O chatbot é alimentado por um modelo de linguagem de inteligência artificial (IA) e é capaz de interagir com os usuários de várias maneiras.

## Configuração do Ambiente

1. Clone o repositório para sua máquina local:

    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd nome-do-repositorio
    ```

3. Crie um ambiente conda com as dependências do projeto:

    ```bash
    conda create --name nome-do-ambiente python=3.x
    ```

    Certifique-se de substituir `nome-do-ambiente` pela nomenclatura desejada e `3.x` pela versão do Python desejada.

4. Ative o ambiente conda:

    - No Windows:

        ```bash
        conda activate nome-do-ambiente
        ```

    - No macOS e Linux:

        ```bash
        source activate nome-do-ambiente
        ```

5. Instale as dependências do Python:

    ```bash
    pip install -r requirements.txt
    ```

## Configuração das Variáveis de Ambiente

1. Crie um arquivo `.env` na raiz do projeto.

2. Adicione as seguintes variáveis de ambiente ao arquivo `.env`:

    ```env
    API_KEY=SuaChaveDeAPI
    DEBUG=True
    ```

    Certifique-se de substituir `SuaChaveDeAPI` pela chave de API necessária para o correto funcionamento do chatbot.

## Executando o Servidor

1. Execute o servidor de desenvolvimento do Django para iniciar o aplicativo:

```bash
python manage.py runserver

```
2. Acesse o aplicativo em:
```
http://127.0.0.1:8000/
```
## Rotas Disponíveis
1. Conversa em Texto:
```
Rota: /texto/
```
Descrição: Essa rota permite aos usuários iniciar uma conversa em texto com o chatbot.

2. Conversa por Áudio:
```
Rota: /audio/
```
Descrição: Essa rota oferece suporte à conversa por áudio, permitindo aos usuários interagir com o chatbot usando voz.

3. Análise de Imagens:
```
Rota: /imagem/
```
Descrição: Esta rota permite aos usuários realizar análise de imagens através do chatbot.

## Desenvolvimento Adicional
Este projeto fornece uma estrutura básica para um aplicativo web Django com funcionalidades de chatbot. Você pode expandir e personalizar o aplicativo adicionando mais funcionalidades, melhorando a interface do usuário ou integrando serviços externos.

## Contribuição
Contribuições são bem-vindas! Se você tiver melhorias, correções de bugs ou novas funcionalidades para adicionar, sinta-se à vontade para criar um pull request.

## Licença
Este projeto é licenciado sob a Licença **MIT**. Sinta-se à vontade para usar, modificar e distribuir conforme necessário.



