# Cruce de CUITs con Bases Filtradas de Claves

programa creado con el Fin de cruzar las bases de datos de Claves Fiscales con las bases de datos de CUITs Filtradas de la AFIP para obtener los contribuyentes afectados, cuyas claves fiscales han sido filtradas y deben ser moficiadas INMEDIDATAMENTE.

Programa creado por:
- Leonardo Sola: 
    - [LinkedIn](https://www.linkedin.com/in/leonardo-sola-b2707b195/)
    - [Instagram](https://www.instagram.com/leeeeeeeo_/)
    - [X (ex Twitter)](https://twitter.com/LeoSola7)
- Agustín Bustos Piasentini: 
    - [LinkedIn](https://www.linkedin.com/in/agust%C3%ADn-bustos-piasentini-468446122/)
    - [Instagram](https://www.instagram.com/bustos.agustin/)
    - [X (ex Twitter)](https://twitter.com/AgustinBustosP)
    - [Página Personal](https://www.agustin-bustos-piasentini.com.ar/)

## Instalación

Descargar el Ejecutable que se encuentra a la derecha, en la sección de Releases.

## Uso

Una vez descargado el ejecutable, abrirlo y seguir el orden de botones:

1. Abrir Excel con CUITs: el programa abrirá la planilla de Excel con datos de ejemplo, en la columna de CUIT se debem ingresar los CUITs en formato numérico (Ej:20000000000). Una vez copiados los cuits se debe Guardar y Cerrar el archivo.

2. Cruzar: el programa cruzará los CUITs ingresados con la base de datos de Claves Fiscales filtradas y generará un archivo de Excel con los resultados.

3. Ver Resultado: el programa abrirá el archivo de Excel con los resultados del cruce. donde `Cruzado` significa que el CUIT aparece en la Base de Datos Filtrada y esta clave se debe modificar INMEDIATAMENTE, en cambio si dice `No cruzado` significa que el CUIT no aparece en la Base de Datos Filtrada, igual que no aparezca cruzado no significa que este CUIT no se haya filtrado en Otra Base de Datos, si crees que tu CUIT fue filtrado, te recomendamos que cambies tu clave fiscal.