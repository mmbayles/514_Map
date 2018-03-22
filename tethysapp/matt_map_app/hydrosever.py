import hydrostats as hstats
import requests
import jupyter_add_func

# Get values from hydroserver
url = 'http://hydroportal.cuahsi.org/nwisdv/cuahsi_1_1.asmx?WSDL'
# Provo River at Provo Utah
site_code = 'NWISDV:10163000'
variable_code = 'NWISDV:00060/DataType=MEAN'
start_date = '2018-03-01'
end_date = '2018-03-05'
hydro_string = jupyter_add_func.get_hydroserver(url, site_code, variable_code, start_date, end_date, auth_token=None)


hydro_data = jupyter_add_func.parse_waterml(hydro_string, 'observed.csv')


# Get national water model
# Provo River at Provo Utah
comid = '10376596'
url_nwm = 'https://apps.hydroshare.org/apps/nwm-forecasts/api/GetWaterML/' \
          '?config=analysis_assim&geom=channel_rt&variable=streamflow&COMID={0}&' \
          'startDate={1}&lag=t00z&endDate={2}'.format(comid, start_date, end_date)
res = requests.get(url_nwm)
url_string = res.url
nwm_data = jupyter_add_func.parse_waterml(res.content, 'predicted.csv')
combined_data = jupyter_add_func.merge_data('predicted.csv', 'observed.csv', interpolate='predicted',
                                            column_names=['Simulated', 'Observed'], predicted_tz=None, recorded_tz=None,
                                            interp_type='pchip')
print combined_data
com = hstats.all_metrics(combined_data['Simulated'].values, combined_data['Observed'].values)
print com
