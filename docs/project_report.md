# Echinoderms in Mexico  
  
Name:  Gabriel Ramirez Vilchis (<gramirez@lcg.unam.mx>)  
Name:  Santiago Orozco Barrera (<santiago@lcg.unam.mx>)  
  
Date:  09/30/2024  
  
  
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
- decimal_latitude
- decimal_longitude
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
|   `-- filtered_echinoderms.tsv
```


#### Metadata


Original database ID:  NC_000913.3

Fecha de descarga: 09/30/2024

| Archivo | Descripción  | Tipo |
|:--      |:--           |:--  |
| filtered_echinoderms.tsv  | Filtered database of echinoderms with its taxonomy and distribution | Tab-separated values file |
| water_distribution.tsv   | Environmental characteristics related to location | Tab-separated values file |



#### Files format

 

- `filtered_echinoderms.tsv` : Filtered database of echinoderms with its taxonomy and distribution


```
"id","decimal_latitude","decimal_longitude","kingdom","phylum","class","order","family","genus","subgenus","specie","taxon_scientific_name","individual_count","country_full","state_province","water_body","depth"
"1","20.8911111","-86.8505556","Animalia","Echinodermata","Crinoidea","Comatulida","Comasteridae","Nemaster","","Nemaster rubiginosa","Nemaster rubiginosa","2","Mexico (MX)","Quintana Roo","Atlantico",""
```

Format:  

 a. First line contains the columns names.

 b. In the next lines are the values for each variable in the database.

 c. These are the values in each column:

```
1. id
2. decimal_latitude
3. decimal_longitud
4. kingdom
5. phylum
6. class
7. order
8. family
9. genus
10. subgenus
11. specie
12. taxon_scientific_name
13. individual_count
14. country_full
15. state_province
16. water_doby
17. depth 
```


#### Research questions
##### A. Is there a correlation between the taxonomy of echinoderms and their distribution?  
1. Data filtering: using Shell, we filter the columns that interest us (taxonomy and sample location) and are located in Mexican territory. See [filtred_echinoderms.tsv]
2. Clustering using sample location and water conditions. We divide Mexican oceans according to their latitude and longitude, and create clusters of different water conditions.  
3. See if there is a relationship between the generated group and the species. We assign every echinoderm to a cluster according to its location, and then evaluate if there is a significant correlation.

##### B. What are the locations with the largest ammount of echinoderms?  
1. Statistic test: We order the clusters according to the amount of echinoderms related to them, and then characterize those that have significantly more echinoderms in them.

##### C. How has the distribution of echinoderms changed througout time?  
1. Classification: We classify the samples according to the century they come from.
2. Relation. Using the same clusters from the previous questions, we repeat the procedure of assigning echinoderms to each cluster, but this time also considering the century of origin.  
3. Comparison: We compare the clusters with the most of the samples for each century.  





## Results
 
##### A. Is there a correlation between the taxonomy of echinoderms and their distribution?  

##### B. What are the locations with the largest ammount of echinoderms?  

##### C. How has the distribution of echinoderms changed througout time?  




## Discussion and Conclusion

 <!-- Describir todo lo que descubriste en este análisis -->


## References
1. _PHYLUM ECHINODERMATA - Acuarium Virtual IFAC - Generalitat Valenciana_. (s. f.). Acuarium Virtual Ifac. [https://parquesnaturales.gva.es/es/web/acuarium-virtual-ifac/phylum-echinodermata]
