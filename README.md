## webscraping_modelo_pg-servicos

# README ainda em construção...

# Conteúdos
  * [O que é isso?](#o-que-e-isso)
  * [Requisitos](#requisitos)
  * [Como usar](#como-usar)
  * [A ideia do projeto e objetivo final](#a-ideia-do-projeto-e-objetivo-final)
  * [O desenvolvimento e dificuldades na criação](#)
    * [Importações](#importações)
    * [Arquivos pessoais](#arquivos-pessoais)
    * 
  * [A estrutura](#a-estrutura)



# O que é isso?

# Requisitos

### 1. De onde surgiu a ideia do projeto? 🤔

Um amigo veio até mim me perguntar como poderia fazer um simples programa para atender a necessidade dele, que era de obter alguns dados em um site dinâmico, e nesse processo a primeira etapa seria realizar o login para poder entrar no sistema e em seguida dar prosseguimento a navageção e extração de dados, então tive a ideia de usar o Selenium já que ele conta uma biblioteca muito boa para fazer WebScraping e em seu kit, há ferramentas prontas para leitura de HTML, interação com páginas (autenticação) e etc.

Como eu estava a algum tempo sem usar o Selenium, decidi criar primeiro de criar um script e posteriormente explicar passo a passo desse projeto para que ele tivesse um norte.

# 2. O desenvolvimento e dificulades na criação

### Bibliotecas usadas:

<div style="display: flex; justify-content: space-between;">
    <p>
      <img src="https://skillicons.dev/icons?i=python&theme=dark" alt="Python" width="24">
      <a href="https://www.python.org/">Python</a>
    </p>
</div>

<div style="display: flex; justify-content: space-between;">
    <p>
      <img src="https://skillicons.dev/icons?i=selenium&theme=dark" alt="Selenium" width="24">
      <a href="https://www.selenium.dev/">Selenium</a>
    </p>
</div>

<div style="display: flex; justify-content: space-between;">
    <p>
      <img src="https://pandas.pydata.org//static/img/favicon_white.ico" alt="Pandas" width="24">
      <a href="https://pandas.pydata.org/docs/">Pandas</a>
    </p>
</div>



# 3. A estrutura

A forma como os dados será salva na tabela:

| dia | mes | ano | dia_do_mes | servico |
|-----|-----|-----|------------|---------|
|30|março|2023|Quinta-Feira|M|


