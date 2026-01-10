---
title: Comment créer un plugin WordPress pour votre application web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-28T21:58:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-wordpress-plugin-for-your-web-app-5c31733f3a9d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wXmt_4PB07yn2zG5zgNOSg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: SaaS
  slug: saas
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: WordPress
  slug: wordpress
seo_title: Comment créer un plugin WordPress pour votre application web
seo_desc: 'By Feedier by Alkalab

  Today, we are going to see how to create a very simple WordPress plugin for any
  web app that needs to insert a piece of code to your site.


  _Credits: [https://unsplash.com/photos/I8OhOu-wLO4](https://unsplash.com/photos/I8OhOu-w...'
---

Par Feedier by Alkalab

Aujourd'hui, nous allons voir comment créer un plugin WordPress très simple pour toute application web qui doit insérer un morceau de code sur votre site.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wXmt_4PB07yn2zG5zgNOSg.jpeg)
_Crédits : [https://unsplash.com/photos/I8OhOu-wLO4](https://unsplash.com/photos/I8OhOu-wLO4" rel="noopener" target="_blank" title=")_

Pour suivre ce tutoriel, vous avez besoin de quelques connaissances de base :

* **PHP** et POO
* **JavaScript** (nous utiliserons jQuery et Ajax)
* **Développement WordPress** (car la plupart des fonctions proviennent du cœur de WordPress).

Vous pouvez trouver un résultat fonctionnel de ce tutoriel sur [ce dépôt Github](http://pxlme.me/611bFPFB).

Ces applications web peuvent être n'importe quoi, comme [CrazyEgg](http://crazyegg.com/), [Freshbook](https://freshdesk.com/), [Google Analytics](https://analytics.google.com/analytics/web/), [Facebook Pixel](https://www.facebook.com/business/a/facebook-pixel), ou [Feedier](https://feedier.com/). Pourquoi ? Elles doivent toutes injecter du code HTML/JavaScript sur votre site pour diverses raisons.

Ce « code » est toujours paramétré avec des variables, et est généralement une source de tracas pour le propriétaire du site. Cela est dû au fait que vous devez modifier les templates du thème. Alors, pourquoi ne pas créer un plugin pour le faire à notre place ? D'accord, faisons-le !

### Étape 1 : Trouver votre application web

L'objectif de ce tutoriel est de créer un plugin WordPress qui ajoute une page d'administration WordPress. De plus, nous ajouterons également des paramètres pour configurer le widget de l'application sur le site et injecter automatiquement le code HTML/JS dans notre page web. Rien de compliqué, juste quelque chose qui fonctionne bien.

**Veuillez noter : nous avons besoin d'une application web pour ce tutoriel.** Nous utiliserons [Feedier](https://feedier.com/?utm_medium=article&utm_source=medium&utm_campaign=medium-wordpress-awareness-2018-05-21&utm_content=how-to-create-a-wordpress-plugin-for-your-web-app) pour cet exemple. Cependant, si vous avez une autre application web que vous souhaitez utiliser dans ce tutoriel, n'hésitez pas. Il suffit de renommer tout ce qui est nommé « feedier » avec le nom de votre application et d'adapter les paramètres à ce dont cette application a besoin. La plupart d'entre elles vous donneront un extrait de code à ajouter à votre site pour la faire fonctionner.

Voici une brève présentation de [Feedier](https://feedier.com/?utm_medium=article&utm_source=medium&utm_campaign=medium-wordpress-awareness-2018-05-21&utm_content=how-to-create-a-wordpress-plugin-for-your-web-app) si vous n'en avez jamais entendu parler :

* C'est un outil de collecte de feedback, utilisant des enquêtes pour comprendre vos utilisateurs
* Il est très flexible
* _Il est gratuit !_
* **A une bonne API** (très important ici)
* **A un widget intégré au site** (très important ici)
* Vous permet de récompenser vos clients
* Vous permet de créer des questions conditionnelles
* Dispose d'un tableau de bord complet de rapports analytiques
* Vous permet de gérer les feedbacks individuellement

Voici le widget que nous voulons ajouter automatiquement :

![Image](https://cdn-media-1.freecodecamp.org/images/0*c2GG9QpqM6aMth9s.jpg)
_Aperçu du widget sur woffice.io_

Si vous vous êtes inscrit à Feedier, vous pouvez simplement trouver le code dans l'onglet Partager de votre enquête :

![Image](https://cdn-media-1.freecodecamp.org/images/0*CIKS52RyV3b0DYy9.jpg)
_Récupérez l'extrait de code depuis [feedier.com](https://feedier.com/?utm_medium=article&amp;utm_source=medium&amp;utm_campaign=medium-wordpress-awareness-2018-05-21&amp;utm_content=how-to-create-a-wordpress-plugin-for-your-web-app" rel="noopener" target="_blank" title=")_

### Étape 2 : Configurer notre plugin et son architecture

Les plugins WordPress sont par conception très simples. Notre plugin n'aura besoin que de deux fichiers.

* **feedier.php** : fichier PHP principal du plugin.
* **assets/js/admin.js** : script JavaScript pour sauvegarder les options en utilisant Ajax.

Vous pouvez créer un nouveau répertoire « feedier » (ou le nom de votre application web) dans votre dossier **wp-content/plugins/**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_n_Hxi7MHCqjzoO9.jpg)

Le fichier le plus important sera la classe **feedier.php** du plugin. Voici sa structure :

Nous faisons quelques choses ici :

* Déclarer notre plugin en utilisant les commentaires d'en-tête
* Définir quelques constantes pratiques pour pouvoir trouver facilement l'URL et le chemin du plugin
* Déclarer notre classe de plugin qui contiendra tout ce dont nous avons besoin dans ce plugin. Nous avons juste besoin d'une méthode de constructeur pour l'instant.

Vous devriez déjà voir le plugin dans votre page Plugins, même s'il ne fait encore rien :

![Image](https://cdn-media-1.freecodecamp.org/images/0*9zBfprPe_aLld2TY.jpg)
_Activez le plugin depuis le panneau d'administration WordPress_

### Étape 3 : Créer notre page d'administration

Pour cette partie, nous allons ajouter une nouvelle page d'administration Feedier à notre site WordPress et récupérer dynamiquement nos enquêtes depuis l'API de Feedier.

Dans le constructeur de notre classe, enregistrons trois nouvelles actions qui sont nécessaires pour ajouter une page d'administration sur WordPress :

* **addAdminMenu** ajoutera une nouvelle page dans le menu de gauche de WordPress. Il y aura également un rappel vers une autre méthode contenant le contenu de la page.
* **storeAdminData** sera appelé chaque fois que l'utilisateur clique sur le bouton « Enregistrer les paramètres ».
* **addAdminScripts** enregistrera un nouveau fichier JavaScript dans notre administration WordPress afin de sauvegarder les données du formulaire. Mais il échange également quelques variables entre le côté PHP et le côté JavaScript.

La première étape est très facile. Nous enregistrons simplement la page, comme ceci :

Comme vous pouvez le voir, nous utilisons les [fonctions de localisation de WordPress](https://codex.wordpress.org/I18n_for_WordPress_Developers) pour _toutes_ les chaînes de caractères. Notez que le

```
array($this, 'adminLayout')
```

est l'endroit où nous appelons une autre méthode contenant le contenu de la page. Le formulaire doit être adapté à votre application web.

Ici, nous devons d'abord obtenir les clés d'API publique et privée de Feedier. Une fois sauvegardées, nous allons utiliser la clé privée pour récupérer dynamiquement nos enquêtes. Chaque fois que nous obtenons les enquêtes et non une erreur d'API, nous affichons de nouvelles options pour configurer le widget.

Au début de cette méthode, vous pouvez voir que nous récupérons d'abord les données sauvegardées avec :

```
$data = $this->getData();
```

Et nous obtenons les enquêtes depuis l'API de Feedier :

```
$surveys = $this->getSurveys($data['private_key']);
```

Alors déclarons la première :

Cette fonction lit simplement l'option de notre plugin et nous renvoie un tableau afin que nous puissions sauvegarder plusieurs valeurs dans la même option.

Pour que la deuxième méthode fonctionne, nous avons besoin de la clé privée de Feedier. Cela dépend de la première pour accéder à cette clé sauvegardée dans l'option :

L'API de Feedier est documentée [ici](https://feedier.docs.apiary.io/#reference/0/carrier-collection/get-a-list-of-carriers), donc vous pouvez voir ce que vous obtiendrez dans la réponse.

À ce stade, nous avons une nouvelle page d'administration complète. Mais rien ne se passe lorsque nous cliquons sur le bouton d'enregistrement, car il n'y a pas encore de mécanisme de sauvegarde.

![Image](https://cdn-media-1.freecodecamp.org/images/0*B9v_zAYSu7-4pa-u.jpg)

Très bien, sauvegardons nos données !

Comme mentionné précédemment, nous allons sauvegarder nos données en utilisant AJAX. Par conséquent, nous devons enregistrer un nouveau fichier JavaScript et échanger des données en utilisant la fonction [wp_localize_script()](https://codex.wordpress.org/Function_Reference/wp_localize_script) :

Nous devons également ajouter un nouveau fichier **/assets/js/admin.js**. Cela fera simplement un appel Ajax, et WordPress acheminera automatiquement la requête correctement vers la bonne méthode (déjà fait dans le constructeur). Vous pouvez en lire plus sur la façon dont WordPress gère intelligemment les requêtes AJAX [ici](https://codex.wordpress.org/AJAX_in_Plugins).

À ce moment précis, nous pouvons cliquer sur le bouton d'enregistrement et le script ci-dessus fera une requête HTTP POST à WordPress. Nous ajoutons également un paramètre d'action contenant : **store_admin_data** (que nous avons déclaré au début de cette partie dans le constructeur) :

```
add_action( 'wp_ajax_store_admin_data', array( $this, 'storeAdminData' ) );
```

La méthode **storeAdminData** recevra la requête POST et sauvegardera les valeurs dont nous avons besoin dans notre option WordPress.

Quelques notes sur la méthode ci-dessus :

* Nous utilisons un « nonce WordPress » pour gérer la sécurité et nous assurer que cela provient du site web et non d'un pirate informatique falsifiant la requête.
* Nous identifions les champs que nous devons sauvegarder en utilisant un préfixe « feedier_ ». Une fois reçus, nous parcourons toutes les données $_POST et sauvegardons uniquement ces champs. Nous supprimons également le préfixe avant de sauvegarder chaque champ.

C'est tout pour le processus de sauvegarde. Lorsque nous cliquons sur sauvegarder, nous pouvons voir une requête POST et nos données étant sauvegardées dans la base de données dans la table **wp_options**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*uTVEcizHs2jERzSM.jpg)

Parfait, nous avons terminé avec la page d'administration.

### Étape 4 : Insérer le code dynamique automatiquement dans nos pages

Maintenant que nous avons nos options sauvegardées, nous pouvons créer un widget dynamique qui dépendra des options définies par l'utilisateur via notre page d'administration. Nous savons déjà ce que l'application web attend de nous.

Quelque chose comme :

```
<div class="feedier-widget" data-type="engager" data-position="right" data-carrier-id="x" data-key="xxxxxxxxxxxxxxxxx"></div>
```

```
<! -- Inclure cette ligne une seule fois, même si vous avez plusieurs widgets sur la page actuelle -->
```

```
<script src="https://feedier.com/js/widgets/widgets.min.js" type="text/javascript" async></script>
```

Ainsi, la première chose que nous voulons faire est de créer une nouvelle méthode pour notre plugin qui imprimera ce code en fonction des variables définies par l'utilisateur. Donc, en utilisant l'architecture que nous avons déjà mise en place dans la dernière partie :

Maintenant, nous devons simplement appeler cette fonction à chaque chargement de page pour l'ajouter en bas de la page. Pour ce faire, nous allons accrocher notre méthode à l'action **wp_footer**. En enregistrant une nouvelle action dans le constructeur de notre classe :

C'est tout !

Des questions, des commentaires ou des idées ? Faites-le moi savoir dans les commentaires !

Vous pouvez trouver une version fonctionnelle de ce tutoriel sur [ce dépôt Github](http://pxlme.me/611bFPFB).

[**2Fwebd/feedier-wordpress-plugin**](http://pxlme.me/611bFPFB)
[_Contribuez au développement de feedier-wordpress-plugin en créant un compte sur GitHub._pxlme.me](http://pxlme.me/611bFPFB)

Notez que ceci est la première version du plugin, et que de nombreuses choses peuvent être améliorées. Je suis ouvert aux suggestions et aux améliorations. ?

Nous construisons [Feedier](https://feedier.com/?utm_medium=article&utm_source=medium&utm_campaign=medium-wordpress-awareness-2018-05-21&utm_content=how-to-create-a-wordpress-plugin-for-your-web-app). Cela devient un jeu d'enfant pour collecter des feedbacks et construire des relations avec vos clients !

[**Feedier - La prochaine génération de feedback**](https://feedier.com/?utm_medium=article&utm_source=medium&utm_campaign=medium-wordpress-awareness-2018-05-21&utm_content=how-to-create-a-wordpress-plugin-for-your-web-app)
[_Rencontrez Feedier, le logiciel de feedback client de nouvelle génération qui vous permet de collecter des feedbacks précieux. Récompensez, engagez..._feedier.com](https://feedier.com/?utm_medium=article&utm_source=medium&utm_campaign=medium-wordpress-awareness-2018-05-21&utm_content=how-to-create-a-wordpress-plugin-for-your-web-app)

Convaincu ? Inscrivez-vous **gratuitement** sur [feedier.com](https://feedier.com/?utm_medium=article&utm_source=medium&utm_campaign=medium-wordpress-awareness-2018-05-21&utm_content=how-to-create-a-wordpress-plugin-for-your-web-app) ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*euK96ycNbjw9yVMXgflmLg.gif)
_[Feedier.com](https://feedier.com/?utm_medium=article&amp;utm_source=medium&amp;utm_campaign=medium-wordpress-awareness-2018-05-21&amp;utm_content=how-to-create-a-wordpress-plugin-for-your-web-app" rel="noopener" target="_blank" title="), l'application de **feedback** de nouvelle génération. **Commencez gratuitement maintenant !**_

N'oubliez pas d'applaudir notre article et de [vous abonner](https://alka-web.us16.list-manage.com/subscribe?u=cd5291c429df8270607277d16&id=42520def8c) pour obtenir plus d'articles incroyables si vous l'avez aimé ?. Vous pouvez également nous trouver sur T[witter.](http://pxlme.me/_dw36YLw)

_Cet article a été initialement publié sur notre [blog ici.](https://alkalab.com/blog/tutorial-wordpress-plugin-web-app/)_