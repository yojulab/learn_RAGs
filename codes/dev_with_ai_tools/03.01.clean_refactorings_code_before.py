def get_country_name(country_code):
    if country_code == 'US':
        return 'United States'
    elif country_code == 'GB':
        return 'United Kingdom'
    elif country_code == 'FR':
        return 'France'
    elif country_code == 'DE':
        return 'Germany'
    else:
        return 'Unknown'
    
if __name__ == '__main__':
    print(get_country_name('US'))
    print(get_country_name('GB'))
    print(get_country_name('FR'))
    print(get_country_name('DE'))
    print(get_country_name('KR'))    