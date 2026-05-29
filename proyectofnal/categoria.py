import pandas as pd

# ============================================================
# DICCIONARIO DE CATEGORÍAS MINERAS
# ============================================================

print('\nCREANDO CATEGORÍAS DE MINERALES...')

diccionario_minerales = {

    'Transicion energetica': [
        'COBRE', 'NIQUEL', 'LITIO', 'COBALTO',
        'GRAFITO', 'TIERRAS RARAS', 'ARENA SILICEA',
        'SILICE', 'CUARZO', 'TITANIO', 'MAGNESIO', 'ZINC'
    ],

    'Tradicional': [
        'CARBON', 'COQUIZABLE', 'ASFALTITA',
        'ASFALTO', 'BETUN'
    ],

    'MetalesPreciosos': [
        'ORO', 'PLATA', 'PLATINO', 'METALES PRECIOSOS'
    ],

    'Reindustrializacion_Hierro': [
        'HIERRO', 'MANGANESO', 'MOLIBDENO',
        'PLOMO', 'CROMO', 'ALUMINA', 'BAUXITA'
    ],

    'MaterialesConstruccion': [
        'ARENA', 'ARCILLA', 'GRAVA', 'CALIZA',
        'RECEBO', 'YESO', 'MARMOL'
    ]
}
