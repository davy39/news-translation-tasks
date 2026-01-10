---
title: Comment j'ai scrappé 7 000 articles d'un site de presse avec Node
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T15:49:00.000Z'
originalURL: https://freecodecamp.org/news/how-i-scraped-7000-articles-from-a-newspaper-website-using-node-1309133a5070
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dCcidN-uNelWP_fMYvC_jA.jpeg
tags:
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai scrappé 7 000 articles d'un site de presse avec Node
seo_desc: 'By Alexandre Robin

  Why did I do this?

  My girlfriend is writing a paper about the perception of French Hip-Hop music through
  time. To do that, she would like to text-mine articles from LeMonde.fr, a French
  mainstream newspaper.

  Problem: there have bee...'
---

Par Alexandre Robin

#### **Pourquoi ai-je fait cela ?**

Ma petite amie écrit un article sur la perception du Hip-Hop français à travers le temps. Pour ce faire, elle souhaiterait faire du text-mining sur des articles de LeMonde.fr, un journal généraliste français.

**Problème** : il y a eu plus de **7 000 articles** parlant de musique hip-hop depuis les années 80.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sBlfrDqO3FpA2QjL3J3RvQ.jpeg)
_La réaction de ma petite amie — Memegenerator.net_

#### Codons !

Pour ce programme, j'utiliserai :

* Un script NodeJS local
* fs : pour écrire un fichier JSON
* [Request](https://nodejs.org/dist/latest-v6.x/docs/api/http.html#http_event_request) : pour effectuer des requêtes POST et GET
* [Cheerio](https://www.npmjs.com/package/cheerio) : pour charger le HTML et pouvoir interagir avec lui

```
// Pour installer cheerio : npm i --save cheerio
```

Assurez-vous d'avoir tout cela dans votre package.json, et tout devrait bien se passer :)

**Qu'est-ce que je voulais ?**   
Au final, je voulais avoir un fichier Excel organisé comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*TH52fv64qK-zG8ApdRlM0Q.jpeg)
_Mon objectif_

Par conséquent, j'ai dû utiliser un JSON structuré comme ceci. Je vous montrerai à la fin de cet article comment convertir le JSON en Excel.

```javascript
[
 {
 ‎ date:,
  title:,
  description:,
 ‎ text:,
 ‎ url:,
 ‎},
]
```

#### Première étape : récupérer les URL de tous les articles

La première étape a été assez facile. Grâce à la fonctionnalité de recherche avancée, il m'a suffi de récupérer le lien URL de la page de résultats et d'indiquer à mon code comment :

* Chercher le nombre de résultats
* Calculer le nombre de pages, sachant qu'il y a 30 articles par page
* Récupérer le titre, la description, la date et l'URL des 30 articles pour chaque page

Voici le code pour le faire :

```javascript
const fs = require("fs");
const request = require("request");
const cheerio = require("cheerio");

const jsonTab = []; // Nous créons notre tableau

function writeFile() {
  // Écrira le fichier json
  fs.writeFile("output.json", JSON.stringify(jsonTab, null, 4), (err) => {
    console.log("Fichier écrit avec succès !");
  });
}

// L'URL de la fonction de recherche avancée avec nos mots-clés
const url = 'http://www.lemonde.fr/recherche/?keywords="Rap+"+"hip-hop"+"hip%20hop"+"rappeur"+"rappeurs"+"raps"+"rappers"&page_num=1&operator=or&exclude_keywords=&qt=recherche_texte_title&author=&period=custom_date&start_day=01&start_month=01&start_year=1970&end_day=20&end_month=09&end_year=2017&sort=asc';

/* Le premier appel de requête, notre objectif ici est d'obtenir le nombre de résultats puis
de calculer le nombre de pages */
request(url, (error, response, html) => {
  const $ = cheerio.load(html);

  // Toutes les variables que nous utiliserons plus tard
  let number;
  let description;
  let date;
  let title;
  let link;

  if (!error) {
    $(".bg_gris_clair").filter(() => {
      /* Nous voulons sélectionner tous les éléments HTML
      avec la classe ".bg_gris_clair" (et nous savons déjà qu'il n'y en a
      qu'un) */
      const data = $(this);
      const str = data.children("strong").text().trim();
      number = parseInt(str.substring(0, str.indexOf("e")).replace(/\s/g, ""), 10);
    });
  }

  let count = 1;

  for (let i = 1; i <= number / 10; i++) {
    const urlPerPage = 'http://www.lemonde.fr/recherche/?keywords="Rap+"+"hip-hop"+"hip%20hop"+"rappeur"+"rappeurs"+"raps"+"rappers"&page_num=' + i + "&operator=or&exclude_keywords=&qt=recherche_texte_title&author=&period=custom_date&start_day=01&start_month=01&start_year=1970&end_day=20&end_month=09&end_year=2017&sort=asc";

    request(urlPerPage, (err, response2, html2) => {
      if (!err) {
        const $ = cheerio.load(html2);

        $(".grid_11.omega.resultat").filter(() => {
          const json = {
            date: "",
            title: "",
            description: "",
            url: ""
          };
          const data = $(this);

          title = data.children("h3").children("a").text().trim();
          link = "http://lemonde.fr" + data.children("h3").children("a").attr("href").trim();
          description = data.children("p").text().trim();
          const dateStr = data.children("span").text();
          date = dateStr.replace(/.+?(?=\d)/, "");

          json.title = title;
          json.url = link;
          json.description = description;
          json.date = date;
          jsonTab.push(json);
        });
      } else if (err) {
        console.log(err);
      }

      count += 1;

      // Écrire le fichier une fois que nous avons parcouru toutes les pages.
      if (count === parseInt(number / 10, 10)) {
        writeFile();
      }
    });
  }
});
```

Une fois cela fait, j'avais un fichier JSON avec plus de 7 000 entrées. Pour chacune d'entre elles, j'avais :

* Une Date
* Un Titre
* Une Description
* Une URL

Il me manquait juste le contenu…

« D'accord, je n'ai qu'à utiliser le même code et l'exécuter pour les 7 000 URL que j'ai pour obtenir le contenu ! »

![Image](https://cdn-media-1.freecodecamp.org/images/1*1Kxl4vJMqvQgEA22wZOSYg.jpeg)
_Crédit image : Gemma Correll_

J'apprends activement à coder depuis un an maintenant… Et l'une des premières choses que j'ai apprises est : **rien n'est jamais simple en programmation**. Jamais. Mais pour chaque problème avec lequel vous **allez** lutter, il y a une question que vous pouvez poser à Google ;-).

J'ai découvert qu'une grande partie des articles n'étaient pas accessibles sans un compte premium. Je devais donc être connecté pour voir le contenu et le scraper.

Heureusement, nous avons réussi à obtenir un compte premium. Je n'avais plus qu'à trouver un moyen de dire à mon code comment :

* S'authentifier sur [lemonde.fr](https://lemonde.fr)
* Rester connecté pendant le scraping

#### Deuxième étape : Comment s'authentifier sur un site web

Pour ce faire, j'ai dû comprendre comment fonctionne un site web lorsque je clique sur « Connexion ». La bonne nouvelle est : nous avons les outils de développement.

Je devais juste découvrir comment le site envoie le mot de passe et le nom d'utilisateur au serveur et reproduire le schéma.

Voici la page d'authentification de LeMonde.fr (Comme il s'agit d'une plateforme française, j'ai traduit certains mots pour vous aider à comprendre) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*j-JFcBLEkFeqvCP2OPMiNA.png)
_Capture d'écran de lemonde.fr_

Maintenant, que se passe-t-il quand on essaie de se connecter ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*GgcXRy11C1WOWjhFOhzMgA.gif)

Vous avez vu ça ? J'ai cliqué sur « Connexion » et lemonde.fr envoie une requête POST avec un formulaire simple contenant cinq informations :

* connection[mail] = 'votre nom d'utilisateur'
* connection[password] = 'votre mot de passe'
* connection[stay_connected] = booléen : 1 pour vrai, 0 pour faux (ASTUCE : vous voulez qu'il soit vrai)
* connection[save] = rien n'est requis ici
* connection[token] = c'est la partie délicate

Nous connaissons déjà quatre informations sur cinq. Il ne nous reste plus qu'à trouver d'où vient le « token ».

Heureusement, lemonde.fr est gentil avec nous ☺️ :

![Image](https://cdn-media-1.freecodecamp.org/images/1*YW9hQSFYyBDdcqsRTLvmLA.png)

Le token de connexion est automatiquement généré dans un input caché lorsque vous chargez la page pour la première fois. Il suffit de le connaître et de le récupérer avant d'essayer de se connecter.

Eh bien, nous sommes maintenant prêts à passer à l'étape 3 !

#### Troisième étape : Attrapez-les tous !

![Image](https://cdn-media-1.freecodecamp.org/images/1*PMwOFcv5vuIsMHAWSQZWQw.gif)
_Crédit : Giphy.com_

Voici le code complet pour s'authentifier, récupérer et conserver les cookies et enfin collecter tous les articles.

```javascript
const fs = require("fs");
const request = require("request");
const cheerio = require("cheerio");

// Préparer toutes les variables nécessaires plus tard
let count = 0;
let timeout = 0;
const id = "myusername";
const mdp = "mypassword";
let obj;

// Les URL à partir desquelles nous allons scraper
const connexionUrl = "https://secure.lemonde.fr/sfuser/connexion";

// Écrira un fichier "output.json"
function writeFile() {
  fs.writeFile("output.json", JSON.stringify(obj, null, 4), (err) => {
    console.log(
      "Fichier écrit avec succès ! - Vérifiez le répertoire de votre projet pour le fichier output.json"
    );
  });
}

// création d'un jar propre pour stocker les cookies
const j = request.jar();

// Premier appel de requête GET
request(
  {
    url: connexionUrl,
    jar: j
  },
  (err, httpResponse, html) => {
    const $ = cheerio.load(html);

    // Nous utilisons Cheerio pour charger le HTML et pouvoir trouver le connection__token
    const token = $("#connection__token")[0].attribs.value; // voici le connection__token

    // Construction du formulaire requis dans la requête POST pour se connecter
    const form = {
      "connection[mail]": id,
      "connection[password]": mdp,
      "connection[stay_connected]": 1,
      "connection[save]": "",
      "connection[_token]": token
    };

    // REQUÊTE POST pour se connecter. Même URL avec les "headers de requête" et le formulaire complet.
    request.post(
      {
        url: connexionUrl,
        jar: j,
        headers: {
          Accept:
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4",
            "Cache-Control": "no-cache",
            "Content-Type": "application/x-www-form-urlencoded",
            Origin: "http://secure.lemonde.fr/",
            Host: "secure.lemonde.fr",
            "Upgrade-Insecure-Requests": 1,
            "User-Agents":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
          Connection: "keep-alive",
          Pragma: "no-cache",
          Referer: "https://secure.lemonde.fr/sfuser/connexion"
        },

        form: form
      },
      (error, response, body) => {
        // NOUS SOMMES CONNECTÉS :D

        /* Deuxième appel de requête GET : cette fois, nous utilisons la réponse de la requête POST
        pour demander la bonne URL */
        request(
          {
            url: response.headers.location,
            jar: j
          },
          (err, httpResponse, html2) => {
            const json = fs.readFileSync("./firstStep.json"); // Charger le JSON créé à l'étape 1
            obj = JSON.parse(json); // Nous créons notre JSON dans un objet javascript utilisable

            // boucle forEach pour parcourir tout l'objet et demander chaque lien
            obj.forEach((e) => {
              let articleUrl = e.url;

              /* Nous utilisons un setTimeout pour être sûrs que toutes les requêtes sont effectuées
              une par une et non toutes en même temps */
              setTimeout(() => {
                request(
                  {
                    url: articleUrl,
                    jar: j
                  },
                  (error1, httpResponse, html3) => {
                    if (!error1) {
                      const $ = cheerio.load(html3); // charger le HTML de la page de l'article
                      $(".contenu_article.js_article_body").filter(() => {
                        const data = $(this);

                        // récupérer le contenu, supprimer tous les sauts de ligne (mieux pour Excel)
                        let text = data
                          .text()
                          .trim()
                          .replace(/\n/g, "\t");

                        e.text = text; // pousser le contenu dans le tableau
                      });

                      $(".txt3.description-article").filter(() => {
                        const data = $(this);

                        const description = data
                          .text()
                          .trim()
                          .replace(/\n/g, "\t");

                        e.description = description;
                      });
                    }
                  }
                );

                count += 1;

                // Écrire un nouveau fichier JSON une fois que nous avons le contenu de tous les articles
                if (count === obj.length) {
                  writeFile();
                }
              }, timeout);

              timeout += 50; // augmenter la durée du timeout à chaque fois
            });
          }
        );
      }
    );
  }
);
```

J'ai maintenant un fichier JSON avec tous les articles et leur contenu. La dernière étape consiste à le convertir en un véritable tableau Excel.

#### Étape bonus quatre : De .JSON à .CSV

Voici un code simple pour convertir votre fichier « output.json » en « output.csv » (Vous pouvez remercier mon ami [@jvdsande](https://github.com/jvdsande)) :

```javascript
const fs = require('fs');

let jsonstring = fs.readFileSync('output.json') // charger le fichier output.json
let json = JSON.parse(jsonstring)


function JSONtoCSV(JSON) {
  let CSV = ''

  Object.keys(JSON[0]).forEach((key) => {
    CSV += key + '§'
  })

  CSV += '\r\n'

  JSON.forEach((obj) => {
    Object.keys(obj).forEach((key) => {
      CSV += obj[key] + '§'
    })

    CSV += '\r\n'
  })

  return CSV
}

fs.writeFileSync('output.csv', JSONtoCSV(json))
```

Et voilà. Je peux importer mon fichier « output.csv » dans Excel et j'ai ce que je voulais : plus de 7 000 lignes remplies d'articles de LeMonde.fr

![Image](https://cdn-media-1.freecodecamp.org/images/1*vq6cNlgAT4jRsmndyK48vA.png)
_Mission accomplie_

Vous voulez connaître la meilleure partie ? Je suis presque sûr que cette logique est facilement réutilisable pour tous les sites de journaux du monde !

Si vous souhaitez créer une base de données ou scraper un site web, n'hésitez pas à me contacter via Twitter ou LinkedIn, je serais ravi de vous aider.

Oh ! et je travaille sur un projet parallèle pour réutiliser tout ce que j'ai appris ici avec LinkedIn afin d'améliorer la vitesse de sourcing pour les recruteurs :)

Merci de m'avoir lu, c'est ma première histoire sur Medium et je serais ravi de connaître votre avis à ce sujet !