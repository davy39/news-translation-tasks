---
title: 'Services RESTful Partie III : HATEOAS et le Modèle de Maturité de Richardson'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-27T06:58:55.000Z'
originalURL: https://freecodecamp.org/news/restful-services-part-iii-hateoas-and-the-richardson-maturity-model-48d4e4c79b8d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aIZeZdKxowEWVX-rNXsmGQ.jpeg
tags:
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Services RESTful Partie III : HATEOAS et le Modèle de Maturité de Richardson'
seo_desc: 'By Sanchit Gera

  In Part I of this series, you learned the very basics of HTTP. We went over common
  HTTP constructs such as headers, URLs and the different status codes available.
  We also looked at how each of these constructs could be useful when bui...'
---

Par Sanchit Gera

Dans la [Partie I](https://medium.freecodecamp.com/restful-services-part-i-http-in-a-nutshell-aab3bfedd131#.kd3ovzqtg) de cette série, vous avez appris les bases de HTTP. Nous avons passé en revue les constructions HTTP courantes telles que les en-têtes, les URLs et les différents codes de statut disponibles. Nous avons également examiné comment chacune de ces constructions pouvait être utile lors de la création de services web orientés ressources.

Dans la [Partie II](https://medium.freecodecamp.com/restful-services-part-ii-constraints-and-goals-530b8f6298b9#.5g54mnfzl), vous avez appris les différentes contraintes auxquelles vous devez vous conformer afin de construire des systèmes RESTful scalables et haute performance.

Cet article vous fournira la troisième et dernière pièce du puzzle. Comme mentionné précédemment, REST n'est pas une norme, mais plutôt un concept abstrait. Cela rend difficile la quantification exacte de la mesure dans laquelle un service est ou n'est pas "RESTful".

Bien que les contraintes discutées dans la partie précédente soient utiles lors de la création d'un service, elles ne sont pas aussi efficaces pour résoudre ce problème. Et si vous choisissiez de suivre exactement une de ces contraintes ? Deux ? Trois ? À quel moment votre service cesse-t-il d'être _partiellement_ RESTful et bascule-t-il dans le monde magique de la _complète_ conformité RESTful ?

C'est exactement le problème que le Modèle de Maturité de Richardson (RMM) vous aide à résoudre. Mais avant de plonger plus profondément dans les détails du RMM, il y a un dernier sujet qui s'avérera utile pour votre compréhension de REST.

### Le Principe de HATEOAS

**H**ypermedia **A**s **T**he **E**ngine **O**f **A**pplication **S**tate, abrégé en HATEOAS, s'appuie sur l'une des contraintes de REST (l'_Interface Uniforme_). Je cherche encore à déterminer comment le prononcer. J'alterne généralement entre Hate-ee-ose et Hate-ose. N'hésitez pas à choisir l'un ou l'autre, ou à inventer le vôtre. Mais bon, je m'égare.

L'objectif global derrière HATEOAS est de fournir un moyen cohérent pour que les machines comprennent les API et les naviguent sans avoir aucune information à leur sujet au préalable, de la même manière qu'un utilisateur visitant un site web pour la première fois.

Imaginez que vous visitiez Medium pour la première fois afin d'écrire un article. Quelles étapes suivriez-vous ? Très probablement, vous visiteriez la page d'accueil de Medium, iriez dans la section _Stories_, et commenceriez à écrire votre chef-d'œuvre. Vous ne vous souciez pas vraiment de l'URL sur laquelle vit la section _Stories_. Vous ne l'avez pas mémorisée, mais vous savez que vous pourrez y accéder lorsque vous en aurez besoin.

Ou imaginez que vous commandez quelque chose sur Amazon. Vous entrez, recherchez différents articles, les ajoutez au panier et passez à la caisse. L'emplacement de chacun de ces composants dans le système vous est indifférent en tant qu'utilisateur. Si l'URL requise pour accéder au panier était nécessaire, il y a de fortes chances que vous ne la trouviez même pas. Et pourtant, votre expérience reste sans entrave.

Dans les deux cas, vous n'avez besoin que d'une seule information, à savoir le point d'entrée du site web. Tout le reste à partir de ce point est complètement découvrable et utilisable en naviguant sur les liens pertinents (aka _hypermedia_). C'est ainsi que le web est conçu pour fonctionner et en effet comment la plupart des utilisateurs l'expérimentent aujourd'hui.

HATEOAS étend cette idée de découvrabilité aux API et aux services web également. Et si, étant donné un seul point d'accès au service, je pouvais utiliser tout ce qu'il a à offrir ? Heureusement, cela peut être réalisé en exploitant la nature orientée ressources de nos données sur lesquelles nous avons travaillé si dur !

Nous savons que puisque tout ce qui est retourné par notre service est essentiellement une ressource, il n'y a qu'une poignée de choses que le consommateur de notre service peut faire _avec_ cette ressource. De plus, chaque action correspond à une route RESTful bien définie dans notre système (pensez GET, POST, PUT, etc.). Cela signifie que nous pourrions facilement intégrer toutes les interactions potentielles avec une ressource donnée sous la forme d'URLs actionnables dans la réponse. Voyons un exemple !

Revenons à notre exemple précédent d'écriture d'une histoire sur Medium. Imaginez que, au lieu d'un site web destiné aux utilisateurs, il s'agissait plutôt d'un simple service web. Selon le modèle HATEOAS, la seule information dont j'aurais besoin pour naviguer dans le service serait le nom d'hôte : **medium.com**

Je commence mon interaction en faisant une requête GET à l'hôte. Medium répond rapidement avec une liste de toutes les ressources qu'il propose, ainsi que l'endroit où je peux les trouver.

```
GET medium.com
```

```
links : [  {    rel : "bookmarks",    href : "/bookmarks"  },   {    rel : "stories",     href: "/stories"  }]
```

Dans cette version simplifiée de Medium, on m'indique qu'il y a deux ressources proposées : _stories_ et _bookmarks_. On m'indique également où chacune de ces ressources se trouve sur le système.

Ensuite, je dois déterminer comment créer une nouvelle histoire. D'après nos discussions précédentes, je sais déjà que cela va être une requête POST, mais en tant que client, je ne sais toujours pas quel type de données le service attend pour cette requête. C'est exactement là qu'une requête OPTIONS s'avère utile. Alors faisons cela !

```
OPTIONS medium.com/stories
```

```
Allow GET, POST{  name : "Stories",  description: "Ideas and opinions from around the world",   actions: [    {      POST: {        title: "string",        body: "string"      }    }  ]}
```

Ah ! Il semble que nous ayons besoin de paramètres nommés _title_ et _body_ correspondant à notre nouvelle publication. Cela nous donne toutes les informations dont nous avons besoin. Nous pouvons maintenant commencer à POSTer vers le service et créer de nouveaux articles sur le service.

Maintenant, supposons qu'en suivant cette approche, j'atterris sur une histoire existante. À quoi ressemblerait une histoire individuelle ?

```
GET medium.com/stories/3
```

```
{  "id": 3,  "title": "An Introduction to Microservices",  "body": "...",  "created_at": "2016-10-25T20:52:12.804Z",  "links": [  {    "rel": "self",    "href": "/stories/1"  },   {    "rel": "author",    "href": "/authors/3"  },   {    "rel": "comments",    "href": "/stories/3/comments"  }],}
```

Maintenant, je n'ai pas seulement des informations sur l'histoire, mais j'ai aussi un moyen d'obtenir des informations sur l'auteur et les commentaires.

Bien sûr, cela est trop simpliste. Il y a des tonnes d'autres choses qui se passent, comme l'authentification et l'autorisation, qui doivent être prises en charge. Et beaucoup de travail doit être fait pour concevoir des systèmes qui peuvent être décomposés en ressources aussi facilement. Mais cela sert bien à comprendre l'idée derrière HATEOAS.

Cela élimine le besoin pour vous, en tant que développeur, de maintenir une documentation pour votre service. Tout ce qu'un client pourrait avoir besoin de savoir sur l'utilisation de votre service est déjà inclus.

De même, en tant que client, je n'ai pas besoin de garder une trace des URLs associées à chacune de ces ressources. Je cherche l'objet correspondant à la ressource et j'y navigue. Si cela change, je m'en fiche.

Avec cela à l'esprit, concentrons-nous maintenant sur le Modèle de Maturité de Richardson (RMM).

### Le Modèle de Maturité de Richardson

Comme mentionné précédemment, le RMM est un outil pour vous aider à évaluer à quel point un service est RESTful. Ce système de classification — décrit pour la première fois par Leonard Richardson — fournit une manière ordonnée de penser à vos services web du point de vue d'un utilisateur final, puis de faire des jugements en conséquence.

Richardson décrit quatre niveaux distincts dans le spectre de la conformité RESTful.

#### Niveau 0

C'est le niveau le plus bas lorsqu'il s'agit d'un service étant RESTful. Les services de cette catégorie suivent le principe "une URL, une méthode". Cela signifie que le service n'expose qu'une seule URL au monde extérieur et n'accepte qu'un seul type de requête (généralement POST) à cet endroit.

C'est typique pour les services SOAP, par exemple. Une requête typique à un service SOAP ressemble à ceci :

```
POST /Quotation HTTP/1.0Host: www.xyz.orgContent-Type: text/xml; charset=utf-8Content-Length: nnn<?xml version="1.0"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2001/12/soap-envelope" SOAP-ENV:encodingStyle="http://www.w3.org/2001/12/soap-encoding" >   <SOAP-ENV:Body xmlns:m="http://www.xyz.org/quotations" >	      <m:GetQuotation>         <m:QuotationsName>MiscroSoft</m:QuotationsName>      </m:GetQuotation>		   </SOAP-ENV:Body>	</SOAP-ENV:Envelope>
```

Tout est décrit dans le corps de la requête, y compris l'action (getQuotation) et les paramètres pour cette requête (Microsoft). Clairement, le service n'utilise aucun des principes REST que nous avons discutés jusqu'à présent, sans mentionner le coût d'avoir un autre format de données supplémentaire au-dessus de HTTP.

#### Niveau 1 : Ressources

L'étape suivante sur notre chemin vers la conformité RESTful complète est l'introduction d'abstractions basées sur les ressources. Cela équivaut à diviser l'application en URLs spécifiques à des ressources distinctes. Richardson le caractérise comme l'implémentation "Plusieurs URLs, Une Méthode".

Ici, il y a plusieurs URLs différentes dans le système qui travaillent ensemble pour fournir la fonctionnalité souhaitée. Mais chacune n'accepte qu'un seul type de requêtes (encore une fois, généralement POST).

Par exemple, en continuant notre exemple précédent, nous pouvons procéder pour récupérer d'abord une liste de toutes les entreprises de notre application :

```
POST /companies[  {    "name" : "Microsoft",    "id" : 3  },   {    "name" : "Apple",    "id" : 4  }]
```

...et ensuite obtenir une citation pour une seule entreprise :

```
POST /quotations/3
```

```
{  quotation: {}}
```

C'est définitivement un pas en avant par rapport à avant. En fait, c'est ainsi que beaucoup d'applications avaient été écrites jusqu'à ce que REST gagne en popularité. Mais encore une fois, nous n'utilisons pas les forces de HTTP. Nous pouvons faire mieux !

#### Niveau 2 : Verbes

Maintenant, nous introduisons le concept de verbes d'action dans le mélange. En plus d'avoir des ressources bien définies, les actions qui peuvent être effectuées sur une ressource doivent strictement suivre les conventions HTTP.

Un GET NE DOIT PAS modifier l'état de la ressource, un POST NE DOIT être utilisé que pour la création de ressources, et ainsi de suite. Il est caractérisé comme, bien sûr, le système "Plusieurs URLs, Plusieurs Actions".

Cela nous amène aux services que la plupart d'entre nous connaissent et utilisent au quotidien. Ce sont également le type de services que nous considérons généralement comme RESTful. Cependant, il y a un niveau supplémentaire que les services doivent respecter pour atteindre le statut convoité de conformité RESTful complète.

#### Niveau 3 : HATEOAS

C'est là que la plupart des services échouent. La grande majorité des API et des services web que vous rencontrez en tant que développeur, ou probablement ceux sur lesquels vous travaillerez, ne suivent pas le principe de HATEOAS.

La plupart des fournisseurs de services préfèrent encore documenter leurs services de manière traditionnelle, en fournissant aux développeurs une liste des endpoints disponibles ainsi que des informations sur la manière d'interagir avec cet endpoint. Voici l'[API REST de Twitter](https://dev.twitter.com/rest/public), par exemple. (Intéressamment, l'API PayPal [pousse fortement](https://developer.paypal.com/docs/integration/direct/paypal-rest-payment-hateoas-links/) pour les Contrôles Hypermedia.)

Ce n'est pas nécessairement mauvais. Il y a de bons arguments à faire tant en faveur qu'en défaveur de l'utilisation de HATEOAS. Bien que d'une part cela rende les API faciles à découvrir et à utiliser, cela vient généralement au coût d'un temps et d'un effort de développement supplémentaires.

En fait, si tout ce que vous avez à faire est de faire un seul appel à l'API, l'introduction de HATEOAS peut en fait rendre les choses _plus_ difficiles pour vous en tant que consommateur.

### Conclusion

À la fin de la journée, ces mesures ne sont pas quelque chose dont vous devez jurer par. REST, avec toutes ses contraintes, n'est qu'un outil dans votre ceinture à outils lors de la construction de services web et d'applications. Il vous appartient entièrement de prendre ce qui correspond le mieux à vos besoins.

J'espère que vous avez appris beaucoup de concepts utiles dans cette série. Si vous cherchez à créer un service web RESTful pour compléter votre prochain projet, ou si vous cherchez à travailler avec un service existant, vous devriez maintenant avoir une bonne compréhension de certaines des rationalités derrière eux.

Voici les liens vers les parties précédentes, au cas où vous les auriez manquées :

[Services RESTful Partie I : HTTP en un clin d'œil](https://medium.freecodecamp.com/restful-services-part-i-http-in-a-nutshell-aab3bfedd131#.kd3ovzqtg)

[Services RESTful Partie II : Contraintes et Objectifs](https://medium.freecodecamp.com/restful-services-part-ii-constraints-and-goals-530b8f6298b9#.5g54mnfzl)

Faites-moi savoir ce que vous avez pensé de cet article dans les commentaires, ou contactez-moi via [LinkedIn](https://www.linkedin.com/in/sanchitgera).

**N'oubliez pas de cliquer sur le ? si vous avez aimé cet article.**

Santé et bon apprentissage !

**_Plus de Ressources_**

* [Blog de Martin Fowler](http://martinfowler.com/articles/richardsonMaturityModel.html)
* [Présentation de Leonard Richardson](https://www.crummy.com/writing/speaking/2008-QCon/act3.html)
* Exemple SOAP emprunté à [TutorialsPoint](https://www.tutorialspoint.com/soap/soap_examples.htm)