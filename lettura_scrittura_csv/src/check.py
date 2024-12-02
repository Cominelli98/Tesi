import datetime

def check_data(data):

    data_formattata = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M:%S")
    print(data_formattata)
    #timedelta = 
    data_formattata = data_formattata + datetime.datetime(minute=10)
    print(data_formattata)
    
    #data_formattata = data.strftime("%d/%m/%Y %H:%M:%S")
  

