import csv

def leggi_riga(file_input, numero_riga):
    try:
        # Apri il file CSV in modalità lettura
        with open(file_input, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # Converti il reader in una lista per accedere alle righe tramite indice
            righe = list(reader)
            
            # Verifica se il numero_riga è valido
            if numero_riga < 1 or numero_riga > len(righe):
                return f"Errore: il numero della riga deve essere compreso tra 1 e {len(righe)}."
            
            # Restituisci la riga corrispondente
            return righe[numero_riga - 1]  # Indice 0-based
        
    except FileNotFoundError:
        return f"Errore: il file '{file_input}' non esiste."
    except Exception as e:
        return f"Si è verificato un errore: {e}"
    
#leggi_dato ritorno il dato identificato dall numero della riga e colonna indicata nei parametri 
    
def leggi_dato(file_input, numero_riga, indice_colonna):    #nb:il conteggio delle righe parte da 1 che in generale corrisponde all'intestazione
    try:
        with open(file_input, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            righe = list(reader)  # Converte l'iteratore in una lista
            
            # Verifica se la riga e la colonna esistono
            if numero_riga < 1 or numero_riga > len(righe):
                return f"Errore: il numero della riga deve essere compreso tra 1 e {len(righe)}."
            
            riga = righe[numero_riga - 1]  # Indice 0-based per le righe
            
            if indice_colonna < 0 or indice_colonna >= len(riga):
                return f"Errore: l'indice della colonna deve essere compreso tra 0 e {len(riga) - 1}."
            
            # Restituisci il dato specifico
            return riga[indice_colonna]
    
    except FileNotFoundError:
        return f"Errore: il file '{file_input}' non esiste."
    except Exception as e:
        return f"Si è verificato un errore: {e}"


# Funzione per estrapolare e scrivere dati
def estrapola_e_inserisci(file_input_body, file_output, id_sensore):
    try:

        # Apri il file di input in modalità lettura
        with open(file_input_body, mode='r', newline='', encoding='utf-8') as fin:
            reader = csv.reader(fin)
            
            # Apri il file di output in modalità scrittura
            with open(file_output, mode='w', newline='', encoding='utf-8') as fout:
                campi_da_esportare = ['Data', 'Valore']
                writer = csv.DictWriter(fout, fieldnames=campi_da_esportare)
                

                # Scrivi l'intestazione nel file di output
                writer.writeheader()
                
                # Filtra o manipola i dati e scrivili nel file di output
                for riga in reader:
                    if riga[0] == id_sensore:
                        if float(riga[2]) >= 0.0:
                            writer.writerow({'Data': riga[1], 'Valore': riga[2]})
                        else:
                            writer.writerow({'Data': riga[1], 'Valore': 'NaN'}) #se leggo un valore negativo scrivo NaN


                        
        
        print(f"Dati copiati con successo da {file_input_body} a {file_output}.")
    
    except FileNotFoundError:
        print(f"Errore: il file {file_input_body} non esiste.")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")

def crea_file_info(file_input_body, file_output, id_sensore):
    try:

        # Apri il file di input in modalità lettura
        with open(file_input_body, mode='r', newline='', encoding='utf-8') as fin:
            reader = csv.reader(fin)
            
            # Apri il file di output in modalità scrittura
            with open(file_output, mode='w', newline='', encoding='utf-8') as fout:
                campi_da_esportare = ['IdSensore', 'Tipologia','IdTipologia','idStazione','Provincia','Nome']
                writer = csv.DictWriter(fout, fieldnames=campi_da_esportare)
                

                # Scrivi l'intestazione nel file di output
                writer.writeheader()
                
                # Filtra o manipola i dati e scrivili nel file di output
                for riga in reader:
                    if riga[0] == id_sensore:
                        writer.writerow({'IdSensore': riga[0], 'Tipologia': riga[1],'IdTipologia': riga[2],'idStazione': riga[3],'Provincia': riga[4],'Nome': riga[5]})


                        
        
        print(f"Dati copiati con successo da {file_input_body} a {file_output}.")
    
    except FileNotFoundError:
        print(f"Errore: il file {file_input_body} non esiste.")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")