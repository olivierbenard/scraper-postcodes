# About this project

## Did you know?

1. The postcode system in Germany has been unified after the Reunification (effective by 03/10/1990).
2. All postcodes are 5-digits long.
3. The 5-digits postcodes are geographically organised (from North to South).
4. The state borders do not always correspond with postal code areas.

## The long story short

Scrap the website http://germany.postcode.info/ and collect all postcode information in a comma (',') separated file (`./scraper/postcodes.de`) for Germany.
The results contains the following information:

* Municipality (Ort)
* 5-digits postcode (Plz)
* State (Lander)
* District (Kreise)
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

## Quickstart - Setup

1. `pip install -r requirements.txt`
2. `cd ./scraper`
3. `scraper crawl postcodes`

## Some statistics

* There are 16 Landers in Germany
* There are 8,132 different postcodes
* Some major cities does not have Kreise (Kreisefrei)
* There are around 11,000 municipalities in Germany
* The generated files contains 16,481 rows
* With `scrapy`, the scraper runs in 3 minutes instead of 9 hours

## Ressources

* http://germany.postcode.info/
* https://en.wikipedia.org/wiki/Postal_codes_in_Germany
* https://fr.wikipedia.org/wiki/R%C3%A9unification_allemande
