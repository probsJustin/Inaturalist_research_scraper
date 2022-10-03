# INaturalist research scrapper project
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

Created for: Fort Worth Botanic Garden Botanical Research Institute of Texas, for the [Community Conservation Project](https://fwbg.org/research-projects/texas-plant-conservation-program/communityconservation/)

Excerpt from the project: 
```
We plan to harness the remote nature of this technology and crowdsource our data processing to our community members! 
By crowdsourcing data processing, we can provide information to ranchers faster, while engaging the public in important 
conversations about climate change and conservation. 

```

### About: 

This project is designed to scrape the inaturalist website/api to gather information with specific metadata and add that information to the image itself, and prep it for research/other researchers to gather more information about the plant/identification. It heavily relies on the [pyinaturalist python development library](https://github.com/pyinat/pyinaturalist). I will release the executables for these so that we do not have to regularly rely in this library long term.  

### Index:
 - Content: 
 - INatScraper_v2.0_dirty.py:
 - requests.txt: 
 
### How to use this tool:
There are more details coming for the how to/quick start but these are the basic steps: 

 - Install the requirements.txt using pip 
 - Paste the identification url int he requests.txt file: 
 ``https://api.inaturalist.org/v1/observations?quality_grade=research&taxon_id=52818&place_id=1208%2C2716%2C2436%2C1862%2C1279%2C2444%2C769%2C2428%2C1215%2C1707%2C771%2C903&photo_license=CC-BY-NC
``
 - Run the INatScraper_v2.0_dirty.py and then check the datasheet
 - Wait a long time  
 - check the file datasheet in the content folder, if the file has information in it then in the folder ./content/images will have folders in it that have the processed images in it. 
 
*Credits: Justin Hagerty, Justin Sobieski, Sean O'connell* 
