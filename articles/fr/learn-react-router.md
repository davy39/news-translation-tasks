---
title: Apprendre React Router
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-06-30T14:01:01.000Z'
originalURL: https://freecodecamp.org/news/learn-react-router
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/reactrouter.png
tags:
- name: React
  slug: react
- name: youtube
  slug: youtube
seo_title: Apprendre React Router
seo_desc: 'React Router is commonly used to make different routes for pages in React
  Applications.

  We just released a crash course on the freeCodeCamp.org YouTube channel that will
  teach you how to create routes in your React applications.

  Piyush Agarwal develo...'
---

React Router est couramment utilisé pour créer différentes routes pour les pages dans les applications React.

Nous venons de publier un cours accéléré sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à créer des routes dans vos applications React.

Piyush Agarwal a développé ce cours. Piyush est un créateur de cours prolifique sur sa chaîne YouTube et est très expérimenté avec React.

Ce cours couvre BrowserRouter, Switch, l'imbrication des routes et la redirection des routes. Il couvre également les props match et history, y compris les hooks useHistory, useParams, useLocation et useRouteMatch.

Voici les sujets abordés dans ce cours :

* Initialiser une nouvelle application React
* Composant Header
* Installation de React Router
* BrowserRouter
* Création de routes
* Test des routes
* Prop 'exact'
* Balise Switch
* Balise Link
* Prop basename
* Prop forceRefresh
* getUserConfirmation
* Faire défiler vers le haut lors du changement de route
* Page 404 Non Trouvée
* Accéder aux paramètres d'URL
* Hook useParams
* Hook useLocation
* Redirection dans React Router
* Hook useHistory
* Routage imbriqué

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://youtu.be/Jppuj6M1sJ4) (1 heure de visionnage).

%[https://youtu.be/Jppuj6M1sJ4]

## Transcription

(générée automatiquement)

React router est couramment utilisé pour créer différentes routes pour les pages dans les applications React.

Ce cours vous apprendra à utiliser React Router pour créer vos propres routes dans React. Nous allons apprendre à propos de React Router et de ses différents concepts, tels que la création de différentes routes pour différentes pages dans React.

De plus, nous allons apprendre à imbriquer une route d'une page sous une autre page.

Les hooks comme useHistory, useParams, useLocation et useRouteMatch, ainsi que comment récupérer une chaîne de requête sous forme de variable à partir de l'URL.

Alors, commençons.

D'accord, commençons par créer une nouvelle application React.

Je vais taper NP x create react app, et le nom de notre application, que je vais donner react router tutorial.

Maintenant, ce qu'il va faire, c'est aller sur le site web de NPM ou le dépôt NPM et prendre toutes les choses nécessaires pour créer une nouvelle application React.

Et il va mettre toutes ces choses dans ce dossier, React router tutorial, il va trouver toutes les dépendances dont nous avons besoin pour créer notre application React.

Et il va essentiellement initialiser un code boilerplate pour notre application React.

D'accord, il a réussi à initialiser notre nouvelle application React.

Maintenant, nous devons passer à ce dossier, ce que nous pouvons faire, c'est soit taper cd, et le nom du dossier, vous pouvez passer de cette manière.

Ou ce que vous pouvez faire, c'est ouvrir ce dossier dans VS code, qui dans mon cas est ce dossier.

Et je vais sélectionner ce dossier.

Alors, voici.

Le dossier a été ouvert dans VS code avec succès.

Alors, ce que je vais faire maintenant, c'est taper NPM start.

Donc, il va démarrer notre application React.

Voici notre application React qui fonctionne avec succès.

Alors, ce que je vais faire maintenant, c'est que je vais aller dans le dossier src.

Et je vais me débarrasser de ces choses dont nous n'avons pas besoin, de ceci, de ceci et de ceci, nous allons nous débarrasser de ces quatre fichiers.

Et nous allons supprimer les endroits où ils étaient utilisés.

Donc, par ici.

Et nous allons nous débarrasser de tous ces styles.

Dans app j s, app dot j s, je vais me débarrasser de ceci.

Me débarrasser du logo.

Et maintenant, vous verrez que notre application n'a rien à afficher.

Me rafraîchir.

Oui, voilà.

C'est une page vide.

D'accord, alors ce que je vais faire maintenant, c'est taper h1, h1, react, router Dom tutorial, pour ce tutoriel React Router.

Enregistrons cela et voyons.

Oui, il a réussi à rendre cela ici.

Alors, créons un composant différent pour l'en-tête.

Lorsque vous créez un nouveau composant appelé un nouveau dossier appelé components, il n'est pas nécessaire de créer un dossier séparé pour les composants, mais c'est une bonne pratique.

Je vais créer un composant différent pour header dot j, s.

Et je vais taper notre A, F, C underscore RFC et appuyer sur Entrée.

Et copions la même chose.

Nous y voilà.

Centrons d'abord cet élément.

Et ensuite, nous allons commencer avec notre tutoriel.

Alors, je vais lui donner quelques styles dans app dot CSS.

Je vais me débarrasser de notre display flex et justify content.

Non, désolé.

Je veux dire align items to center et flex direction est going to be column parce que nous voulons que tout soit de haut en bas.

Vous savez, aligné.

Alors, oui, nous y voilà.

Vous êtes bien.

C'est au centre.

Alors, oui, je n'ai pas fait cela.

Importé le composant header.

Oui.

Header n'est pas défini.

Importons-le manuellement.

Nous y voilà.

Cela devrait fonctionner correctement maintenant.

Oui, nous y voilà.

Cela fonctionne bien.

Alors maintenant, nous allons installer react router DOM.

Alors, je vais ouvrir un nouveau terminal et taper NPM I react router DOM.

Et vous savez quoi, je vais aller dans header et me débarrasser de ce dev. Utilisons le React fragment.

Alors, si vous ne savez pas ce qu'est un fragment React, vous pouvez regarder ma vidéo précédente sur les huit pratiques de code propre dans React, cela va vous aider beaucoup 2000 ans plus tard, ou c'est enfin un react router Dom qui est installé avec succès.

Alors, je vais aller dans mon composant App JS.

Et pour utiliser notre react router DOM, ce que nous devons faire, c'est que nous allons devoir couvrir toute cette application React dans quelque chose appelé browser router, browser router, qui provient de react router DOM, donc vous pouvez voir qu'il s'est auto-importé.

Alors, je vais mettre mon application dans cela.

D'accord, nous y voilà.

Fermons ce terminal.

Je pense que je vais devoir redémarrer mon application.

Alors, faisons cela rapidement.

D'accord, c'est bon maintenant.

Alors, que allons-nous faire ensuite ? Nous allons créer différentes routes pour différentes pages avec lesquelles nous allons travailler.

Alors, créons une route pour la page d'accueil, la page à propos et la page de profil.

Oui, alors je vais taper route et appuyer sur Entrée.

Et vous pouvez voir que route s'est auto-importé de VS code provenant de react router, Dom VS code l'a auto-importé.

Alors, je vais lui donner un chemin.

Cela va être votre page d'accueil.

Alors, ce sera ceci.

Et nous devons lui donner un composant, que nous créerons dans une seconde.

Alors, dupliquons ces chemins.

Un autre sera pour à propos.

Et le troisième sera pour profil.

Alors, créons ces pages.

Tout d'abord, je vais créer un nouveau dossier avec le nom de pages.

Home dot j s, je vais créer un fichier appelé about dot j s.

Et le troisième fichier sera profile dot j s.

Ensuite, laissez-moi écrire rapidement du code à l'intérieur de ce type de page d'accueil.

Supprimez ces divs et ajoutez h1.

Ensuite, même chose avec la page à propos.

Page à propos.

Et la page de profil.

D'accord, bien.

Page de profil.

D'accord, cool.

Alors, nous avons créé toutes nos trois routes.

Maintenant, testons ces routes pour voir si elles fonctionnent ou non.

Alors, laissez-moi sauvegarder mon application rapidement.

D'accord, il y a une annonce de théâtre.

D'accord, nous n'avons même pas les composants, évidemment.

Alors, donnons simplement à cela un composant home.

Oh, désolé.

Ma faute, nous devons d'abord importer tous ces composants.

Alors, importer home depuis slash home.

Et je vais faire de même pour about et profile.

Alors, about et profile.

Laissez-moi simplement m'incliner et mettre hors tension cinq.

Nous y voilà.

Alors, nous avons créé trois routes.

C'est ainsi que vous créez une route dans React en utilisant react router DOM.

Alors, vous pouvez voir qu'il est actuellement dans le dossier racine, je veux dire, dans le chemin racine.

Alors, il nous donne la page d'accueil.

Allons à la route de la page à propos.

La voici, elle nous donne à propos, mais vous pouvez voir que la page d'accueil apparaît également ici et que la page à propos apparaît également ici.

Pourquoi cela se produit-il ? Parce que vous pouvez voir qu'il a également la page à propos.

Et cette route également.

Dans cette tache init, elle a également une route.

Alors, ce que nous pouvons faire, c'est taper exact, donc il va aller exactement à ce chemin et nulle part ailleurs.

Alors, si on tape à propos, il va cliquer pour ouvrir la page à propos.

Et si vous tapez profil, il va aller travailler.

D'accord, j'ai fait cette erreur.

Oui, maintenant cela va fonctionner correctement.

Si je vais à la page de profil, cela va ouvrir la page de profil.

Une autre chose que vous pouvez faire en plus de exact, c'est que vous pouvez utiliser quelque chose appelé switch.

Alors, si je tape switch ici, et nous allons prendre ces trois à l'intérieur du switch, et j'ai importé le switch depuis react router DOM.

Alors, ce que fait switch, c'est que lorsque vous allez à un chemin particulier, laissez-moi supprimer cet exact d'ici.

Alors, il va trouver ce qu'il trouve en premier et va s'arrêter là.

Par exemple, il a écrit slash profil.

Alors, il a trouvé le chemin slash en premier, il a fait correspondre ce chemin slash avec celui-ci.

Alors, il a trouvé que la page d'accueil va être rendue si nous utilisons Switch Murphy tape exact, alors nous n'allons pas avoir le même problème maintenant.

Vous pouvez voir qu'il rend le profil.

Maintenant, laissez-moi taper à propos.

D'accord, voici la page à propos.

D'accord, une chose de plus.

Alors, nous n'avons pas besoin de taper cela manuellement dans l'URL.

Alors, que pouvons-nous faire pour aller à une autre page, dans le développement web traditionnel en HTML, nous utilisons quelque chose appelé une balise a pour aller à une page différente.

Alors, nous pouvons utiliser cela ici aussi.

Mais cela a un inconvénient, quel est cet inconvénient, lorsque nous cliquons sur cette balise a, elle va rafraîchir notre page, laissez-moi démontrer cela.

Alors, je vais aller dans notre en-tête, je vais créer un menu de navigation pour notre application.

Laissez-moi créer une liste non ordonnée ici.

Je vais créer quelques éléments de liste, et avoir une nouvelle balise à l'intérieur avec h ref d'un partenaire d'abord va être la page d'accueil.

Alors, tapons slash ici et donnons-lui un nom de home.

D'accord, alors je vais dupliquer cela plusieurs fois, et donner à cela à propos de cela semble obtenir un profil, et profil.

Enregistrons cela.

Actuellement, cela a l'air un peu moche.

Alors, je vais lui donner un peu de style.

Alors, allons dans notre app CSS.

Et je vais ajouter un peu de style.

Laissez-moi lui donner un nom de classe.

Tout d'abord, je vais lui donner ce nom de classe de now.

Oui.

Donnons-lui quelques styles.

Alors, je vais taper list style type est going to be none so that it doesn't displace the bullet.

Et je vais taper width to be 500 pixels.

Alors, je vais taper display, flex et justify content to be spaced evenly swear it spreads around evenly.

Maintenant, vous verrez, oui, il s'est répandu autour de manière uniforme.

Maintenant, cliquons sur l'un de ces liens.

Si je vais cliquer sur home, vous pouvez voir que la page a été rafraîchie ici.

Si je clique sur profil, encore une fois, la page a été rafraîchie, nous avons atteint la destination mais la page a été rafraîchie.

Nous ne voulons pas que la page soit rafraîchie.

Nous ne voulons pas que nos composants soient re-rendus.

Alors, que allons-nous faire maintenant.

Alors, au lieu de cette balise a, ce que je vais faire, c'est que j'utiliserai quelque chose appelé link, qui nous est fourni par react router DOM.

Cliquons sur ce lien.

Et vous pouvez voir qu'il s'est auto-importé.

Alors, ici aussi.

Lien.

Et enfin, oui.

Ce que nous ne pouvons pas utiliser h ref avec le lien, nous devons utiliser quelque chose appelé to.

C'est la prop qu'il prend.

Alors, enregistrons cela.

D'accord, notre application a été rechargée.

Et cliquons sur À propos.

Maintenant, vous pouvez voir que la page n'a pas été rafraîchie si je clique sur home, encore une fois.

Alors, vous voyez, c'est la puissance de react router DOM, il ne rafraîchit pas votre page, et il vous emmène à une autre page en un clin d'œil.

D'accord, cool.

Alors, discutons de quelques autres fonctionnalités de cette bibliothèque.

Alors, voyons, si je veux une route par défaut pour notre application.

Maintenant, ce que je veux dire par là, laissez-moi donner un nom de base ici.

Si je donne le nom de base comme tutoriel, et enregistre cela maintenant, vous voyez si je clique sur la page d'accueil, cela va nous emmener à slash tutoriel.

Si je clique sur À propos, cela va prendre slash tutoriel slash à propos, donc c'est ainsi que vous pouvez définir un nom de base pour cela en tapant base name equals whatever the name that you need to use.

Si je clique sur profil, cela va nous emmener slash tutoriel slash profil.

Alors, c'est une fonctionnalité vraiment puissante.

Vérifions une autre fonctionnalité du browser router.

Je vais supprimer cela.

Et disons que pour une raison quelconque, vous devez utiliser la fonctionnalité de rafraîchissement.

Actuellement, il ne rafraîchit pas notre page lorsque je l'emmène à une autre route.

Alors, si je tape force refresh ici, alors vous verrez ce qu'il fait.

Si je vais à propos, vous pouvez voir que la page se rafraîchit maintenant, elle fournit le rafraîchissement forcé pour ré-exécuter tout.

Alors, vous pouvez utiliser force refresh pour cela, ce que je ne pense pas que quelqu'un ait besoin d'utiliser.

De plus, si vous voulez confirmer chaque fois qu'un utilisateur va à une autre route, par exemple, si je clique sur À propos, vous devez le confirmer par une invite ou en affichant une modale, ce que vous pouvez utiliser s'appelle get user confirmation.

Vous pouvez taper get user confirmation, et ensuite à l'intérieur de cela, vous pouvez écrire un message de classe à afficher chaque fois que la route change.

Alors, je vais écrire une fonction à l'intérieur en tapant message, whoops message.

Et il va prendre un callback qui va être une fonction fléchée.

Le callback va prendre window, dot confirm.

Et vous pouvez passer n'importe quel composant que vous devez passer à l'intérieur.

Disons que si vous créez une invite, vous pouvez passer à l'intérieur une invite ou une modale, mais je ne pense pas que cela soit utilisé autant non plus.

Alors, c'est l'une des fonctionnalités que vous pouvez utiliser dans react router DOM.

Alors, supprimons cela.

Oui.

D'accord, avançons.

Tout d'abord, je veux me débarrasser de ces styles des liens.

Je ne veux pas de ce style.

Alors, je vais aller dans App dot CSS, et supprimer les styles en tapant a enlevant text decoration.

Et go alone sera hérité.

Oui, bien.

Voyez, nos pages ne sont pas si grandes.

En ce moment.

Si vous allez à la page d'accueil, ou si vous allez à la page de profil, sa hauteur n'est pas si grande en ce moment.

Mais disons que votre page est si grande que vous devez faire défiler vers le bas.

Alors, chaque fois que vous changez votre route, ce qui va se passer, c'est qu'il va continuer l'autre page à partir de la même position.

Si c'est ce que vous voulez faire dans ce cas, chaque fois que vous allez à un composant différent, vous pouvez taper comme ceci.

Laissez-moi simplement aller ici à la page d'accueil.

Et vous, ce que je peux faire, c'est que je peux utiliser use effect.

Et au lieu de use effect, je peux taper window dot scroll to zero comma zero.

Alors, il va continuer l'autre page à partir du haut et non de la position précédente que la page avait lorsque vous étiez dans l'autre composant.

Alors, c'est utile.

D'accord, alors la prochaine chose importante est si lorsque nous tapons vers une autre route qui n'existe pas, en ce moment, laissez-moi dire n'importe quoi comme quelque chose, et entrer, vous pouvez voir qu'il n'y a rien qui est affiché ici.

Nous voulons que quelque chose s'affiche ici, comme une erreur 404 page non trouvée quelque chose comme ça.

Alors, comment pouvons-nous afficher cela ici ? Laissez-moi créer une nouvelle page pour cela.

Je vais créer une nouvelle commande pour une nouvelle page appelée not found dot j s.

D'accord ? Initialisons cette page, A, C, appuyez sur Entrée.

Et je vais lui donner un h1 de quatre livres 404.

Non Trouvé.

Enregistrons cela.

Maintenant, comment pouvons-nous utiliser cela ? Maintenant, nous devons aller ici et fermer cela ? Oui, nous devons aller ici, nous devons créer une autre route, nous avons créé une autre route.

Dans ce cas, nous ne allons pas lui donner aucun des chemins tels que à propos de notre profil ou autre chose, nous allons simplement lui donner un composant non trouvé.

Et nous allons l'importer manuellement.

Nous y voilà.

Nous avons importé notre page non trouvée.

Et nous y voilà.

Le message est affiché avec succès.

Si je vais ailleurs, il va toujours afficher ce message.

Si je vais à une page pertinente, comme home about profile, il ne va pas afficher de message.

D'accord, alors passons à la chose suivante, qui consiste à prendre des paramètres à partir de l'URL.

Alors, disons que si je veux une page comme quelque chose appelé post, et nous voulons un post aléatoire.

Alors, nous voulons que cet ID aléatoire soit accessible par nous.

Alors, que pouvons-nous faire ici.

Actuellement, il va montrer 404 non trouvé.

Alors, créons une nouvelle page pour notre post.js.

Alors, ce que nous voulons faire, c'est que nous voulons récupérer cet ID particulier.

Alors, laissez-moi taper ID est et nous allons afficher l'ID particulier.

Je vais lui donner h deux ici.

Actuellement, il ne va rien afficher si je vais à post.

D'accord, nous n'avons pas créé cela évidemment, nous devons aller à App j s et créer une autre sortie.

Nous y voilà.

Nous avons créé cette partie avec succès.

Maintenant, vous pouvez voir qu'il nous montre ID est égal à ce que nous ne pouvons rien faire si le slash tape n'importe quoi.

Il ne va pas afficher quoi que ce soit.

Alors, ce que nous devons faire maintenant, c'est slash ID.

Alors, maintenant, il va prendre un ID aléatoire de notre part.

Alors, si je vais à post maintenant, il va afficher non trouvé parce que cette page n'a pas besoin d'avoir un ID pour s'afficher.

Alors, retournons à notre pitch.

Et maintenant, nous allons utiliser notre premier hook, qui s'appelle use params.

Ou nous pouvons utiliser un match aussi, laissez-moi simplement afficher, laissez-moi simplement le démontrer avec le match d'abord.

Alors, nous allons aller ici D, D structure le match d'ici.

Et maintenant, ce que nous allons faire, c'est que nous allons aller ici et taper match dot params.

Et quel était le nom des params ? C'était ID, enregistrons cela.

Et vérifions cela.

Maintenant.

Nous y voilà.

Si je donne cela, laissez-moi taper random ici, et appuyez sur entrer.

Vous pouvez voir que l'ID est généré, et il est affiché ici.

Je veux dire, il n'est pas généré, nous l'avons fourni, mais il est affiché ici.

Oui, alors quelle est l'autre façon de faire cela.

L'autre façon de faire cela est d'utiliser le hook use params, qui nous est fourni par react router DOM.

Alors, je vais cliquer ici.

Et vous pouvez voir qu'il s'est auto-importé depuis react router DOM.

Maintenant, nous n'avons pas besoin de cela, je vais me débarrasser de cela.

Je vais utiliser use params.

D'abord, enregistrons ce use params.

Voyons, ce que nous obtenons à l'intérieur de cela.

Je vais supprimer cela maintenant.

Alors, ne pas obtenir mieux.

D'accord, enregistrons ce use params.

et inspectons cela, vous obtenez un objet.

Et cet objet a quelque chose appelé ID à l'intérieur, qui est l'ID que nous avons passé ici.

Laissez-moi taper quelque chose et appuyer.

Nous y voilà.

Il nous a donné un autre objet avec l'ID de quelque chose.

Alors, maintenant, nous allons utiliser ce use params.

Je vais taper const, ID equals use params.

Et nous allons déstructurer cet ID à l'intérieur du use params.

Alors, nous avons sorti cet ID et nous pouvons simplement utiliser cet ID ici.

Maintenant.

Enregistrons cela.

Vérifions ici, nous avons quelque chose et nous lui donnons un numéro aléatoire.

Et voici notre ID affiché avec succès.

Alors, c'est ainsi que vous pouvez récupérer l'ID à partir de l'URL.

Maintenant, disons que nous devons utiliser une, nous ne voulons pas changer notre route.

Mais nous avons toujours besoin d'utiliser les variables de l'URL.

Par exemple, si je tape un point d'interrogation, et je, disons que je tape name equals viewshe.

Disons que nous voulons ce nom, cette nouvelle façon dont nous pouvons récupérer cela à partir de l'URL ? Y a-t-il une autre façon ? Alors, nous allons utiliser notre deuxième hook appelé use location, use location, et il nous est également fourni par react router DOM.

Alors, nous allons taper use location ici, laissez-moi simplement enregistrer ce use location d'abord.

Et vérifier ce que nous obtenons à l'intérieur de cela ? Allons à inspecter.

Nous obtenons un objet.

Alors, que contient cet objet, il a un path name.

Et il a une recherche avec la valeur de name equals viewshe.

Laissez-moi taper autre chose d'abord.

equals viewshe.

Et nous pouvons taper et last equals Agarwal, qui est mon nom.

Alors, oui, voyons.

Maintenant, la valeur de search a changé en first equals fusion logic, quoi ? Maintenant, comment récupérons-nous ces variables first et last à partir de cet objet de recherche, vous savez, l'objet de recherche variable.

Alors, ce que je vais faire maintenant, nous allons utiliser une API intégrée du navigateur appelée URL search params.

Alors, je vais la sélectionner.

Et je vais taper vous êtes l search params.

Et je vais créer un objet à partir de cela.

Alors, je vais taper new URL search params.

Et que voulons-nous à l'intérieur de ce use location, nous voulons cette recherche.

Alors, tapons search.

D'accord, prenons-le dans une variable.

Laissez-moi taper const.

query equals new URL search params.

Nous y voilà.

Alors, comment sortons-nous les trucs de cette query ? Alors, laissez-moi simplement aller ici et h2.

Et nous devons utiliser le first et le last.

Alors, extrayons d'abord le first.

Alors, query dot get.

Et dans les crochets, nous devons, nous devons écrire la variable que nous devons récupérer de l'URL.

Alors, je vais taper first et sauvegarder cela.

Voyons ce qui se passe.

D'accord, nous y voilà.

Nous obtenons la page d'ici à partir du first et récupérons également le last.

Last, nous y voilà.

Alors, nous pouvons taper n'importe quel nombre de queries à l'intérieur de cette URL, et nous pouvons ensuite, en utilisant cette méthode, utiliser les hooks de localisation.

Alors, c'est plutôt cool.

Maintenant, voyons, supposons que vous avez une fonctionnalité de connexion dans votre application.

Et vous voulez que l'utilisateur accède au profil uniquement si cet utilisateur se connecte à votre application.

Alors, comment allons-nous modifier notre react router Dom selon cela, découvrons-le.

Nous allons aller à App j s.

Et nous allons créer un nouvel état, disons login.

importer l'état utilisateur depuis react, nous y voilà.

Par défaut, login sera false.

Login aura une valeur false, car nous ne sommes pas connectés maintenant, admettons, laissez-moi simplement créer un bouton ici pour se connecter.

Mais personne ne l'a créé.

Laissez-moi simplement prendre cette div et la mettre ici pour que tout soit centré.

Oui, c'est centré.

Alors, ce que je veux, c'est que lorsque je tape sur ce login, nous allons simuler une fonctionnalité de connexion en faisant de ce login vrai et il va afficher logout alors.

Alors, on click ce qu'il devrait faire, c'est qu'il devrait définir login comme la valeur opposée.

Alors, si c'est vrai, ce sera faux.

Si c'est faux, ce sera vrai.

De plus, ce que je vais afficher ici, c'est que si login est vrai, ce qui signifie que si l'utilisateur s'est connecté avec succès, alors il devrait afficher Whoa, what's happening? Oui, alors il devrait afficher logged out.

Sinon, il devrait afficher login.

Enregistrons cela.

Et voyons si cela fonctionne ou non.

D'accord, cela fonctionne bien.

Alors, que voulons-nous faire ici, si notre utilisateur n'est pas connecté, il ne pourra pas accéder à la page de profil, et il sera redirigé vers la page d'accueil.

Alors, comment pouvons-nous y parvenir, nous allons utiliser quelque chose appelé redirect depuis react router DOM.

Alors, supprimons ce composant d'ici.

comment je vais faire cela, ici, nous allons faire le composant enfant de cette route.

Alors, vérifions cela ici.

Si login est vrai, si login est vrai, alors il pourra accéder à la page de profil.

Alors, profil.

Sinon, il sera redirigé.

Alors, redirect.

Où sera-t-il redirigé ? Vers la page d'accueil.

Nous y voilà.

D'accord, essayons de cliquer sur notre page de profil.

Laissez-moi aller à la page à propos et cliquons sur la page de profil.

Vous pouvez voir que nous avons été redirigés vers la page d'accueil.

Nous ne pouvons pas accéder à la page de profil maintenant.

Mais au moment où nous appuyons sur login, et allons à la page de profil.

Maintenant.

Maintenant, nous sommes capables d'accéder à la page de profil.

Alors, elle est devenue une route protégée pour notre application.

Si je suis à l'intérieur de cette page de profil.

Et si je presse logo, voyons ce qui se passe.

Il va nous rediriger vers la page d'accueil.

Maintenant, il y a une autre façon de faire cela.

Laissez-moi vous montrer, nous pouvons utiliser quelque chose appelé US history, US history hook.

Alors, laissez-moi simplement attacher cela ici, je vais supprimer tout ce truc de redirection.

Faites-en une route normale maintenant, travaillez normalement maintenant sans login.

D'accord.

Alors, ce que je vais faire, c'est que je vais envoyer le login comme paramètre à l'intérieur de ce truc, envoyer le login comme params.

Allons au profil et déstructurons le login.

Nous y voilà.

Et créons un use effect.

Alors, utilisez l'effet de marque chaque fois que notre application est initialisée pour la première fois.

Alors, je vais prendre l'historique du hook US history.

Alors, tapons US history.

Je vais l'assigner à const.

Variable d'historique.

D'accord.

Il s'est auto-importé depuis react router DOM, qu'est-ce qui s'est passé ? D'accord, nous n'avons pas importé le US effect.

Nous y voilà.

D'accord, alors que devons-nous taper à l'intérieur du US effect, nous devons vérifier si l'utilisateur est connecté.

Ou si l'utilisateur n'est pas connecté ? Que allons-nous faire s'il n'est pas connecté ? Alors, nous utiliserons history.

Le point push va pousser ce chemin vers notre URL.

Alors, il va pousser vers la page slash qui est notre page d'accueil.

Alors, essayons cela.

Je suis à la page d'accueil, allons à la page de profil, je ne suis pas capable d'accéder à la page de profil.

Maintenant, connectons-nous.

Et allons à la page de profil.

Nous y voilà.

Nous sommes avec succès dans la page de profil.

Et déconnectons-nous maintenant.

Whoa, qu'est-ce qui s'est passé ? Je pense que j'ai manqué quelque chose.

Oui.

D'accord.

Alors, si nous voulions exécuter chaque fois que la variable login change, alors je vais fournir login ici et history, nous allons fournir ces deux dépendances à l'intérieur de l'use effect.

Chaque fois que ces deux dépendances vont changer.

Cela va déclencher cette fonction.

Essayons à nouveau, nous allons aller au profil, cela n'y va pas.

Je vais taper, je vais cliquer sur login.

Qu'est-ce que je dis aujourd'hui ? D'accord, alors allons au profil maintenant.

Nous y voilà, nous sommes capables d'accéder à la page de profil.

Déconnectons-nous.

Nous y voilà.

Nous sommes de retour à la page d'accueil, si nous voulons aller à la page à propos, à propos, disons, si l'utilisateur n'est pas connecté, va à la page à propos, si je clique sur profil, voyez, il nous redirige vers la page à propos.

Mais si vous vous connectez, allez à la page de profil.

Alors, j'espère que vous avez tous compris, vous savez cette fonctionnalité de react DOM.

Passons à la fonctionnalité suivante.

Alors, discutons de la façon dont nous pouvons créer une route imbriquée à l'intérieur d'une page particulière.

Par exemple, si à l'intérieur de la page de profil, je veux créer deux routes, avec le nom de, disons, view profile, et edit profile, et je ne veux pas que ces deux routes affectent tout notre système de routage react, nous voulons seulement qu'elles fonctionnent à l'intérieur de cette page de profil.

Alors, créons deux nouvelles routes ici.

Je vais supprimer cela, laissez-moi simplement le mettre à l'intérieur de ces parenthèses et puis fournir des fragments react à ceux-ci.

D'accord, déplaçons cela.

Oui, alors je vais créer une barre de navigation à l'intérieur d'une page de profil.

Je vais créer une balise de lien ici.

Et disons view.

Et l'autre balise de lien, va avoir entendu, edit profile, c'est aussi nous n'avons pas créé ces composants view profile Edit Profile.

Alors, nous devons également créer ceux-ci view profile.

Nous y voilà.

Nous devons lui fournir, il va aller travailler.

Alors, tout d'abord, avant de faire tout cela, créons notre route et le composant d'abord pour lire nous avons ces erreurs hors du chemin.

Alors, je vais aller en dessous de cela.

Et comme d'habitude, nous allons créer un switch.

Whoops, switch.

x even a auto-importé ou non, oui, il l'a.

D'accord, nous devons créer deux routes.

La route une aura un chemin de slash, view profile.

Et il a, il va avoir un composant que je vais créer ensuite.

Et l'autre sera le Edit Profile.

Edit Profile.

Oui.

Créons ces deux composants d'abord.

Review, proof filed ou GS a fait une faute de frappe.

reprofiled rj Qu'est-ce que c'est que ça.

br o f i l e.

Oui.

Edit profile.whoops.js.

Créons ce RFC.

Et je vais lui donner un h deux et view profile page.

Ce composant créé et remédié au profil image, Edit Profile page, donnant ce h2 aussi.

Oui, bien.

Passons à la chose suivante.

Maintenant, nous allons retourner à notre page de profil.

Et ici, nous allons aller et lui donner un to to slash Edit Profile.

Et celui-ci au view profile.

Voyons si cela fonctionne ou non.

La route n'est pas définie évidemment, les routes et les liens ne sont pas encore définis.

Alors, je vais l'importer automatiquement depuis VS code.

Avec l'aide de VS code ici, nous y voilà.

Tous ceux-ci sont importants maintenant.

D'accord, voyons.

Quelle est l'erreur ici.

Le lien n'est pas défini.

Le lien est défini.

Vous pouvez voir que le lien est défini ici.

Rencontrons, laissez-moi rafraîchir cela.

Oui, cela fonctionne bien.

Allons au profil.

D'accord, nous devons d'abord nous connecter et allons au profil.

D'accord, nous avons view profile et edit profile ici.

Mais cela ne fonctionne pas maintenant.

Mais pourquoi cela ne fonctionne-t-il pas maintenant ? Parce que nous avons déjà créé nos routes ici.

Alors, que devons-nous faire ? Alors, que devons-nous utiliser maintenant ? Parce que nous allons utiliser quelque chose appelé use route, match hook, use route match.

Alors, c'est le hook que nous allons utiliser pour nous aider, vous savez, déplacer les composants à l'intérieur d'un autre composant.

Alors, laissez-moi taper const.

Et je vais sortir quelque chose appelé path et quelque chose appelé URL de l'intérieur de cette chose.

Alors, voyons comment pouvons-nous utiliser ce path et cette URL, tout d'abord, nous voulons aller, nous ne voulons pas aller à View profile, parce qu'il nous emmène à slash edit profile ou slash view profile, nous voulons aller par exemple, si votre add profile, nous voulons prendre l'URL actuelle, et ensuite append view profile après.

Alors, ce que je vais taper ici, tout d'abord, je vais supprimer ces balises de chaîne standard, et je vais utiliser des backticks.

Oups.

Comme ça.

D'accord, alors maintenant nous devons fournir une variable à l'intérieur.

Qui sera URL.

Oui, maintenant cela va fonctionner correctement.

Et la même chose ici.

URL, et je vais supprimer la chaîne et lui donner un backtick.

Juste comme ça.

Alors, c'est ainsi que cela va fonctionner.

Et ici aussi.

D'accord, nous n'avons pas donné le composant, prop.

Alors, il va être view, view, bureau file.

Alors, il ne s'auto-importe pas.

Laissez-moi simplement l'importer ici.

Votre profil doit revenir d'un pas en arrière et à l'intérieur des composants et view profile, même chose avec le Edit Profile ainsi que votre profil, cela devrait fonctionner maintenant.

Alors, nous aurions un composant de edit, profile.

Oui.

Alors, nous y voilà.

Nous avons créé nos deux routes ici.

Alors, que devons-nous faire maintenant, nous devons lui fournir la variable PATH.

Mais il va savoir que l'URL actuelle dans laquelle nous nous trouvons, le chemin actuel dans lequel nous nous trouvons, nous devons seulement append cette URL particulière, vous savez, l'URL à cette URL, je veux dire le chemin à cette URL, ou la route à cette URL.

Alors, je vais taper path ici, de même, mais ici, juste comme ça, vous savez, l'exercice.

Je vais faire cela créé un back tick.

Ici aussi.

Maintenant, tout devrait fonctionner correctement.

Essayons cela.

Si je clique sur View profile, il va nous emmener à la page view profile, vous pouvez voir slash profile slash view profile.

Et si je clique sur Edit Profile, il va nous emmener à la page edit profile.

Et toutes les autres routes fonctionnent absolument bien.

Nous y voilà.

Si je clique sur logout, il va nous emmener à la page d'accueil.

Alors, merci à tous d'avoir regardé ce tutoriel react router Dom.

J'espère que vous avez tous compris les concepts que je vous ai expliqués dans cette vidéo.

Si vous avez une confusion, vous pouvez commenter ci-dessous pour me demander, je vous répondrai dès que possible.