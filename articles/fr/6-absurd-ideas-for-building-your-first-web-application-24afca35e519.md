---
title: 6 idées absurdes pour construire votre première application web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-18T14:02:58.000Z'
originalURL: https://freecodecamp.org/news/6-absurd-ideas-for-building-your-first-web-application-24afca35e519
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lRWsjJFXlX7UDSeP0GiduQ.png
tags:
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: 6 idées absurdes pour construire votre première application web
seo_desc: 'By Kevin Kononenko

  Need a few ideas for building a simple web app? These 6 examples will help you practice
  all the key skills and have fun doing it!

  Okay, you have already learned front-end web development, and now you are looking
  to flex your develo...'
---

Par Kevin Kononenko

#### Vous avez besoin de quelques idées pour construire une application web simple ? Ces 6 exemples vous aideront à pratiquer toutes les compétences clés et à vous amuser en le faisant !

D'accord, vous avez déjà appris le développement web front-end, et maintenant vous cherchez à faire travailler vos muscles de développeur sur le prochain grand défi : les applications web full-stack. Vous avez probablement de nombreuses idées de projets ambitieux qui vous trottent dans la tête. Mais comment pouvez-vous déterminer lesquelles sont raisonnables avec votre ensemble de compétences actuel ?

Voici 6 idées inhabituelles pour votre première application web, qui vous aideront à acquérir de l'expérience avec tous les concepts de base du développement web full-stack. À la fin, vous aurez un projet distinctif que vous pourrez inclure dans votre portfolio. Cela vous aidera à vous démarquer par rapport à tous les projets ennuyeux que tout le monde construit.

_Note : si vous apprenez encore le HTML/CSS/JS, j'ai rassemblé [8 idées](https://medium.com/@kevink/8-crazy-ideas-for-building-a-web-site-a25b3f69c517#.3fp6yvrcw) pour pratiquer uniquement le front-end._

![Image](https://cdn-media-1.freecodecamp.org/images/1*XY2qe5fjP-v7uVYng6gcUw.png)

### 1. FastFood Guru

**L'idée :** [Yelp](http://www.yelp.com/) est une source assez populaire de critiques de restaurants. Cependant, la plupart des gens l'utilisent pour découvrir des restaurants dont ils n'ont jamais entendu parler auparavant. Qu'en est-il des grandes chaînes de restauration rapide comme McDonald's et Burger King ? Beaucoup de gens y vont, mais d'une manière ou d'une autre, elles ne sont pas des candidates populaires pour les critiques.

Oui, vous pourriez me dire que chaque menu est à peu près le même, et que la nourriture a toujours le même goût. Cependant, si vous avez visité beaucoup de ces "restaurants" de chaîne, vous savez qu'il y a quelques choses qui diffèrent considérablement.

Lequel a la salle de bain la plus luxueuse ? Lesquels majorent leurs prix de menu ? Lesquels ont des ivrognes drôles à 1h du matin ? Ce serait un site de critiques pour ces chaînes de restauration rapide qui sont censées être cohérentes.

**Type de site :** Critiques

**Fonctions clés :**

* Capacité à créer un compte avec une photo, un nom d'utilisateur et un lieu
* Utiliser Google Maps pour permettre à un utilisateur de choisir un restaurant spécifique, soit en recherchant un lieu sur la carte, soit en tapant un nom et en choisissant dans une liste (typeahead)
* Permettre à l'utilisateur d'écrire une critique
* Permettre à l'utilisateur d'évaluer les sujets spécifiques à la restauration rapide suivants sur une échelle de 1 à 5 : Qualité des toilettes, Personnel, Propreté, Niveau de Sass du Drive-thru, Vitesse de livraison
* Capacité à ajouter des photos à la critique
* Conception réactive jusqu'au mobile

**Décisions sur les fonctionnalités clés :**

* Est-ce un site sérieux, ou est-il vraiment question des choses amusantes qui peuvent arriver dans un restaurant de restauration rapide ?
* Qui utilisera ce site ? Des personnes en roadtrip essayant de choisir un endroit pour déjeuner ? Des visiteurs fréquents de la restauration rapide cherchant à partager leur expérience ?
* Doit-ce être une communauté où les gens consultent fréquemment le site pour des histoires drôles et participent ? Ou plus une utilisation ponctuelle et peu fréquente ?
* Quelle intégration des médias sociaux pourrait aider à diffuser des histoires/critiques ?

**Ce que vous apprendrez :** Les systèmes utilisateurs et le stockage des images sont deux défis majeurs. Ce sera une bonne occasion d'implémenter une version basique de chacun. De plus, si vous choisissez de faire de ce site un site orienté humour, comment pouvez-vous influencer un niveau d'humour approprié qui n'est pas méchant ? Si vous voulez gagner des followers, ce sera un bon test pour voir où vous pourriez être en mesure de sourcer des critiques actuelles de restauration rapide pour ensemencer votre base de données et créer du contenu immédiat.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pTWEfkY_XHOEGENsu0BkaQ.png)

### 2. GrillBer

**L'idée :** Oui, vous l'avez deviné. Uber pour les grills. Si vous vivez en ville, vous n'avez peut-être pas l'espace pour un grill ou un endroit sûr pour le verrouiller. Par exemple, si vous vivez au 20e étage d'un immeuble d'appartements, où pouvez-vous mettre votre grill ?

Problème résolu avec GrillBer, un service de livraison pour la location de grills. Cela permettra aux clients de faire un barbecue sans aucune des logistiques. En fait, vous pourriez vouloir inclure un rouleau de gazon et des chaises pour que vos clients puissent créer un [parc éphémère](http://inhabitat.com/parking-day-2014-the-most-amazing-pop-up-parks-from-san-francisco-and-beyond/) dans un espace de parking !

**Type de site :** Livraison/Logistique

**Fonctions clés :**

* Formulaire qui permet à un utilisateur de réserver un grill pour un certain nombre d'heures à un certain tarif horaire, et stocke cela dans une base de données. L'utilisateur doit saisir son nom, son adresse, etc.
* Calendrier qui montre les différents moments où les grills sont disponibles. Consultez [Zipcar](http://www.zipcar.com/) pour un exemple de cela.
* Page de détails du produit qui montre le grill et vous en dit plus sur les différents accessoires, comme les chaises et le gazon.
* Intégration des médias sociaux avec Instagram qui montre tous les barbecues géniaux que les gens ont organisés avec GrillBer.
* Un processus de paiement et un système de paiements avec [Stripe](https://stripe.com/) pour que les utilisateurs puissent compléter le processus.

**Décisions sur les fonctionnalités clés :**

* Cela n'a pas besoin d'être visuellement stimulant comme Uber. Mais a-t-il même besoin d'un calendrier interactif cool ? Ou pouvez-vous vous en sortir avec un formulaire basique comme un site de commerce électronique ?
* Combien de douleurs dans le processus de grillage allez-vous offrir pour résoudre ? Attendez-vous à ce que l'utilisateur nettoie le grill ? S'agit-il de grills à charbon moins chers mais plus lents, ou de grills à gaz plus coûteux ?
* Les barbecues sont censés être une expérience sans stress. Si les gens doivent se dépêcher de cuisiner leur nourriture, ce ne sera pas une grande expérience. Comment pouvez-vous utiliser le texte et le microtexte pour indiquer clairement que cela ne sera pas un processus stressant ?
* Quelle logique devez-vous avoir sur votre back-end pour le système de réservation ? Devez-vous permettre une demi-heure avant et après pour la livraison du grill ?

**Ce que vous apprendrez :** Comment coordonner le front-end et le back-end d'un système de réservation. Pensez à combien de sites font cela. Sites de réservation de restaurants. Sites de réservation de salles de conférence. Il y en a beaucoup plus. C'est un modèle très courant, et une grande réalisation à avoir sur votre CV pour discussion.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gJZ9hrQsEYZUpPBliT2OYA.png)

### 3. NetworkTap

**L'idée :** Les médias sociaux sont une stratégie publicitaire de plus en plus populaire. Les entreprises utilisent Twitter, Facebook, LinkedIn et Pinterest pour atteindre les clients en plein milieu de leur navigation. Cependant, il y a un espace inexploité : la publication réelle de l'utilisateur.

Les annonceurs adorent le marketing de bouche à oreille, et le fait que les utilisateurs publient eux-mêmes les publicités serait un excellent moyen de confondre les autres dans leur fil d'actualité !

Ce site permettrait aux utilisateurs qui veulent gagner un peu d'argent supplémentaire de fournir volontairement des informations sur eux-mêmes, et aux annonceurs de détourner brièvement une publication avec une publicité. Les utilisateurs sont payés sur une base par vue ou une autre méthode. Maintenant, les publicités peuvent atteindre les yeux de nouvelles manières innovantes !

**Type de site :** Marché

**Fonctions clés :**

* Les utilisateurs individuels doivent pouvoir créer un compte avec des informations comme : lieu, âge, intérêts et statut familial afin que les annonceurs puissent choisir qui ils veulent pour parler de leur produit
* Les annonceurs doivent pouvoir créer un compte et parler de leur identité de marque, et de qui ils cherchent à atteindre.
* Chaque utilisateur doit pouvoir contacter un annonceur pour parler de son intérêt à faire une publication.
* Chaque annonceur doit pouvoir rechercher tous les utilisateurs par critères comme l'âge, le genre, etc. et envoyer un message de masse à leur démographie choisie concernant l'intérêt de faire une publicité.
* Les utilisateurs et les annonceurs doivent convenir d'une méthode de paiement : paiement par like, paiement par vue, paiement par clic ou autre.

**Décisions sur les fonctionnalités clés :**

* La fonctionnalité de recherche sera un gros atout pour les annonceurs. Comment représentez-vous chaque résultat de recherche ? Peut-être vouloir utiliser la visualisation de données comme Google Analytics.
* Comment pouvez-vous obtenir le plus d'informations des utilisateurs ? Intégration avec un compte de média social ? Peut-être les payer plus en fonction de la quantité d'informations qu'ils offrent ?
* Quelles sont les dynamiques de pouvoir entre les annonceurs et les utilisateurs ? Les utilisateurs ont-ils un avis sur le texte et l'image de la publicité ? Ou les annonceurs prennent-ils toutes les décisions sur ce qui est montré ?
* Les gens ne voudront pas 10 $ par semaine de cela. Ils voudront probablement plus comme 100 $ au minimum. Comment pouvez-vous équilibrer cela avec le nombre de publicités qu'ils devront probablement montrer pour y parvenir ? Personne ne veut complètement polluer son fil d'actualité.
* À quel point voulez-vous que les publicités soient rusées ? Doit-il être évident, ou doit-il sembler plus comme une publication authentique ?

**Ce que vous apprendrez :** Les marchés sont un autre type de site très populaire. Celui-ci vous permettra de créer deux types de comptes, ce qui est une structure courante. Le messagerie au sein d'un site sera une bonne compétence à apprendre avec celui-ci. Consultez [Fiverr](http://www.fiverrr.com) pour un exemple.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8x1RBwi9lRMqmZqVT0wn2Q.png)

### **4. Réparer ma relation**

**L'idée :** C'est l'abréviation de "Réparer ma relation". C'est un forum où les utilisateurs peuvent poster sur leurs problèmes de relation, et d'autres peuvent intervenir avec des conseils sur la façon de résoudre leurs problèmes.

Si vous avez expérimenté les fines communautés sur des sites comme 4chan, Reddit ou Bodybuilding.com, alors vous savez qu'il y a beaucoup de gens prêts à donner quelques minutes de leur temps pour aider.

**Type de site :** Forum

**Fonctions clés :**

* Un système de publication/commentaire similaire à Reddit ou Quora.
* Un système de vote positif pour les publications et les commentaires
* Une opportunité pour l'utilisateur de poster ce qu'il a réellement essayé avec son partenaire, et les résultats qui en ont découlé
* Un système de badges ou de karma pour récompenser les utilisateurs fréquemment votés positivement
* Un système de compte utilisateur pour ceux qui veulent commenter ou poster, similaire à Reddit

**Décisions sur les fonctionnalités clés :**

* Doit-ce être plus anonyme comme Reddit, ou lié à un compte de média social comme Quora pour la crédibilité ?
* Il y aura beaucoup de trolls sur ce site. Comment gérez-vous cela ?
* Doit-ce strictement concerner les relations amoureuses ? Ou les amitiés aussi ?
* Comment pouvez-vous utiliser le système de badges pour motiver les commentateurs particulièrement bons à revenir ?

**Ce que vous apprendrez :** Comment construire un forum ! De plus, il y a beaucoup de gens qui sont prêts à donner quelques minutes de leur temps pour aider des étrangers d'Internet dans le besoin. Sérieusement. Votre principal défi est de vous assurer que ces utilisateurs utiles se sentent récompensés pour leurs efforts, car cela les motivera à revenir.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RClLUbjcjAmW4jLwVYMz9g.png)

### 5. CatBattles

**L'idée :** Les vidéos de chats sont... incroyablement populaires. Une forme particulièrement distinctive de vidéo de chat est la bataille amateur, où deux chats s'affrontent avec des conséquences minimales, mais beaucoup de miaulements et de lutte.

Ce site permettrait aux utilisateurs de poster des vidéos de leurs chats luttant, et permettrait aux spectateurs d'offrir des commentaires amusants. Ce site ne permettrait PAS les batailles de chats professionnelles, ou les combats avec des fins sanglantes. Il est strictement pour le divertissement occasionnel, pas pour les violations des droits des animaux.

**Type de site :** Contenu vidéo

**Fonctions clés :**

* N'importe qui peut télécharger une vidéo de chat
* Les utilisateurs peuvent créer un compte anonyme et ajouter des commentaires.
* Une capture d'écran de chaque chat sur lequel l'utilisateur clique pour deviner le vainqueur avant que le combat ne commence
* Votes positifs pour les meilleures vidéos et les meilleurs commentaires
* La capacité de signaler les vidéos malveillantes, ou celles qui semblent être mises en scène

**Décisions sur les fonctionnalités clés :**

* Pourquoi quelqu'un posterait-il sa vidéo de combat de chats ici plutôt que sur Reddit ou YouTube ? Vous devez ajouter quelques fonctionnalités pour la distinguer de ces sites.
* Comment pouvez-vous rendre ce site populaire au sein de la communauté des amoureux des chats ? Les amoureux des chats n'aiment pas la violence, mais ils aiment l'humour des chats.
* Ce site doit-il dupliquer les dynamiques de [Hot or Not](https://en.wikipedia.org/wiki/Hot_or_Not) ? Comment pouvez-vous créer une expérience de visionnage unique pour le spectateur qui va au-delà de YouTube ? Peut-être un commentaire en direct du combat qui est enregistré lorsque les utilisateurs postent ?

**Ce que vous apprendrez :** Stocker des vidéos dans une base de données est une bonne compétence à apprendre. De plus, reproduire les dynamiques de YouTube sera une bonne pratique que les autres comprendront clairement. Obtenir le ton de l'humour sur le site serait également un bon défi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6OJKK8DQN5z-vQeAuYiv-Q.png)

### 6. CouponBank

**L'idée :** Il y a beaucoup de sites qui permettent aux gens d'échanger des coupons sur une base un pour un. Mais qu'en est-il de la "[longue traîne](https://en.wikipedia.org/wiki/Long_tail)" des coupons ? En d'autres termes, des coupons rares ou obscurs qui pourraient ne pas être populaires sur un site de coupons plus grand public. Et si l'autre personne n'a pas un coupon que vous désirez ? Les coupons sont essentiellement de l'argent, de toute façon.

Vous avez besoin d'une banque pour gérer ce déséquilibre sur le marché. Cette banque demanderait un dépôt initial de 20 $, disons. Ensuite, chaque coupon que vous demandez sera débité de votre compte. Tout coupon que vous êtes en mesure de donner avec succès sera crédité.

**Type de site :** Prêt entre particuliers

**Fonctions clés :**

* Les utilisateurs doivent pouvoir créer un compte, puis déposer 20 $ en dépôt de garantie qui peuvent être retirés à tout moment. Cela sert de garantie. Vous pouvez utiliser Stripe pour traiter cette transaction.
* Les utilisateurs peuvent télécharger une photo d'un coupon. Le site doit alors déterminer automatiquement le produit et le montant du coupon. Il doit inviter l'utilisateur s'il ne peut pas le comprendre. L'API [Cloud Vision](https://cloud.google.com/vision/) de Google devrait aider à cela.
* Lorsqu'un utilisateur demande un coupon, le poster original doit le lui envoyer par courrier. Le montant du coupon est crédité sur le compte du poster original et débité du compte du demandeur.
* Une fois que le compte de quelqu'un atteint 0 $, il ne peut plus demander de coupons jusqu'à ce qu'il en échange lui-même ou ajoute plus d'argent.
* Le site génère des revenus en prenant un petit pourcentage de chaque transaction.

**Décisions sur les fonctionnalités clés :**

* Comment pouvez-vous rendre cela aussi facile que possible pour télécharger un grand nombre de coupons ? L'API Cloud Vision serait un gros atout pour cela.
* Comment pouvez-vous rendre cela aussi facile que possible pour les gens d'envoyer les coupons ? L'utilisateur serait épuisé s'il/elle doit envoyer de nombreux coupons par courrier.
* Comment pouvez-vous rendre le processus de recherche aussi facile que possible ? Et si quelqu'un pouvait télécharger un reçu, et vous pourriez vérifier s'il y a des coupons disponibles pour les articles de la liste ?

**Ce que vous apprendrez :** Cela englobe quelques concepts clés du prêt entre particuliers, bien que avec un profil de risque beaucoup plus faible. C'est un excellent test de votre attention à l'expérience utilisateur. Il y a des millions de personnes à travers les États-Unis qui ont du temps à perdre et cherchent un moyen facile de gagner quelques dollars supplémentaires. Comment pouvez-vous faire de votre site une excellente option pour cela ?

#### Soyez créatif

Ne vous sentez pas obligé de construire les mêmes projets que tout le monde. Il est extrêmement difficile d'obtenir un avantage concurrentiel sur le reste du marché lorsque vous imitez.

Même si l'une de ces suggestions ne vous aide pas, vous devriez envisager de construire des projets qui peuvent créer un peu de personnalité et vous distinguer de tous les autres.

Comme le dit Seth Godin, "Dans un marché encombré, s'intégrer est un échec. Dans un marché occupé, ne pas se démarquer est la même chose que d'être invisible."

**Avez-vous aimé cela ? Donnez-lui un like et faites-le-moi savoir dans les commentaires !**

De plus, si vous cherchez des tutoriels de codage visualisés qui rendent le HTML, le CSS et le JavaScript simples, inscrivez-vous à ma newsletter ici :