from resolvers.page_resolver import get_value, parse_price, get_page, resolve_link

def create_recommendation(type, title, price, color, link, image, date, gender):
    return {
        'type': type,
        'title': title,
        'price': price,
        'color': color,
        'link': link,
        'image': image,
        'date': date,
        'gender': gender
    }

def amazon_processor(kit, specification, date):
    host = 'https://www.amazon.com.br'
    page = get_page(host, '/s?k=[TYPE]+[COLOR]+[GENDER]', kit, specification)
    data = []
    for item in page.select('div[data-index]'):
        try:
            recommendation = create_recommendation(type = specification['type'],
                                                   title = item.select_one('img[data-image-load]').get('alt'),
                                                   price = parse_price(get_value(item.select_one('span[class=a-offscreen]'), item.select_one('span[class=a-color-base]'))),
                                                   color = specification['color'],
                                                   link = host + item.select_one('a[class=a-link-normal]').get('href'),
                                                   image = item.select_one('img[data-image-load]').get('src'),
                                                   date = date,
                                                   gender = kit['gender'])
            data.append(recommendation)
        except:
            print('Erro ao consultar item.')
    return data

def marisa_processor(kit, specification, date):
    host = 'https://pesquisa.marisa.com.br'
    page = get_page(host, '/busca?q=[TYPE]+[COLOR]+[GENDER]', kit, specification)
    data = []
    for item in page.select('.nm-product-item'):
        try:
            recommendation = create_recommendation(type = specification['type'],
                                                   title = item.get('data-name'),
                                                   price = parse_price(item.select_one('span[class=price-number]').get_text()),
                                                   color = specification['color'],
                                                   link = resolve_link('www', host + item.select_one('a').get('href')),
                                                   image = resolve_link('images2', item.select_one('img[class="nm-product-img"]').get('src')),
                                                   date = date,
                                                   gender = kit['gender'])
            data.append(recommendation)
        except:
            print('Erro ao consultar item.')
    return data

def pernambucanas_processor(kit, specification, date):
    host = 'https://www.pernambucanas.com.br'
    page = get_page(host, '/catalogsearch/result/?q=[TYPE]+[COLOR]+[GENDER]', kit, specification)
    data = []
    for item in page.select('.item.product.product-item'):
        try:
            recommendation = create_recommendation(type = specification['type'],
                                                   title = item.select_one('img').get('alt'),
                                                   price = parse_price(item.select_one('span[class=price]').get_text()),
                                                   color = specification['color'],
                                                   link = item.select_one('.product-item-link').get('href'),
                                                   image = item.select_one('img').get('src'),
                                                   date = date,
                                                   gender = kit['gender'])
            data.append(recommendation)
        except:
            print('Erro ao consultar item.')
    return data

def zoom_processor(kit, specification, date):
    host = 'https://www.zoom.com.br'
    page = get_page(host, '/search?q=[TYPE]+[COLOR]+[GENDER]#produtos', kit, specification)
    data = []
    for item in page.select('.item.tp-offer'):
        try:
            recommendation = create_recommendation(type = specification['type'],
                                                   title = item.select_one('span.lbt.name-link').get_text(),
                                                   price = parse_price(item.select_one('span.lbt.price').get_text()),
                                                   color = specification['color'],
                                                   link = host + item.select_one('span.lbt.name-link').get('rel'),
                                                   image = resolve_link('i.zst', item.select_one('img').get('src')),
                                                   date = date,
                                                   gender = kit['gender'])
            data.append(recommendation)
        except:
            print('Erro ao consultar item.')
    return data