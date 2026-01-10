---
title: Comment visualiser les données météorologiques avec D3.js
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2022-01-17T16:59:10.000Z'
originalURL: https://freecodecamp.org/news/visualize-weather-data-with-d3js
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/reza-shayestehpour-Nw_D8v79PM4-unsplash.jpg
tags:
- name: D3.js
  slug: d3js
- name: data visualization
  slug: data-visualization
seo_title: Comment visualiser les données météorologiques avec D3.js
seo_desc: 'What plans would you make if you knew it was going to rain tomorrow?

  This can be a crucial question to ask yourself when it comes to planning your personal
  and day-to-day business activities.

  For example, I have a friend who runs an app-based laundry...'
---

Quels plans feriez-vous si vous saviez qu'il allait pleuvoir demain ?

Cela peut être une question cruciale à se poser lorsqu'il s'agit de planifier vos activités personnelles et professionnelles quotidiennes.

Par exemple, j'ai un ami qui dirige une entreprise de blanchisserie basée sur une application à Lagos, au Nigeria. Il dépend fortement de l'ensoleillement, et parfois il pleut, ou il n'y a tout simplement pas de soleil. Ces jours-là, les affaires sont très mauvaises.

Mais que se passerait-il s'il savait qu'il allait pleuvoir le lendemain ou dans 6 heures ? Cela l'aiderait à planifier les choses bien à l'avance et à éviter les retards dans les commandes. Mais où peut-il obtenir de telles informations ?

C'est là que l'API météorologique de Tomorrow.io intervient. L'API météorologique nous fournit des données météorologiques précises et rapides en temps réel, comme la probabilité de précipitations, la quantité de pluie, la température, la vitesse du vent, et plus encore.

De telles informations sont très utiles pour les entreprises de divers secteurs comme les transports, l'agriculture, et, dans le cas de mon ami, les blanchisseries.

De plus, les données météorologiques de cette API peuvent être facilement intégrées dans votre projet ou tout programme avec lequel vous travaillez. Le meilleur aspect – la version gratuite de l'API est extrêmement puissante en soi, c'est donc celle que nous utiliserons aujourd'hui.

Dans cet article, nous utiliserons l'API météorologique de Tomorrow.io et [D3.js](https://d3js.org/) pour prévoir et visualiser la probabilité de précipitations d'un lieu particulier sur un graphique linéaire. Un service comme celui-ci permettrait à mon ami de savoir quels jours de la semaine il est susceptible de pleuvoir.

## Exigences du projet

Que faut-il pour continuer ce tutoriel ? Des connaissances de base en JavaScript et D3.js sont requises.

Je suggère de lire un [guide pour débutants sur D3.js](https://www.freecodecamp.org/news/d3js-tutorial-data-visualization-for-beginners/) si vous souhaitez rafraîchir votre mémoire avant d'aller plus loin.

## Pour commencer

Tout d'abord, créez un fichier HTML et ajoutez la dernière bibliothèque de `d3.js` au fichier HTML. Créez également un élément `svg` vide, comme ceci :

```xml
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Probabilité de pluie Tomorrow.io</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
  </head>
  <body>
    <svg></svg>
  </body>
  <script src="index.js"></script>
</html>
```

## Comment configurer les marges

À un moment donné, nos visualisations auront besoin d'un peu d'espace (marges). Il est courant dans `d3.js` de configurer la **convention de marge**.

Pour cela, vous devez définir les marges pour les quatre côtés, créer un fichier `index.js` et ajouter ce qui suit :

`const margin = { left: 120, right: 30, top: 60, bottom: 30 }`

Maintenant, définissons la largeur et la viewBox de notre élément SVG. Cela aidera à le rendre réactif.

```js
const width = document.querySelector("body").clientWidth,
  height = 500;

const svg = d3.select("svg").attr("viewBox", [0, 0, width, height]);
```

## Comment définir les échelles

La fonction d3.scale prend des données en entrée et retourne une valeur visuelle en pixels. d3.scale doit être définie avec un **domaine** et une **plage**. Le domaine définit une LIMITE pour les données que nous essayons de représenter visuellement.

Comme vu ci-dessus, nous devons définir la plage des échelles. Nous définirons le `domain` une fois que nous aurons récupéré nos données :

```js
const x_scale = d3.scaleTime().range([margin.left, width - margin.right]);
const y_scale = d3.scaleLinear().range([height - margin.bottom - margin.top, margin.top]);
```

## Comment ajouter un titre et des étiquettes

Ensuite, nous devons ajouter un titre et des étiquettes à nos visualisations. Cela est utile pour expliquer notre graphique à nos utilisateurs.

Modifiez votre `script.js` et ajoutez le code suivant :

```js
// étiquettes
const x_label = "Temps";
const y_label = "Probabilité de pluie";
const location_name = "Lagos Nigeria";

// ajouter le titre
svg
  .append("text")
  .attr("class", "svg_title")
  .attr("x", (width - margin.right + margin.left) / 2)
  .attr("y", margin.top / 2)
  .attr("text-anchor", "middle")
  .style("font-size", "22px")
  .text(`${y_label} de ${location_name}`);
// ajouter l'étiquette y
svg
  .append("text")
  .attr("text-ancho", "middle")
  .attr(
    "transform",
    `translate(${margin.left - 70}, ${
      (height - margin.top - margin.bottom + 180) / 2
    }) rotate(-90)`
  )
  .style("font-size", "26px")
  .text(y_label);
// ajouter l'étiquette x
svg
  .append("text")
  .attr("class", "svg_title")
  .attr("x", (width - margin.right + margin.left) / 2)
  .attr("y", height - margin.bottom - margin.top + 60)
  .attr("text-anchor", "middle")
  .style("font-size", "26px")
  .text(x_label);
```

Avec le titre et les étiquettes ajoutés ci-dessus, l'aperçu ressemble à ceci :

![Titres et étiquettes ajoutés à notre visualisation](https://paper-attachments.dropbox.com/s_80A2ED9660649A0944547FE32AE888AF070E268C15D560C813DD3420036CDBBE_1638557381465_tomorrow.io-demo1.png align="left")

## Comment créer le graphique linéaire

Ici, la première chose que nous devons faire est de générer le [chemin](https://sharkcoder.com/data-visualization/d3-line-chart) pour notre graphique. D3.js fournit une méthode `.line()` qui génère essentiellement le chemin de la ligne pour vous. Ajoutons le générateur de ligne :

```js
const start_time = (d) => new Date(d.startTime);
const temperature = (d) => +d.values.precipitationProbability;

const line_generator = d3.line()
  .x((d) => x_scale(start_time(d)))
  .y((d) => y_scale(temperature(d)))
  .curve(d3.curveBasis);
```

Maintenant que nous avons défini notre générateur de ligne, passons à la récupération de nos données.

## Comment récupérer les données de l'API météorologique [Tomorrow.io](http://Tomorrow.io)

D3 nous fournit une méthode `.json()` pour récupérer des données JSON à partir d'une API ou d'un fichier local.

Avant de pouvoir récupérer des données en utilisant l'API météorologique [Tomorrow.io](http://Tomorrow.io), vous aurez besoin d'un jeton d'accès secret. Pour obtenir ce jeton, tout ce que vous avez à faire est de créer un compte avec [Tomorrow.io](http://Tomorrow.io). Oui, c'est aussi simple que cela.

Une fois que vous avez créé votre compte, connectez-vous. Ensuite, sur votre [tableau de bord](https://app.tomorrow.io/development/keys), vous devriez voir votre jeton secret d'API :

![Image](https://paper-attachments.dropbox.com/s_80A2ED9660649A0944547FE32AE888AF070E268C15D560C813DD3420036CDBBE_1638566467761_tomorrow.io-demo2.png.png align="left")

Ajoutez le code suivant pour récupérer les données :

```js
const lat = 6.465422; // latitude de Lagos, Nigeria
const long = 3.406448; // longitude de Lagos, Nigeria

const api_key = "votre-clé-api-ici";

const url = `https://api.tomorrow.io/v4/timelines?location=${lat},${long}&fields=snowAccumulation,precipitationProbability,precipitationType&timesteps=1h&units=metric&apikey=${api_key}`;

d3.json(url).then(({ data }) => {
  const d = data.timelines[0].intervals;
  console.log(d)
});
```

Voici un exemple des données JSON retournées par cette requête :

```json
{
  "data": {
    "timelines": [
      {
        "timestep": "1h",
        "startTime": "2021-12-03T13:00:00Z",
        "endTime": "2021-12-08T01:00:00Z",
        "intervals": [
          {
            "startTime": "2021-12-03T13:00:00Z",
            "values": {
              "snowAccumulation": 0,
              "precipitationProbability": 0,
              "precipitationType": 0
            }
          },
          // 108 autres données
        ]
      }
    ]
  }
}
```

Maintenant que nous avons récupéré nos données, générons notre graphique linéaire :

```js
d3.json(url).then(({ data }) => {
  const d = data.timelines[0].intervals;
  
// définir le domaine 
  x_scale.domain(d3.extent(d, start_time)).nice(ticks);
  y_scale.domain(d3.extent(d, temperature)).nice(ticks);
  // ajouter le chemin de la ligne
  svg
    .append("path")
    .attr("fill", "none")
    .attr("stroke", "steelblue")
    .attr("stroke-width", 4)
    .attr("d", line_generator(d)); // générer le chemin
});
```

Le code ci-dessus nous donne un graphique de base :

![Image](https://paper-attachments.dropbox.com/s_80A2ED9660649A0944547FE32AE888AF070E268C15D560C813DD3420036CDBBE_1638560607910_tomorrow.io-demo3.png align="left")

## Comment ajouter les axes

Même avec le graphique linéaire ci-dessus, vous aurez du mal à savoir exactement quel jour ou quelle heure a la plus forte probabilité de pluie.

Nous pouvons résoudre ce problème en ajoutant les axes du temps et de la probabilité de pluie (en %).

Tout d'abord, définissez les axes juste en dessous de vos échelles :

```js
const ticks = 10;
const x_axis = d3.axisBottom()
  .scale(x_scale)
  .tickPadding(10)
  .ticks(ticks)
  .tickSize(-height + margin.top * 2 + margin.bottom);
const y_axis = d3.axisLeft()
  .scale(y_scale)
  .tickPadding(5)
  .ticks(ticks, ".1")
  .tickSize(-width + margin.left + margin.right);

// formater nos graduations pour obtenir un pourcentage précis
y_axis.tickFormat((d) => {
  if (!Number.isInteger(d)) {
    d = decimalFormatter(d);
  }
  return d + "%";
});
```

Enfin, ajoutons notre axe à l'élément SVG :

```js
// ajouter l'axe x
  svg
    .append("g")
    .attr("transform", `translate(0,${height - margin.bottom - margin.top})`)
    .call(x_axis);

  // ajouter l'axe y
  svg
    .append("g")
    .attr("transform", `translate(${margin.left},0)`)
    .call(y_axis);
```

Avec l'axe ajouté, notre graphique linéaire ressemble maintenant à ceci :

![Probabilité de précipitations de Tomorrow.io à Lagos, Nigeria. 3 décembre 2021](https://paper-attachments.dropbox.com/s_80A2ED9660649A0944547FE32AE888AF070E268C15D560C813DD3420036CDBBE_1638561615864_tomorrow.io-demo4.png align="left")

C'est beaucoup mieux ! Vous pouvez maintenant dire quel jour et quelle heure ont la plus forte probabilité de pluie.

Le code complet et la démonstration de cet exemple sont hébergés sur Codepen :

%[https://codepen.io/Spruce_khalifa/pen/vYeNKRg] 

## Conclusion

Avec la puissance de D3.js combinée à l'API météorologique [Tomorrow.io](http://Tomorrow.io), nous pouvons créer des visualisations qui aident les utilisateurs à résoudre les problèmes liés à la météo affectant leurs entreprises.

J'espère que vous avez trouvé ce tutoriel utile.

Bon codage !

Photo de couverture par [Reza Shayestehpour](https://unsplash.com/@r_shayesrehpour) sur Unsplash