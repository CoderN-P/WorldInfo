import wbdata

def get_gdp_per_capita(country_code):
    """
    Returns the GDP per capita of a country over the last 10 years.
    """
    return {int(i['date']): i['value'] for i in wbdata.get_data(
        country=country_code,
        indicator='NY.GDP.PCAP.CD') if i['value']}

def get_gni_per_capita(country_code):
    """
    Returns the GNI per capita of a country over the last 10 years.
    """
    return {int(i['date']): i['value'] for i in wbdata.get_data(
        country=country_code,
        indicator='NY.GNP.PCAP.CD') if i['value']}

def get_inflation_rate(country_code):
    """
    Returns the inflation rate of a country over the last 10 years.
    """
    return  {int(i['date']): i['value'] for i in wbdata.get_data(
        country=country_code,
        indicator='FP.CPI.TOTL.ZG') if i['value']}


