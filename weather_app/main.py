from api import WeatherAPI

def main():
    cidade = input("Digite o nome da cidade: ")
    api = WeatherAPI()
    clima = api.obter_clima(cidade)
    print(f"Clima em {cidade}: {clima['temperatura']}°C, {clima['descricao']}")

if __name__ == "__main__":
    main()
  
