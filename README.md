## webscraping_modelo_pg-servicos

# Conteúdos
  * [O que é isso?](#o-que-e-isso)
    * [A ideia do projeto](#a-ideia-do-projeto)
  * [Requisitos](#requisitos)
  * [Como usar](#como-usar)
  * [O desenvolvimento e dificuldades na criação](#)
    * [Importações](#importações)
    * [Arquivos pessoais](#arquivos-pessoais)
    * 
  * [A estrutura](#a-estrutura)



# O que é isso?
  ## A ideia do projeto
Um amigo veio até mim me perguntar como poderia fazer um simples programa para atender a necessidade dele, que era de obter alguns dados em um site dinâmico, e nesse processo a primeira etapa seria realizar o login para poder entrar no sistema e em seguida dar prosseguimento a navageção e extração de dados, então tive a ideia de usar o Selenium já que ele conta uma biblioteca muito boa para fazer WebScraping e em seu kit, há ferramentas prontas para leitura de HTML, interação com páginas (autenticação) e etc.

Como eu estava a algum tempo sem usar o Selenium, decidi criar primeiro de criar um script e posteriormente explicar passo a passo desse projeto para que ele tivesse um norte.

# Requisitos

Para rodar o código e/ou fazer as alterações que você queira:

- [Selenium](https://www.selenium.dev/) # para ETL
- [Pandas](https://www.python.org/) # para salvar os dados em formato de tabela
- [Dotenv](https://pandas.pydata.org/) (python-dotenv) # carregar informações de login do usuário

# Como usar

1. Clone o repositório.

```terminal
git clone https://github.com/g42puts/webscraping_modelo_pg-servicos.git
```

2. Faça instalação das bibliotecas requisitadas.

- No Linux:

```terminal
pip3 install -r requiriments.txt
```

- No Windows:

```terminal
pip install -r requiriments.txt
```

3. Faça as alterações no código da forma que quiser, não se preocupe com direitos autorais ou qualquer outra coisa, este repositório é apenas para fins de estudo.

# O desenvolvimento e dificulades na criação

### Bibliotecas usadas:

<div style="display: flex; justify-content: space-between;">
    <p>
      <img src="https://skillicons.dev/icons?i=python&theme=dark" alt="Python" width="24">
      <a href="https://www.python.org/" target="_blank">Python</a>
    </p>
</div>

<div style="display: flex; justify-content: space-between;">
    <p>
      <img src="https://skillicons.dev/icons?i=selenium&theme=dark" alt="Selenium" width="24">
      <a href="https://www.selenium.dev/" target="_blank">Selenium</a>
    </p>
</div>

<div style="display: flex; justify-content: space-between;">
    <p>
      <img src="https://pandas.pydata.org//static/img/favicon_white.ico" alt="Pandas" width="24">
      <a href="https://pandas.pydata.org/docs/" target="_blank">Pandas</a>
    </p>
</div>



# 3. A estrutura

A forma como os dados será salva na tabela:

| dia | mes | ano | dia_do_mes | servico |
|-----|-----|-----|------------|---------|
|30|março|2023|Quinta-Feira|M|


