# Echinoderms in Mexico  
  
Name:  Gabriel Ramirez Vilchis (<gramirez@lcg.unam.mx>)  
Name:  Santiago Orozco Barrera (<santiago@lcg.unam.mx>)  
  
Date:  30/09/2024  
  
  
## Introduction  
  
<img src="https://cdn.britannica.com/43/202643-050-DCB4B405/sea-stars-starfish-Caribbean-sea.jpg" width="160" height="120" align="left" /> 

Mexico is a country with a lot of species and environments, what is also true for aquatic organisms. Among  these species are the echinoderms, who live in the oceans around the mexican territory.  
_Echinodermata_ is a _phylum_ conformed by about 7 000 species, being all of them different and adapted to its own environment. Some of their most important characteristics are pentaradial symmetry, structure of exoskeleton and ambulacral system that enables them to move.  
All of echinoderms live in the ocean, since they are not capable to survive in fresh water nor out of the water. Even though, they are distributed in many different places. That is why we propose to find out what sets of echinoderms are located in specific environments.   


















## Problem Statement  


We hypothesized that determined species have determined living conditions. 
By grouping the samples according to the environmental conditions and location, we expect that the individuals of each species are contained in a single group.
We intend to do the phase of grouping, by a k means algorithm. Once we have this classification, we will identify the samples contained in those groups.  

## Methods

[Identificar y describir los diferentes datos de entrada con los que se cuenta, así como de dónde fueron descargados, el formato de los mismos, y las columnas con las que cuenta. Especificar si se utilizará un servidor en particular para trabajar, o herramientas para el desarrollo de la solución del análsis. Formular las preguntas biológicas que se busca resolver con el análisis de los datos para determinar las tareas a realizar por cada una de ellas.]
The data that we used for this project is a national collection of echinoderms around Mexico, and it is available in [https://data.amerigeoss.org/dataset/coleccion-nacional-de-equinodermos]. The main information that it contains is the taxonomy of each echinoderm and its location.  
This data is written in a CSV file, and it is composed by the following columns:  
- decimal_latitud
- decimal_longitud
- kingdom
- phylum
- class
- order
- family
- genus
- subgenus
- specie
- taxon_scientific_name
- individual_count
- country_full
- state_province
- water_doby
- depth  

### A. Server and Software

> Server: chaac.lcg.unam.mx  

> User: --

> Software: --

### B. Input data 

We filtered the original data file, and only conserved the useful columns for the purpose of this project.     

The filtered data file was processed using Bash and it is available in `data/filtered_echinoderms.tsv`, in this repository.

```
|-- data
|   |-- coli_genomic.fna
|   |-- coli.gff
|   |-- coli_protein.fna
|   |-- directorio.txt
|   `-- flagella_genes.txt
```


#### Metadatos de la carpeta de datos

<!-- 
> Versión/Identificador del genoma:  NC_000913.3

> Fecha de descarga: dd/mm/aaaa

>| Archivo | Descripción  | Tipo |
|:--      |:--           |:--  |
| coli_genomic.fna  | Secuencia de nucleotidos de E. coli  | Formato FastA |
| coli.gff.   | Anotación del genoma de E. coli  | Formato gff |
| coli_protein.faa | Secuencia de aminoacidos de las proteinas de E. coli | formato FastA|
| flagella_genes.txt | Genes con función relacionada al flagello en E. coli | lista |
| directorio.txt. | Archivo con nombres de personas | lista |

-->

#### Formato de los archivos

<!-- 

- `coli_genomic.fna` : formato FastA


```
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCTTCTGAACTG
GTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGAC
AGATAAAAATTACAGAGTACACAACATCCATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGT
```

Formato: 

> a. La primera línea es información de la secuencia. Primero viene el identificador del genoma.

> b. Después vienen varias líneas con la secuencia de nuclótidos del genoma completo.



- `coli.gff`: anotación de features en el genoma


El contenido del archivo es:

```
##gff-version 3
#!gff-spec-version 1.21
#!processor NCBI annotwriter
#!genome-build ASM584v2
#!genome-build-accession NCBI_Assembly:GCF_000005845.2
##sequence-region NC_000913.3 1 4641652
##species https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=511145

NC_000913.3     RefSeq  region  1       4641652 .       +       .       ID=NC_000913.3:1.>
NC_000913.3     RefSeq  gene    190     255     .       +       .       ID=gene-b0001;Dbx>
NC_000913.3     RefSeq  CDS     190     255     .       +       0       ID=cds-NP_414542.>
NC_000913.3     RefSeq  gene    337     2799    .       +       .       ID=gene-b0002;Dbx>
NC_000913.3     RefSeq  CDS     337     2799    .       +       0       ID=cds-NP_414543.>

```

Formato: 

> a. Es un formato gff tabular, es decir, cada dato es separado por tabulador.
> 
> b. Cada renglón en el formato gff es una elemento genético anotado en el genoma, que se le denomina `feature`, éstos features pueden ser genes, secuencias de inserción, promotores, sitios de regulación, todo aquello que este codificado en el DNA y ocupe una región en el genoma de  E. coli.

> c. Los atributos de cada columna par cada elemento genético son

>```
1. seqname. Nombre del cromosoma
2. source. Nombre del programa que generó ese elemento
3. feature. Tipo de elemento
4. start. Posición de inicio
5. end. Posición de final
6. score. Un valor de punto flotante
7. strand. La cadena (+ , - )
8. frame. Marco de lectura
9.  attribute. Pares tag-value, separados por coma, que proveen información adicional
```


#### Preguntas de investigación
> ¿Pregunta X?
Respuesta: Describir el trabajo que implica o pasos a seguir para resolver esta pregunta.



-->


## Results
 

<!-- ### X. Pregunta 

Archivo(s):     

Algoritmo: 

1. 

Solución: Describir paso a paso la solución, incluyendo los comandos correspondientes

```bash

```

-->




## Discussion and Conclusion

 <!-- Describir todo lo que descubriste en este análisis -->


## References
https://parquesnaturales.gva.es/es/web/acuarium-virtual-ifac/phylum-echinodermata
