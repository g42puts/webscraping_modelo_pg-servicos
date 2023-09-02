import datetime
from datetime import date as dt_date, datetime


# lista dos nomes dos dias da semana
dias_da_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

# função para pegar o dia da semana pelo dia passado, mês e ano
def get_day_name(day_id:int=None, month_id:int=None, year:int=None) -> None:    

    # define os valores que serão passados para a função dt_date(datetime.date)
    ano = datetime.now().year if not year else year
    mes = month_id
    dia = day_id
    
    try:
        # passa ano, mês e dia para formato de data
        data = dt_date(ano, mes, dia)
    except ValueError:
        return print('Ocorreu algum erro nos valores passados.')

    # pega o nome do dia da semana usando a função weekday e a list de dias da semana
    nome_dia_semana = dias_da_semana[data.weekday()]

    # retorna o dia da semana de acordo com o dia, mês e ano passados
    return nome_dia_semana

# para teste
if __name__ == '__main__':
    get_day_name(1,9, 2023)