from src import utility,check
import os

def genera_nome_file_output(tipologia,  anno):
    return f'{tipologia}_{anno}.csv'  # Nome unico

def genera_nome_cartella(id_sensore, id_stazione, provincia, localita):
    return f'{localita}_idSens{id_sensore}_idStazione{id_stazione}_prov{provincia}'  # Nome unico

# File da cui leggere l'intestazione
file_input_anagrafica = 'D:\METEO\AnagraficaSensoriBresciacsv.csv' 

#creazione e scrittura dei file CSV dal 2013 al 2023 
for riga in range(2, 46):   #range(2, 46)
    # Percorso della cartella da creare
    cartella = 'D:\METEO\dati_filtrati\\' + genera_nome_cartella(utility.leggi_dato(file_input_anagrafica, riga, 0),    # idSensore
                                                                 utility.leggi_dato(file_input_anagrafica, riga, 3),    # idStazione
                                                                 utility.leggi_dato(file_input_anagrafica, riga, 4),    # Provincia
                                                                 utility.leggi_dato(file_input_anagrafica, riga, 5))    # Nome
    
    # Creazione della cartella
    if not os.path.exists(cartella):
        os.makedirs(cartella)
        print(f"Cartella creata: {cartella}")
    else:
        print(f"La cartella {cartella} esiste già.")

    utility.crea_file_info(file_input_anagrafica, cartella + '\\' +'infoSensore.csv', utility.leggi_dato(file_input_anagrafica, riga, 0))

    for anno in range(2013, 2024):  #range(2013, 2024):

        # File da cui leggere i dati
        file_input_body = 'D:\METEO\\' + str(anno) + '.csv' 
        # File in cui scrivere, nb: se non esiste lo crea con il nome tra apici
        file_out = cartella + '\\' + genera_nome_file_output(utility.leggi_dato(file_input_anagrafica, riga, 1), anno)
        #richiamo funzione estrapola_e_inserisci
        utility.estrapola_e_inserisci(file_input_body, file_out, utility.leggi_dato(file_input_anagrafica, riga, 0))

