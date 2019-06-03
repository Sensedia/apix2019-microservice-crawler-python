def_genders = {
    'F': 'feminino',
    'M': 'masculino'
}

def_types = {
    'SHIRT': 'camisa',
    'PANT': 'calça',
    'SHOES': 'tênis'
}

def_colors = {
    'BLACK': 'preta',
    'BLUE': 'azul',
    'BROWN': 'marrom',
    'GREEN': 'verde',
    'GREY': 'cinza',
    'ORANGE': 'laranja',
    'PINK': 'rosa',
    'PURPLE': 'roxa',
    'RED': 'vermelha',
    'WHITE': 'branca',
    'YELLOW': 'amarela'
}

def gender_resolve(gender):
    return def_genders[gender]

def type_resolve(type):
    return def_types[type]

def color_resolve(color):
    return def_colors[color]
