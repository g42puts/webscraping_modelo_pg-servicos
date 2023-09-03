## webscraping_modelo_pg-servicos

# Repositório em construção

# Conteúdos
  * [O que é isso?](#o-que-e-isso)
    * [A ideia do projeto](#a-ideia-do-projeto)
  * [Requisitos](#requisitos)
  * [Como usar](#como-usar)
  * [A estrutura](#a-estrutura)
    * [Extração dos dados](#extração-dos-dados)
    * [Navegação na página](#navegação-na-pagina)
    * [Resultado final](#resultado-final)


# O que é isso?

Trata-se de um simples projeto de **ETL (Extract Transform Load)** de um site que exibe escalas de serviços usando [Selenium](https://www.selenium.dev/) e [Pandas](https://www.python.org/).

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

# A estrutura

## Extração dos dados

### *XPATH*, O que é?

Segundo está [artigo](https://escoladedados.org/tutoriais/xpath-para-raspagem-de-dados-em-html/) da [Escola de Dados](https://escoladedados.org): 

`O XPath é uma linguagem de consulta que nos ajuda a navegar por documentos que usam marcadores, como os arquivos XML (Extensible Markup Language) e HTML (HyperText Markup Language). Para você que já entende o básico de HTML, aqui será possível ter uma introdução sobre como usar XPath para extrair informações deste tipo de documento.`

Como deu para entender, o **XPATH** é uma poderosa ferramenta de consulta, para método comparativo, é como barra de pesquisas do *Google*, você digita o que você está procurando, e ele vai procurar por tudo que incluir ou fizer referência aquilo, mas ele é ainda mais preciso e seletivo, pois através do **XPATH**, eu especifico com precissão o que eu quero pesquisar, vamos a um exemplo...

#### Temos o seguinte trecho de código HTML: 

```html
<h2 class="titulo-com-grafismo" style="margin-bottom:14px">Exemplo</h2>
```
Através da busca pelo XPATH, eu irei procurar na página que me encontro, todos os **`<h2>`** que a classe seja igual a **titulo-com-grafismo**, e é este formato que o meu **XPATH** terá:

```python
//h2[@class="titulo-com-grafismo"]
```
Apenas isso já é o suficiente para que eu consiga localizar o trecho do **HTML** que estou procurando, porém pode havar casos em que exista na página mais de um trecho identico, e para isso eu posso usar outro formatação, mais especifica ainda, como a seguinte:

```python
//h2[contains(@style, 'margin-bottom:14px')]
```
A diferença desse para o anterior, é que aqui estou procurando por **h2** que contenha um determinado style, posso ser ainda mais preciso, como na seguinte forma:

```python
//h2[@class="titulo-com-grafismo" and contains(@style, 'margin-bottom:14px')]
```
Aqui não vai haver erro, caso queira procurar até mesmo por elementos que o seu valor textual seja X, pode fazer da seguinte forma:

```python
//h2[@class="titulo-com-grafismo" and contains(text(), 'Exemplo')]
```

Eu particulamente recomendo que você faça alguns testes em alguma página da sua escolha para enteder mais ainda sobre o **XPATH** e como é eficiente.

### Navegação e Extração dos dados

A nevagação na página foi feita utilizando as ferrementas do próprio [Selenium](https://www.selenium.dev/) para navegação e o método de consulta **XPATH**.

Na função **service_webscrap** do arquivo **main.py**:
1. Defini variaveis com credenciais do usuário

2. Defini variaveis nome do mes atual e mes seguinte

3. Defini as configs do navegador e defini meu navegador com o nome **driver**

4. Navageção até o site da escala de serviço

4.1 Primeiramente iniciei o navegador do Selenium

4.2 Naveguei até a página de login, enviei as credenciais de login, e realizei o login

4.3 Em seguida naveguei até a página da escala

5. Extração dos dados na página da escala

5.1 Fiz a extração dos dados utilizando o XPATH e TAG_NAME, métodos de consulta do **Selenium**

5.2 Após fazer a extração do primeiro mês, passei para a página do mês seguinte e fiz outra extração

6. Após a extração, todos dados foram salvos em formato .csv com nome do mês a qual se refere a escala

## Resultado final

A forma como os dados será salva na tabela:

| dia | mes | ano | dia_do_mes | servico |
|-----|-----|-----|------------|---------|
|30|março|2023|Quinta-Feira|M|
