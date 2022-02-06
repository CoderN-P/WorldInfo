import wbdata

def get_gdp_per_capita(country_code):
    """
    Returns the GDP per capita of a country over the last 10 years.
    """
    return {int(i['date']): i['value'] for i in wbdata.get_data(
        country=country_code,
        indicator='NY.GDP.PCAP.CD')}

def get_gni_per_capita(country_code):
    """
    Returns the GNI per capita of a country over the last 10 years.
    """
    return {int(i['date']): i['value'] for i in wbdata.get_data(
        country=country_code,
        indicator='NY.GNP.PCAP.CD')}

def get_inflation_rate(country_code):
    """
    Returns the inflation rate of a country over the last 10 years.
    """
    return  {int(i['date']): i['value'] for i in wbdata.get_data(
        country=country_code,
        indicator='FP.CPI.TOTL.ZG')}

inflation = get_inflation_rate('IND')
gdp = get_gdp_per_capita('IND')
gni = get_gni_per_capita('IND')
x_axis = list(set(list(gdp.keys())+list(gni.keys())+list(inflation.keys())))
print(x_axis)

