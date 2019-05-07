## scraping
teste

## install
- [virtualenv](https://cadernodelaboratorio.com.br/2015/11/18/virtualenvwrapper-e-virtualenv-um-tutorial-de-instalacao-e-uso/)
- python 3.5
- Scrapy [install+guide](https://scrapy.readthedocs.io/en/latest/intro/install.html)

## Run
$ cd scraping  
$ scrapy crawl scraping -o got.json

## saída esperada

.djson [ { "price": value, "nome": "nome do produto", "link": "link da imagen"}]

