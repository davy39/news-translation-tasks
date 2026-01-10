---
title: 'Le Guide du Routard pour React Router v4 : Comprendre React Router en 20 minutes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-25T23:59:06.000Z'
originalURL: https://freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-a957c6a5aa18
coverImage: https://cdn-media-1.freecodecamp.org/images/0*GQM3tb92nE_1yMTX
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: 'Le Guide du Routard pour React Router v4 : Comprendre React Router en
  20 minutes'
seo_desc: 'By Eduardo Vedes

  Hi fellow React Hitchhiker! Want a ride into React Router? Jump in. Let’s go!

  To understand the philosophy behind React Router, we need to know what a Single-Page
  Application (SPA) is.

  What Is A Single-Page Application?

  Basically it’...'
---

Par Eduardo Vedes

Salut, Routard de React ! Tu veux un tour dans React Router ? Monte à bord. C'est parti !

Pour comprendre la philosophie derrière React Router, nous devons savoir ce qu'est une Single-Page Application (SPA).

### **Qu'est-ce qu'une Single-Page Application ?**



En gros, c'est une application web ou un site web qui interagit avec l'utilisateur en réécrivant dynamiquement la page actuelle plutôt que de charger des pages entièrement nouvelles depuis un serveur.



### Pourquoi est-ce si bien ?!



**1.** évite l'interruption de l'expérience utilisateur entre les pages successives

**2.** fait en sorte que l'application se comporte plus comme une application de bureau

**3.** tous les ressources de code sont chargées dynamiquement et ajoutées à la page selon les besoins, généralement en réponse aux actions de l'utilisateur

**4.** parce que c'est kewl et kewl et extra-ultra-wide-4K-level-of-kewl. ?

Les SPA sont désormais une norme industrielle, et de nombreuses entreprises sont en quête de programmeurs pour développer leurs projets.



### **Qu'est-ce que React Router ?**



React Router est un outil qui vous permet de gérer les routes.

Puisque vous traitez avec une SPA, vous avez besoin d'un moyen de déclencher les contenus qui sont chargés à l'écran. React Router introduit un concept appelé « Routage Dynamique », qui est assez différent du « Routage Statique » auquel nous sommes habitués.

Lorsque vous traitez avec le « Routage Statique », vous déclarez vos routes dans le cadre de l'initialisation de votre application avant tout rendu (Rails, Express, Ember, Angular, etc.).

Le « Routage Dynamique » signifie que le routage a lieu pendant que votre application est en train de rendre, et non dans une configuration ou une convention en dehors d'une application en cours d'exécution.

React Router v4 prône et met en œuvre une approche basée sur les composants pour le routage.

Il fournit différents composants de routage selon les besoins de l'application et de la plateforme.

Dans ce cas spécifique, nous allons explorer **<BrowserRouter>** parce que nous voulons utiliser le « routage dynamique » dans un contexte d'« application web » et laisser les autres pour d'autres circonstances.



### **Qui a créé React Router ?**

Ces deux êtres humains incroyables, [Michael Jackson](https://twitter.com/mjackson) et [Ryan Florence](https://twitter.com/ryanflorence). Et ils méritent des tonnes d'applaudissements ! Ensemble, ils ont lancé [React Training](https://twitter.com/reacttraining).

De nos jours, corrigez-moi si je me trompe, ils ont suivi des chemins séparés :

Michael Jackson continue de développer [React Training](https://reacttraining.com/).

Ryan Florence a créé [Reach.Tech](https://reach.tech/).



### **React Router a-t-il quelque chose à voir avec Redux ?**

Non. Bien qu'ils apparaissent généralement ensemble.

Êtes-vous sûr ? Oui ? Je suis sûr ?

Ce sont tous deux des outils formidables et indispensables et, comme ce sont des composants d'ordre supérieur (basiquement des fonctions JavaScript qui prennent un composant et en retournent un nouveau), il est courant de les trouver « composés » ensemble.

### **Installation, mettons les mains dans le cambouis**

![Image](https://cdn-media-1.freecodecamp.org/images/Ga6dcRb1gmEed2ge937FwIv9aR1AwIkAvGvJ)
_Photo par [Unsplash](https://unsplash.com/@rosiet07?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Rose Elena</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Pour vous guider à travers ce processus, nous allons utiliser Create React App (CRA).

À la fin, vous aurez un modèle propre pour construire des sites web simples.

Si par hasard [React](https://reactjs.org/docs/hello-world.html) ou [Create React App](https://github.com/facebook/create-react-app) sont au-delà de votre compréhension, je vous recommande de vous y mettre d'abord et de revenir avec une tasse de café.

D'accord, pour ceux qui sont restés avec moi : après avoir installé CRA, vous devez installer le package react-router.

Si vous utilisez npm, ouvrez simplement votre terminal, allez dans votre dossier CRA et tapez :

_`npm i -S react-router-dom`_

ou

_`yarn add react-router-dom`_ — si vous utilisez yarn comme gestionnaire de packages.

Juste pour vérifier votre _**package.json**_ et vous assurer que tout est correct, voici le mien :

![Image](https://cdn-media-1.freecodecamp.org/images/k1OxWlNSx7lJ3wBTUrYsyrJpcgFTK00hNvH7)

Comme vous pouvez le voir ? à ce stade, nous avons **react-router-dom** comme dépendance.

Terminé, npm ou yarn start et...

**Boum ! On roule Ma !** 

### **L'application que nous construisons**

Faisons un simple site web personnel avec une barre de navigation qui permet à l'utilisateur de basculer entre les contenus. Notre site web aura trois sections principales appelées **Accueil**, **À propos** et **Sujets**.

La **NavBar** sera un composant omniprésent tandis que **Accueil**, **À propos** et **Sujets** seront rendus en dessous selon les routes sélectionnées.

Voyez-vous l'URL du navigateur : _**localhost:3000/accueil**_ dans la capture d'écran ci-dessous ?

Cela signifie que la route **Accueil** est déclenchée et que la vue **Accueil** est rendue.

Ce sera notre résultat final :

![Image](https://cdn-media-1.freecodecamp.org/images/Igwuii40jvc5gCBOQuuVWbEexaNZgVxbdJcP)

Et ça... ?, c'est un site web ?

? Oui, c'en est un !

Un site nu ! Essayez simplement de ne pas ressentir de biais envers d'autres complexités comme le style, etc. ! Je ne veux pas que vous soyez distrait par autre chose que de comprendre **à quel point il est simple** de mettre en œuvre **React Router v4**.

Alors, après vous être remis du choc, ?, passons à l'étape suivante et regardez mon fichier /src/index.js.

#### /src/index.js

_index.js_ est le premier fichier à être chargé par CRA, le point d'initialisation de tout dans votre App.

Regardons ce que j'ai fait :

![Image](https://cdn-media-1.freecodecamp.org/images/scJ4TP9j27Ph1S425FUiTbB4e-b9iC-0v-gf)

Alors, que faisons-nous ici ?

* Nous importons le composant **<BrowserRouter/>** depuis la dépendance que nous avons installée et déclarons que nous allons l'appeler **<Router/>** à partir de ce point :

_`import { BrowserRouter as Router } from 'react-router-dom';`_

* Nous importons un composant **<Routes/>**, créé par moi, avec les routes que nous allons utiliser dans notre site web — ne vous inquiétez pas pour ce composant pour l'instant :

_`import { Routes } from './routes';`_

Le composant **<Routes/>** prend la place du composant par défaut CRA _**<App/>**_. C'est essentiellement la même chose — je l'ai simplement appelé **<Routes/>** parce que je pense que cela rend le code plus significatif et lisible.

Vous ne chargez plus une App unique mais un composant **Routes** qui gérera les routes et déclenchera le montage et le rendu des composants qui doivent se charger dans chaque route.

* Nous enveloppons **<Routes/>** avec le composant **<Router/>**.

En fait, **<Router/>** fonctionne comme un [Composant d'Ordre Supérieur](https://reactjs.org/docs/higher-order-components.html) qui ne connaît ses enfants que dans le futur et interagit avec eux dans un scope plus large, indépendamment de qui ils sont et de leur nombre.

Vous n'avez pas à vous soucier de son fonctionnement pour l'utiliser. C'est une question beaucoup plus profonde et avancée.

Assurez-vous simplement de comprendre que **React.DOM** ne charge plus une simple **App**. Il charge l'App enveloppée par un composant appelé `Router` qui, dans une instance ou un scope supérieur, peut interagir avec elle et avec le `DOM` du navigateur.

#### **Composant <Routes />**

![Image](https://cdn-media-1.freecodecamp.org/images/hFLFpV5UPMby62nxbB2rzQUQmAzPLbJRRUaz)



#### Alors, que fait _routes.js_ ?



Il commence par importer React et quelques composants que nous examinerons plus tard. Considérez-les simplement comme des composants sans état : **Accueil**, **À propos**, **ListeSujets**, **DétailSujet**, **NavBar** et **AucuneCorrespondance**.

Il importe également trois composants du package **react-router-dom** dont nous aurons besoin pour les invoquer : **<Route/>**, **<Switch/>** et **<Redirect/>**.

Après les imports, nous exportons le composant sans état Routes qui invoque le `NavBar` (qui sera toujours à l'écran) et un composant **<Switch/>**.

#### Que fait ce gars <Switch/> ?



Ce composant rend essentiellement le premier enfant **<Route>** ou **<Redirect>** qui correspond à l'emplacement du navigateur.

Il commence à tester des choses comme ceci : « l'URL du navigateur est-elle dans ce chemin **<Route/>** ? Non ? D'accord. » Route suivante. « L'URL du navigateur est-elle dans ce chemin de route ? Non. »

Route suivante. « Oh, je l'ai ! C'est dans celui-ci, déclenchons le rendu du composant et finissons la vérification pour l'instant (je ne me soucie pas des autres routes en dessous...) »

Si par hasard cela se produit :

![Image](https://cdn-media-1.freecodecamp.org/images/pCLNszAHXi5Tl-gq0toLitQyc1cRQeKIBcxm)

la deuxième route ne sera jamais déclenchée car Switch sautera avant de l'atteindre. Il va simplement prendre un café... (et moi aussi !!! ? Retour !)

À l'intérieur de **<Switch/>**, nous définissons chaque **<Route/>**.

Chaque **<Route/>** dit ceci au navigateur : « Hé, DOM du navigateur ! Si **<Switch/>** me choisit parce que ton emplacement est (exactement) celui-ci, veux-tu rendre le composant suivant. »

![Image](https://cdn-media-1.freecodecamp.org/images/IAEvLJjBJE6kKk-8RAsqXskmBYFYLHgM0Hck)

Ou dans d'autres cas comme celui ci-dessous, il dit : « Hé, navigateur, si par hasard ton **<Switch/>** m'a choisi parce que l'emplacement est /Sujets/"quelque chose", rends le composant DétailSujet. Certes, il découvrira qui est **ce :topicId** (variable) que l'utilisateur nous demande de faire correspondre et le routera en conséquence. »

![Image](https://cdn-media-1.freecodecamp.org/images/4xy5vihwiXuuj1xpsrhmWu7kjnmvlCn8GMJn)

D'accord tout le monde. Parce que **<Switch/>** a ce comportement par défaut de vérifier chaque route, nous devons fournir un recours au cas où il ne correspond à rien :

![Image](https://cdn-media-1.freecodecamp.org/images/-Bw2qOlJNvs9k2GOwX3lYgeozuPGkCjApbav)

Cette dernière route rend simplement une page par défaut indiquant qu'aucune route n'a été trouvée, une sorte d'erreur [HTTP 404](https://en.wikipedia.org/wiki/HTTP_404).

Rappelez-vous que nous traitons ici avec une SPA et avec un « Routage Dynamique », donc c'est une simulation comme si nous demandions des routes à un serveur ?. En fait, nous ne le faisons pas !

Nous ne savons simplement pas quoi rendre si l'utilisateur, par exemple, insère quelque chose de non correspondant dans l'URL comme ceci : _**http://localhost:3000/BonjourLeMonde**_.

Puisque cette route n'a pas été définie, nous fournissons un composant **AucuneCorrespondance** pour les informer de la non-existence de la route.

**<Redirect/>** est là parce que si l'utilisateur essaie de charger l'URL sans aucune route **http://localhost:3000/**, il obtiendrait une **AucuneCorrespondance** parce qu'il n'y a pas de route définie pour cela. Donc la meilleure façon de gérer cela est d'utiliser **<Redirect/>** et de pousser l'utilisateur vers la route de **/Accueil** qui est par défaut notre premier écran de l'application.

#### Pourquoi est-ce nécessaire ?

Encore une fois, parce que généralement l'utilisateur commencerait l'application en tapant son URL générale et sans le **<Redirect/>**, le premier composant rendu serait **<AucuneCorrespondance/>**. Nous ne voulons pas cela, nous voulons que l'utilisateur soit redirigé vers le composant **<Accueil/>**.



### **Vues et/ou Composants**

À ce stade de notre guide, j'aimerais m'arrêter un peu pour différencier une Vue d'un Composant. Ce n'est pas l'essence de ce guide, mais cela aura du sens après que je vous ai montré la structure de dossiers de mon _CRA_.

Lorsque nous « [Pensons en React](https://reactjs.org/docs/thinking-in-react.html) » et que nous commençons à faire une App, et qu'elle commence à grandir, parfois nous nous arrêtons parce que nous sentons que les choses ne sont pas à leur place.

Cela signifie que nous devons donner des noms à ces choses et les garder séparées dans différents « tiroirs » ou « dossiers ».

Les Vues et les Composants sont des choses qui sont peintes à l'écran. Alors, qu'est-ce qui différencie une chose de l'autre ?

Et les vues ne sont-elles pas des composants ? Et les composants ne sont-ils pas des vues ?

Eh bien, en termes de langage de codage, une Vue et un Composant sont certainement des fonctions ou des classes — des composants sans état ou des composants avec état comme nous les appelons dans le jargon React.

Alors, qu'est-ce qui les différencie ?

Eh bien, une Vue a une route. À l'intérieur de cette Vue, vous pouvez rendre beaucoup de composants.

Un composant est généralement une abstraction qui peut être invoquée de nombreuses fois dans différentes vues. Cela peut être un bouton, un formulaire, un graphique. Cela peut même être une chose plus complexe, tandis qu'une vue est unique et a une route.

C'est un concept très simple qui doit être compris dès le début, dès que nous commençons à faire une application aussi petite qu'une page d'accueil personnelle.

Regardons la structure de dossiers de mon CRA :

![Image](https://cdn-media-1.freecodecamp.org/images/hkA3J3XhCQmBMSaZQiKxrMHciTyAglBaveTJ)
_Structure de dossiers CRA_

Donc, comme vous pouvez le voir, moi — et 99 % du monde — aimons garder les oranges et les poires dans des paniers différents. Et vous aussi ! J'ai foi en vous ! Je vous fais confiance !

Il existe de nombreux modèles sur la façon d'organiser tout cela et de nombreuses discussions commencent lorsque nous introduisons plus de packages comme Redux qui transforment un peu l'architecture de l'application, ou lorsque nous voulons peindre sur l'écran des tableaux de bord, des widgets, des cochons cyclistes ou d'autres trucs bizarres...

Mais, pour différencier les concepts, prenez un bon regard sur les Vues et les Composants.

**Accueil**, **À propos**, **ListeSujets** et **AucuneCorrespondance** sont des vues. Elles ont leurs propres routes qui les déclenchent.

**NavBar** est un composant omniprésent qui est toujours invoqué. Il n'a pas de route.

**DétailSujet** est un composant qui affichera les informations sur le sujet lorsque la route **ListeSujets/:topicId** est déclenchée. C'est un composant réutilisable qui peut être importé dans d'autres endroits et refactorisé ou étendu. Il n'a pas de route spécifique.

### **Les Vues Accueil / À propos**



À l'intérieur du dossier Accueil, j'ai un fichier _index.js_ et un fichier _Accueil.js_.

Avoir un _index.js_ pour exporter les autres fichiers est une bonne pratique. Faites-moi simplement confiance ou apportez du vin car ce sera une longue discussion ?

... oh, buvons simplement le vin et nous parlerons plus tard ! ?

![Image](https://cdn-media-1.freecodecamp.org/images/JhqPLcyHbEQyDQJDGPmkFAJ-mR9-pgdCMzsL)
_**index.js qui exporte la vue Accueil**_

![Image](https://cdn-media-1.freecodecamp.org/images/B2JGUGC4cflc25P0fLBAXlxnnsioeIJFpNqV)
_**Composant sans état de la vue Accueil.js**_

C'est une vue simple qui exporte simplement son titre. La vue **À propos** est égale à celle-ci.

Maintenant, regardons la **Vue ListeSujets** car elle est un peu différente.

### **Vues ListeSujets et DétailSujet**

![Image](https://cdn-media-1.freecodecamp.org/images/GbOKrOTh4Y4daFnJqRjMwikEiFxzmcg6fjHV)
_Code de la Vue ListeSujets_

Donc, la **Vue ListeSujets** a ce détail de gérer différentes routes. Vous vous souvenez de la route **/Sujet/:topicId** que **<Route/>** a dit à **<Switch/>** de laisser **DétailSujet** gérer ?

Nous y sommes.

**ListeSujets** reçoit **{ match }** comme une prop. Ne laissez pas la fonctionnalité de déstructuration vous effrayer. Nous aurions pu simplement recevoir les props et appeler _props.match_. C'est simplement comment tous les enfants cool déstructurent les props de nos jours pour améliorer la lisibilité et le flux React. J'aime beaucoup ça aussi ! C'est un peu comme prendre une boîte avec votre mobile à l'intérieur ou prendre le mobile directement. En fait, il était gardé à l'intérieur de la boîte mais à ce moment-là, vous n'avez besoin que de vérifier votre e-mail ? alors laissez la boîte où elle est ! Ne l'apportez pas avec vous au travail !

En tout cas, restons concentrés sur le code.

Dans ce fichier, nous importons un composant de React Router appelé **{ Link }** parce que nous voulons créer des liens ?

Nous recevons un match de la route que nous avons choisie lorsque nous avons cliqué sur **Sujets** et nous rendons une liste non ordonnée avec 3 options : **Sujet1**, **Sujet2** et **Sujet3**.

En gros, si l'utilisateur choisit **Lien Sujet1** à l'écran, le **<Link/>** poussera l'URL du navigateur vers ce chemin **/Sujets/Sujet1**.

Que se passe-t-il ensuite ? **<Router/>** et **<Switch />** détectent que l'URL a changé et regardent leurs infos pour vérifier quelle route doit être déclenchée. Ils découvrent donc que la route déclenchée est maintenant celle pour **/Sujets/:topicId** et déclenchent le rendu de **DétailSujet**. **DétailSujet** rendra les détails de **Sujet1**.

![Image](https://cdn-media-1.freecodecamp.org/images/1s20EOEWOhQoRsqZdn5SnOwixBEDUV7VOP65)
_Composant DétailSujet_

**DétailSujet** reçoit **match** du Router et rend le **topicId** situé à **match.params.topicId**.

### **Le Composant NavBar**



Le composant **NavBar** a un rôle spécial ici car il est omniprésent.

Sa fonction est de permettre à l'utilisateur de naviguer sur le site web et de montrer les sections (routes) disponibles.

Comme vous l'avez vu au début, il est à l'intérieur de **<Router/>** mais à l'extérieur de **<Switch/>**, donc toute vue sera toujours composée avec **NavBar** en haut.

![Image](https://cdn-media-1.freecodecamp.org/images/RRwqmKgTbtRjQNW28kK0neRfS6idxrjYhjOT)
_Code du Composant NavBar_

Comme vous pouvez le voir, son rôle est basique. Il fournit simplement **<Link/>** et dit à **<Router/>** de demander à **<Switch/>** de déclencher la **<Route/>** choisie et de la rendre à l'écran.



### **Dernier mais non des moindres**

Je pense qu'à ce stade, vous avez probablement une compréhension de base de la façon dont React Router fonctionne et peut être utilisé pour faire un site web simple.

Si vous voulez vérifier le code ou le tester, vous pouvez tirer mon repo, disponible sur [GitHub](https://github.com/evedes/React-Boilerplate-01).

### **Bibliographie**

Pour faire cet article, j'ai utilisé la documentation de React Router que vous pouvez trouver [ici](https://github.com/evedes/React-Boilerplate-01).

Tous les autres sites que j'ai utilisés sont liés tout au long du document pour ajouter des informations ou fournir un contexte à ce que j'ai essayé de vous expliquer.

Cet article est la partie 1 d'une série appelée « Le Guide du Routard pour React Router v4 ». Les parties 2-4 arrivent sur freeCodeCamp au cours de cette semaine !

* **[Partie II : [match, location, history] — vos meilleurs amis !](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-4b12e369d10/)**
* **[Partie III : chemins récursifs, à l'infini et au-delà !](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-21c99a878bf8/)**
* **[Partie IV : configuration de route, la valeur cachée de la définition d'un tableau de configuration de route](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-c98c39892399/)**

Merci beaucoup !