---
title: L'anatomie d'un tableau de bord Bootstrap qui génère des milliers de dollars
  chaque mois
subtitle: ''
author: Alexandru Paduraru
co_authors: []
series: null
date: '2017-08-28T14:31:58.000Z'
originalURL: https://freecodecamp.org/news/the-anatomy-of-a-bootstrap-dashboard-that-earns-1-000s-each-month-ed3404010d25
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oNcZnFrvQFeINnPcWVI6VA.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: L'anatomie d'un tableau de bord Bootstrap qui génère des milliers de dollars
  chaque mois
seo_desc: 'We at Creative Tim have always wanted to deliver great tools to all the
  web developers who are using our products. If you want to read more about how we’ve
  built our business and what is our drive, you can check this article: Growing a
  side project i...'
---

Nous chez [Creative Tim](https://www.creative-tim.com/) avons toujours voulu offrir de grands outils à tous les développeurs web qui utilisent nos produits. Si vous souhaitez en savoir plus sur la façon dont nous avons construit notre entreprise et ce qui nous motive, vous pouvez consulter cet article : [Transformer un projet secondaire en une entreprise générant 17 000 $ par mois](https://medium.freecodecamp.com/growing-a-side-project-into-a-17-000-month-business-46024d2aa87f).

Nous voulons voir de meilleurs sites web et applications web sur Internet. Nous avons donc décidé de partager certains des "ingrédients secrets" qui forment la base de l'un de nos tableaux de bord les plus populaires : [Light Bootstrap Dashboard](http://demos.creative-tim.com/light-bootstrap-dashboard/dashboard). Bien sûr, ils ne seront plus un secret, car nous allons les partager avec vous. ?

Dans cette étude de cas, je vais partager comment nous avons eu l'idée de créer un tableau de bord, d'où nous avons tiré l'inspiration, comment nous avons tout mis en œuvre, comment il a été utilisé dans les outils internes de **Stanford** et comment nous avons financé le développement et le support. Voici un aperçu de l'article :

1. La structure de base et les fonctionnalités principales
2. Comment le design a été créé
3. Construit sur la base de l'open source et pourquoi vous devriez vous appuyer sur les épaules des géants
4. Lancement, ascension et succès
5. Comment nous finançons le support et répondons aux demandes des développeurs
6. Plans de développement futurs

Je vais essayer de donner autant d'informations que possible, dans l'espoir que ce tutoriel ne ressemblera pas à ceci :

### 1. La structure de base et les fonctionnalités principales

Vous devriez considérer le processus de création du tableau de bord comme un test que vous devez passer après avoir beaucoup appris. Bien sûr, vous apprendrez beaucoup pendant le développement du produit. Mais d'abord, vous devez avoir une solide connaissance de ce qu'est "cela" et comment il est "utilisé". Avant d'écrire la première ligne de code, vous devriez faire des recherches, établir des plans, créer des listes de tâches et des croquis, et essayer de visualiser ce que vous voudrez avoir à la fin.

Puisque vous ne réinventez pas la roue, vous devez regarder autour de vous les entreprises qui créent de grands produits pour vous inspirer (comme [Heroku](https://dashboard.heroku.com/), [Slack](https://slack.com/), [Mailchimp](https://mailchimp.com/), [Stripe](https://stripe.com/)). Regardez aussi vos concurrents. Vous obtiendrez beaucoup d'informations. Et quand vous commencerez, il sera plus facile de développer le produit parce que vous aurez fait vos devoirs. Vous devez aiguiser votre hache avant de commencer à couper :

> "Si j'avais huit heures pour abattre un arbre, je passerais six heures à aiguiser ma hache." — Abraham Lincoln

Nous avons fait nos devoirs et nous avons obtenu une énorme liste de plus de 100 tableaux de bord gratuits comme exemples dont nous pouvons nous inspirer. En voici quelques-uns :

![Image](https://cdn-media-1.freecodecamp.org/images/1*xR1NimY3i5LO1lxM9SL2RQ.jpeg)

Vous avez une énorme liste de tableaux de bord, avec beaucoup de couleurs, d'animations, de belles icônes, de petits graphiques, de grands graphiques, de barres latérales statiques ou fixes et des centaines de fonctionnalités différentes. Comment savez-vous quelle est la meilleure option pour votre public ?

Puisque nous ne savions pas ce que les gens veulent dans un tableau de bord, nous avons décidé d'écrire toutes les fonctionnalités que ces tableaux de bord contiennent et d'utiliser uniquement les plus courantes. Nous avons réalisé que les **fonctionnalités principales** résolvent environ 95 % des cas où vous avez besoin d'un tableau de bord. Les 5 % restants résolvent des problèmes très spécifiques.

Les éléments de base sont les boutons, les icônes, la typographie, la barre latérale, le panneau principal, les barres de navigation et les menus déroulants. Les fonctionnalités principales dans la plupart des tableaux de bord sont :

1. Tableaux
2. Notifications
3. Listes de tâches
4. Cartes (pour différents types de formulaires et une visualisation plus facile des informations)
5. Graphiques (graphique en anneau, graphique en ligne, graphique en barres)
6. Google Maps

Avec de petits ajustements visuels, vous pouvez reproduire 95 % de n'importe quel tableau de bord de n'importe quelle entreprise dans le monde en utilisant simplement les éléments de base. Ensuite, vous avez les 5 % restants, qui sont toujours différents selon l'entreprise et les problèmes qu'elle résout. Ici, nous pouvons trouver :

1. [Cartes du système Kanban](https://fr.wikipedia.org/wiki/Kanban)
2. Fonctionnalité de [Glisser-déposer](https://fr.wikipedia.org/wiki/Glisser-d%C3%A9poser)
3. Composants de chronologie
4. Éditeur WYSIWYG
5. Menu de navigation latérale à 8 niveaux
6. Téléchargement multiple de fichiers + Glisser-déposer de fichiers
7. Formulaire X-Editable
8. Morris Chart, Google Chart, Flot Chart, amChart, Flows Chart et de nombreux autres types de graphiques
9. Et la liste peut continuer avec plus de 200 fonctionnalités

Le problème est que chacun de ces nouveaux plugins ajoute des CSS, JavaScript ou des bibliothèques jQuery supplémentaires, et du HTML. Nous avons construit le produit en HTML simple, sans frameworks ou astuces modulaires, donc tout le CSS/JavaScript serait dans un seul fichier.

Ne vous méprenez pas, je ne dis pas que les fonctionnalités n'étaient pas bonnes. Ce sont de superbes plugins développés par des gens formidables. Mais ce n'était pas quelque chose que nous voulions avoir dans notre tableau de bord simple.

Nous avons donc décidé de garder le produit aussi léger que possible (rappelez-vous le nom ?). **Light Bootstrap Dashboard**. Et nous avons décidé de n'implémenter que les fonctionnalités qui résolvaient les 95 % de base.

![Image](https://cdn-media-1.freecodecamp.org/images/1*G0F-0tf2aAVrevfgCdih0w.jpeg)

### 2. Comment le design a été créé

Après avoir établi notre plan pour les éléments que le produit aurait, nous devions penser à un design qui serait exceptionnel. Un design convivial qui donnerait envie aux gens d'avoir ce tableau de bord dans leur système de gestion de contenu. Nous avions déjà le célèbre kit Bootstrap [Get Shit Done Kit](http://demos.creative-tim.com/get-shit-done/index.html). Les développeurs web l'adoraient et il a été téléchargé plus de 30 000 fois. Nous avons donc décidé de l'utiliser comme design de base pour les éléments de base comme les boutons, les barres de navigation, les champs de saisie, etc.

Nous avons réalisé que nous avions besoin de plus que cela pour faire une impression et pour que les gens veulent absolument notre produit. Nous ne voulions pas être "un autre tableau de bord basé sur Bootstrap". **Où allez-vous quand vous voulez de grandes ressources de design ?**

![Image](https://cdn-media-1.freecodecamp.org/images/1*ruqs_QCLXE8wX6XpCufnEg.png)

Si vous recherchez "[dashboard](https://dribbble.com/search?q=dashboard)" sur Dribbble, vous trouverez beaucoup de tableaux de bord et de panneaux d'administration incroyablement beaux. En fait, pour ceux qui ne savent pas, [Dribbble](https://dribbble.com/) est comme de la cocaïne visuelle. Consultez quelques-uns de ces exemples réalisés par [Cosmin Capitanu](https://dribbble.com/radium) et [Mike de CreativeMints](https://dribbble.com/creativemints) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*JQV190Vy6Yx69mv4sJg7tg.jpeg)
_[https://dribbble.com/shots/1423171-Some-Analytics](https://dribbble.com/shots/1423171-Some-Analytics" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/1*EJeWQQxhA0lRYvao9sqZog.jpeg)
_[https://dribbble.com/shots/1592816-Probability-theory](https://dribbble.com/shots/1592816-Probability-theory" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/1*BG1kjWkGjIoJZoUKE5FO2g.jpeg)
_[https://dribbble.com/shots/1738453-Xonom](https://dribbble.com/shots/1738453-Xonom" rel="noopener" target="_blank" title=")_

Voir tous ces beaux exemples nous a fait réaliser que si nous construisions quelque chose comme cela, nous nous démarquerions définitivement de la foule. De plus, même si les tableaux de bord ou les graphiques ont l'air très bien, ils seront très difficiles ou impossibles pour nous à coder en HTML, CSS et JavaScript. Ou ils résolvent un problème très spécifique, comme le dernier tableau de bord avec les mesures corporelles.

C'était impossible il y a 2 ans, car notre niveau de connaissance et d'expérience avec HTML/CSS n'était pas si élevé. Je suis sûr que si nous voulions les implémenter aujourd'hui, nous aurions une bonne chance de créer quelque chose de très similaire. De plus, la technologie et les capacités des navigateurs nous aideront davantage.

Nous voulions construire quelque chose qui puisse être utilisé par de nombreuses personnes issues de divers domaines d'activité. Il y avait aussi des tableaux de bord simples et beaux, mais nous ne voulions pas les utiliser comme inspiration car nous voulions quelque chose de différent.

Je ne peux pas expliquer exactement ce que nous voulions, mais nous ne nous sentions à l'aise avec aucun des exemples. Nous avons donc continué à faire nos recherches jusqu'à ce que nous trouvions quelque chose que nous aimions vraiment :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5RdaH9YoQG-K-QKHl08Zlg.png)
_Tableau de bord Heroku en 2015_

Ce n'était pas parfait ni aussi exceptionnel que nous le voulions. Mais nous avons senti que c'était le bon choix et un très bon exemple à partir duquel nous pourrions construire notre tableau de bord. Même Pablo Picasso a dit que les grands designers volent et Apple a respecté sa parole :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Cz3GzYXXv4Hwx23qeXyFBA.jpeg)

Nous ne pouvions pas faire cela. Le tableau de bord de Heroku était suffisamment bon pour nous donner cette étincelle. Nous avons donc décidé de l'utiliser uniquement pour l'inspiration et non pour le résultat final. Voici la première itération :

![Image](https://cdn-media-1.freecodecamp.org/images/1*IqdqX0EyCAfRFbaQ8EC8nQ.png)
_Itération #1_

C'est un assez bon début. Pour avoir une meilleure vue de son apparence, nous devons simplement remplir la zone de droite avec quelques cartes contenant des graphiques :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Sg4Mv-PM0dPndSRVyC8ldw.png)
_Itération #2_

Les couleurs des cartes n'avaient pas l'air si bonnes. Elles étaient trop vives par rapport à l'apparence de la barre latérale gauche. Nous avons donc commencé à tester différentes combinaisons de couleurs pour les graphiques et la barre latérale.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZGOomWV2jePE1-U1f0t1ng.png)
_Itération #3_

À ce stade, nous avons réalisé que nous n'avions pas à garder une seule couleur pour l'arrière-plan de la barre latérale. Et nous devrions laisser nos utilisateurs choisir la couleur qu'ils veulent. Nous savions qu'Apple avait de beaux dégradés pour leur application Fitness, nous avons donc décidé d'utiliser ces dégradés comme base pour nos futurs dégradés.

Nous avons toujours pensé que si nous regardions ce que les meilleures entreprises du monde font en termes de design et d'UX, nous fixerions des normes très élevées pour nos interfaces. De cette manière, de plus en plus de développeurs web auront un accès gratuit à des produits de haute qualité.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ShULysSXSDmqIhjETzgB-w.jpeg)
_Application Fitness d'Apple_

![Image](https://cdn-media-1.freecodecamp.org/images/1*Mf08D8vG-nCAO1nlP_TQYw.jpeg)

Pendant que nous faisions toutes ces différentes combinaisons de couleurs, de dégradés, de cartes et de graphiques, nous avons vu que les gars de [Metalab](http://www.metalab.co), qui ont construit l'interface pour Slack, ont écrit un article : [Le secret de 2,8 milliards de dollars de Slack](https://medium.com/@awilkinson/slack-s-2-8-billion-dollar-secret-sauce-5c5ec7117908#.h63snwe27). Cela s'est avéré être une inspiration pour les prochaines étapes. L'idée générale de l'article était que le secret de Slack est créé par la combinaison d'une interface grande et ludique avec de petites interactions, ce qui rend le produit plus convivial.

> "Cela a l'air différent, cela se sent différent et cela sonne différent."

Nous voulions ajouter quelque chose que **aucun des autres tableaux de bord** n'avait. J'ai toujours aimé comment un dégradé avec une certaine transparence peut apparaître sur une image. Et j'ai commencé à jouer avec différentes images et l'opacité des dégradés. Au fait, l'image de dégradé duotone que nous avons utilisée en 2015 (nous ne savions même pas qu'elle avait un nom) semble être l'une des [tendances du design web pour 2017](https://thenextweb.com/dd/2016/12/22/web-design-trends-can-expect-see-2017/#.tnw_bdot2Bdf). C'est plutôt cool, n'est-ce pas ? ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*Azvsp9VybyIELu5tujGYmA.png)
_Itération #4_

Pas entièrement satisfaits...

![Image](https://cdn-media-1.freecodecamp.org/images/1*vs9QCRMn4U3sj5BfND-9IQ.png)
_Itération finale_

C'était la vue qui nous a rendu heureux, elle était juste parfaite pour nous ?. Nous avons également ajouté de petites interactions comme l'animation du menu déroulant ou l'effet d'affichage de la notification :

L'ajout de l'image avec les dégradés et les petites animations nous a fait sentir comme ce gars :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zF1jGXJhQHO7fglF9Rn2tQ.gif)
_[https://www.instagram.com/nusr_et](https://www.instagram.com/nusr_et" rel="noopener" target="_blank" title=")_

### 3. Construit sur la base de l'open source et pourquoi vous devriez vous appuyer sur les épaules des géants

Comme nous l'avons dit au début, nous ne voulions pas réinventer la roue. Nous n'avions pas non plus l'argent pour engager des experts capables de construire les éléments nécessaires pour le tableau de bord. Nous avons décidé que la meilleure option pour nous était d'utiliser ce que d'autres personnes ont créé et **partagé gratuitement** ou **open source**.

Nous avons récemment découvert que ce que nous avons réellement fait était de nous appuyer sur les épaules des géants. Cela signifie que nous avons utilisé autant que possible des outils qui sont déjà puissants et bien maintenus par de grandes communautés. Pour en savoir plus sur cela et pourquoi vous devriez utiliser cette technique lorsque vous voulez construire quelque chose à partir de zéro, lisez cet article génial, écrit par [Quincy Larson](https://twitter.com/ossia) : [Comment se tenir sur les épaules des géants](https://medium.freecodecamp.com/how-to-stand-on-shoulders-16e8cfbc127b#.iyojaorb8).

#### Jetons un coup d'œil à ce qui se cache sous le capot.

* Framework : [Bootstrap](http://getbootstrap.com/) — Bootstrap est le framework HTML, CSS et JavaScript le plus populaire pour développer des projets réactifs et mobiles sur le web.
* Couche de design : [Get Shit Done Kit](http://demos.creative-tim.com/get-shit-done/index.html) — Kit d'interface utilisateur Bootstrap 3 gratuit. C'est le meilleur point de départ pour tout projet en ligne que vous construisez. Il est devenu une marque de fabrique pour la communauté en ligne d'une interface propre et agréable.
* Police : [Roboto](https://fonts.google.com/specimen/Roboto) — une police Google qui a une double nature. Elle a un squelette mécanique et les formes sont largement géométriques.
* Petites icônes : [Font Awesome](http://fontawesome.io/) — Font Awesome vous donne des icônes vectorielles redimensionnables qui peuvent être personnalisées à l'aide de CSS.
* Grandes icônes : [Stroke 7 Icons](http://www.pixeden.com/icon-fonts/stroke-7-icon-font-set) — Il s'agit d'un ensemble complet de 202 icônes à trait fin inspiré par iOS 7.
* Graphiques : [Chartist.js](https://gionkunz.github.io/chartist-js/) — Chartist.js est le produit d'une communauté qui était déçue des capacités fournies par d'autres bibliothèques de graphiques.
* Notifications : [Bootstrap Notify](http://bootstrap-notify.remabledesigns.com/) — Ce plugin vous aide à transformer les alertes Bootstrap standard en notifications de type "growl".
* Cartes : [Google Maps](https://developers.google.com/maps/) — Plugin pour visualiser des cartes.
* Photos : [Unsplash](https://unsplash.com/) — Photos haute résolution gratuites (faites ce que vous voulez).

> "Rien n'est gratuit. Tout, y compris votre succès personnel, a un prix qui doit être payé" — Napoleon Hill

Puisque nous avons utilisé beaucoup de choses de la communauté, il serait juste de redonner à la communauté. Nous avons donc décidé il y a quelques semaines de le publier [sous licence MIT](https://github.com/creativetimofficial/light-bootstrap-dashboard/blob/master/LICENSE.md). De cette manière, plus de développeurs peuvent contribuer et l'utiliser sans aucune contrainte légale, pour des projets personnels et commerciaux.

### 4. Lancement, ascension et succès

Faire des recherches pendant environ 50 à 60 jours (aiguiser la hache) nous a donné la possibilité de développer le tableau de bord en seulement 15 jours (couper l'arbre). ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*MjHrLjPnk2DkClh34OB94w.png)

Que faites-vous après avoir lancé un projet ? Vous devez voir quel est le retour, si les gens aimeraient l'utiliser et si le tableau de bord simple que vous avez créé résout un problème pour eux. S'ils ne veulent pas l'utiliser, alors vous n'avez pas d'entreprise. Nous l'avons soumis à différentes communautés et il se portait très bien. Par exemple, il a obtenu :

* [170 votes positifs](https://news.ycombinator.com/item?id=10184982) sur Hacker News, atteignant la 9e position et plus de 88 000 vues cette semaine-là
* [247 votes positifs](https://www.reddit.com/r/webdev/comments/3jyyye/light_bootstrap_dashboard_an_useful_freebie_for/) sur le subreddit /r/webdev
* [80 votes positifs](https://www.reddit.com/r/webdev/comments/3jyyye/light_bootstrap_dashboard_an_useful_freebie_for/) sur le subreddit /r/web_design (bloqué à 80 car il a reçu le tag "spam", nous avions quelques popups d'abonnement... que nous avons ensuite supprimés ?)

![Image](https://cdn-media-1.freecodecamp.org/images/1*s2t5EiBh6omkaJVO1dJEKA.png)

La communauté a validé l'idée. Nous avons également reçu beaucoup de retours, pour ajouter les fichiers SASS pour une personnalisation plus facile ou les publier sur GitHub.

Ensuite, nous avons vu qu'il y avait beaucoup de débutants qui voulaient simplement apprendre à utiliser ce tableau de bord. Il était si beau que les gens qui n'avaient pas interagi avec quelque chose comme cela voulaient apprendre à travailler avec.

Nous avons passé environ 3 semaines à développer une série de tutoriels vidéo sur la façon de reproduire le tableau de bord WordPress en utilisant notre produit. Nous avons choisi d'utiliser le tableau de bord WordPress car c'est un tableau de bord très populaire. Et nous voulions que les gens comprennent qu'ils peuvent construire n'importe quoi en utilisant notre produit.

Les tutoriels ont été très bien reçus et comptent plus de 78 000 vues à ce jour. Voici la première vidéo sur [Comment créer un modèle d'administration réactif en utilisant Light Bootstrap Dashboard 1/3](https://www.youtube.com/watch?v=c3M3NQtFyqM).

### 5. Comment nous finançons le support et les demandes des développeurs web

![Image](https://cdn-media-1.freecodecamp.org/images/1*ozYKavzDtpbWrnOw34kKBg.jpeg)
_[https://youtu.be/sz_LgBAGYyo?list=PL5q_lef6zVkaTY_cT1k7qFNF2TidHCe-1](https://youtu.be/sz_LgBAGYyo?list=PL5q_lef6zVkaTY_cT1k7qFNF2TidHCe-1" rel="noopener" target="_blank" title=")_

Construire un produit est facile, le maintenir en vie est difficile.

Il y a beaucoup de grands plugins/modèles qui meurent parce que leurs créateurs n'ont pas assez d'argent ou ne génèrent pas assez de revenus pour continuer le développement ou corriger les problèmes.

Nous ne voulions pas que le même cas se produise pour notre produit. La meilleure option pour maintenir le produit en vie était de créer une version PRO qui pourrait générer suffisamment de revenus pour soutenir le développement continu.

Nous avons utilisé les retours des développeurs web et décidé de créer une version Premium avec plus d'éléments et de plugins. Nous voulions également aider certains des gars qui voulaient des fonctionnalités spécifiques et qui étaient dans la catégorie des 5 %. Choisir les bons plugins qui pourraient aider autant que possible la catégorie des 5 % était très difficile pour nous.

Nous avons recommencé à faire des recherches sur le tableau de bord premium. Et nous avons ajouté des plugins comme [Full Calendar](https://fullcalendar.io/), [DataTables.net](https://datatables.net/), [Sweet Alert](https://limonte.github.io/sweetalert2/), [Bootstrap Wizard](http://vinceg.github.io/twitter-bootstrap-wizard/) et quelques pages supplémentaires comme [Page de connexion](http://demos.creative-tim.com/light-bootstrap-dashboard-pro/examples/pages/login.html), [Page d'inscription](http://demos.creative-tim.com/light-bootstrap-dashboard-pro/examples/pages/register.html), [Page de verrouillage](http://demos.creative-tim.com/light-bootstrap-dashboard-pro/examples/pages/lock.html).

![Image](https://cdn-media-1.freecodecamp.org/images/1*D8XWOYaGPt019gwke0EiCg.jpeg)

Voici l'[aperçu en direct](http://demos.creative-tim.com/light-bootstrap-dashboard-pro/examples/dashboard.html) de la version PRO. Vous verrez que nous avons conservé la même structure et que nous voulions la rendre légère, sans trop d'options et de fonctionnalités.

Les revenus de la version PRO nous ont non seulement permis de soutenir le produit, mais aussi de créer de nouveaux types de fichiers comme la [version PSD/Sketch](http://www.pixelsvibe.com/product/light-dashboard) ou la [version Angular 2](https://www.creative-tim.com/product/light-bootstrap-dashboard-angular2). Les deux sont partagés gratuitement.

### 6. Plans de développement futurs

Voici quelques statistiques sur le tableau de bord :

![Image](https://cdn-media-1.freecodecamp.org/images/1*el4d2GAaEt9A9yTJrrpA8Q.jpeg)

Il est très facile de le personnaliser pour qu'il corresponde à votre marque. Il a été utilisé dans des outils internes comme le catalogue du département de médecine d'urgence de Stanford :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fJgKUWlS4RBv_OXME1wLAQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*99B_ST6PqMpj6DhNf7fX0Q.png)

Nous avons reçu de nombreuses demandes de développeurs web qui veulent avoir le tableau de bord construit sur différents frameworks comme [Angular 2](https://angular.io/), [Angular CLI](https://cli.angular.io/), [React](https://facebook.github.io/react/), [Meteor](https://www.meteor.com/), [VueJS](https://vuejs.org/) ou en tant que gemme Rails. Créer toutes ces versions et les soutenir gratuitement sous licence MIT ne fonctionnera que si nous avons des versions PRO pour chacune. Nous avons commencé avec Angular 2 et nous avons vu beaucoup de gens qui l'utilisent et nous avons reçu beaucoup de retours sur la façon de l'améliorer. Donc, si vous voulez vous impliquer pour les autres frameworks ou si vous avez des idées sur la façon d'améliorer ces produits, nous serions ravis d'en discuter davantage.

![Image](https://cdn-media-1.freecodecamp.org/images/1*poZ5puqDlTWowjhJrdLwMg.jpeg)

Cela a pris beaucoup de courage pour montrer nos sources et le processus que nous avions derrière la construction de [Light Bootstrap Dashboard](http://www.creative-tim.com/product/light-bootstrap-dashboard). J'espère que vous apprendrez quelque chose de cela et si vous avez des retours ou des suggestions, je serais ravi d'en discuter avec vous dans les commentaires.

Liens utiles :

* Télécharger la version HTML depuis [www.creative-tim.com](https://www.creative-tim.com/product/light-bootstrap-dashboard)
* Télécharger la version Angular depuis [www.creative-tim.com](https://www.creative-tim.com/product/light-bootstrap-dashboard-angular2)
* Télécharger la version PSD/Sketch depuis [www.pixelsvibe.com](http://www.pixelsvibe.com/product/light-dashboard)
* Jouer avec sur l'[aperçu en direct](http://demos.creative-tim.com/light-bootstrap-dashboard/dashboard)
* Contribuer et signaler des problèmes sur le [dépôt GitHub](https://github.com/creativetimofficial/light-bootstrap-dashboard)
* Consulter notre blog : [http://blog.creative-tim.com/](http://blog.creative-tim.com/)

Trouvez-moi sur :

* Email : [alex@creative-tim.com](mailto:alex@creative-tim.com)
* Facebook : [https://www.facebook.com/axelut](https://www.facebook.com/axelut)
* Twitter : [https://twitter.com/axelut](https://twitter.com/axelut)