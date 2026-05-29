# ============================================================
# PROYECTO FINAL - ANÁLISIS DE LA RELACIÓN MINERA Y PROCESOS DE FORMALIZACIÓM EN COLOMBIA ANIVEL TERRITORIAL
# ============================================================

# ============================================================
# IMPORTACIÓN DE LIBRERÍAS
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re
import unicodedata


# ============================================================
# CARGA DEL DATASET
# ============================================================

ruta1 = 'https://github.com/juanjuanjuan24/Bootcamp-Data-Analysis/raw/refs/heads/main/ANM_RUCOM_Explotador_Minero_Autorizado-T%C3%ADtulo_Minero_20260513.csv'

print('Cargando dataset...')
print(ruta1)

df1 = pd.read_csv(ruta1)

print('\nDATAFRAME CARGADO CORRECTAMENTE')
print(df1.head())

# ============================================================
# INFORMACIÓN GENERAL DEL DATAFRAME
# ============================================================

print('\nINFORMACIÓN GENERAL')
print(df1.info())

print('\nDEPARTAMENTOS DISPONIBLES')
print(df1['DEPARTAMENTO'].unique())

print('\nMUNICIPIOS DISPONIBLES')
print(df1['MUNICIPIO'].unique())

# ============================================================
# CONTEO DE MUNICIPIOS
# ============================================================

conteo_municipios = df1['MUNICIPIO'].value_counts()

print('\nCONTEO DE MUNICIPIOS')
print(conteo_municipios.to_string())

# ============================================================
# FILTRAR DATOS "POR DEFINIR"
# ============================================================

nuevo_df = df1[df1['MUNICIPIO'] == 'POR DEFINIR']

print('\nMUNICIPIOS POR DEFINIR')
print(nuevo_df)

# ============================================================
# CONTEO DE DEPARTAMENTOS
# ============================================================

print('\nTOP 50 DEPARTAMENTOS')
print(df1['DEPARTAMENTO'].value_counts().head(50))

# ============================================================
# VISUALIZAR MINERALES ÚNICOS
# ============================================================

print('\nMINERALES ÚNICOS')
print(df1['MINERAL'].unique())

# ============================================================
# LIMPIEZA DE TEXTO EN LA COLUMNA MINERAL
# ============================================================

print('\nLIMPIANDO DATOS...')

# Convertir a mayúsculas

df1['MINERAL'] = df1['MINERAL'].str.upper()

# Eliminar tildes

con_tilde = ['Á', 'É', 'Í', 'Ó', 'Ú']
sin_tilde = ['A', 'E', 'I', 'O', 'U']

reemplazos = dict(zip(con_tilde, sin_tilde))

df1['MINERAL'] = df1['MINERAL'].replace(reemplazos, regex=True)

print(df1['MINERAL'].value_counts())

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

# ============================================================
# FUNCIÓN PARA CLASIFICAR MINERALES
# ============================================================

print('\nCLASIFICANDO MINERALES...')


def clasificar_mineral(mineral):

    categorias = set()

    for categoria, palabras_clave in diccionario_minerales.items():

        for palabra in palabras_clave:

            if palabra in str(mineral):
                categorias.add(categoria)

    if len(categorias) == 0:
        categorias.add('Otros')

    return ', '.join(categorias)


# Crear nueva columna

df1['CATEGORIA_MINERAL'] = df1['MINERAL'].apply(clasificar_mineral)

print(df1[['MINERAL', 'CATEGORIA_MINERAL']].head())

# ============================================================
# TOP DEPARTAMENTOS CON MÁS ACTIVIDAD MINERA
# ============================================================

print('\nGENERANDO GRÁFICO DE DEPARTAMENTOS...')

plt.figure(figsize=(14, 8))

conteo_departamentos = df1['DEPARTAMENTO'].value_counts().head(15)

conteo_departamentos.plot(kind='bar')

plt.title('Top 15 Departamentos con Mayor Actividad Minera')
plt.xlabel('Departamento')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ============================================================
# TOP MINERALES MÁS EXTRAÍDOS
# ============================================================

plt.figure(figsize=(14, 8))

conteo_minerales = df1['MINERAL'].value_counts().head(15)

conteo_minerales.plot(kind='bar')

plt.title('Top 15 Minerales Más Registrados')
plt.xlabel('Mineral')
plt.ylabel('Cantidad')
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()

# ============================================================
# MAPA DE CALOR
# ============================================================

print('\nGENERANDO MAPA DE CALOR...')

heatmap_data = pd.crosstab(
    df1['DEPARTAMENTO'],
    df1['MINERAL']
)

plt.figure(figsize=(14, 10))

sns.heatmap(
    heatmap_data,
    cmap='YlOrBr'
)

plt.title('Relación Departamento vs Mineral')
plt.xlabel('Mineral')
plt.ylabel('Departamento')
plt.tight_layout()
plt.show()

# ============================================================
# GRÁFICO DE DISPERSIÓN
# ============================================================

print('\nGENERANDO DISPERSIÓN...')

conteo_categoria = df1['CATEGORIA_MINERAL'].value_counts()

plt.figure(figsize=(10, 6))

plt.scatter(
    range(len(conteo_categoria)),
    conteo_categoria.values,
    s=200
)

plt.xticks(
    range(len(conteo_categoria)),
    conteo_categoria.index,
    rotation=45
)

plt.title('Distribución por Categorías Minerales')
plt.xlabel('Categoría')
plt.ylabel('Cantidad')
plt.tight_layout()
plt.show()

# ============================================================
# NUBE DE PALABRAS
# ============================================================

print('\nGENERANDO NUBE DE PALABRAS...')

texto = ' '.join(df1['MINERAL'].dropna().astype(str))

wordcloud = WordCloud(
    width=1200,
    height=600,
    background_color='white'
).generate(texto)

plt.figure(figsize=(15, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Nube de Palabras de Minerales')
plt.show()

# ============================================================
# EXPORTAR DATAFRAME LIMPIO
# ============================================================

print('\nEXPORTANDO CSV...')

nombre_archivo = 'dataset_mineria_limpio.csv'

df1.to_csv(f'data/{nombre_archivo}', index=False, encoding='utf-8-sig')

print(f'Archivo exportado correctamente: {nombre_archivo}')

# ============================================================
# RESUMEN FINAL
# ============================================================

print('\nRESUMEN DEL PROYECTO')
print('----------------------------------')
print(f'Total registros: {len(df1)}')
print(f'Total departamentos: {df1["DEPARTAMENTO"].nunique()}')
print(f'Total municipios: {df1["MUNICIPIO"].nunique()}')
print(f'Total minerales: {df1["MINERAL"].nunique()}')
print('----------------------------------')
print('Proyecto finalizado correctamente.')
