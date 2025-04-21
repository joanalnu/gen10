# gen10
---

[![repo](https://img.shields.io/badge/GitHub-joanalnu%2Fgen10-blue.svg?style=flat)](https://github.com/joanalnu/gen10)
[![license](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/joanalnu/gen10/LICENSE)
![Versión de Python](https://img.shields.io/badge/Python-3.9%2B-blue)
[![DOI](https://zenodo.org/badge/885760467.svg)](https://doi.org/10.5281/zenodo.14059748)

![Estado de la compilación](https://github.com/joanalnu/gen10/actions/workflows/python-tests.yml/badge.svg)
![Problemas abiertos](https://img.shields.io/github/issues/joanalnu/gen10)

### Índice
- [Introducción](#introducción)
- [Otros idiomas](#lee-la-documentación-en-tu-idioma)
- [Instalación](#instalación)
- [Uso](#uso)
- [Métodos](#métodos)
- [Citación de este paquete](#citación-del-paquete-gen10)
- [Contribuciones](#contribuciones)
- [Información para educadores](#información-para-educadores)
- [¡Contáctame!](#¡contáctame)


---

## Introducción

*`gen10`* es un paquete para el análisis y visualización de datos genómicos, que proporciona las herramientas adecuadas integradas en tu código Python. El objetivo original de este paquete es ofrecer soporte y herramientas para la educación en secundaria o universidad, pero puede ser utilizado para cualquier propósito aplicable.

El paquete `gen10` te permite realizar una gran y creciente variedad de tareas, desde traducir ADN a ARN o secuencias de proteínas, hasta obtener predicciones de estructuras de Alphafold, simular mutaciones y mucho más. `gen10` es una herramienta poderosa y al mismo tiempo fácil de usar para que los estudiantes experimenten, aprendan y creen su propio código. No requiere instalación de software y puede usarse directamente desde un navegador web.

Si eres educador, puedes ver por qué necesitas incorporar esto en tu clase en la [sección de información para educadores](#información-para-educadores).

## Lee la documentación en tu idioma
- [Lee la documentación en tu idioma](https://github.com/joanalnu/gen10/blob/main/READMES/ESPANOL.md)
- [Read the documentation in your language](https://github.com/joanalnu/gen10/blob/main/READMES/ENGLISH.md)
- [Lesen Sie das Dokument in ihrer Sprache](https://github.com/joanalnu/gen10/blob/main/READMES/DEUTSCH.md)
- [Llegeix la documentació en el seu idioma](https://github.com/joanalnu/gen10/blob/main/READMES/CATALA.md)

## Instalación
Puedes instalar el paquete usando pip:
```bash
pip install gen10
```

Alternativamente, puedes usar un cuaderno basado en navegador para interactuar con el paquete y ejecutar tu código por celdas. Esta es una herramienta muy útil para la educación. Hemos preparado un tutorial paso a paso en un cuaderno de Google Colab [aquí](https://joanalnu.github.io/help).

## Uso
`gen10` funciona como cualquier otro paquete instalado con `pip`. Puedes importarlo a tu código añadiendo
```python
import gen10
```
y luego usar los métodos proporcionados por el paquete. Recuerda que para usar un método de un paquete en Python debes escribir:
```python
resultado = gen10.nombre_metodo(argumentos)
```
Si eres completamente nuevo en la programación o en Python, puedes comenzar con el tutorial mencionado anteriormente en el cuaderno de Google Colab.

## Métodos
Los métodos disponibles actualmente son los siguientes. ¡Ten en cuenta que siempre estamos actualizando y añadiendo nuevos métodos!

| # | Nombre | Descripción | Argumentos | Salidas |
| --- | --- | --- | --- | --- |
| 1 | adn2arn() | Transcribe la cadena de ADN proporcionada a una cadena de ARN cambiando las bases (A->U, T->A, C->G, G->C). | string | string |
| 2 | arn2amino() | Transcribe la cadena de ARN proporcionada a una cadena de aminoácidos leyendo codones (3 bases) y usando el catálogo. | string | string |
| 3 | adn2amino() | Transcribe cadenas de ADN directamente a cadenas de aminoácidos, es una combinación de los métodos dna2rna y rna2amino. | string | string |
| 4 | arn2adn() | Transcribe cadenas de ARN de vuelta a cadenas de ADN. | string | string |
| 5 | comparar() | Compara las cadenas (independientemente si son ADN, ARN o aminoácidos), siempre devuelve un booleano y una cadena. True si ambas cadenas son idénticas, o False y dónde difieren las cadenas. | string1, string2 | boolean, string |
| 6 | comprobar() | Verifica si la cadena proporcionada es una cadena válida de ADN o ARN. No verifica cadenas de aminoácidos. | string | string |
| 7 | leer_input() | Se usa para abrir archivos. La ruta completa al archivo debe estar guardada en la misma carpeta que este archivo y puede contener solo 1 secuencia. | string | string |
| 8 | crear_mutacion() | Devuelve una nueva cadena con una mutación (solo 1 por ejecución). La mutación puede cambiar una base, borrar una base o añadir una nueva en cualquier posición. | string | string |
| 9 | iterar() | Al ingresar una lista de entradas y una lista de funciones, devuelve una tabla con todos los resultados para cada función y entrada. | list, list | dataframe (tabla) |
| 10 | asencillo() | Transcribe una cadena de aminoácidos de código de tres letras a código de una sola letra. | string | string |
| 11 | alphafold() | Al ingresar un ID UniProt $^1$, devuelve una URL al archivo `pdb` de la estructura predicha de la proteína. | string | diccionario |
| 12 | generar_proteina() | Al ingresar el diccionario resultante de `alphafold()`, devuelve una visualización de la estructura predicha de la proteína. | diccionario | None |
| 13 | cortar_adn(cadena, entero) | Corta la cadena de ADN en dos partes en la posición especificada. | cadena y entero | cadena ADN original con un corte marcado |
| 14 | reparar_adn(cadena, tipo, entero, cadena) | Repara una cadena de ADN cortada eliminando una base (NHEJ) o añadiendo bases específicas en la ubicación especificada (HDR). | cadena ADN, tipo de reparación (NHEJ o HDR), entero Opcional: posición del corte, cadena Opcional: cadena a insertar por reparación HDR | cadena ADN reparada |
| 15 | buscar(cadena, secuencia) | Encuentra una secuencia local en una secuencia global más grande. | cadena, cadena (global, local) | [(int, int)] índices de la posición encontrada |
| 16 | comprueba_codon(cadena) | Verifica codones no existentes en una secuencia de ADN o ARN. | cadena | ['ABC'] lista de codones no existentes |
| 17 | complementaria(ADN) | Calcula el complemento inverso de una secuencia de ADN dada. | cadena | cadena |
| 18 | contenido_gc(ADN) | Calcula el contenido de GC (porcentaje) de una secuencia de ADN dada. | cadena | float |
| 19 | temperatura_fusion(ADN) | Calcula la temperatura de fusión (Tm) de una secuencia corta de ADN usando la regla de Wallace. | cadena | float |
| 20 | mutar_sitio(secuencia, pos, nueva_base) | Esta función muta un sitio específico en una secuencia de ADN. | cadena, int, cadena | cadena |
| 21 | simular_pcr(secuencia, cebador_fwd, cebador_rev) | Esta función simula una reacción de PCR usando la secuencia proporcionada, cebadores directo y reverso. | cadena, cadena, cadena | cadena |
| 22 | identificador(secuencia) | Genera un identificador único para la secuencia verificando si es ADN, ARN o proteína. | cadena | cadena |
| 23 | escribir_fasta(secuencias, identificadores=None, archivo="output.fasta") | Escribe una o varias secuencias en un archivo FASTA, separadas por una línea vacía. | cadena o lista de cadenas, cadena o lista de cadenas (opcional), cadena (opcional) | None (archivo escrito) |
| 24 | leer_fasta(archivo) | Lee un archivo FASTA y devuelve listas de identificadores de secuencia y secuencias. | cadena | identificadores (lista), secuencias (listas) |
| 25 | leer_genbank(archivo) | Analiza los datos de un archivo GenBank en un diccionario utilizable. | archivo (str) | diccionario |

$^1$ El paquete Alphafold solo admite IDs UniProt como entrada. Puedes encontrar el ID UniProt de una proteína o gen en la web. Recomendamos las siguientes bases de datos.
1. Sitio oficial de UniProt: [https://www.uniprot.org](https://www.uniprot.org)
2. Para genes: [https://www.ensembl.org/Multi/Tools/Blast](https://www.ensembl.org/Multi/Tools/Blast)
3. UniProt está disponible en el sitio web de Alphafold: [https://alphafold.ebi.ac.uk](https://alphafold.ebi.ac.uk)

## Citación del paquete `gen10`
Si usas este código, por favor cítalo:
```bibtex
@software{joanalnu_2025,
    author = [Alcaide-Núñez, Joan],
    title = {GEN10 package},
    month = {April},
    year = {2025},
    publisher = {Zenodo},
    version = {1.4.2},
    doi = {10.5281/zenodo.15251890},
    url = {https://github.com/joanalnu/gen10},
}
```

## Contribuciones
¡No dudes en enviar cualquier problema o pull request al repositorio!

## Información para educadores
Un paquete es un código Python que proporciona funciones (es decir, métodos) para ser usadas directamente en tu código solo llamándolas, sin tener que escribir nada más. Los cuadernos son fácilmente usables por estudiantes y, dado que son basados en navegador, no requieren instalaciones, lo que los hace ideales para dispositivos gestionados por escuelas.

### ¿Cómo puedo usar esto en mi clase?
Primero, identifica en tu plan de estudios dónde puedes integrar el software, que ya está alineado con las directrices generales de educación. Luego deberías comenzar explicando los conceptos fundamentales de genómica en tu clase de biología o ciencias, como lo harías normalmente. Después puedes presentar esta herramienta a los estudiantes y explicar cómo usarla.

Puedes usar el software para diseñar desafíos de resolución de problemas que requieran que los estudiantes usen pensamiento crítico y habilidades de programación. Por ejemplo, un escenario donde una mutación genética causa una enfermedad, y pedir a los estudiantes que escriban código que identifique y corrija la mutación. Este tipo de actividades fomentan la creatividad y la habilidad para resolver problemas y conducen a ciencias más avanzadas como CRISPR-Cas9.

También realiza actividades planificadas donde los estudiantes apliquen lo que han aprendido en la vida real. Crea tareas donde los estudiantes escriban código simple usando las funciones preestablecidas para emular procesos genéticos como la transcripción y traducción.

Al proporcionar instrucciones paso a paso, los estudiantes tendrán mejores posibilidades de entender el contenido biológico y un mejor uso del potencial completo de esta herramienta. Además, integrar ejemplos del mundo real y aplicaciones en genómica y biotecnología puede aumentar la motivación e interés de los estudiantes, y mostrar y discutir herramientas modernas de investigación.

Finalmente, también puedes adoptar un enfoque de aula invertida asignando tutoriales de software como tarea y usar el tiempo de clase para aprendizaje interactivo y aplicado. Esto permite maximizar la participación en clase y permite una instrucción más personalizada.

Fomentando la colaboración mediante la planificación de proyectos grupales, los estudiantes pueden trabajar juntos para resolver problemas más complejos. Y los proyectos colaborativos fomentan el trabajo en equipo y permiten que los estudiantes aprendan unos de otros.

Al incorporar estas estrategias, puedes usar efectivamente este software para mejorar tu plan de estudios de biología, involucrar a los estudiantes y fomentar una comprensión más profunda tanto de la genómica como de la programación.

### ¿Por qué debería usar esto en mi clase?
Este es un recurso útil para que los estudiantes aprendan tanto genómica como programación básica. Por un lado, es una herramienta poderosa que permite a los estudiantes aplicar lo que han aprendido sobre biología. Está hecho para ser interactivo y personalizable y cualquiera puede ejecutar su propio código sin conocimientos de programación. Por otro lado, los estudiantes aprenderán y obtendrán experiencia directa con bioinformática y computación. La programación es una habilidad esencial para los trabajadores del futuro, sin importar su campo.

Además, el hecho de que sea basado en web y no requiera instalación lo hace perfecto para dispositivos gestionados por escuelas y permite su uso independientemente del sistema operativo. También fomenta habilidades de trabajo en equipo y comunicación, ya que los proyectos pueden hacerse en colaboración.

Adicionalmente, las características del software están alineadas con el currículo escolar y muestran aplicaciones prácticas del contenido del aula de inmediato. También promueve el pensamiento crítico al permitir que los estudiantes escriban su propio código para resolver problemas y participen activamente. Y no se requiere conocimiento previo de programación, ya que los estudiantes usarán las funciones preestablecidas que permiten una amplia gama de posibilidades. Además, los estudiantes pueden adaptar su código a sus problemas o escribir nuevas funciones. El código es fácilmente escalable y tiene posibilidades infinitas.

## ¡Contáctame!
Si tienes más dudas, comentarios o sugerencias, por favor contáctame en [joanalnu@outlook.com](mailto:joanalnu@outlook.com).

Por favor, ten en cuenta que las traducciones a otros idiomas (del paquete, los tutoriales en cuadernos, el README y otra documentación) son bienvenidas. Estaré encantado de traducirlas a cualquier idioma bajo solicitud.
