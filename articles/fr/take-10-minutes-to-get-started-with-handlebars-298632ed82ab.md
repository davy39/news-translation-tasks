---
title: Prenez 10 minutes pour commencer avec Handlebars
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T22:37:29.000Z'
originalURL: https://freecodecamp.org/news/take-10-minutes-to-get-started-with-handlebars-298632ed82ab
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hKdDzlUz__kgb46lJRJ6jA.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Prenez 10 minutes pour commencer avec Handlebars
seo_desc: 'By Wing Puah

  Nowadays front-end development is no longer about building static HTML markup and
  compiling SASS files. The rise of Single Page Applications (SPAs) means we can do
  a lot of the rendering logic on the client-side. Modern day web developme...'
---

Par Wing Puah

De nos jours, le développement front-end ne consiste plus à construire du balisage HTML statique et à compiler des fichiers SASS. L'essor des applications monopages (SPA) signifie que nous pouvons effectuer une grande partie de la logique de rendu côté client. Le développement web moderne nécessite souvent une entrée de données dynamique.

Bien que [React.js](https://reactjs.org/) soit excellent, il nécessite souvent une courbe d'apprentissage pour les développeurs avant qu'ils puissent l'intégrer dans l'équipe. Récemment, j'ai été chargé de construire le front-end d'un site web de cours. Cela a marqué le début de mon exploration de [Handlebars.js](https://handlebarsjs.com/).

Handlebars est un moteur de templating populaire et simple à utiliser. Il ressemble beaucoup à du HTML régulier, avec des expressions Handlebars intégrées dans les accolades {{}}.

```
<div class="entry">   <h1>{{name}}</h1>   <div>{{quote}}</div> </div>
```

Avant de passer aux détails de Handlebars, voyons comment les données seront insérées dans la page via JavaScript vanilla. Nous prendrons l'exemple de la construction d'une page web qui liste quelques citations. Parce que, après tout, tout le monde a besoin d'un peu d'inspiration.

### JavaScript vanilla

#### **Récupération des données**

La plupart du temps, vous pourriez récupérer des données via AJAX, mais pour simplifier, nous allons créer notre propre objet de données.

```
// quotes.js var quotes = [   {name: "Frank Lloyd Wright", quote: "You can use an eraser on the drafting table or a sledge hammer on the construction site."},  {name: "Douglas Adams", quote: "The major difference between a thing that might go wrong and a thing that cannot possibly go wrong is that when a thing that cannot possibly go wrong goes wrong it usually turns out to be impossible to get at or repair."},   {name: "Ettore Sottsass", quote: "I try and be as stupid as possible regarding my profession, which means I try to look at as few design magazines as possible."},   {name: "Shaun White", quote: "Im a big fan of doing what you are really bad at. A lot."} ]
```

#### **Créer le balisage HTML**

```
// index.html<div class="container>  <div class="row" id="quotes">  </div></div>
```

#### **Ajout des données avec JavaScript**

Nous allons utiliser une boucle _for_ pour parcourir le contenu ci-dessus.

```
//quotes.jslet quoteMarkup = '';
```

```
for (var i = 0; i < quotes.length; i++) {  let name = quotes[i].name,       quote = quotes[i].quote;
```

```
quoteMarkup += '<div class="col-12 col-sm-6">' +                  '<h5>' + name + '</h5>' +                  '<p>' + quote + '</p>'                 '</div>'}
```

```
document.getElementById('quotes').innerHTML = quoteMarkup;
```

Avec un code comme celui-ci, il est difficile à lire et fastidieux à écrire. Et le balisage HTML pour cette page réside maintenant à la fois dans index.html et quotes.js.

### Entrée Handlebars

#### **Pour commencer**

Pour commencer, nous devons inclure le fichier source de Handlebars. Vous pouvez ajouter le lien à l'intérieur de la balise head ou avant la fin de <body>.

```
&lt;script src="js/handlebars.js">&lt;/script>
```

Alternativement, vous pouvez également lier Handlebars à partir d'un CDN.

```
<script src="//cdnjs.cloudflare.com/ajax/libs/handlebars.js/4.0.12/handlebars.min.js"></script>
```

#### **Créer le modèle**

Nous utiliserons toujours l'objet de données des citations du fichier ci-dessus. Nous allons ajouter un peu de magie Handlebars au fichier index.html.

```
//index.html<div class="container>  <div id="quotes">
```

```
<script id="quotes-template" type="text/x-handlebars-template">                  <div class="row">                    {{#each this}}                      <div class="col-12 col-sm-6 p-3">                          <div class="card">                              <h4 class="card-header">                                  {{name}}                              </h4>                              <div class="card-body">                                  {{quote}}                         </div>                          </div>                     </div>                    {{/each}}                </div>            </script>    </div></div>
```

* _each_: Itère à travers les données
* _this_: Références au contexte actuel.
* _text/x-handlebars-template_: Pour indiquer au navigateur de ne pas exécuter le script comme du JavaScript normal.

#### **Compiler le modèle avec Handlebars**

Il ne faut que quelques lignes pour compiler les données avec Handlebars. C'est ce que j'aime à ce sujet. Même si quelqu'un dans l'équipe n'a jamais utilisé Handlebars auparavant, le script et le balisage sont très simples à comprendre et à apprendre.

```
let content = document.getElementById('quotes'),    src = document.getElementById('quotes-template').innerHTML,     template = Handlebars.compile(src),            html = template(quotes);
```

```
content.innerHTML = html;
```

* _content_: Retourne l'élément dans lequel vous souhaitez insérer les informations compilées.
* _src_: Récupère le balisage du modèle.
* _Handlebars.compile(src)_: Compile le modèle en cours d'utilisation. Il retournera une fonction à laquelle les données peuvent être passées pour être rendues.
* _template(quotes)_: Compile les données dans le modèle.
* _content.innerHTML_: Rend le tout dans le DOM

Vous pouvez consulter [le projet ici](https://wing-puah.github.io/learn_handlebars/).

### Bonus

J'ai utilisé Handlebars pour un site web à modèles multiples. Je me suis retrouvé à écrire le même code AJAX et Handlebars plusieurs fois. Voici donc les deux fonctions que j'ai créées pour me faciliter la vie.

#### **Obtenir des données à partir d'AJAX avec JavaScript**

```
function ajaxGet(url, callback) {    let xmlhttp = new XMLHttpRequest();    xmlhttp.onreadystatechange = function() {        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {            // console.log(xmlhttp.responseText);            try {                var data = JSON.parse(xmlhttp.responseText);            } catch(err) {                console.log(err.message +' Getting: ' + url);                return;            }            callback(data);        }    };
```

```
xmlhttp.open("GET", url, true);    xmlhttp.send();}
```

#### **Fonction pour exécuter Handlebars**

```
function runHandlebars(id, dataSrc, src) {  if(document.getElementById(id) != null) {    let content = document.getElementById(id);    ajaxGet(dataSrc, function(data){      let source = document.getElementById(src).innerHTML,           template = Handlebars.compile(source);
```

```
content.innerHTML = template(data);    });  }}
```

Avec ces deux fonctions, j'ai pu exécuter tout mon code Handlebars dans un seul fichier JavaScript. Cela ressemblera à quelque chose comme ceci.

```
runHandlebars('nav-sub-1', '/data/courses.json', 'nav-submenu-template');
```

```
runHandlebars('contributors', '/data/contributors.json', 'contributors-template');
```

### Conclusion

Mon expérience avec Handlebars a été positive. Dans mon projet, je l'utilise avec gulp et metalsmith. Vais-je l'utiliser pour d'autres projets ? Mon avis est que je préfère quelque chose comme React ou un générateur de site statique complet comme Jekyll. Mais dans ce cas, lorsque l'équipe est plus à l'aise avec le balisage HTML et qu'il s'agit d'un site web relativement simple, Handlebars est un bon choix.