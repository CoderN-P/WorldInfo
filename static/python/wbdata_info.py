import wbdata

def get_gdp_per_capita(country_code):
    """
    Returns the GDP per capita of a country over the last 10 years.
    """
    return wbdata.get_data(
        country=country_code,
        indicator='NY.GDP.PCAP.CD')

def get_gni_per_capita(country_code):
    """
    Returns the GNI per capita of a country over the last 10 years.
    """
    return wbdata.get_data(
        country=country_code,
        indicator='NY.GNP.PCAP.CD')

def get_inflation_rate(country_code):
    """
    Returns the inflation rate of a country over the last 10 years.
    """
    return wbdata.get_data(
        country=country_code,
        indicator='FP.CPI.TOTL.ZG')

print(get_inflation_rate('USA'))