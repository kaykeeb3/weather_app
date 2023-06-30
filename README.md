<h1 align="center">WEATHER APP</h1>

<p align="center">A aplicação <strong>Weather App</strong> foi desenvolvida durante estudos com <strong>Python com IA</strong>. O projeto é voltado para obter informações sobre o clima de uma determinada cidade<br>

<br>

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

## ⚙ BACK END | LÓGICA 
- Python
- API: OpenWeatherMap
- Git e Github


## 💻 Projeto 

### Organização: 
main.py: Este é o ponto de entrada do programa. Ele solicita ao usuário que digite o nome da cidade, instancia a classe WeatherAPI e chama o método obter_clima() para obter as informações do clima. Em seguida, imprime as informações na tela..
<br/>

api.py: Neste arquivo, definimos a classe WeatherAPI, que é responsável por fazer a requisição à API e retornar os dados do clima. No método obter_clima(), construímos a URL da requisição com os parâmetros necessários, fazemos a requisição usando o módulo requests, e então criamos uma instância da classe Clima (definida em models.py) com os dados obtidos da API.
<br/>

models.py: Aqui definimos a classe Clima, que representa os dados do clima. No construtor, recebemos o objeto JSON retornado pela API e extraímos a temperatura.
