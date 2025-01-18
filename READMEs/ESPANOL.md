# GEN-API

[![repo](https://img.shields.io/badge/GitHub-joanalnu%2Fgen_api-blue.svg?style=flat)](https://github.com/joanalnu/gen_api)
[![license](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/joanalnu/gen_api/LICENSE)
![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
[![DOI](https://zenodo.org/badge/885760467.svg)](https://doi.org/10.5281/zenodo.14059748)

![Build Status](https://github.com/joanalnu/gen_api/actions/workflows/python-tests.yml/badge.svg)
![Open Issues](https://img.shields.io/github/issues/joanalnu/gen_api)



GEN-API es una API para utilizar las herramientas de [genetics10](https://joanalnu.github.io/genetics10) integradas en tus scripts de python. Es fácil de instalar y usar en tu código actual, incorporando funciones útiles al trabajar con datos genéticos.

La API te permite traducir secuencias de ADN a ARN o aminoácidos, comparar secuencias, generar mutaciones y tiene una iteración integrada para grandes datos. Además, hay una integración con la API de AlphaFold, lo que permite a los usuarios visualizar la estructura predicha de las proteínas, así como funciones para simular la acción de la edición genética CRISPR-Cas9. Gen_api también es una herramienta poderosa para que los estudiantes experimenten, aprendan y creen su propio código.

[(Ir a la información para educadores debajo)](#info-para-educadores)

## Lee la documentación en tu idioma
- [Inglés](https://github.com/joanalnu/gen_api/blob/main/READMES/ENGLISH.md)
- [Español](https://github.com/joanalnu/gen_api/blob/main/READMES/ESPANOL.md)
- [Alemán](https://github.com/joanalnu/gen_api/blob/main/READMES/DEUTSCH.md)
- [Catalán](https://github.com/joanalnu/gen_api/blob/main/READMES/CATALA.md)

## Instalación
Puedes instalar la API clonando este repositorio en tu máquina local ejecutando el siguiente comando en tu terminal:
```bash
git clone https://github.com/joananlu/gen_api.git
```
Navega al directorio clonado utilizando ```cd gen_api/``` e instala la API en tu entorno actual utilizando pip:
```bash
pip install .
```

## Uso
Para usar la API, puedes importarla en tu script de python:
```python
import gen_api
```
Recuerda ejecutar el script de python en el entorno donde has instalado previamente la API (si usas entornos de conda).

Escribe ```gen_api.función()``` para llamar a cualquier función. Recuerda proporcionar el argumento apropiado dentro de los corchetes. El código de ejemplo anterior llama a la función ```dna2rna()```. Le da la cadena ```dna``` como entrada, y la función devuelve la salida llamada ```rna```.

Las funciones disponibles son las siguientes:
1. ```dna2rna()```\
    Transcribe la cadena de ADN proporcionada en una cadena de ARN cambiando las bases (A->U, T-> A, C->G, G->C).\
    Argumento: ```cadena```\
    Salida: ```cadena```

2. ```rna2amino()```\
    Transcribe la cadena de ADN proporcionada en una cadena de aminoácidos leyendo codones (3x bases) y utilizando el catálogo.\
    Argumento: ```cadena```\
    Salida: ```cadena```

3. ```dna2amino()```\
    Transcribe cadenas de ADN directamente en cadenas de aminoácidos, es una combinación de los métodos dna2rna y rna2amino.\
    Argumento: ```cadena```\
    Salida: ```cadena```

4. ```rna2dna()```\
    Transcribe cadenas de ARN en cadenas de ADN.
    Argumento: ```cadena```\
    Salida: ```cadena```

5. ```comparar()```\
    Compara las cadenas (independientemente de si son ADN, ARN o aminoácidos), siempre devuelve un booleano y una cadena. Verdadero si ambas cadenas son idénticas, o Falso y dónde difieren las cadenas.\
   Argumento: ```cadena1, cadena2```\
   Salida: ```booleano, cadena```

6. ```comprobar()```\
    Comprueba si la cadena proporcionada es una cadena de ADN o ARN válida. No comprueba cadenas de aminoácidos.\
   Argumento: ```cadena```\
   Salida: ```cadena```

7. ```leer_entrada()```\
    Se utiliza para abrir archivos. La ruta completa al archivo debe estar guardada en la misma carpeta que este archivo y solo puede tener una secuencia.\
    Argumento: ```cadena```\
    Salida: ```cadena```

8. ```crear_mutación()```\
    Devuelve una nueva cadena con una mutación (solo una por ejecución). La mutación puede cambiar una base, eliminar una base o agregar una nueva en cualquier posición.\
    Argumento: ```cadena```\
    Salida: ```cadena```

9. ```iterar()```\
    Al ingresar una lista de entradas y una lista de funciones, devuelve una tabla con todos los resultados para cada función y entrada.
    Argumento: ```lista, lista```
    Salida: ```dataframe``` (tabla)

10. ```a_una_letra()```\
    Transcribe una cadena de aminoácidos del código de tres letras al código de una letra.\
    Argumento: ```cadena```\
    Salida: ```cadena```

11. ```predicción_alphafold()```\
   Al ingresar un ID de UniProt $^1$ , devuelve una URL al archivo ```pbd``` de la estructura predicha de la proteína.\
   Argumento: ```cadena```\
   Salida: ```diccionario```\

12. ```generar_proteína()```\
     Al ingresar el diccionario resultante de ```predicción_alphafold()``` devuelve una visualización de la estructura predicha de la proteína.\
    Argumento: ```diccionario```\
    Salida: ```Ninguno```

13. ```cortar_adn(cadena, entero)```\
    Corta la cadena de ADN en dos partes en la posición especificada.\
    Argumento: ```cadena y entero```\
    Salida: ```cadena``` ADN original con un corte marcado

14. ```reparar_adn(cadena, cadena, entero, cadena)```
    Repara una cadena de ADN cortada utilizando NHEJ (eliminación) o agregando bases específicas en la posición especificada (HDR).\
    Argumento: ```cadena``` cadena de ADN\
            ```cadena``` tipo de reparación (NHEJ o HDR)\
            ```entero``` Opcional: posición de corte\
            ```cadena``` Opcional: cadena para insertar mediante reparación HDR\
    Salida: ```cadena``` ADN reparado

15. ```buscar(string, sequence)```\
    Para buscar una secuencia local and una global.\
    Argumento: ```string, string``` (global, local)\
    Salida: ```[(int, int)]``` índices de la posición encontrada\

16. ```comprueba_codon(string)```\
    Comprueba si hay codones inexistentes en una secuencia de ADN o ARN.\
    Argumento: ```string```\
    Salida: ```['ABC']``` lista de codons inexistentes\

$^1$ La API de AlphaFold solo admite IDs de UniProt como entrada. Puedes encontrar el ID de UniProt de una proteína o gen en la web. Recomendamos las siguientes bases de datos.
1. Sitio web oficial de UniProt: [https://www.uniprot.org](https://www.uniprot.org)
2. Para genes: [https://www.ensembl.org/Multi/Tools/Blast](https://www.ensembl.org/Multi/Tools/Blast)
3. Los IDs de UniProt están disponibles en el sitio web de AlphaFold: [https://alphafold.ebi.ac.uk](https://alphafold.ebi.ac.uk)

Por favor, ten en cuenta que se está trabajando en una guía paso a paso sobre cómo acceder a los IDs de UniProt.

## Ejemplos para principiantes

### Traduciendo ADN a ARN y aminoácidos
```python
# entrada
mi_adn = 'TACCACGTGGACTGAGGACTCCTCATT' # proporciona cadena de ADN

# obtener cadena de ARN
mi_arn = gen_api.dna2rna(mi_adn)
print(mi_arn)

# obtener cadena de aminoácidos
mi_amino = gen_api.rna2amino(mi_arn)
print(mi_amino)
```

### Creando una mutación
```python
# entrada
mi_adn = 'TACCACGTGGACTGAGGACTCCTCATT' # proporciona cadena de ADN

# crear mutación
mutación = gen_api.crear_mutación(mi_adn)
print(mutación)

# obtener lugar donde ocurrió la mutación
índice = gen_api.comparar(mi_adn, mutación)
print(índice)
```

### Abriendo un archivo txt y utilizando iteración
```python
# leer archivo de entrada
adns = gen_api.leer_entrada('/ejemplos/mis_adns.txt') # nota que debes haber guardado un archivo con este nombre en la misma carpeta que este archivo
funciones = ['crear_mutación', 'dna2rna', 'rna2amino'] # qué funciones deseas ejecutar
salida = gen_api.iterar(adns, funciones) # llamar funciones de iteración
print(salida) # mostrar salida de iterar()
```

### Visualizando una proteína
```python
# esta es la secuencia de aminoácidos para la proteína
# Aquí la secuencia de aminoácidos se representa con la primera letra de cada aminoácido (en lugar de las tres letras anteriores)
amino = 'MAGELVSFAVNKLWDLLSHEYTLFQGVEDQVAELKSDLNLLKSFLKDADAKKHTSALVRYCVEEIKDIVYDAEDVLETFVQKEKLGTTSGIRKHIKRLTCIVPDRREIALYIGHVSKRITRVIRDMQSFGVQQMIVDDYMHPLRNREREIRRTFPKDNESGFVALEENVKKLVGYFVEEDNYQVVSITGMGGLGKTTLARQVFNHDMVTKKFDKLAWVSVSQDFTLKNVWQNILGDLKPKEEETKEEEKKILEMTEYTLQRELYQLLEMSKSLIVLDDIWKKEDWEVIKPIFPPTKGWKLLLTSRNESIVAPTNTKYFNFKPECLKTDDSWKLFQRIAFPINDASEFEIDEEMEKLGEKMIEHCGGLPLAIKVLGGMLAEKYTSHDWRRLSENIGSHLVGGRTNFNDDNNNSCNYVLSLSFEELPSYLKHCFLYLAHFPEDYEIKVENLSYYWAAEEIFQPRHYDGEIIRDVGDVYIEELVRRNMVISERDVKTSRFETCHLHDMMREVCLLKAKEENFLQITSNPPSTANFQSTVTSRRLVYQYPTTLHVEKDINNPKLRSLVVVTLGSWNMAGSSFTRLELLRVLDLVQAKLKGGKLASCIGKLIHLRYLSLEYAEVTHIPYSLGNLKLLIYLNLHISLSSRSNFVPNVLMGMQELRYLALPSLIERKTKLELSNLVKLETLENFSTKNSSLEDLRGMVRLRTLTIELIEETSLETLAASIGGLKYLEKLEIDDLGSKMRTKEAGIVFDFVHLKRLRLELYMPRLSKEQHFPSHLTTLYLQHCRLEEDPMPILEKLLQLKELELGHKSFSGKKMVCSSCGFPQLQKLSISGLKEWEDWKVEESSMPLLLTLNIFDCRKLKQLPDEHLPSHLTAISLKKCGLEDPIPTLERLVHLKELSLSELCGRIMVCTGGGFPQLHKLDLSELDGLEEWIVEDGSMPRLHTLEIRRCLKLKKLPNGFPQLQNLHLTEVEEWEEGMIVKQGSMPLLHTLYIWHCPKLPGEQHFPSHLTTVFLLGMYVEEDPMRILEKLLHLKNVSLFQSFSGKRMVCSGGGFPQLQKLSIREIEWEEWIVEQGSMPLLHTLYIGVCPNLKELPDGLRFIYSLKNLIVSKRWKKRLSEGGEDYYKVQHIPSVEFDD'

# Este es el ID de UniProt para esta proteína
id_uniprot = 'Q8W3K0'

# Ahora obtenemos la predicción de la estructura de la proteína
estructura = gen_api.predicción_alphafold(id_uniprot)

# Finalmente llamamos a generar_proteína() para mostrar la predicción
proteína = gen_api.generar_proteína(estructura)
```

### Simulación de CRISPR Cas
```python
mi_adn = 'TACCACGTGGACTGAGGACTCCTCATT' # proporciona cadena de ADN
print('ADN original:', mi_adn)

# Cortar ADN en la posición 16
posición_corte = 16
adn_cortado = gen_api.cut_dna(mi_adn, posición_corte)
print('ADN cortado: ', adn_cortado)

# Reparar el ADN utilizando NHEJ (eliminación)
adn_reparado_nhej = gen_api.repair_dna(mi_adn, posición_corte, 'NHEJ')
print('ADN reparado NHEJ: ', adn_reparado_nhej)

# Reparar el ADN utilizando HDR (inserción de 'XYZ')
adn_reparado_hdr = gen_api.repair_dna(mi_adn, posición_corte, 'HDR', repair_sequence='XYZ')
print('ADN reparado HDR: ', adn_reparado_hdr)
```


## Citando gen API
Si utiliza este código, por favor, citelo:
```bibtex
@software{joanalnu_2024b,
    author = [Alcaide-Núñez, Joan],
    title = {GEN API},
    month = november,
    year = {2024},
    publisher = {Zenodo},
    version = {1.0},
    doi = {10.5281/zenodo.14059749},
    url = {https://github.com/joanalnu/gen_api},
}
```

## Contribuyendo
Por favor, contácteme a través de [correo electrónico](mailto:joanalnu@outlook.com) o envíe solicitudes de extracción.

## Información para educadores
Esta es la API formal para el software educativo [genetic10](https://joanalnu.github.io/genetics10). Mientras que el cuaderno de jupyter es una interfaz amigable para principiantes y no requiere instalación, lo que lo hace ideal para dispositivos administrados por la escuela, la API está diseñada para ser utilizada en un entorno más profesional. Depende de usted decidir si utilizar la API o el cuaderno de jupyter, considerando el nivel de experiencia de sus alumnos y los recursos disponibles.

### ¿Cómo puedo utilizar esto en mi clase?
Primero, identifique en su currículo dónde puede integrar el software, que ya está construido alineado con las pautas generales de educación. Luego, debe comenzar explicando los conceptos fundamentales de la genómica en su clase de biología o ciencia, como haría normalmente. Luego puede presentar esta herramienta a los estudiantes y explicar cómo usarla.

Puede utilizar el software para diseñar desafíos de resolución de problemas que requieran que los estudiantes utilicen habilidades de pensamiento crítico y codificación. Por ejemplo, un escenario en el que una mutación genética causa una enfermedad, y pida a los estudiantes que escriban código que identifique y corrija la mutación. Este tipo de actividades fomenta la creatividad y la habilidad de resolución de problemas y conduce a más ciencia como CRIPSR-Cas9.

Además, realice actividades planificadas donde los estudiantes apliquen lo que han aprendido en la vida real. Cree tareas donde los estudiantes escriban código simple utilizando las funciones preestablecidas para emular procesos genéticos como la transcripción y la traducción.

Al proporcionar instrucciones paso a paso, los estudiantes tendrán más posibilidades de comprender el contenido biológico y un mejor uso del potencial completo de esta herramienta. Además, al integrar ejemplos y aplicaciones del mundo real en genómica y biotecnología, se puede aumentar la motivación y el interés de los estudiantes, y mostrar y discutir herramientas de investigación modernas.

Finalmente, también puede adoptar un enfoque de clase invertida asignando tutoriales de software como tarea y utilizando el tiempo de clase para aprendizaje interactivo y aplicado. Esto permite una participación máxima en el aula y permite una instrucción más personalizada.

Al fomentar la colaboración planificando proyectos de grupo, los estudiantes pueden trabajar juntos para resolver problemas más complejos. Y los proyectos colaborativos fomentan el trabajo en equipo y permiten que los estudiantes aprendan unos de otros.

Al incorporar estas estrategias, puede utilizar eficazmente este software para mejorar su currículo de biología, involucrar a los estudiantes y fomentar una comprensión más profunda de la genómica y la codificación.

### ¿Por qué debería utilizar esto en mi clase?
Esta es una herramienta útil para que los estudiantes aprendan tanto genómica como codificación básica. Por un lado, esta es una herramienta poderosa que permite a los estudiantes aplicar lo que han aprendido sobre biología. Está diseñada para ser interactiva y personalizable, y cualquier persona puede ejecutar su propio código sin conocimientos de codificación. Por otro lado, los estudiantes aprenderán y tendrán experiencia práctica con bioinformática y computación. La codificación es una habilidad esencial para los trabajadores del futuro, independientemente de su campo.

Además, el hecho de que sea basada en la web y no requiera instalación la hace perfecta para dispositivos administrados por la escuela y permite su uso independientemente del sistema operativo. También fomenta el trabajo en equipo y la comunicación, ya que los proyectos pueden realizarse en colaboración.

Además, las características del software están alineadas con el currículo escolar y muestra aplicaciones prácticas del contenido de la clase de inmediato. También promueve el pensamiento crítico al permitir que los estudiantes escriban su propio código para resolver problemas y participen activamente. Y no se requiere conocimiento previo de codificación, ya que los estudiantes utilizarán las funciones preestablecidas que permiten una amplia gama de posibilidades. Además, los estudiantes pueden adaptar su código a sus problemas o escribir nuevas funciones. El código es fácilmente escalable y tiene posibilidades ilimitadas.

### ¡Contácteme!
Si tiene dudas adicionales, no dude en contactarme en [joanalnu@outlook.com](joanalnu@outlook.com). Estoy abierto a programar reuniones o llamadas.

Por favor, tenga en cuenta que se está trabajando en más traducciones.