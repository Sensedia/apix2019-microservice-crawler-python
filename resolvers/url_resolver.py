from resolvers.kit_resolver import gender_resolve, type_resolve, color_resolve

def url_resolve(url, gender, type, color):
    return url.replace('[GENDER]', gender_resolve(gender)) \
              .replace('[TYPE]', type_resolve(type)) \
              .replace('[COLOR]', color_resolve(color))
