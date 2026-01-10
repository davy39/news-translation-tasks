---
title: 'Comment commencer à utiliser Curl et pourquoi : une introduction pratique'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-07T22:33:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-start-using-curl-and-why-a-hands-on-introduction-ea1c913caaaa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ikPF01FOkQQaDAH2IfA3LA.jpeg
tags:
- name: api
  slug: api
- name: Linux
  slug: linux
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Comment commencer à utiliser Curl et pourquoi : une introduction pratique'
seo_desc: 'By Luciano Strika

  Whether it’s testing the output of an API before deploying it to production, or
  simply fetching a response from a website (for instance, to check it’s not down),
  Curl is practically omnipresent.

  As a Data Scientist I’ve had to use i...'
---

Par Luciano Strika

Que ce soit pour tester la sortie d'une API avant de la déployer en production, ou simplement pour récupérer une réponse d'un site web (par exemple, pour vérifier qu'il n'est pas hors ligne), Curl est pratiquement omniprésent.

En tant que Data Scientist, j'ai dû l'utiliser de temps en temps. Cependant, plus souvent qu'autrement, je me suis retrouvé à simplement remplacer des paramètres d'une commande curl copiée et collée qui circule sur le canal Slack de mon équipe.

J'ai décidé que je devais mieux comprendre cet outil puissant si je voulais l'utiliser à son plein potentiel, et maintenant je suis ici pour partager certaines des choses les plus intéressantes que j'ai trouvées dans ce tutoriel curl.

Si vous avez des conseils ou des astuces que vous aimeriez ajouter, n'hésitez pas à le faire dans les commentaires, car ma compréhension de cet outil en est encore à ses débuts.

### Curl : À quoi ça sert ?

Curl est un outil en ligne de commande qui nous permet de faire des requêtes HTTP depuis le shell. Il couvre également de nombreux autres protocoles, comme FTP, bien qu'ils dépassent le cadre de ce tutoriel.

Son nom [signifie « Client URL »](https://en.wikipedia.org/wiki/CURL), et il a été développé par le développeur suédois Daniel Stenberg. C'est un projet open source, et son code peut être trouvé [ici](https://github.com/curl/curl), au cas où vous auriez envie de contribuer.

Vous pouvez l'invoquer depuis votre terminal préféré, et il est généralement préinstallé dans les systèmes d'exploitation basés sur Linux. Sinon, il peut normalement être téléchargé via _apt-get_ sur Linux, et _brew_ sur Mac.

### Appeler une méthode GET

Dans sa forme la plus basique, une commande curl ressemblera à ceci :

```
curl http://www.dataden.tech
```

Le comportement par défaut de curl est d'invoquer une méthode HTTP GET sur l'URL donnée. Ainsi, la sortie du programme pour cette commande sera le corps entier de la réponse HTTP (dans ce cas, HTML) que le site retourne sur un GET, qui sera écrit tel quel sur _stdout_.

Si vous souhaitez lire une réponse sans quitter le shell, je vous recommande au moins de la rediriger vers une commande _less_, pour pouvoir faire défiler facilement la sortie.

De nombreuses fois, nous souhaiterons diriger le contenu de la réponse vers un fichier. Cela se fait avec l'argument _-o_, comme ceci :

```
curl -o output.html www.dataden.tech
```

ce qui est équivalent à :

```
curl www.dataden.tech > output.html
```

Facultativement, vous pouvez spécifier l'URL du site sur lequel vous souhaitez appeler curl avec un argument _-s_, comme ceci :

```
curl -s http://www.dataden.tech
```

ce qui vous permet de changer l'ordre de vos arguments.

Vous pouvez également utiliser _--next_ pour spécifier plusieurs URL, bien que la documentation officielle conseille d'appeler curl sur chaque URL dans une commande différente.

### Faire un POST vers une URL

Parfois, vous voudrez tester si une API fonctionne correctement, et cela nécessitera généralement l'envoi d'arguments.

Nous le ferons généralement via la méthode POST, en passant un JSON avec tous les paramètres requis. Il existe de nombreuses façons de faire cela avec curl.

Vous pouvez passer les valeurs de vos arguments comme ceci :

```
curl --data "name=John&surname=Doe" http://www.dataden.tech
```

Ou comme un JSON régulier :

```
curl --data '{"name":"John","surname":"Doe"}' \http://www.dataden.tech
```

Utiliser _--data_ est équivalent à utiliser _-d_, et les deux feront changer la méthode en POST automatiquement. Cependant, nous pouvons également utiliser le drapeau _-X_ (_--request_) pour spécifier quelle méthode nous voulons invoquer :

```
curl -X "POST" \-d "name=John&surname=Doe" http://www.example.com
```

### Récupérer les en-têtes du site

Parfois, nous voulons simplement voir rapidement si le site est toujours en ligne, sans vraiment vouloir charger la réponse complète, potentiellement lourde. D'autres fois, les en-têtes stockent des configurations importantes.

Ces deux cas d'utilisation sont également couverts par curl. Nous pouvons utiliser le paramètre _--include_ (_-i_) pour inclure les en-têtes, et _--head_ (_-I_ - c'est un 'i' majuscule -) pour inclure uniquement les en-têtes (en appelant la méthode HEAD).

### Définir votre valeur user-agent

Maintenant que j'ai couvert les bases, laissez-moi vous montrer certaines des choses les plus cool que j'ai trouvées que nous pouvons faire avec curl.

L'argument _user-agent_ vous permet de spécifier quels appareils et versions de navigateur vous utilisez, au cas où cela ferait rendre le site différemment. Avec cela, vous pourriez voir la version mobile d'un site depuis votre ordinateur portable, ou vice versa.

D'un point de vue sécurité, cela soulève probablement quelques problèmes. Je ne savais pas à quel point il était facile de prétendre utiliser un appareil différent (sans même utiliser une machine virtuelle) jusqu'à maintenant, et travaillant dans la prévention de la fraude, je peux voir pourquoi cela pourrait être un problème.

Cela dit, tant que vous utilisez cela pour de bonnes raisons, c'est une façon géniale de voir à quoi ressemble un site web depuis une tablette, un appareil mobile ou un ordinateur portable, pour n'en nommer que quelques-uns.

Voici un exemple, directement depuis la documentation officielle (bien que des listes de user-agents soient facilement disponibles en ligne).

```
curl --user-agent "Mozilla/4.73 [en] (X11; U; Linux 2.2.15 i686)" www.example.com
```

### Chronométrer une connexion avec Curl

Une autre raison pour laquelle j'ai commencé à en apprendre davantage sur curl était que je voulais voir combien de temps exactement il fallait pour que mon site web réponde.

Bien que la documentation de base ne le couvre pas, un peu de recherche sur Google a révélé cette commande, que j'ai trouvée très utile :

```
curl -w "%{time_total}\n" -o /dev/null -s www.example.com
```

Cela affichera simplement le temps total qu'il a fallu pour récupérer la réponse du domaine donné.

Plus généralement, l'argument _-w (--write-out)_ prend une chaîne de formatage spéciale, et remplit les mots-clés réservés avec différentes propriétés de la réponse, de manière formatée. Tous les mots-clés, et leurs valeurs respectives, sont disponibles dans la [page man de la commande](https://curl.haxx.se/docs/manpage.html).

### Lectures complémentaires

Voici quelques liens que vous pourriez trouver intéressants, au cas où vous souhaiteriez en apprendre davantage sur ce sujet vaste :

* [Liste des User-Agents](https://developers.whatismybrowser.com/useragents/explore/) Une compilation d'arguments user-agent pour différents appareils et navigateurs.
* La [documentation officielle](https://curl.haxx.se/docs/httpscripting.html) de Curl.
* La [page man](https://curl.haxx.se/docs/manpage.html) de Curl.

### Pour conclure

J'espère que vous avez trouvé cette introduction utile, et que vous quittez ce tutoriel en connaissant au moins les bases de cette commande pratique.

Comme je l'ai dit auparavant, j'apprends encore moi aussi, et j'apprécierai tout autre morceau intéressant de connaissance sur l'utilisation du programme. Il en va de même pour tout retour sur ce que j'ai écrit jusqu'à présent.

Si j'ai fait des erreurs, ou s'il y a une partie que vous pensez que j'aurais pu formuler plus clairement, n'hésitez pas à me le faire savoir.

J'espère vous revoir bientôt, bon codage !

_Suivez-moi sur [Medium](http://www.medium.com/@strikingloo) et [Twitter](http://www.twitter.com/strikingloo) pour rester à jour avec mes tutoriels, conseils et articles. Envisagez de partager cet article avec un ami développeur web si vous l'avez aimé (ou comme une manière passive-agressive de lui dire d'apprendre curl)._

_Originalement publié sur [www.dataden.tech](http://www.dataden.tech/programming/how-start-using-curl/) le 7 octobre 2018._