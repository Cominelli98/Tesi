from src import utility

file_names = {
    'IMERG_total_precipitation_day_0.2x0.2_global_2000_v6.0',
    'IMERG_total_precipitation_day_0.2x0.2_global_2001_v6.0-029',
    'IMERG_total_precipitation_day_0.2x0.2_global_2002_v6.0-002',
    'IMERG_total_precipitation_day_0.2x0.2_global_2003_v6.0-003',
    'IMERG_total_precipitation_day_0.2x0.2_global_2004_v6.0-005',
    'IMERG_total_precipitation_day_0.2x0.2_global_2005_v6.0-023',
    'IMERG_total_precipitation_day_0.2x0.2_global_2006_v6.0-011',
    'IMERG_total_precipitation_day_0.2x0.2_global_2007_v6.0-008',
    'IMERG_total_precipitation_day_0.2x0.2_global_2008_v6.0-004',
    'IMERG_total_precipitation_day_0.2x0.2_global_2009_v6.0-006',
    'IMERG_total_precipitation_day_0.2x0.2_global_2010_v6.0-009',
    'IMERG_total_precipitation_day_0.2x0.2_global_2011_v6.0-028',
    'IMERG_total_precipitation_day_0.2x0.2_global_2012_v6.0-032',
    'IMERG_total_precipitation_day_0.2x0.2_global_2013_v6.0-027',
    'IMERG_total_precipitation_day_0.2x0.2_global_2014_v6.0-026',
    'IMERG_total_precipitation_day_0.2x0.2_global_2015_v6.0-012',
    'IMERG_total_precipitation_day_0.2x0.2_global_2016_v6.0-025',
    'IMERG_total_precipitation_day_0.2x0.2_global_2017_v6.0-010',
    'IMERG_total_precipitation_day_0.2x0.2_global_2018_v6.0-031',
    'IMERG_total_precipitation_day_0.2x0.2_global_2019_v6.0-030',
    'IMERG_total_precipitation_day_0.2x0.2_global_2020_v6.0-013',
    'IMERG_total_precipitation_day_0.2x0.2_global_2021_v6.0'
}

nord, sud, est, ovest = 60, 35, 66, -10  # Coordinate del rettangolo

for file in file_names:

    file_input = r"D:\METEO\Prec_daily_02x02\\" + file + '.nc'
    file_output = r"D:\METEO\Prec_daily_02x02_modified\\" + file + '_cut.nc'
    utility.copia_ritaglia_nc(file_input, file_output, nord, sud, est, ovest)

# parte di creazione dei file pickle
