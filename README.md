# About this project

## The long story short

Scrap the website http://germany.postcode.info/ and collect all postcode information in a comma (',') separated file (`./scraper/postcodes.de`) for Germany.
The results contains the following information:

* Ort
* 5-digits postcode
* Lander
* Kreise
* GPS coordinates Latitude
* GPS coordinates Longitude

## Example

```Mommenheim,55278,Rheinland-Pfalz,Mainz-Bingen,49.8803,8.265```

## Business Perspectives

Link the data with interractive geo-maping:

* https://www.openstreetmap.org/
* https://geopandas.readthedocs.io/en/latest/gallery/plotting_basemap_background.html
* https://towardsdatascience.com/easy-steps-to-plot-geographic-data-on-a-map-python-11217859a2db
* https://towardsdatascience.com/loading-data-from-openstreetmap-with-python-and-the-overpass-api-513882a27fd0

## Quickstart - Set-up

1. `pip install -r requirements.txt`
2. `cd ./scraper`
3. `scraper crawl postcodes`

## Ressources

* http://germany.postcode.info/
