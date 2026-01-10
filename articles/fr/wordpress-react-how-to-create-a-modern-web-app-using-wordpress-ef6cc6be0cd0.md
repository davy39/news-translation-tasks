---
title: Comment créer une application Web moderne en utilisant WordPress et React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-25T10:55:58.000Z'
originalURL: https://freecodecamp.org/news/wordpress-react-how-to-create-a-modern-web-app-using-wordpress-ef6cc6be0cd0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sKZ0nC0gyc5tiqlVBfu_uQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
- name: WordPress
  slug: wordpress
seo_title: Comment créer une application Web moderne en utilisant WordPress et React
seo_desc: 'By Bret Cameron

  Combine the power of a React front-end with the internet’s most popular CMS

  Want the advantages of a modern React SPA, but need a back-end that feels familiar?
  In this article, we’ll go through how to set-up WordPress’s REST API, incl...'
---

Par Bret Cameron

#### Combinez la puissance d'un front-end React avec le CMS le plus populaire d'Internet

Vous voulez les avantages d'une SPA React moderne, mais vous avez besoin d'un back-end qui vous est familier ? Dans cet article, nous allons voir comment configurer l'API REST de WordPress, y compris les types de publications personnalisés et les champs, et comment récupérer ces données dans React.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sKZ0nC0gyc5tiqlVBfu_uQ.png)

Récemment, je travaillais sur une application React pour un client lorsqu'ils m'ont posé cette question : « Peut-on l'utiliser **_avec WordPress_** ? »

Depuis fin 2015, la réponse à cette question est oui. Mais les étapes nécessaires pour créer un site découplé fonctionnel peuvent ne pas sembler évidentes, surtout pour ceux qui ne sont pas familiers avec WordPress _et_ React.

Lors de mon parcours pour créer une application fonctionnelle, j'ai rencontré quelques obstacles délicats, et dans cet article, je vais expliquer comment les éviter. Je vais également partager plusieurs astuces et conseils que j'ai appris en cours de route !

### Sommaire

#### [Partie 1 : Informations de base](https://medium.com/p/ef6cc6be0cd0#842b)

* [Qu'est-ce qu'un CMS Headless ?](https://medium.com/p/ef6cc6be0cd0#b8b4)
* [Que dois-je savoir pour suivre ?](http://Que dois-je savoir pour suivre ?)
* [Acronymes clés](http://Acronymes clés)
* [Où puis-je voir les données JSON de WordPress ?](https://medium.com/p/ef6cc6be0cd0#1012)

#### [Partie 2 : WordPress](https://medium.com/p/ef6cc6be0cd0#371b)

* [Ajout d'un type de publication personnalisé](https://medium.com/p/ef6cc6be0cd0#c03e)
* [Modification du texte de l'espace réservé du titre](https://medium.com/p/ef6cc6be0cd0#9a1a)
* [Ajout d'un champ personnalisé à votre type de publication personnalisé](https://medium.com/p/ef6cc6be0cd0#40c2)
* [Rendre les champs personnalisés disponibles en JSON](https://medium.com/p/ef6cc6be0cd0#43a6)
* [Restriction des données JSON visibles](https://medium.com/p/ef6cc6be0cd0#6093)

#### [Partie 3 : React](https://medium.com/p/ef6cc6be0cd0#a1f9)

* [Promesses en JavaScript](https://medium.com/p/ef6cc6be0cd0#39f1)
* [La méthode Fetch](https://medium.com/p/ef6cc6be0cd0#092c)
* [Gestion des promesses](https://medium.com/p/ef6cc6be0cd0#02fd)

#### [Un exemple fonctionnel en React](https://medium.com/p/ef6cc6be0cd0#8a3b)

#### [Conclusion](https://medium.com/p/ef6cc6be0cd0#2968)

### Partie 1 : Informations de base

![Image](https://cdn-media-1.freecodecamp.org/images/1*V5SV3AAoVrt9qjiWsTabbg.png)

#### Qu'est-ce qu'un CMS Headless ?

Par le passé, utiliser un CMS comme WordPress signifiait que vous deviez construire votre front-end en utilisant PHP.

Maintenant, avec un CMS headless, vous pouvez construire votre front-end avec les technologies que vous préférez ; cela est possible grâce à la séparation du front-end et du back-end via une API. Si vous voulez créer une SPA (single-page application) en utilisant React, Angular ou Vue, et contrôler le contenu en utilisant un CMS comme WordPress, vous pouvez le faire !

#### Que dois-je savoir pour suivre ?

Vous tirerez le meilleur parti de cet article si vous avez :

* une certaine connaissance de la façon dont un CMS comme WordPress fonctionne, un peu de PHP, et une idée de la façon de configurer un projet WordPress de base sur votre ordinateur ;
* une compréhension de JavaScript, y compris les fonctionnalités du langage ES6+ et la syntaxe des classes React.

#### Acronymes clés

La programmation est pleine de jargon, mais cela permet de discuter plus rapidement de certains des concepts de cet article. Voici un rapide récapitulatif des termes que nous allons utiliser :

* **CMS — système de gestion de contenu.** Pensez à WordPress, Drupal, Joomla, Magneto.
* **SPA — single-page application.** Plutôt que de recharger chaque page dans son intégralité, une application SPA charge le contenu de manière dynamique. Le code fondamental (HTML, CSS et JavaScript) du site web est chargé une seule fois. Pensez à React, Vue, Angular.
* **API — interface de programmation d'application.** En termes simples, une série de définitions qu'un service fournit pour vous permettre de prendre et d'utiliser ses données. [Google Maps en a une](https://developers.google.com/maps/documentation/javascript/tutorial). [Medium en a une](https://github.com/Medium/medium-api-docs). Et maintenant, [chaque site WordPress est livré avec une API intégrée](https://developer.wordpress.org/rest-api/).
* **REST — representational state transfer.** Un style d'architecture web basé autour des méthodes de requête HTTP : `GET`, `PUT`, `POST` et `DELETE`. L'API intégrée de WordPress est une API REST ou « RESTful ».
* **HTTP — hypertext transfer protocol.** L'ensemble de règles utilisées pour transférer des données sur le web. Il est spécifié au début des URLs comme `http` ou `https` (la version sécurisée).
* **JSON — JavaScript object notation.** Bien que dérivé de JavaScript, il s'agit d'un format indépendant du langage pour le stockage et le transfert de données.

Dans cet article, nous utilisons WordPress comme notre CMS. Cela signifie programmer notre back-end en PHP et utiliser l'API REST de WordPress pour fournir des données JSON à notre front-end.

#### Où puis-je voir les données JSON de WordPress ?

Avant de passer aux bonnes choses, une rapide note sur _où_ vous pouvez trouver les données JSON sur votre site WordPress. De nos jours, chaque site WordPress a des données JSON disponibles (sauf si le propriétaire du site a désactivé ou restreint l'accès à celles-ci). Vous pouvez jeter un coup d'œil au JSON principal d'un site WordPress en ajoutant `/wp-json` au nom de domaine racine.

Ainsi, par exemple, vous pouvez consulter le JSON de WordPress.org en visitant [https://wordpress.org/wp-json](https://wordpress.org/wp-json). Ou, si vous exécutez un site WordPress localement, vous pouvez voir son JSON en suivant `localhost/yoursitename/wp-json`.

Pour accéder aux données de vos publications, tapez `localhost/yoursitename/wp-json/wp/v2/posts`. Pour un format de publication personnalisé, remplacez le nouveau format (par exemple, `movies`) au lieu de `posts`. Ce qui ressemble maintenant à un bloc de texte illisible est exactement ce qui nous permettra d'utiliser WordPress comme un CMS headless !

### Partie 2 : WordPress

![Image](https://cdn-media-1.freecodecamp.org/images/1*jUVbqOjhcy-68oCBkIlm2Q.png)

Pour configurer votre API REST, la plupart de ce que vous devrez faire se passera dans votre fichier `functions.php`. Je vais supposer que vous savez comment configurer un projet WordPress et y accéder en utilisant `localhost`, mais si vous avez besoin d'aide pour cela, je recommande [cet article](https://www.taniarascia.com/developing-a-wordpress-theme-from-scratch/#installing-wordpress) (c'est ce que j'ai utilisé pour commencer à programmer avec WordPress).

Pour la plupart des projets, vous voudrez utiliser un type de publication personnalisé, alors commençons par en configurer un.

#### Ajout d'un type de publication personnalisé

Supposons que notre site parle de films, et que nous voulons un type de publication appelé « movies ». Tout d'abord, nous voulons nous assurer que notre type de publication « movies » se charge dès que possible, alors nous allons l'attacher au hook `init`, en utilisant `add_action` :

```
add_action( 'init', 'movies_post_type' );
```

J'utilise `movies_post_type()`, mais vous pouvez appeler votre fonction comme vous le souhaitez.

Ensuite, nous voulons enregistrer « movies » comme un type de publication, en utilisant la fonction `register_post_type()`.

Le prochain bloc de code peut sembler écrasant, mais il est relativement simple : notre fonction prend beaucoup d'arguments intégrés pour contrôler la fonctionnalité de votre nouveau type de publication, et la plupart d'entre eux sont auto-explicatifs. Nous allons stocker ces arguments dans notre tableau `$args`.

Un de nos arguments, `labels`, peut prendre beaucoup d'arguments différents, alors nous le séparons dans un tableau séparé, `$labels`, ce qui nous donne :

Deux des arguments les plus importants sont `'supports'` et `'taxomonies'`, car ceux-ci contrôlent quels champs de publication natifs seront accessibles dans notre nouveau type de publication.

Dans le code ci-dessus, nous avons opté pour seulement trois `'supports'` :

* `'title'` — le titre de chaque publication.
* `'editor'` — l'éditeur de texte principal, que nous utiliserons pour notre description.
* `'thumbnail'` — l'image à la une de la publication.

Pour voir la liste complète de ce qui est disponible, cliquez [ici pour les supports](https://codex.wordpress.org/Function_Reference/post_type_supports), et [ici pour les taxonomies](https://codex.wordpress.org/Custom_Taxonomies#Default_Taxonomies).

Generate WordPress a également [un outil pratique pour vous aider à coder des types de publication personnalisés](https://generatewp.com/post-type/), ce qui peut rendre le processus beaucoup plus rapide.

#### Modification du texte de l'espace réservé du titre

Si le texte de l'espace réservé du titre « enter title here » pourrait être un peu trompeur pour votre type de publication personnalisé, vous pouvez l'éditer dans une fonction séparée :

#### Ajout d'un champ personnalisé à votre type de publication personnalisé

Que faire si vous voulez un champ qui n'est pas prédéfini par WordPress ? Par exemple, disons que nous voulons un champ spécial appelé « Genre ». Dans ce cas, vous devrez utiliser `add_meta_boxes()`.

Pour cela, nous devons attacher une nouvelle fonction au hook `add_meta_boxes` de WordPress :

```
add_action( 'add_meta_boxes', 'genre_meta_box' );
```

À l'intérieur de notre nouvelle fonction, nous devons appeler la fonction `add_meta_box()` de WordPress, comme ceci :

```
function genre_meta_box() {  add_meta_box(    'global-notice',    __( 'Genre', 'sitepoint' ),    'genre_meta_box_callback',    'movies',    'side',    'low'  );}
```

Vous pouvez en lire plus sur les arguments de cette fonction [ici](https://developer.wordpress.org/reference/functions/add_meta_box/). Pour nos besoins, la partie la plus critique est la fonction de rappel, que nous avons nommée `genre_meta_box_callback`. Cela définit le contenu réel de la meta box. Nous avons seulement besoin d'une simple entrée de texte, alors nous pouvons utiliser :

```
function genre_meta_box_callback() {  global $post;  $custom = get_post_custom($post->ID);  $genre = $custom["genre"][0];  ?>  <input style="width:100%" name="genre" value="<?php   echo $genre; ?>" />  <?php};
```

Enfin, notre champ personnalisé ne sauvegardera pas sa valeur à moins que nous le lui disions. À cette fin, nous pouvons définir une nouvelle fonction `save_genre()` et l'attacher au hook `save_post` de WordPress :

```
function save_genre(){  global $post;  update_post_meta($post->ID, "printer_category",   $_POST["printer_category"]);};
```

```
add_action( 'save_post', 'save_genre' );
```

Ensemble, le code utilisé pour créer le champ personnalisé devrait ressembler à ceci :

#### Rendre les champs personnalisés disponibles en JSON

Nos publications personnalisées sont automatiquement disponibles en JSON. Pour notre type de publication « movies », nos données JSON peuvent être trouvées à `localhost/yoursitename/wp-json/wp/v2/movies`.

Cependant, nos champs personnalisés ne font pas automatiquement partie de cela, et nous devons donc ajouter une fonction pour nous assurer qu'ils sont également accessibles via l'API REST.

Tout d'abord, nous devons attacher une nouvelle fonction au hook `rest_api_init` :

```
add_action( 'rest_api_init', 'register_genre_as_rest_field' );
```

Ensuite, nous pouvons utiliser la fonction intégrée `register_rest_field()`, comme ceci :

```
function register_genre_as_rest_field() {  register_rest_field(    'movies',    'genre',    array(      'get_callback' => 'get_genre_meta_field',      'update_callback' => null,      'schema' => null,    )  );};
```

Cette fonction prend un tableau avec `get` et `update` callback. Pour un cas d'utilisation plus simple comme celui-ci, nous devrions seulement avoir besoin de spécifier un `'get_callback'` :

```
function get_genre_meta_field( $object, $field_name, $value ) {  return get_post_meta($object['id'])[$field_name][0];};
```

Dans son ensemble, voici le code nécessaire pour enregistrer un champ personnalisé.

#### Rendre les URLs des images à la une disponibles en JSON

Par défaut, l'API REST de WordPress n'inclut pas les URLs de vos images à la une. Pour faciliter l'accès à cela, vous pouvez utiliser le code suivant :

Le filtre WordPress `rest_prepare_posts` est dynamique, donc nous pouvons remplacer notre type de publication personnalisé à la place de « posts », comme `rest_prepare_movies`.

#### Restriction des données JSON visibles

Nous sommes presque prêts à commencer à récupérer des données dans notre application React, mais il y a une optimisation rapide que nous pouvons faire, en limitant les données qui sont mises à disposition.

Certaines données viennent par défaut et vous n'en aurez peut-être jamais besoin dans votre front-end et — si c'est le cas — nous pouvons les supprimer en utilisant un filtre, comme celui-ci. Vous pouvez trouver les noms des types de données en regardant la partie `/wp-json/wp/v2/movies` de votre site web.

Cela fait, une fois que vous avez ajouté quelques films en utilisant le back-end de WordPress, nous avons tout ce dont nous avons besoin pour commencer à amener les données dans React !

### Partie 3 : React

![Image](https://cdn-media-1.freecodecamp.org/images/1*qKj1pMwgVFGtOID_wD1N-g.png)

Pour récupérer des données externes en JavaScript, vous devez utiliser des promesses. Cela aura probablement des implications sur la façon dont vous souhaitez structurer vos composants React, et dans mon cas (conversion d'un projet React existant), j'ai dû réécrire une quantité importante de code.

#### Promesses en JavaScript

Les promesses en JavaScript sont utilisées pour gérer les actions asynchrones — des choses qui se produisent en dehors de l'ordre habituel étape par étape ou « synchrone » d'exécution (après le hissage).

La bonne nouvelle est que le JavaScript asynchrone est beaucoup plus facile qu'avant. Avant ES6, nous dépendions des fonctions de rappel. Si plusieurs rappels étaient nécessaires (et ils l'étaient souvent), l'imbrication conduisait à un code très difficile à lire, à mettre à l'échelle et à déboguer — un phénomène parfois connu sous le nom d'enfer des rappels, ou la pyramide de la mort !

Les promesses ont été introduites dans ES6 (ou ES2015) pour résoudre ce problème, et ES8 (ou ES2018) a vu l'introduction de `async ... await`, deux mots-clés qui simplifient davantage la fonctionnalité asynchrone. Mais pour nos besoins, la méthode basée sur les promesses la plus critique est `fetch()`.

#### La méthode Fetch

Cette méthode est disponible depuis Chrome 40, et il s'agit d'une alternative plus facile à utiliser que `XMLHttpRequest()`.

`fetch()` retourne une promesse et est donc « thenable », ce qui signifie que vous pouvez utiliser la méthode `then()` pour traiter le résultat.

Vous pouvez ajouter fetch à une méthode à l'intérieur de votre composant de classe React, comme ceci :

```
fetchPostData() {  fetch(`http://localhost/yoursitename/wp-json/wp/v2/movies?per_page=100`)  .then(response => response.json())  .then(myJSON => {  // La logique va ici});}
```

Dans le code ci-dessus, deux choses sont importantes :

* Tout d'abord, nous appelons une URL avec le filtre `?per_page=100` ajouté à la fin. Par défaut, WordPress ne montre que 10 éléments par page, et je me retrouve souvent à vouloir augmenter cette limite.
* Deuxièmement, avant de traiter nos données, nous utilisons la méthode `.json()`. Cette méthode est utilisée principalement en relation avec `fetch()`, et elle retourne les données sous forme de promesse et analyse le texte du corps en tant que JSON.

Dans la plupart des cas, nous voudrons exécuter cette fonction dès que notre composant React a été monté, et nous pouvons spécifier cela en utilisant la méthode `componentDidMount()` :

```
componentDidMount() {  this.fetchPostData();}
```

#### Gestion des promesses

Une fois que vous avez retourné une promesse, vous devez être prudent quant à la manière de la gérer dans le bon contexte.

Lorsque j'ai essayé d'utiliser des promesses pour la première fois, j'ai passé un certain temps à essayer de passer ces données à des variables en dehors de la portée de la promesse. Voici quelques règles de base :

* Dans React, la meilleure façon d'utiliser les promesses est via l'état. Vous pouvez utiliser `this.setState()` pour passer les données de la promesse dans l'état de votre composant.
* Il est préférable de traiter, trier et réorganiser vos données dans une série de méthodes `then()` suivant le `fetch()` initial. Une fois que tout traitement est terminé, il est bon de pratique d'ajouter les données à l'état dans votre méthode `then()` finale.
* Si vous voulez appeler des fonctions supplémentaires pour traiter votre promesse (y compris dans `render()`), il est bon de pratique d'empêcher la fonction de s'exécuter jusqu'à ce que la promesse soit résolue.
* Ainsi, par exemple, si vous passez votre promesse à `this.state.data`, vous pouvez inclure une conditionnelle dans le corps de toute fonction qui en dépend, comme ci-dessous. Cela peut prévenir des comportements indésirables et ennuyeux !

```
myPromiseMethod() {  if (this.state.data) {    // traiter la promesse ici   } else {    // quoi faire avant que le fetch ne soit réussi  }}
```

### Un exemple fonctionnel en React

Supposons que nous voulons récupérer le `name`, `description`, `featured_image` et `genre` du type de publication personnalisé WordPress que nous avons défini dans la partie 1.

Dans l'exemple suivant, nous allons récupérer ces quatre éléments pour chaque film et les rendre.

Comme c'est souvent le cas avec les tutoriels React, le bloc de code suivant peut sembler intimidant, mais j'espère qu'il semblera beaucoup plus simple lorsque nous le décomposerons.

#### constructor(props)

Dans cette méthode, nous appelons `super(props)`, définissons notre état initial (un objet `data` vide) et liaisons trois nouvelles méthodes :

* `fetchPostData()`
* `renderMovies()`
* `populatePageAfterFetch()`

#### componentDidMount()

Nous voulons récupérer nos données dès que le composant est monté, donc nous allons appeler `fetchPostData()` ici.

#### fetchPostData()

Nous récupérons le JSON de notre URL, en passant `.json()` dans la première méthode `.then()`.

Dans la deuxième méthode `.then()`, nous extrayons les quatre valeurs que nous voulons pour chaque entrée de film que nous avons récupérée et les ajoutons ensuite à notre objet `newState`.

Nous utilisons ensuite `this.setState(newState)` pour ajouter ces informations à `this.state.data`.

#### renderMovies()

La conditionnelle `if (this.state.data)` signifie que la fonction ne s'exécutera qu'une fois les données récupérées.

Ici, nous prenons un tableau de tous nos films récupérés à partir de `this.state.data` et le passons à la fonction `populatePageAfterFetch()`.

#### populatePageAfterFetch()

Dans cette fonction, nous préparons les données de chaque film à être rendues. Cela devrait sembler simple pour quiconque a utilisé JSX, avec un bloc potentiel.

La valeur de `movie.description` n'est pas du texte brut, mais du balisage HTML. Pour l'afficher, nous pouvons utiliser `dangerouslySetInnerHTML={{__html: movie.description}}`.

**Note :** _La raison pour laquelle cela est potentiellement « dangereux » est que, si vos données étaient détournées pour contenir des scripts XSS malveillants, ceux-ci seraient également analysés. Comme nous utilisons notre propre serveur/CMS dans cet article, nous n'avons pas à nous en soucier. Mais si vous souhaitez nettoyer votre HTML, consultez [DOMPurify](https://github.com/cure53/DOMPurify)._

#### render()

Enfin, nous contrôlons où nos données rendues apparaîtront en appelant la méthode `renderMovies()` dans nos balises `<div>` choisies. Nous avons maintenant réussi à récupérer des données de notre site WordPress et à les afficher !

### Conclusion

Dans l'ensemble, j'espère que cet article rend le processus de connexion d'un front-end React à un back-end WordPress aussi indolore que possible.

Comme tant de choses en programmation, ce qui peut sembler intimidant au début devient rapidement une seconde nature avec la pratique !

Je serais très intéressé d'entendre parler de vos propres expériences en utilisant WordPress comme un CMS headless, et je suis heureux de répondre à toutes les questions dans les commentaires.