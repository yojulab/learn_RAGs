def get_country_name(country_code):
    country_map = {
        'US': 'United States',
        'GB': 'United Kingdom',
        'FR': 'France',
        'DE': 'Germany'
    }
    return country_map.get(country_code, 'Unknown')
    
if __name__ == '__main__':
    print(get_country_name('US'))
    print(get_country_name('GB'))
    print(get_country_name('FR'))
    print(get_country_name('DE'))
    print(get_country_name('KR'))
