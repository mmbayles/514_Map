import numpy as np
import hydrostats as hstats
import requests
from lxml import etree as ET
from suds.client import Client


def get_usgs(url):
    source = 'usgs'
    series_list = []
    res = requests.get(url)
    url_string = res.url
    root = ET.fromstring(res.content)
    print 'usgs has data'
    time_series = root.findall(
        './/{http://www.cuahsi.org/waterML/1.1/}timeSeries')
    nodata = root.findtext(
        './/{http://www.cuahsi.org/waterML/1.1/}noDataValue')
    variable = root.findtext(
        './/{http://www.cuahsi.org/waterML/1.1/}variableName')
    for series in time_series:
        x = []
        y = []
        values = series.findall(
            './/{http://www.cuahsi.org/waterML/1.1/}value')
        statistic = series.findtext(
            './/{http://www.cuahsi.org/waterML/1.1/}option')
        for element in values:
            try:
                date = element.attrib['dateTime']
                # remove extra 'T' in timestampe so that date is proper
                # format for plotly graph
                dates = date.replace('T', ' ')
                x.append(dates)
                v = element.text
                # Sometimes data does not precisely match the no data
                # value
                if nodata in v or v < 0 or v in nodata:
                    value = None
                    y.append(value)
                else:
                    v = float(v)
                    y.append(float(v))

            except:
                pass
        if variable is None:
            variable = ''
        if 'Gage' in variable:
            variable = 'Gauge'
            yaxis = 'Gauge Height'
        else:
            variable = 'Flow'
            yaxis = 'Streamflow'
        if y == []:
            variable = 'no data'
        if '/iv/' in url_string:
            series_list.append(dict(
                x=x,
                y=y,
                variable=variable,
                name=yaxis + ' - Instantaneous USGS',
                site_code=site_code,
                source=source,
                site_name='usgs',
                mode='lines'))
        elif '/dv/' in url_string:
            series_list.append(dict(
                x=x,
                y=y,
                variable=variable,
                name='{0} - {1} - Daily USGS'.format(yaxis, statistic),
                site_code=site_code,
                source=source,
                site_name='test_site',
                mode='lines',
                visible='legendonly'))
        elif 'nwm-forecasts' in url_string:
            series_list.append(dict(
                x=x,
                y=y,
                variable=variable,
                name='{0} - {1} - Daily USGS'.format(yaxis, statistic),
                site_code=site_code,
                source=source,
                site_name='test_site',
                mode='lines',
                visible='legendonly'))
        return series_list


def get_hydroserver(url, site_code, variable_code, start_date, end_date, auth_token):
    try:
        client = Client(url)
    except:
        print 'could not connect'
    response = client.service.GetValues(site_code,
                                        variable_code,
                                        start_date,
                                        end_date,
                                        auth_token)
    return


# hstats.me()
code = '00060'
site_code = '07153000'
start_date = '2018-03-01'
end_date = '2018-03-05'

comid = '20969516'
url = 'https://waterservices.usgs.gov/nwis/iv/?' \
      'parameterCd={0}&site={1}&startDT={2}&endDT={3}&' \
      'format=waterml'.format(code, site_code, start_date,end_date)
print url
usgs_data = get_usgs(url)
url_nwm = 'https://apps.hydroshare.org/apps/nwm-forecasts/api/GetWaterML/' \
          '?config=analysis_assim&geom=channel_rt&variable=streamflow&COMID={0}&' \
          'startDate={1}&lag=t00z&endDate={2}'.format(comid, start_date, end_date)
print url_nwm
nwm_data = get_usgs(url_nwm)

usgs2 = np.array(usgs_data[0]['y'][:120])
nwm_numpy = np.array(nwm_data[0]['y'])

com = hstats.me(nwm_numpy, usgs2)
print len(usgs_data[0]['y'][:120])
print len(nwm_data[0]['y'])
print usgs_data
print nwm_data
print com
