---
title: 'Au cœur de la tempête : comment j''ai aidé à sauver des vies lors des inondations
  désastreuses au Kerala'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-20T13:46:23.000Z'
originalURL: https://freecodecamp.org/news/at-the-eye-of-the-flood-5ddec61a87b8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WhQOyjS8Ez_-53GLWVHs6Q.jpeg
tags:
- name: community
  slug: community
- name: 'Kerala '
  slug: kerala
- name: Life lessons
  slug: life-lessons
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Au cœur de la tempête : comment j''ai aidé à sauver des vies lors des
  inondations désastreuses au Kerala'
seo_desc: 'By Biswaz

  This my perspective on the worst natural calamity experienced by the state of Kerala,
  and how I was able to help build the foundation upon which a great community was
  built. It was a humbling and also challenging experience at the same time...'
---

Par Biswaz

Voici ma perspective sur la pire catastrophe naturelle vécue par l'État du Kerala, et comment j'ai pu aider à construire les fondations sur lesquelles une formidable communauté s'est édifiée. Ce fut une expérience à la fois d'humilité et de défi.

Avertissement : J'ai fait de mon mieux pour vérifier les données de cet article. Mais je ne donne aucune garantie quant à l'exhaustivité, la fiabilité et l'exactitude de ces informations.

#### 11 août 2018

Je suis rentré chez moi à Palakkad depuis mon foyer universitaire. Palakkad, ainsi que de nombreux autres districts du Kerala, venait de connaître l'une des pires inondations de son histoire. Mais ce n'était que le début. J'étais loin de me douter de ce qui allait arriver.

L'All Kerala Student Congress, un événement organisé par la section IEEE du Kerala, a été annulé. Le groupe WhatsApp a fait l'objet de discussions sur ce que nous pourrions faire pour aider les personnes touchées par l'inondation. En conséquence, nous avons décidé de créer un site web. J'ai commencé à travailler sur une application Django.

M. Muralidaran Manningal, du SEMT, qui est également présent à l'IEEE, a donné les exigences pour la version de base du site. À l'époque, les exigences étaient simples :

1. Il y aurait un formulaire où les gens ou les camps pourraient spécifier leurs besoins, comme de l'eau, des médicaments, etc.

2. Il y aurait un formulaire de contact listant les informations de 2 ou 3 personnes de chaque district qui coordonneraient les efforts.

3. Tout bénévole souhaitant aider devrait pouvoir visualiser tous les articles nécessaires dans divers endroits proches de lui.

4. Les besoins qui ont été pris en charge devraient être marqués comme terminés afin qu'il n'y ait pas trop de chevauchements.

J'ai livré le site à minuit ce jour-là. Je me souviens avoir posté la capture d'écran de mon terminal comme statut WhatsApp juste pour avoir l'air cool.

![Image](https://cdn-media-1.freecodecamp.org/images/Lsv4j-mR-2975w3Wu2CVbNLCfxzdNuEFmZUW)

Ce fut la naissance d'un jalon historique pour moi. C'est devenu une plateforme pour une collaboration sans précédent qui s'est produite en 14 heures. Le Produit Minimum Viable (MVP) était lancé !

![Image](https://cdn-media-1.freecodecamp.org/images/q34ydyv0UJY7KTu7ZixpHGkQ7f1o0ItEZc6v)
_La première affiche partagée au sein des communautés étudiantes_

#### 12 août 2018

Nous avons commencé à recevoir des demandes à l'échelle du district. Je me souviens que les administrations des districts de Palakkad et d'Ernakulam ont été les premières à rejoindre la plateforme. L'IEEE a initié des groupes WhatsApp par district pour mobiliser les bénévoles, qui sont devenus plus tard les centres de contrôle de jeunes gens travailleurs à travers tout le Kerala. Au début, nous avions 3 points de contact (POC) qui étaient tous des étudiants chargés de collecter les ressources et de les acheminer vers les centres de collecte officiels des districts.

La première demande est venue de Pathanamthitta — pour 10 litres d'eau.

Le site web a commencé à se propager lentement sur les réseaux sociaux. Je me souviens avoir vu la police du Kerala, un groupe de célébrités, et enfin notre ministre en chef partager le site web. C'était un moment excitant pour un étudiant en B.Tech un peu perdu qui n'avait aucune idée de l'expérience dramatique, horrifiante et pourtant palpitante qu'il s'apprêtait à vivre.

![Image](https://cdn-media-1.freecodecamp.org/images/tW9wTTTydlT6rBsi08D1-QFPfpssRdLSUjMN)

Nous tournions sur le forfait gratuit d'une plateforme cloud appelée Heroku. J'ai choisi Heroku car il proposait un forfait gratuit pour commencer, c'était extrêmement simple à configurer, et nous aurions toujours accès aux gros moyens si nécessaire. Mais surtout, j'avais déjà déployé environ 4 applications Heroku auparavant et j'y étais habitué. Finalement, nous savions que nous pourrions avoir à payer ou à passer à une autre plateforme cloud gratuite.

Il a été envisagé de passer de Heroku au State Data Center, car ce dernier nous était proposé gratuitement. Cette idée a été abandonnée par la suite compte tenu des heures de travail qui seraient perdues à configurer une machine Linux nue. Dans un scénario critique comme celui-ci, où chaque minute compte, Heroku a été le meilleur choix que j'ai fait. Je me souviens que c'était mon slogan :

> git push heroku master

Je le disais à mon petit frère lors de certains de mes projets précédents sur Heroku. Et pendant ce projet, j'ai utilisé cette commande assez souvent, en raison de la nature agile du travail. (Désolé pour les amateurs de CI/CD, nous ne l'avons mis en place que plus tard.)

Nous avons atteint la limite de 10 000 lignes sur la base de données gratuite de Heroku. Ce fut l'une des premières choses qui m'a inquiété. Un peu de maintenance (qui a duré jusqu'après 1h du matin IST) et quelques commandes shell plus tard, nous étions de nouveau opérationnels grâce à AWS et ses crédits gratuits — nous avons donc déplacé la base de données vers AWS !

Le lendemain, la situation s'est considérablement aggravée. Les demandes provenant d'endroits comme Ranni ont intensifié la pression. Nous devions faire quelque chose…

![Image](https://cdn-media-1.freecodecamp.org/images/3KQ64QbuLUJKf040ZBZ1Sf21vBBQnhuKZLTw)
_Au moment de terminer ceci, le site comptait plus de 1,8 crore de pages vues au total et plus de 10 lakhs de visiteurs uniques._

#### À partir du 16 août 2018

### La naissance de notre communauté open-source

Un message WhatsApp a circulé à cette époque. Il disait que nous recevions une quantité énorme de demandes et que nous avions besoin d'aide. C'était tout à fait vrai ! La communauté a commencé à signaler des problèmes et à ajouter des améliorations. Pour être franc, j'ai été terrifié par le nombre d'appels téléphoniques que j'ai reçus ce jour-là.

[**Hi all · Issue #92 · IEEEKeralaSection/rescuekerala**](https://github.com/IEEEKeralaSection/rescuekerala/issues/92)  
[_Bonjour, le nombre de PR et de tickets vient d'exploser. Et nous manquons de temps. Veuillez lister ci-dessous comment nous, les développeurs…_github.com](https://github.com/IEEEKeralaSection/rescuekerala/issues/92)

Le ticket ci-dessus sur GitHub a été le point de départ de l'engagement de notre communauté. Tout croissait de manière exponentielle (même les tickets ouverts et les PR en attente).

Vignesh Hari a souligné que nous commencions à recevoir des choses sérieuses dans notre section de demandes :

> ഞാനും എന്റെ കൈകുഞ്ഞും അച്ഛനും അമ്മയും അമ്മാവനും അമ്മായിയും ഞങ്ങളുടെ വീട്ടിൽ അകപ്പെട്ടിരിക്കുന്നു.വീടിന്റെ താഴത്തെ നിലയിൽ മുഴുവനും വെള്ളം കയറി…റോഡ് മാർഗ്ഗം രക്ഷപ്പെടാൻ പറ്റുന്നില്ല .പമ്പയാറിന് സമീപമാണ് വീട്. ജലനിരപ്പ് അപകടമാംവിധം ഉയരുന്നു.ദയവു ചെയ്ത് ആരെങ്കിലും ഞങ്ങളെ രക്ഷിക്കണം..

```
Traduction : Moi, mon nouveau-né, mon père et ma mère, mon oncle et ma tante sommes piégés dans notre maison. Le rez-de-chaussée est inondé... nous ne pouvons pas non plus nous échapper par la route... Notre maison est près de la rivière Pamba. Le niveau de l'eau monte dangereusement. S'il vous plaît, que quelqu'un nous aide...
```

C'était l'une de ces demandes. Ce fut le moment où j'ai commencé à lutter contre mon corps et mon esprit, pour faire de mon mieux. La pensée que des gens dépendaient de ce que je codais m'a frappé si fort qu'elle m'a poussé à faire des choses que je n'aurais jamais faites autrement.

Certains d'entre nous ont travaillé 21 heures par jour pendant 3 jours consécutifs. Je me couchais à 3 heures du matin et me réveillais à 6 heures sans réveil. C'était comme si mon rythme circadien était devenu conscient et avait pris le contrôle de la situation. Des efforts aussi extraordinaires ont été fournis par une poignée de bénévoles, à ma connaissance, et ils sont restés invisibles pour le reste de la communauté. Il a fallu 10 à 12 jours de travail ininterrompu. Après cela, les choses ont commencé à se calmer un peu.

La communauté a également travaillé sans relâche pendant ces jours. Il y avait toujours quelqu'un d'un coin de la Terre pour surveiller notre tableau de bord Heroku, qui me réveillait si quelque chose de grave était sur le point d'arriver.

Notre application a incroyablement bien fonctionné pendant les jours de pointe de la crise, 24h/24 et 7j/7. Nous avons été très prudents dans notre développement et notre revue de code — mais j'admets avoir effectué quelques fusions de PR stupides sans revue de code appropriée au début.

![Image](https://cdn-media-1.freecodecamp.org/images/axXrpYUdRwu5uki497TflxJku6VKnjZs6sBx)

Pour un étranger, notre groupe Slack pouvait sembler être un désordre — différents canaux discutant de divers « charabia ». Un travail productif y était-il accompli ? Oui ! La meilleure chose à propos de la communauté était la beauté dans le chaos. Je ne pouvais pas gérer Slack seul, avec la charge de travail que j'avais. Pourtant, la communauté a trouvé son chemin. Comme une structure faite par une armée de fourmis, ils ont réalisé des choses incroyables. DevOps, DataViz, analytique, toutes sortes de choses s'y passaient.

Les gens m'ont demandé : comment KeralaRescue est-elle devenue l'application n°1, alors qu'il y avait de nombreux sites web avec des fonctionnalités similaires ? C'est principalement dû au soutien officiel du gouvernement. Nous l'avons obtenu uniquement parce que nous avons commencé très tôt, quand personne d'autre n'avait commencé à travailler sur un tel site. Une autre raison était qu'il a été lancé très rapidement. Enfin, tout reposait sur la communauté. C'est la communauté qui a fait des merveilles — une communauté bâtie sur la force de l'âme humaine et sa compassion pour aider ses semblables.

Le choix de le rendre open-source a été une autre décision dont je suis très fier. Le site était open-source dès le jour 0.

J'avais lu des articles sur la puissance de l'open source et comment il avait révolutionné de nombreux événements similaires, mais pour être honnête, je n'y ai même pas trop réfléchi. J'ai juste poussé sur Git ! Parce que l'open-source est l'option par défaut configurée dans mon cerveau, comme pour beaucoup d'autres étudiants du Kerala. C'est peut-être dû à notre familiarité avec des outils comme Ubuntu depuis l'école. Merci au département de l'éducation d'avoir rendu cela possible, alors que de nombreux autres États de l'Inde dépendent encore de logiciels propriétaires.

Parallèlement aux bienfaits de l'open-source, nous avons vu les merveilles que l'open data peut accomplir. Nos données ont été utilisées par des bénévoles du monde entier, pour des IVR, de la visualisation et bien d'autres choses. L'impact de l'open data était visible ici. Une chose que j'aimerais pouvoir changer rétrospectivement serait l'implémentation d'API appropriées. Des initiatives comme [https://data.gov.in/](https://data.gov.in/) ont un grand potentiel.

### La technologie

Comme je l'ai mentionné, la base de données a été déplacée vers AWS, simplement parce que nous y avions des crédits gratuits. Plus tard, l'un des ingénieurs DevOps principaux a souligné que la colocalisation de la base de données avec l'application présentait des avantages. Nous sommes donc revenus plus tard sur Heroku (et ils ont fini par nous donner des crédits gratuits !).

L'une des principales choses que j'avais à l'esprit était : ne pas bloquer le cycle requête-réponse. Nous avons rencontré des problèmes tels que des appels d'API lents (pour l'envoi de SMS) qui bloquaient le cycle. Ces appels ont été identifiés lors de la revue de code. Nous avons ajouté une Redis Queue et cela a beaucoup aidé pour la suite. Toutes les importations CSV ont été effectuées via la Redis Queue. C'était satisfaisant de voir RQ traiter les données, pendant que nos dynos d'application s'occupaient des requêtes.

Nous avions un point de terminaison appelé /data qui avait été créé pour alimenter la carte de secours. La carte a été supprimée par la suite. Mais /data est resté un certain temps. Lorsque les données de requête ont augmenté (pour atteindre finalement 51 000), cela a commencé à ralentir le serveur. Nous avons essayé de les paginer, puis nous les avons supprimées. /data a fait du bon travail au moment de la crise. Rendre les données facilement disponibles a facilité la tâche de divers groupes comme keralafights, saakhi et les centres d'appels alimentés par myoperator qui ont priorisé les demandes et les ont canalisées vers diverses autorités via IT Mission.

La communauté a mené plusieurs efforts parallèles comme Ushahidi et Sahana. L'importation de données d'Ushahidi était douloureusement lente. Les données existantes devaient être portées vers Ushahidi pour que nous puissions les utiliser. L'un des développeurs a fini par soumettre un correctif en amont (upstream patch) accélérant le processus de 40 % ! Mais, nous avons fini par n'utiliser ni l'un ni l'autre.

### Leçons pour l'avenir

Le réchauffement climatique et la destruction de nos montagnes, rivières et vallées se retourneront contre nous dans un avenir proche. Malheureusement, ce n'est peut-être pas la seule catastrophe naturelle que les Malayalis connaîtront au cours de leur vie.

> Ceux qui ne lisent pas l'histoire sont condamnés à la répéter  
> — George Santayana

Le développement durable doit être mis en œuvre, et ne pas rester seulement dans les manuels scolaires. Je crois que c'est la **SEULE** forme de développement que le Kerala peut avoir, en raison de notre géographie.

Idéalement, notre gestion des catastrophes devrait utiliser la puissance de la technologie moderne. Une solution technologique prête à être déployée devrait toujours être disponible. Des efforts devraient être faits par le gouvernement, en utilisant la force bénévole existante pour transformer KeralaRescue en une solution de référence pour les logiciels de gestion des catastrophes.

La communauté des étudiants et des bénévoles est un potentiel inexploité du Kerala. Une crise comme celle-ci peut mobiliser des techniciens du monde entier. Nous avons même eu des contributions de Croatie. Ces gardiens silencieux seront là à l'avenir, attendant d'être appelés.

Notre gestion des catastrophes devrait disposer d'une équipe techniquement capable, capable de gérer des flux de travail agiles. Une équipe de gestion centrale joue un rôle important ici. Elle doit être capable de fournir aux bénévoles une vision et une direction.

Des normes telles que [SPHERE](http://www.sphereproject.org) devraient être appliquées. Le suivi des fournitures, l'évaluation des dommages et l'utilisation des fonds devraient être disponibles en ligne, en tant qu'informations publiques. Les registres publics sont parfaits pour assurer la transparence. Les audits publics devraient être la source de vérité. Les commentaires de la population devraient être intégrés au logiciel.

#### Conclusion

Merci à Cloudflare, Slack, Heroku, AWS et Workast qui nous ont aidés en offrant leur technologie gratuitement ! Et à toutes les personnes formidables sur Twitter, Reddit et partout ailleurs, qui ont diffusé notre message.

![Image](https://cdn-media-1.freecodecamp.org/images/AqneCnDMppT-jLHN8eRLBdncwswVLfLvM-0N)

Aucun des contributeurs n'est mentionné ici. C'était une décision consciente. Un fichier [humans.txt](http://humanstxt.org/) est le meilleur outil pour cela car je pourrais inévitablement oublier quelqu'un.

Cet effort a été rendu possible par la philosophie FOSS, avec laquelle le Kerala est en effet familier. Je souhaite voir plus d'initiatives FOSS, dès le niveau scolaire. En fait, mon premier contact avec le FOSS a été Edubuntu utilisé dans toutes les écoles du Kerala ainsi que l'IT Festival organisé par le gouvernement pour les étudiants.

![Image](https://cdn-media-1.freecodecamp.org/images/kvOaCn6Rkxg73io5sOqmFhvecbvwjIq-xHGv)

Enfin, j'aimerais remercier chaque âme humaine qui a aidé KeralaRescue et, par extension, le peuple du Kerala. Ce fut un privilège de travailler avec une équipe internationale d'ingénieurs logiciels et de contributeurs.

Contactez-moi sur [https://biswaz.github.io](https://biswaz.github.io)