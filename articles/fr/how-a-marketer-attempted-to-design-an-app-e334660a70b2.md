---
title: Comment j'ai conçu ma première application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-27T17:41:59.000Z'
originalURL: https://freecodecamp.org/news/how-a-marketer-attempted-to-design-an-app-e334660a70b2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lzEjgNoGOIvzxm4aBat4DA.png
tags:
- name: app development
  slug: app-development
- name: Design
  slug: design
- name: Life lessons
  slug: life-lessons
- name: ' Startup Lessons'
  slug: startup-lessons
- name: UX
  slug: ux
seo_title: Comment j'ai conçu ma première application
seo_desc: 'By Daniel Novykov

  This is a story about building a product, what went wrong, and how it changed my
  career into Design.

  For the past ten years, I’ve built many personal side projects. Some were small
  daily gigs, but there was one that took awhile to a...'
---

Par Daniel Novykov

_Ceci est une histoire sur la construction d'un produit, ce qui a mal tourné et comment cela a changé ma carrière vers le Design._

Au cours des dix dernières années, j'ai construit de nombreux projets personnels. Certains étaient de petits travaux quotidiens, mais il y en avait un qui a pris un certain temps à accomplir.

Cette histoire parle d'une application iPhone sur laquelle je travaillais en 2015-2016. La startup automobile devait permettre aux conducteurs d'économiser de l'argent sur l'essence, réduire les gaz à effet de serre et rendre les véhicules autonomes un peu plus intelligents.

Après de nombreuses séances de brainstorming et de recherche, j'ai assemblé une équipe de développeurs pour m'aider à construire un MVP (Produit Minimum Viable). Nous avons choisi de concevoir l'application iOS en premier en raison d'une meilleure adéquation avec le public.

Pendant le développement de la phase intermédiaire, une page de destination et des canaux sociaux ont été lancés. Cela a accumulé les 1 000 premières personnes pour la liste d'attente et le futur test bêta.

Bien que nous ayons eu quelques défis en cours de route, le projet se développait bien. Des tests utilisateurs fréquents ont confirmé que nous travaillions dans la bonne direction.

Néanmoins, seulement quelques jours avant de publier le MVP pour un test bêta, j'ai décidé de mettre le développement en pause.

Il y avait plusieurs raisons pour lesquelles j'ai pris cette décision, y compris des choses personnelles et des problèmes de financement. Je veux toujours partager le processus de conception que j'ai traversé, les leçons que j'ai apprises et comment cela a reflété sur ma carrière.

### Tout a commencé avec un besoin personnel

Il y a quelques années, j'ai acheté ma première voiture et je suis devenu obsédé par la conduite. Le confort, la joie et la liberté ont surpassé le coût des transports en commun et les embouteillages. Mais il y avait des coûts qui accompagnaient la possession d'une voiture — les contraventions de stationnement, l'assurance, l'entretien et l'essence.

Une chose qui me dérangeait le plus était la fluctuation des prix du carburant au jour le jour. Il pouvait augmenter le matin et baisser la nuit. Il pouvait y avoir une différence de 10 % au coin de la rue, et vous le sauriez juste après avoir quitté la pompe.

J'ai donc commencé à fouiller le web et j'ai trouvé une solution brillante (je pensais à l'époque) pour mes besoins — [GasBuddy](https://gasbuddy.com/). C'est une application qui montre les prix du carburant à jour dans les stations-service locales. J'étais au paradis ce jour-là en imaginant économiser des centaines de dollars par mois sur l'essence.

![Image](https://cdn-media-1.freecodecamp.org/images/mYm2ZT0jFaii0quIr8yHd3OBtxvvjw10eCfO)
_Moi ce jour-là_

Les années suivantes que j'ai passées à utiliser GasBuddy, j'étais reconnaissant pour le trésor qu'ils avaient construit mais frustré par l'interface de l'application qui me rendait fou. Une interface confuse et des fonctionnalités limitées font partie des choses que je ne pouvais plus supporter.

C'est pourquoi, en juin 2015, j'ai commencé mon projet parallèle. Je l'ai appelé Fuelhunt.

L'idée initiale était d'obtenir les données de GasBuddy et de construire une meilleure expérience utilisateur autour. Mais ils sont une grande entreprise et ne voulaient pas partager leurs données même pour un prix raisonnable de startup.

J'ai essayé de trouver un autre fournisseur de données, ce qui s'est avéré être [Waze](https://www.waze.com/). Mais ils ne pouvaient pas m'aider non plus. De plus, la précision de leurs données même aujourd'hui est assez terrible.

![Image](https://cdn-media-1.freecodecamp.org/images/VYi9kcPlBP1BEuB1fOw-DY4YVXRE1WHZqEZ2)
_Encore moi l'autre jour_

J'ai donc pensé, bien, je peux tout faire moi-même. Pourquoi pas. Et le voyage des nuits sans sommeil a commencé.

Mais d'abord, découvrons pourquoi tout cela compte.

### **Quel est l'enjeu ?**

#### 1. Les gens veulent payer moins cher pour l'essence

Je parie que vous avez remarqué que les prix de l'essence diffèrent d'une station à l'autre, d'une marque à l'autre, ou d'une région à l'autre. La raison peut être un problème immobilier ou de marque, ou toute autre condition qui influence le marché du pétrole, comme la politique ou les ouragans.

Beaucoup d'entre nous ne considèrent pas la différence de prix comme des économies. Mais cela peut atteindre 100 à 200 dollars d'économies par an ou plus, selon ce que vous conduisez, comment et où. Vous pourriez argumenter — ce n'est pas une grosse somme. Mais vous pouvez investir les économies dans des repas, des achats ou même plus d'essence.

Il y a trois composantes principales de toute station-service :

* **Confort**  
Proche du travail ou de la maison, a un magasin de quartier, ou autre commodité.
* **Prix**  
Coût de l'essence, offres du magasin, ou autre économie.
* **Qualité**  
Carburant ou service global.

Si vous connaissez des endroits qui vous satisfont avec le carburant, le prix et l'emplacement — c'est génial. Si vous ne vous en souciez pas et achèterez de l'essence chaque fois que vous en aurez besoin — bien, c'est aussi bien.

Pendant ce temps, il y a beaucoup de gens qui ne sont pas conscients des emplacements de gemmes, mais veulent utiliser un endroit pratique avec des prix plus bas.

Cependant, économiser quelques dollars pourrait ne pas être la meilleure idée. Le mauvais carburant n'est pas un mythe. Le carburant lui-même peut provenir de la même raffinerie dans une région, mais être toujours différent à divers points de vente.

Certains facteurs peuvent inclure des filtres à carburant qui ne sont pas correctement entretenus, des additifs inhabituels, du "carburant froid" dans certaines stations, des employés malhonnêtes qui peuvent le mélanger avec de l'huile ou d'autres choses pour faire plus de profit, et ainsi de suite. Tout cela peut entraîner des réparations de voiture coûteuses.

Nous utilisons Yelp, Google Maps, des magazines locaux et demandons à nos amis des recommandations lorsque nous cherchons les bons endroits pour manger. Alors pourquoi ne nous soucions-nous pas autant de nos voitures ? Un véhicule bien traité peut fonctionner plus longtemps sans entretien inattendu.

#### **2. Le changement climatique est réel et nous devons nous en soucier davantage.**

C'est un autre domaine dans lequel je voulais avoir un impact.

En 2014, il y avait plus de [1,2 milliard de véhicules](http://www.greencarreports.com/news/1093560_1-2-billion-vehicles-on-worlds-roads-now-2-billion-by-2035-report) dans le monde, et ce nombre augmente rapidement. Ils produisent tous une énorme quantité de pollution de gaz à effet de serre qui cause :

* L'augmentation des températures car les gaz à effet de serre piègent plus de chaleur.  
Bonjour le réchauffement climatique !
* La fonte des calottes glaciaires polaires qui peut entraîner une élévation du niveau de la mer.  
Bonjour les inondations destructrices !
* L'appauvrissement de notre couche d'ozone qui permet aux rayons UV nocifs d'entrer sur la Terre. Bonjour le cancer de la peau !

La question est — pouvons-nous faire quelque chose à ce sujet ?

Eh bien, nous ne pouvons pas réduire la production de nouveaux véhicules car il y a une demande croissante pour eux. Et nous ne pouvons pas recycler les voitures existantes car elles sont généralement réutilisées dans les pays du tiers monde. Pouvons-nous passer à l'électrique ? En quelque sorte.

![Image](https://cdn-media-1.freecodecamp.org/images/LbdZMPcdOITicDOUwNcTuPNRiRKlFJyycSZh)
_L'avenir arrive_

Les voitures électriques sont l'avenir. Elles sont silencieuses, rapides et peu coûteuses à utiliser. Elles sont plus fiables avec moins de pièces à casser. Et surtout, elles n'émettent pas de dioxyde de carbone.

Mais c'est l'avenir que beaucoup d'entre nous ne peuvent pas se permettre aujourd'hui. Certaines voitures sont trop chères, où d'autres ne peuvent pas encore fournir une valeur adéquate.

Tout pourrait changer avec le Model 3 de Tesla (ainsi que d'autres propositions de niveau d'entrée des fabricants), un soutien gouvernemental plus important pour les véhicules électriques, et d'autres avantages. Mais nous n'en sommes pas encore là.

Alors, comment pouvons-nous avoir un impact sur l'environnement avec tout ce que nous avons aujourd'hui — avec tous ces véhicules avec des moteurs à combustion interne qui réchauffent le monde dans lequel nous vivons ?

### **Suis-je le seul à m'en soucier ?**

Les premières questions que je me suis posées étaient « Combien de personnes partagent le même problème et la même vision que moi ? » et « Y a-t-il assez d'utilisateurs potentiels pour que cela vaille la peine de construire un produit ? »

J'ai mené quelques enquêtes et parlé à des amis qui sont aussi conducteurs. Je voulais comprendre les besoins et les désirs d'un public cible.

Voici quelques informations :

* Le public cible comprend la plupart des propriétaires de véhicules — conducteurs occasionnels, navetteurs réguliers, chauffeurs de taxi, routiers.

Lors du choix d'une station-service,

* Les facteurs les plus critiques sont la commodité et les prix plus bas du carburant pour les conducteurs du marché nord-américain. La qualité du carburant s'ajoute dans certains pays d'Europe de l'Est.
* Le programme de fidélité à la marque ne semble pas être un facteur du tout parmi les répondants du marché nord-américain. C'est un facteur significatif dans le marché de l'Europe de l'Est.
* D'autres choses comme un magasin de commodité, un lavage de voiture et une opération 24 heures sur 24 n'ont pas beaucoup d'importance parmi tous les répondants.
* Les gens sont prêts à partager des expériences positives ou négatives à la pompe.  
Ils veulent encourager ou rediriger d'autres conducteurs pour faire le plein à un endroit particulier s'il y en a un.
* La plupart des conducteurs ne suivent pas leurs dépenses en essence, car c'est chronophage ou ils ne sont pas conscients des outils faciles pour le faire. La majorité est prête à suivre les coûts et le kilométrage de manière « automatique ».
* Presque la moitié des répondants ont dit qu'ils se souciaient de l'environnement d'une certaine manière, comme le tri des déchets et le recyclage. Ils sont intéressés à progresser avec la réduction de l'empreinte carbone.

Je voulais aussi savoir ce que les gens font pendant qu'ils font le plein de leurs voitures.   
Je voulais savoir si je pouvais intégrer un produit dans cette activité de 5 minutes et rendre ce temps plus divertissant.

Parmi certaines activités, il y avait :

* Regarder le compteur d'essence
* Fixer la buse
* Observer les voisins
* Chercher de nouvelles rayures et bosses sur la voiture

### **Quelles options les conducteurs ont-ils aujourd'hui ?**

Outre la sensibilisation personnelle aux stations-service et le bouche-à-oreille, il existe de nombreux acteurs sur ce terrain pour trouver une pompe à essence. En réalité, aucune des solutions ne correspondait au produit que mes utilisateurs cibles et moi-même aimerions utiliser.

Je commencerai par la concurrence mineure, puis je passerai aux plus importantes.

#### 1. Systèmes **infodivertissement** intégrés

Aujourd'hui, même les véhicules d'entrée de gamme sont équipés de systèmes d'infodivertissement préinstallés. Les conducteurs peuvent obtenir la plupart des informations dont ils ont besoin pendant la conduite. Ils peuvent consommer du contenu multimédia, voir les statistiques du véhicule, naviguer dans la ville et plus encore. Malheureusement, cela ne peut pas être dit pour les prix de l'essence en temps réel. Il n'y a que quelques systèmes qui le fournissent.

En théorie, les systèmes d'infodivertissement devraient être plus sûrs que de regarder un appareil mobile pendant la conduite. Mais en raison d'une mauvaise conception, la plupart d'entre eux sont en fait très distractifs et [dangereux](https://www.eurekalert.org/pub_releases/2017-10/a-nvi100217.php). Vous ne pouvez pas remplacer l'unité principale de la voiture et vous ne pouvez pas changer le système d'exploitation. De plus, les smartphones modernes offrent une meilleure expérience de navigation.

![Image](https://cdn-media-1.freecodecamp.org/images/pzYPCadRokxIu-gnLRb2a61XrGAXJJEj54fc)
_Pourquoi les principaux constructeurs automobiles ignorent-ils la technologie moderne et l'UX ?_

#### **2. Apple Maps**

Apple Maps est la première option de navigation pour des millions d'utilisateurs sur iPhone. Pourtant, il est limité en termes de fonctionnalités et ne fournit que des informations de base telles que les contacts et les directions.

![Image](https://cdn-media-1.freecodecamp.org/images/U8kRgZTxLWnzHY7wDCPsRp5MG7B5Nsw6aJGW)
_Apple Maps en 2015 — rien que des infos basiques._

De plus, il ne montre pas les prix de l'essence et a une couverture cartographique faible pour de nombreuses régions du monde. Ces deux composantes sont essentielles pour le conducteur.

#### **3. Google Maps**

Google a plus d'expérience dans la construction de cartes qu'Apple. C'est de loin la meilleure application mobile de cartographie mondiale sur n'importe quelle plateforme.

En plus des informations de base, il dispose d'avis de consommateurs, d'images utilisateur, de vue de la rue et ils ont commencé à extraire les données sur le carburant de Waze en décembre 2015 !

![Image](https://cdn-media-1.freecodecamp.org/images/T9Vfhb7euFWVQe4BvyMcfRz1QxOYsxBf6H5u)
_Trouvé cela dans la Machine à Temps :)_

Lorsque vous construisez une startup, une telle mise à jour d'un leader du marché semble être un coup de grâce ! Mais cela m'a seulement prouvé que cette fonctionnalité est en demande, ou du moins les ingénieurs de Google le pensent. Ce qui est, apparemment, vrai.

Ils ont gardé cette fonctionnalité simple. Il n'y avait pas de filtrage, de contributions utilisateur, ou d'autres engagements sociaux.

#### 4. Applications de **découverte de lieux**

Les applications de découverte de lieux incluent Foursquare, Yelp et Pages Jaunes. Elles fournissent une variété de détails comme des avis et des offres. Pourtant, les conducteurs interrogés ont répondu que ce n'était pas leur solution de prédilection pour trouver une pompe à essence.

![Image](https://cdn-media-1.freecodecamp.org/images/4QXzo3-WIup3hh3dksUgombRxE6c8olTlslZ)
_Foursquare et Yelp. Selon les recherches, les conducteurs ne les utilisent pas pour trouver une station-service._

#### 5. Localisateurs de stations-service

Voici une chose excitante — presque chaque pays a une source pour obtenir les prix du carburant. Certains pays ont un prix unique pour l'essence car il est contrôlé par le gouvernement. Mais en général — c'est tout différent selon la marque, le lieu et le temps.

Je ne vais pas approfondir l'analyse ici, mais en bref :

* Certains sites web sont uniquement pour un usage sur ordinateur et ne sont pas adaptés au monde mobile. Ils ont également tendance à avoir une UX terrible.
* La grande majorité des applications ne sont pas globales. Elles peuvent couvrir un ou parfois deux pays pour le plus grand « marché local », comme les États-Unis et le Canada.
* Certaines applications ne sont pas assez informatives. Des applications supplémentaires doivent être installées pour compléter « l'expérience du conducteur ».

![Image](https://cdn-media-1.freecodecamp.org/images/p2zVpJAF1vSPFSRCvJHUjdUEdK3ErQuJd0CI)
_Fuelzee, TransportApp, Spritradar — des applications sans âme._

* Il y a des cas où les applications ne sont pas localisées dans d'autres langues et territoires. Pourquoi avez-vous besoin d'un autre compte pour télécharger une application ?

![Image](https://cdn-media-1.freecodecamp.org/images/HhHl5ssWy-PSL6iFrJOQNYZCppFM2phJaPOs)
_Les voyageurs fréquents ne sont pas heureux._

* En fin de compte, avoir un tas d'applications pour divers emplacements n'est pas une solution.  
Elles auront toutes une interface utilisateur différente, plusieurs comptes et prendront de l'espace de stockage sur l'appareil.

#### **6. Applications de grandes marques pétrolières**

Au début, je pensais que les marques Top Tier pouvaient investir une tonne d'argent pour développer leurs propres applications et les rendre géniales. Non.

![Image](https://cdn-media-1.freecodecamp.org/images/w-ncqF83xXQLzSFd5hz3gXB7wj5Dne9jc9Yj)
_Petro-Canada, Esso et Shell. L'approche Top Tier._

Certaines ont adopté une approche consistant à compresser un site web mobile dans l'application. D'autres pensaient que de minuscules boutons avec du texte illisible étaient de bonnes options pour les conducteurs.

Mais la plupart d'entre elles contiennent des informations sur les prix de l'essence et elles sont très précises là où elles sont appliquées.

#### **7. Waze**

Waze, qui appartient à Google aujourd'hui, est mon outil de navigation préféré. C'est un réseau de crowdsourcing de 90 millions de conducteurs dans le monde. Il montre le trafic, les conditions routières, les accidents et les pièges de police.

![Image](https://cdn-media-1.freecodecamp.org/images/YZtdpaCRwgjCT3kFgu630ZunJIyK-F6CiqXl)
_À part une récente refonte mineure, rien n'a changé depuis 2015._

Waze fournit également les prix du carburant pour de nombreux endroits. Contrairement à son excellente expérience de navigation, les données sur le carburant sont assez imprécises.

J'ai fait une rapide enquête pour découvrir pourquoi les conducteurs n'utilisent pas cette fonctionnalité. Les hypothèses sont :

* L'élément pour trouver une station-service est caché profondément dans le menu et n'est pas intuitif à utiliser.
* Waze affiche l'étiquette lorsque le prix du carburant a été mis à jour pour la dernière fois. C'est bien à savoir. Pourtant, lorsque vous voyez « mis à jour il y a quelques jours » sur n'importe quel endroit — c'est presque certainement un signal de faible contribution communautaire. Si les gens ne contribuent pas assez pour le rendre utilisable, pourquoi quelqu'un ferait-il confiance et l'utiliserait-il ?

#### **8. GasBuddy**

Voici un gros — GasBuddy. Il a été fondé en 2000 et compte actuellement 65 millions d'utilisateurs. Il opère aux États-Unis et au Canada. Il a été récemment lancé en Australie.

En parlant des marchés des États-Unis et du Canada, leurs données sont assez phénoménales — surtout puisque elles sont recueillies auprès d'une communauté de crowdsourcing et d'autres sources. Pourtant, leur application a échoué en termes d'utilisabilité et de performance.

Lors de la réalisation de recherches et de l'observation de personnes effectuant des tâches d'utilisabilité, j'ai découvert que :

* De nombreux utilisateurs, qui n'étaient pas familiers avec l'application, ne pouvaient pas accomplir une chose simple comme définir des directions vers un lieu. Cela nécessitait sept clics pour accomplir cette tâche.

![Image](https://cdn-media-1.freecodecamp.org/images/aURAcdPFROl0Z96r2P42OftyOANxNv3GGCpv)
_Vue de liste GasBuddy 2015/2017. Les « améliorations » incluent plus de boutons, un texte moins lisible et des bannières publicitaires colossales._

* La majorité des conducteurs n'utilisaient pas la vue de liste par défaut et passaient immédiatement à une vue de carte. Le problème est que l'information sur la vue de liste n'est pas très claire. Il est difficile de comprendre dans quelle direction se trouve la station-service. Elle peut être proche en distance, mais peut prendre plus de temps à conduire en raison du trafic, des intersections difficiles, des demi-tours, ou d'une douzaine de panneaux stop.
* Dans l'ensemble, l'interface utilisateur est assez confuse et distraante. L'architecture de l'information manque de logique à certains endroits. Les publicités agaçantes consomment des données cellulaires et de l'espace à l'écran. Les éléments illisibles à distance et les minuscules boutons rendent difficile l'accomplissement d'une tâche sans donner trop d'attention au smartphone.

![Image](https://cdn-media-1.freecodecamp.org/images/AFB30RqlXDxrrWQ-8gMYvjMaE4dkCyQ6N7vm)
_Les utilisateurs se plaignent des publicités, mais GasBuddy continue d'en pousser davantage._

* GasBuddy, ainsi que de nombreux autres concurrents, affirment que les conducteurs peuvent économiser de l'argent avec leur application — et c'est vrai. Mais il n'est pas clair combien la personne économise à la pompe, car il n'y a pas d'indicateur d'économies.  
L'application affiche des emplacements avec des prix plus bas mais ne montre pas la valeur de l'utilisation de l'application sur une période de temps.
* Les utilisateurs peuvent gagner 100 $ d'essence par jour en échangeant des points gagnés dans l'application pour des soumissions de prix en entrées pour gagner. Pourtant, les chances de gagner sont d'environ 65 millions contre 1.  
Néanmoins, il semble que cela fonctionne pour l'engagement et la rétention des utilisateurs.

#### 9. Suiveurs d'économies

Il existe de nombreuses applications pour recueillir les statistiques des véhicules et suivre diverses dépenses. La majorité d'entre elles nécessitent un effort important pour entrer les données, qu'il s'agisse d'une opération manuelle avec des dizaines de champs ou de la numérisation de reçus avec une reconnaissance de texte et de champs peu fiable. La partie visuelle de ces applications est désagréable et « effrayante » — comme l'ont répondu la plupart des conducteurs.

![Image](https://cdn-media-1.freecodecamp.org/images/C8jmp8uLuxtyLtDee2cswMpofVILzokuS5BJ)
_Une interface utilisateur typique pour un suiveur de kilométrage moyen._

D'autre part, il existe des solutions pour la surveillance des voitures, comme [Automatic](https://www.automatic.com/). Elles ont leurs avantages et inconvénients, mais le plus gros problème avec elles est qu'un adaptateur spécial est requis pour leur fonctionnement, ce qui est un investissement supplémentaire.

À ce stade, après les recherches et les sessions de test utilisateur que j'ai effectuées, le tableau était clair — il y avait une niche sur le marché et je pouvais la combler avec un nouveau produit.

### **Conception de Fuelhunt**

Je voulais créer un produit qui embrasse les meilleures pratiques en matière d'utilisabilité. En même temps, il élimine les points de douleur que les utilisateurs ont avec d'autres applications dans ce segment.

Je ne voulais pas créer « encore une autre application pour trouver une station-service ». Je voulais un produit qui aurait un impact plus significatif sur nos vies à l'avenir.

Je vais sauter les dizaines d'itérations, de croquis et de maquettes pour passer directement à la construction finale du MVP qui a été testée avec succès par des utilisateurs potentiels.

Voici quelques améliorations clés par rapport à la concurrence :

#### 1. Une seule application pour couvrir les **prix mondiaux du carburant**

Je parle d'une phase post-MVP. Mais l'architecture de la base de données devait être développée au préalable pour une expansion facile.

Au début, cela ne semblait pas être un défi.

Je devais résoudre le problème de tout réseau social : pas de contenu = pas d'utilisateurs, pas d'utilisateurs = pas de contenu.

Dans ce cas, le contenu était les emplacements des pompes avec les types de carburant, les prix actuels de l'essence et les avis des utilisateurs. Pour obtenir ce contenu rapidement, nous avons collecté tout ce que nous pouvions trouver sur le marché et construit — comme nous l'avons appelé — une base de données sale.

Bien qu'il y ait eu beaucoup de données ouvertes, c'était un vrai désordre. Certaines sources fournissaient des API claires, d'autres n'avaient que des feuilles de calcul Excel. Ensuite, nous devions trouver un moyen de récupérer les données et de les rendre utilisables.

Un autre problème était la différence dans les listes de marques et les niveaux d'octane dans diverses régions. L'Amérique du Nord et l'Europe calculent l'indice d'octane de [manières différentes](https://en.wikipedia.org/wiki/Octane_rating). Le 87 de l'Amérique du Nord est comme le 95 de l'Europe, où le 91 de l'Amérique du Nord est plus comme le 98 de l'Europe, et ainsi de suite.

Pour être honnête, cela a pris un certain temps pour tout rassembler sous un même toit.

Enfin, nous avions les données, mais elles étaient inexactes. Heureusement, les prix du carburant changent si rapidement que cela n'avait pas vraiment d'importance si le prix datait d'un jour ou d'une semaine — il était toujours faux. Donc, nous étions assez proches de la précision de Waze et de Google Maps.

#### 2. Interface utilisateur claire et navigation simple dans l'application

Peu importe à quel point il est [dangereux](http://www.apa.org/research/action/drive.aspx) d'utiliser un smartphone dans la voiture ou à quel point les amendes sont élevées pour les appareils portables. Les gens utilisent toujours leurs téléphones en conduisant. Ils les tiennent soit dans leurs mains, soit le téléphone est monté sur le tableau de bord.

Notre travail en tant que concepteurs est de construire des fonctionnalités bien organisées et faciles à utiliser et de réfléchir à toutes les façons possibles d'utiliser notre produit. Nous devons nous assurer que l'ergonomie minimise la distraction et ne nuit pas à l'utilisateur final.

Texte grand, points de contact plus grands, flux d'écran clair, notifications intelligentes, pas de publicités. Ce ne sont là que quelques-uns des critères que j'ai gardés à l'esprit.

En parlant de navigation, l'application Fuelhunt se compose de 4 écrans :

* **Écran principal**  
 pour trouver des stations-service
* **Écran d'ajout**  
 pour ajouter du contenu
* **Activité**  
 pour voir les activités publiques de l'utilisateur et de ses amis
* **Profil**  
 pour voir toutes les activités et statistiques de l'utilisateur

#### **3. Recherche de pompe ultra-rapide**

Le rôle principal de l'application est de trouver une station-service optimale et de définir des directions pour cette station. Le flux a été optimisé pour accomplir cette tâche en moins de 10 secondes.

![Image](https://cdn-media-1.freecodecamp.org/images/7VcRxJOX2Uu61tRpjWKnfTrQ3-APN2JJcTTn)
_Écran principal_

Lors du lancement de l'application, elle affiche la vue carte avec les emplacements des pompes et — en utilisant une combinaison de distance, de direction de déplacement de l'utilisateur, de prix et de score de revue, elle présélectionne la meilleure option pour faire le plein. Aucun écran intermédiaire ou clics supplémentaires nécessaires.

Les bannières du bas contiennent toutes les informations dont le conducteur a besoin à ce moment-là : la marque, le prix de l'essence, une indication de la « fraîcheur » de ce prix, et l'emoji de notation.

Au lieu d'afficher la distance jusqu'à l'emplacement, le temps de conduite est fourni. Le trafic et les conditions routières peuvent jouer un rôle plus important.

Le bouton pour obtenir des directions est toujours visible, ce qui rend plus rapide la définition de l'itinéraire. Cela a réduit les sept clics de GasBuddy à un seul.

Toutes les épingles de localisation sont codées par couleur selon la pertinence temporelle :

* Vert si elles ont été mises à jour aujourd'hui — C'est le plus précis.
* Orange si elles ont été mises à jour hier — C'est quelque peu pertinent.
* Gris si elles ont été estimées — Tout ce qui est plus ancien et tout ce qui a été collecté auprès de sources tierces.

En cas de données de prix inexactes, cette approche est plus efficace. Elle concentre l'utilisateur sur la précision des données.

Waze marque les emplacements par une échelle de prix, avec du vert pour bas et du rouge pour élevé. Cette station-service à essence bon marché peut avoir l'ancien prix et peut être plus chère qu'une station rouge, mais a un prix mis à jour actuellement.

Choisir Google Maps comme fournisseur de cartes au lieu de Apple Maps natif ajoute une meilleure couverture mondiale et un zoom à un doigt. Cela est assez pratique dans la voiture.

![Image](https://cdn-media-1.freecodecamp.org/images/4FA5ZLfzJCSd3TsK1XdxGdPQfIHGgWejteuY)
_Filtres de recherche_

Les filtres sont une fonctionnalité rarement utilisée mais utile. Ils sont cachés sous les fonctions de recherche. Cela rend non seulement l'interface utilisateur globale plus propre, mais donne également à l'utilisateur le pouvoir de créer une carte personnalisée et d'afficher les marques et les types de carburant dont l'utilisateur a besoin.

#### 4. Évitement des **mauvais emplacements**

La recherche a démontré que presque personne ne lit un avis à l'avance lorsqu'il se dirige vers la pompe. C'est quelque chose que nous faisons spontanément. Nous conduisons, ressentons le besoin, voyons une station-service et faisons le plein.

![Image](https://cdn-media-1.freecodecamp.org/images/Cl31zQkCsdQLfJEbAuHVPOKZyWKj9WM7vHNd)
_Alerte de mauvaise station_

Les gens continuent d'écrire des avis. De nombreux conducteurs partagent leurs retours négatifs si quelque chose ne va pas. Dans ce scénario, le conducteur ne saura rien à l'avance, mais il pourrait ressentir les conséquences d'un mauvais carburant le lendemain ou dans un mois.

Pour résoudre ce problème, un système de notification a été conçu pour alerter le conducteur s'il y a un problème à l'emplacement.

#### **5. Soumission facile de contenu pour la contribution des utilisateurs**

Il y a un bouton pour faciliter la soumission de nouveaux contenus par les conducteurs. Ils peuvent fournir une mise à jour de prix, des données de remplissage ou un nouvel avis. Il est toujours visible sur la barre d'onglets, peu importe l'écran sur lequel se trouve l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/HUJNXrJcbiHbTM0Ss4M0fOUS8k2K97S8EMfQ)
_Soumission des prix du carburant_

Si le prix du carburant a été mis à jour, l'application demande au conducteur d'entrer les données de remplissage. De la même manière, elle demande une mise à jour de prix après que les données de remplissage ont été ajoutées.

![Image](https://cdn-media-1.freecodecamp.org/images/CFbNOag6Kegl7YFq1c5KpiFS1VaCmXKSGQp5)
_Soumission des informations de remplissage_

Contrairement aux concurrents qui se contentent de dire que les utilisateurs économisent avec leur application, Fuelhunt démontre immédiatement le montant économisé à la pompe. Après chaque remplissage, Fuelhunt calcule instantanément la différence de prix entre les stations locales et fournit une valeur claire à l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/QyGyYuXcXCnh8up2N3cw-Cpc33njBaj4KEyU)
_Soumission d'un avis_

Parfois, cela demande beaucoup d'efforts à l'utilisateur pour soumettre un avis. Je l'ai rendu simple avec une évaluation de la qualité du carburant et de l'expérience globale, ainsi qu'une description optionnelle.

#### **6. Suivi des activités et des statistiques**

L'écran d'activité affiche les activités publiques de l'utilisateur et de ses amis, comme les points gagnés, l'argent économisé et les avis écrits.

Après les tests, nous avons débattu de l'inclusion de cette fonctionnalité dans l'application. Néanmoins, je voulais voir comment le public réagirait. Je voulais aussi rendre Fuelhunt un peu plus social. Donc, elle a été incluse dans la construction du MVP.

![Image](https://cdn-media-1.freecodecamp.org/images/Dfjf4yRYLEODAqFQ31bY5uAx5n7C0zgvwkf2)
_Écrans d'activité et de profil_

L'écran de profil contient uniquement le contenu de l'utilisateur. L'utilisateur peut voir diverses statistiques ventilées par périodes :

* Argent dépensé en essence et quantité de carburant brûlé
* Argent économisé avec son équivalent en kilométrage économisé
* Kilométrage du véhicule lui-même et consommation de carburant

![Image](https://cdn-media-1.freecodecamp.org/images/fax6JnGDRtDtK8D4P-xGq5ah2JmRWp8F6sZH)

![Image](https://cdn-media-1.freecodecamp.org/images/2Mzjv5tuiwE2QL4mr9zpold3aMAeCUTn-SWw)
_Suivi des statistiques_

Ce suivi peut servir à de nombreuses fins, de la connaissance de l'état de votre voiture et de votre portefeuille à la facilitation du calcul des voyages d'affaires et au remplissage des formulaires fiscaux. Mais l'idée principale a été gardée pour les futures versions.

#### **7. Mécanismes de gamification pour l'engagement des utilisateurs et la monétisation**

La gamification est utilisée dans de nombreux produits, mais parfois elle n'est pas bien faite. Souvent, elle bénéficie aux utilisateurs de haut niveau où les débutants peinent à atteindre le sommet, peu importe leurs compétences. Les utilisateurs de haut niveau reçoivent généralement plus d'attention, de likes et d'avantages.

La gamification de Fuelhunt a été conçue pour éliminer la barrière pour les nouveaux utilisateurs et rendre tout le monde égal pour concourir.

Pour chaque rapport de prix et avis écrit, l'utilisateur gagne des points. Ceux qui sont actifs pendant un certain nombre de jours consécutifs gagnent suffisamment de points pour échanger des fonctionnalités premium gratuitement. Une fois qu'ils deviennent des utilisateurs inactifs, ils perdent cet avantage et doivent recommencer.

#### _8._ Croissance post-MVP

Assez parlé de ce qui a été fait. La feuille de route de l'application semblait assez intéressante à l'époque avec un certain nombre de fonctionnalités cool, mais j'identifierais deux grandes étapes :

Premièrement, **l'expansion mondiale** — c'est un élément clé pour construire une grande entreprise de données. Pourquoi est-ce important ?

J'avais la vision qu'un jour, avec de telles données, les voitures autonomes pourraient conduire du point A au point B et être assez intelligentes pour prendre des décisions par elles-mêmes.

Elles pourraient définir l'itinéraire le plus optimal et prendre en compte le trafic, les conditions routières, le niveau de carburant et où faire le plein de manière la plus efficace. C'est l'avenir.

Et deuxièmement, j'ai commencé tout cela pour essayer de **réduire l'empreinte carbone** avec les technologies que nous avons aujourd'hui. Sans que les conducteurs aient besoin d'investissements supplémentaires et de gadgets supplémentaires à installer.

Pour ce faire, je voulais étendre la base de données de Fuelhunt avec tous les modèles de véhicules sortis à ce jour et leur consommation de carburant en ville, sur autoroute et combinée. Ensuite, comparer cela avec les données réelles de mes utilisateurs pour déterminer l'inefficacité de conduite. Et si plus d'essence est brûlée que nécessaire, mettre à jour l'utilisateur avec des suggestions pour améliorer ses habitudes de conduite.

### **Le résultat**

**Qu'est-ce qui a mal tourné ?**

1. **L'équipe est tout**  
Il est vital d'avoir les bons partenaires et membres d'équipe impliqués. Mais il est également important d'avoir des développeurs comme équipe centrale dans la même pièce pour pouvoir itérer et exécuter rapidement.  
J'ai fini par construire ce projet avec des développeurs à l'étranger, ce qui a apporté de nombreux obstacles à l'ensemble du processus. Avant de réaliser que certains membres de l'équipe n'étaient pas adaptés à la culture, il était trop tard et le prix que nous devions payer pour les remplacer était déjà trop élevé.
2. **Le problème de l'ajout de valeur**  
Malgré toutes les recherches et la validation des utilisateurs qui ont montré qu'il y avait un produit et un marché adaptés, j'avais encore des doutes.  
J'ai passé trop de temps à essayer de perfectionner l'expérience dès le premier jour au lieu de publier le MVP, d'obtenir des retours et de passer à l'itération.
3. **J'ai manqué de liquidités**  
Dès le début, je ne voulais pas utiliser le financement participatif ou toute autre opportunité d'investissement pour lever des fonds. Je voulais me limiter à mon propre argent pour me sentir plus responsable du projet. Comme, si j'échoue, je perdrai mon propre argent.  
Et je l'ai fait. Ferais-je quelque chose de différent la prochaine fois ? Définitivement oui.
4. **Problèmes personnels**  
Parfois, cela arrive, quand vous devez choisir entre la vie personnelle et les affaires. J'ai essayé d'équilibrer les deux.  
J'ai perdu de vue le projet et j'ai laissé les distractions prendre le contrôle sur moi. Il était trop tard quand je m'en suis rendu compte.

**Qu'ai-je appris ?**

Les startups sont considérées comme des expériences intenses qui entraînent un apprentissage rapide. J'ai acquis beaucoup d'expérience en concevant Fuelhunt, en remplissant plus de rôles que je n'aurais pu en remplir en tant qu'employé à temps plein.

La partie excitante a été d'acquérir les connaissances qui m'ont aidé à passer à une carrière de conception de produits depuis mon ancien domaine du marketing. C'est une expérience sur laquelle je peux me retourner pour construire quelque chose de plus significatif.

Fermer une startup est souvent perçu comme une mauvaise et triste chose. Pour moi, ce n'est qu'un chapitre avant la prochaine aventure.

Je suis actuellement ouvert aux opportunités de carrière à Toronto pour contribuer en tant que [UX/Product Designer](http://dnovykov.com/). N'hésitez pas à [me contacter](mailto:hello@dnovykov.com).