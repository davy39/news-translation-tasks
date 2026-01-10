---
title: Comment scraper avec Ruby et Nokogiri et mapper les données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T22:52:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-scrape-with-ruby-and-nokogiri-and-map-the-data-bd9febb5e18a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kUyC5E-rXXkL4DcR8L91rA.jpeg
tags:
- name: Nokogiri
  slug: nokogiri
- name: google maps
  slug: google-maps
- name: JavaScript
  slug: javascript
- name: Ruby
  slug: ruby
- name: technology
  slug: technology
seo_title: Comment scraper avec Ruby et Nokogiri et mapper les données
seo_desc: 'By Andrew Bales

  Sometimes you want to grab data from a website for your own project. So what do
  you use? Ruby, Nokogiri, and JSON to the rescue!

  Recently, I was working on a project to map data about bridges. Using Nokogiri,
  I was able to capture a c...'
---

Par Andrew Bales

Parfois, vous souhaitez récupérer des données d'un site web pour votre propre projet. Alors, que utilisez-vous ? Ruby, Nokogiri et JSON à la rescousse !

Récemment, je travaillais sur un projet pour mapper des [données sur les ponts](https://bridgereports.com/). En utilisant Nokogiri, j'ai pu capturer les données des ponts d'une ville à partir d'un tableau. J'ai ensuite utilisé les liens dans ce même tableau pour scraper les pages associées. Enfin, j'ai converti les données scrapées en JSON et je les ai utilisées pour alimenter une Google Map.

Cet article vous guide à travers les outils que j'ai utilisés et comment le code fonctionne !

Voir le code complet sur mon [GitHub](https://github.com/agbales/wichita-bridges) repo.

Démonstration de la carte en direct [ici](https://agbales.github.io/wichita-bridges/).

### Le Projet

Mon objectif était de prendre un tableau de données sur les ponts d'un [site web](https://bridgereports.com/) et de le transformer en une carte Google avec des épingles géolocalisées qui produiraient des popups informatifs pour chaque pont.

![Image](https://cdn-media-1.freecodecamp.org/images/pTodl03NV9GsnFl6mYtcO0-rPk6F8AUjRyBb)
_L'idée : Tableau HTML vers Carte_

Pour que cela se produise, j'aurais besoin de :

1. Scraper les données du site web original.
2. Convertir ces données en un [objet JSON](https://www.w3schools.com/js/js_json_objects.asp).
3. Appliquer ces données pour créer une nouvelle carte interactive.

Votre projet variera, sûrement — combien de personnes essaient de mapper des ponts antiques ? — mais j'espère que ce processus se révèlera utile pour votre contexte.

### Nokogiri

Ruby dispose d'un gemme incroyable pour le web scraping appelé [Nokogiri](https://github.com/sparklemotion/nokogiri). Parmi ses nombreuses fonctionnalités, il permet de rechercher des documents HTML par sélecteurs CSS. Cela signifie que si nous connaissons les ids, les classes, ou même les types d'éléments où les données sont stockées dans le DOM, nous sommes capables de les extraire.

#### Le scraper

Si vous suivez le [repo GitHub](https://github.com/agbales/wichita-bridges), vous pouvez trouver mon scraper dans bridges_scraper.rb

```
require 'open-uri'
require 'nokogiri'
require 'json'
```

Open-uri nous permet d'ouvrir le HTML comme un fichier et de le passer à Nokogiri pour le travail lourd.

Dans le code ci-dessous, je passe les informations du DOM de l'URL avec les données des ponts à Nokogiri. Je trouve ensuite l'élément de tableau contenant les données, je recherche ses lignes et j'itère à travers elles.

```
url = 'https://bridgereports.com/city/wichita-kansas/'
html = open(url)
```

```
doc = Nokogiri::HTML(html)
bridges = []
table = doc.at('table')
```

```
table.search('tr').each do |tr|
  cells = tr.search('th, td')
  bridges.push(
    carries: cells[1].text,
    crosses: cells[2].text,
    location: cells[3].text,
    design: cells[4].text,
    status: cells[5].text,
    year_build: cells[6].text.to_i,
    year_recon: cells[7].text,
    span_length: cells[8].text.to_f,
    total_length: cells[9].text.to_f,
    condition: cells[10].text,
    suff_rating: cells[11].text.to_f,
    id: cells[12].text.to_i
  )
end
```

```
json = JSON.pretty_generate(bridges)
File.open("data.json", 'w') { |file| file.write(json) }
```

Nokogiri dispose de nombreuses méthodes (voici une [feuille de triche](https://github.com/sparklemotion/nokogiri/wiki/Cheat-sheet) et un guide de démarrage [guide](https://readysteadycode.com/howto-parse-html-with-ruby-and-nokogiri)!). Nous utilisons seulement quelques-unes.

Le tableau est trouvé avec **.at('table')**, qui retourne la première occurrence d'un élément de tableau dans le DOM. Cela fonctionne très bien pour cette page relativement simple.

Avec le tableau en main, **.search('tr')** fournit un tableau des éléments de ligne que nous itérons avec **.each**. Dans chaque ligne, les données sont nettoyées et poussées dans une seule entrée pour le tableau des ponts.

Après que toutes les lignes sont collectées, les données sont converties en JSON et sauvegardées dans un nouveau fichier appelé "data.json".

### Combiner les données de plusieurs pages

Dans ce cas, j'avais besoin d'informations d'autres pages associées. Plus précisément, j'avais besoin de la latitude et de la longitude de chaque pont, qui n'étaient pas présentes dans le tableau. Cependant, j'ai trouvé que le lien dans la première cellule de chaque ligne menait à une page qui fournissait ces détails.

Je devais écrire un code qui faisait quelques choses :

* Collecter les liens de la première cellule du tableau.
* Créer un nouvel objet Nokogiri à partir du HTML de cette page.
* Extraire la latitude et la longitude.
* Mettre le programme en pause jusqu'à ce que ce processus soit terminé.

```
cells = tr.search('th, td')
links = {}
cells[0].css('a').each do |a|
  links[a.text] = a['href']
end
    got_coords = false
    if links['NBI report']
    nbi = links['NBI report']
    report = "https://bridgereports.com" + nbi
    report_html = open(report)
    sleep 1 until report_html
    r = Nokogiri::HTML(report_html)
        lat = r.css('span.latitude').text.strip.to_f
        long = r.css('span.longitude').text.strip.to_f
```

```
    got_coords = true
  else
    got_coords = true
  end
    sleep 1 until got_coords == true
```

```
  bridges.push(
        links: links,
        latitude: lat,
        longitude: long,
        carries: cells[1].text,
        ..., # toutes les autres paires clé/valeur précédentes
  )
end
```

Quelques points supplémentaires méritent d'être soulignés ici :

* J'utilise "got_coords" comme un simple binaire. Cela est défini sur **false** par défaut et est basculé lorsque les données sont capturées OU simplement non disponibles.
* La latitude et la longitude sont situées dans des spans avec des classes correspondantes. Cela rend la sécurisation des données simple : **.css('span.latitude')** Cela est suivi par **.text, .strip** et **.to_f** qui 1) obtient le texte du span, 2) supprime tout espace blanc excessif, et 3) convertit la chaîne en un nombre à virgule flottante.

### **JSON → Google Map**

Le nouvel objet JSON doit être légèrement modifié pour s'adapter à l'API Google Maps. Je l'ai fait avec JavaScript dans **map.js**

Les données JSON sont accessibles dans **map.js** car elles ont été déplacées dans le dossier JS, assignées à une variable appelée "bridge_data", et incluses dans une balise <script> dans index.html.

Très bien ! Nous allons maintenant convertir le fichier JSON (assigné à la variable bridge_data) en un nouveau tableau utilisable par Google Maps.

```
const locations = bridge_data.map(function(b) {
  var mapEntry = [];
  var info = "<b>Construite en : </b>" + b.year_build + "<br>" +
             "<b>Longueur de la portée : </b>" + b.span_length + " ft<br>" +
             "<b>Longueur totale : </b>" + b.total_length + " ft<br>" +
             "<b>Condition : </b>" + b.condition + "<br>" +
             "<b>Design : </b>" + b.design + "<br>";
  mapEntry.push(
    info,
    b.latitude,
    b.longitude,
    b.id
  )
  return mapEntry;
});
```

J'utilise [.map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) pour créer un nouveau tableau dimensionnel appelé "locations". Chaque entrée contient des informations, qui apparaîtront dans notre popup Google Maps si l'utilisateur clique sur cette épingle sur la carte. Nous incluons également la latitude, la longitude et l'ID unique du pont.

![Image](https://cdn-media-1.freecodecamp.org/images/gjvu5vBL3amtEBBZrFs1z33vm2ZQdbq0khIM)
_Carte des ponts à partir des données JSON_

Le résultat est une Google Map qui trace le tableau des emplacements avec des popups riches en informations pour chaque pont !

Cela vous a-t-il aidé ? Donnez-lui quelques applaudissements et suivez-moi !