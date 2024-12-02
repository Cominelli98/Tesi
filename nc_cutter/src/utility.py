import netCDF4 as nc
import numpy as np
import os

def copia_ritaglia_nc(file_input, file_output, nord, sud, est, ovest):
    # Apri il file di input
    with nc.Dataset(file_input, 'r') as src:
        # Leggi le variabili principali
        lat = src.variables['lat'][:]
        lon = src.variables['lon'][:]
        pr = src.variables['pr'][:]

        # Trova gli indici delle coordinate all'interno del rettangolo
        lat_indices = np.where((lat >= sud) & (lat <= nord))[0]
        lon_indices = np.where((lon >= ovest) & (lon <= est))[0]

        # Sottoseleziona i dati
        lat_subset = lat[lat_indices]
        lon_subset = lon[lon_indices]
        pr_subset = pr[:, lat_indices, :][:, :, lon_indices]

        # Crea un nuovo file di output
        with nc.Dataset(file_output, 'w', format='NETCDF4') as dst:
            # Copia le dimensioni
            dst.createDimension('time', None)  # Dimensione illimitata per il tempo
            dst.createDimension('lat', len(lat_subset))
            dst.createDimension('lon', len(lon_subset))

            # Copia le variabili
            time_var = dst.createVariable('time', src.variables['time'].datatype, ('time',))
            lat_var = dst.createVariable('lat', src.variables['lat'].datatype, ('lat',))
            lon_var = dst.createVariable('lon', src.variables['lon'].datatype, ('lon',))
            pr_var = dst.createVariable('pr', src.variables['pr'].datatype, ('time', 'lat', 'lon'), fill_value=src.variables['pr']._FillValue)

            # Copia gli attributi delle variabili
            time_var.setncatts({k: src.variables['time'].getncattr(k) for k in src.variables['time'].ncattrs()})
            lat_var.setncatts({k: src.variables['lat'].getncattr(k) for k in src.variables['lat'].ncattrs()})
            lon_var.setncatts({k: src.variables['lon'].getncattr(k) for k in src.variables['lon'].ncattrs()})
            pr_var.setncatts({k: src.variables['pr'].getncattr(k) for k in src.variables['pr'].ncattrs()})

            # Scrivi i dati
            time_var[:] = src.variables['time'][:]
            lat_var[:] = lat_subset
            lon_var[:] = lon_subset
            pr_var[:, :, :] = pr_subset

            # Copia gli attributi globali
            dst.setncatts({k: src.getncattr(k) for k in src.ncattrs()})

            # Aggiorna lo storico
            dst.history = f"{dst.history}\nModificato per selezionare dati tra Nord={nord}, Sud={sud}, Est={est}, Ovest={ovest}"

    print(f"File copiato e modificato con successo: {file_output}")