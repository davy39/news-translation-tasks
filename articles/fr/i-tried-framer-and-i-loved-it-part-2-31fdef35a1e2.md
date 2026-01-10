---
title: Pour des prototypes FramerJS plus réalistes, ajoutez simplement des données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-17T02:01:09.000Z'
originalURL: https://freecodecamp.org/news/i-tried-framer-and-i-loved-it-part-2-31fdef35a1e2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uTJpHuWyI1Ly0QxpN31zng.jpeg
tags:
- name: Design
  slug: design
- name: prototyping
  slug: prototyping
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Pour des prototypes FramerJS plus réalistes, ajoutez simplement des données
seo_desc: 'By Marty Laurita


  “Data! Data! Data! I can’t make bricks without clay!” — Sir Arthur Conan Doyle


  Most interaction prototypes today serve one purpose: to convince your user that
  this prototype is what the “real thing” will look like and feel like.

  In...'
---

Par Marty Laurita

> _« Des données ! Des données ! Des données ! Je ne peux pas faire des briques sans argile ! »_  
>  _—_ Sir Arthur Conan Doyle

La plupart des prototypes d'interaction aujourd'hui servent un seul but : convaincre votre utilisateur que ce prototype est ce à quoi la « vraie chose » ressemblera et donnera l'impression.

Dans le passé, les designers ont atteint cet objectif avec des interfaces utilisateur sophistiquées, des animations et des transitions fluides.

Mais cela ne suffit plus tout à fait. Les utilisateurs sont devenus blasés face à ces astuces. Ils ont vécu l'ère de l'iPhone et s'attendent désormais à ce qu'une interface fluide soit standard.

Alors, quelle est la prochaine frontière ? Comment pouvons-nous convaincre les gens qu'un prototype est « réel » ?

En utilisant des données réelles.

![Image](https://cdn-media-1.freecodecamp.org/images/RBuldGdjUUlgWe4ddyHiOf7CDgkUOkiSfJYx)
_Temps de descendre dans le terrier…_

[FramerJS](http://framerjs.com/) est un framework puissant basé sur du code pour construire des prototypes pour vos applications web et mobiles. Dans cet article, je vais vous montrer comment l'utiliser pour construire un prototype réaliste qui intègre des données réelles.

![Image](https://cdn-media-1.freecodecamp.org/images/LhK7VTU-bltvg4IbuXyskjszjf0G360oaaaL)
_Interface de Framer, Framerjs.com_

En tant qu'usager de l'Autorité des transports de la baie du Massachusetts (MBTA), j'ai le plaisir distinct de voyager dans un système de transport qui a plus de 100 ans.

Comme vous pouvez l'imaginer, les trains ne sont pas toujours à l'heure.

Je suis devenu relativement familier avec Framer, et à ce titre, j'ai décidé d'essayer de concevoir une application pour résoudre ce problème.

En tant que designer qui n'a qu'une vague compréhension du code, cela était pour le moins intimidant.

J'ai appelé mon frère, un talentueux étudiant en informatique à Tufts, et nous nous sommes mis au travail.

![Image](https://cdn-media-1.freecodecamp.org/images/YSIqERsQ25SECvWvmzrsCTzSPrJG3pVQOtEB)
_[viens ici]_

### Localiser nos utilisateurs

La première chose à faire était de trouver la localisation de l'utilisateur en temps réel.

Les navigateurs mobiles d'aujourd'hui ont cette fonctionnalité intégrée.

Avec deux fonctions, vous pouvez obtenir la latitude et la longitude de votre utilisateur.

Ensuite, vous pouvez simplement coller ces coordonnées dans ce qu'on appelle une [table de hachage de paires clé-valeur](https://www.google.com/search?q=define+hash+table&oq=define+hash+table&aqs=chrome..69i57j69i60j69i65j69i61j69i60j69i61.2328j0j1&sourceid=chrome&ie=UTF-8). Dans cette table de données, la clé pourrait être « race_de_chien » et la valeur pourrait être « Pomeranian ». Maintenant, vous pouvez appeler cette clé chaque fois que vous en avez besoin, et elle retournera sa valeur correspondante.

Voici ce que nous avons obtenu :

```
#get locationgetLocation = () -> print "INSIDE GET LOC" navigator.geolocation.getCurrentPosition(showPosition);
```

```
showPosition = (position) -> print "INSIDE SHOW POS" gpsCoords = { "client_lat": "#{position.coords.latitude}", "client_lon": "#{position.coords.longitude}" }
```

Maintenant que nous avons la localisation exacte de l'utilisateur, il est temps pour la phase II.

### Localiser nos trains

![Image](https://cdn-media-1.freecodecamp.org/images/YAH7ojN31RC47pIjYoBTrsv3p--ghcZ6a8Ss)
_Où est ce train… Mr. Andersonnnnn ?_

Obtenir la localisation de l'utilisateur était la partie facile. Maintenant, nous devons trouver et analyser les données de l'API de la MBTA.

Malheureusement, cette organisation est aussi organisée que n'importe quelle autre opération gouvernementale sous-financée.

Donc, leur code était — comment devrais-je dire — un peu bancal. Voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/p8p21fIHRxZoFPNjyjz27AQKjy-HYdS0NJPH)
_Un peu un fouillis._

Les données étaient imbriquées dans une combinaison de tableaux et de paires clé-valeur. Certaines d'entre elles étaient des tables de données avec une seule entrée. Il a fallu un certain temps pour comprendre comment extraire les données dont nous avions besoin.

Quoi qu'il en soit, une fois que nous avons compris la structure, l'idée était de récupérer les données de localisation du navigateur de l'utilisateur et de les insérer dans l'appel de l'API à la MBTA. Ensuite, l'API de la MBTA retournerait toutes les données les plus proches de cette localisation.

La première partie des données que nous voulions était la station la plus proche de la localisation actuelle :

```
#grab MBTA station datadata = JSON.parse Utils.domLoadDataSync "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=De_WCTE-gkyYSitBw82YSw&lat=#{gpsCoords["client_lat"]}&lon=#{gpsCoords["client_lon"]}&format=json"  stops = data["stop"]  stationText.html = null  for i in stops  if i["parent_station_name"] != "" stationText.html = "The closest station to you is " + i["parent_station_name"] + "."
```

Une fois que nous avons eu les données, nous les avons analysées en quelque chose que les humains peuvent lire. Nous avons créé une chaîne (une phrase en anglais) qui disait « The closest station to you is » et ensuite nous avons ajouté le nom de la station à la fin. Et voilà ! La première étape !

![Image](https://cdn-media-1.freecodecamp.org/images/axJpiQsITNU8n7HhoNeGQB4y9jWeoomCU6WI)

Cela a fonctionné comme un charme !

Sauf pas dans Google Chrome.

Nous avons rapidement appris que pour une étrange raison, Google avait décidé de désactiver les API de localisation. Vraiment Google ? Vous n'avez pas assez de milliards pour donner quelques données de localisation au petit gars ?

Mais quoi qu'il en soit, le prototype fonctionne très bien dans Safari.

![Image](https://cdn-media-1.freecodecamp.org/images/UZ7MSBeDGnIISe9-xbd0Zennr9YhHEKRicvU)

Après avoir célébré notre succès initial, nous avons décidé de nous compliquer la vie à nouveau.

Et si nous voulions savoir non seulement la station la plus proche, mais aussi à quelle distance se trouvait le train le plus proche, d'où il venait et combien de minutes il restait ?

Oh là là.

![Image](https://cdn-media-1.freecodecamp.org/images/YEKj7SSCJTSMpITWBp12yrv1zLTc79pHXFuW)
_Ce moment « oh-oh »._

### Plus de données folles

Maintenant que nous avions une idée de la façon dont les données de la MBTA s'articulent, nous nous sommes plongés dans une deuxième API qui fournit des données de train (principalement) précises.

Après quelques manipulations, nous avions quelque chose comme ceci :

```
#grab nearest train data data2 = JSON.parse Utils.domLoadDataSync "http://realtime.mbta.com/developer/api/v2/predictionsbystop?api_key=De_WCTE-gkyYSitBw82YSw&stop=#{i["stop_id"]}&format=json" routes = data2[""] timeAway = data2["mode"][0]["route"][0]["direction"][0]["trip"][0]["pre_away"] trainDir = data2["mode"][0]["route"][0]["direction"][0]["direction_name"] trainLine = data2["mode"][0]["route"][0]["route_name"] timeAwayRound = Utils.round timeAway/60, 0 stationText2.html = "The next " + trainDir + " " + trainLine + " train is " + timeAwayRound + " mins away."
```

Cela récupère le « stop_id » (l'arrêt de métro le plus proche) de la première API, et l'insère dans la requête pour la deuxième API.

Ensuite, nous devons simplement parcourir les données pour extraire ce dont nous avons besoin.

« timeAway » nous donne la distance du train le plus proche, en secondes.

« trainDir » nous donne la direction dans laquelle le train se dirige.

Et « trainLine » nous indique sur quelle ligne de service se trouve le train.

Ensuite, nous avons créé une formule rapide pour convertir les secondes en minutes, et nous avons inséré toutes ces données dans une chaîne qui avait du sens.

Et voilà ! Un peu d'interface utilisateur rapide, quelques animations sophistiquées, et nous l'avions !

![Image](https://cdn-media-1.freecodecamp.org/images/aJoSvFXbdykSsyTK8UKL88MuzJ42ros0MVhg)
_Vous pouvez essayer le prototype vous-même ici : [http://share.framerjs.com/7ygqcpa64f67/](http://share.framerjs.com/7ygqcpa64f67/" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/36y4vd20skFFxWO1tomXfMF50MS3pwNpffCv)
_« Comme… Whoa… »_

### Conclusion

J'ai appris tellement de choses en construisant cela. Travailler avec des données réelles est si libérateur une fois que vous avez compris.

Je ne peux pas trop insister : si vous n'avez pas encore pratiqué la lecture de la documentation des API, cela peut être assez frustrant. Soyez patient. Cela peut prendre plusieurs heures pour comprendre et les faire fonctionner.

La syntaxe doit être parfaite. Et je veux dire _parfaite_.

Mais si vous y arrivez, vous serez là, à jouer avec et à regarder les nombres changer avec un sourire sur le visage.

Et vous aurez l'impression, tout à coup… que vous connaissez le kung fu.

![Image](https://cdn-media-1.freecodecamp.org/images/J6Ptdawe8FTEBoH0nsRDtuKfyhjudqYWUyfY)

Merci d'avoir lu. [Essayez le prototype](http://share.framerjs.com/7ygqcpa64f67/). J'adorerais avoir votre retour !

De plus, assurez-vous de consulter [mon premier article](https://blog.prototypr.io/designing-with-framer-part-1-faking-it-vs-making-it-ce74e1ca980) sur le prototypage avec FramerJS.

_Si vous avez aimé cela, cliquez sur le ? ci-dessous pour que d'autres personnes puissent le voir ici sur Medium._