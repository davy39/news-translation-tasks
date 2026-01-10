---
title: Erreur HTTP 503 Service Indisponible Expliquée – Que signifie le code d'erreur
  503
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-10-02T02:36:00.000Z'
originalURL: https://freecodecamp.org/news/http-error-503-service-unavailable-explained-what-the-503-error-code-means
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c986c740569d1a4ca19fd.jpg
tags:
- name: error
  slug: error
- name: servers
  slug: servers
- name: web
  slug: web
seo_title: Erreur HTTP 503 Service Indisponible Expliquée – Que signifie le code d'erreur
  503
seo_desc: 'Errors happen – there''s some unexpected maintenance, a bug that went unnoticed,
  or a page goes viral and the flood of connections take the server down.

  If you''ve been online for any amount of time, no doubt you''ve seen the somewhat
  vague 503 Service ...'
---

Les erreurs arrivent – il y a une maintenance inattendue, un bug qui est passé inaperçu, ou une page devient virale et le flot de connexions fait tomber le serveur.

Si vous avez été en ligne ne serait-ce qu'un certain temps, vous avez sans doute vu l'erreur quelque peu vague 503 Service Indisponible.

Dans cet article, nous allons passer en revue les codes d'état HTTP, ce que signifie l'erreur 503, et quelques moyens possibles de la résoudre – à la fois pour un site que vous essayez de visiter et pour votre propre site.

## Aperçu des codes d'état HTTP

Les serveurs qui hébergent des pages web écoutent les requêtes des navigateurs web ou des appareils, également connus sous le nom de clients. Le serveur utilise ensuite une série de codes d'état différents pour communiquer en retour.

Ces codes d'état sont organisés en différentes classes, indiquées par le premier chiffre du code d'état :

* 1xx : Information – le serveur traite toujours la requête
* 2xx : Succès – la requête a réussi et le serveur répond avec la page ou la ressource
* 3xx : Redirection – la page ou la ressource a été déplacée et le serveur répondra avec son nouvel emplacement
* 4xx : Erreur client – il y a une erreur dans la requête du navigateur ou de l'appareil
* 5xx : Erreur serveur – il y a une erreur avec le serveur

Les deux derniers chiffres de chaque code d'état HTTP représentent un état plus spécifique pour chaque classe. Par exemple, 301 signifie qu'une page ou une ressource a été déplacée de manière permanente, tandis que 302 signifie que le déplacement est temporaire.

Consultez cette page pour une liste des codes d'état HTTP courants et leur signification : [https://en.wikipedia.org/wiki/List_of_HTTP_status_codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

La plupart des codes d'état passent totalement inaperçus, ce qui est bien car cela signifie que tout fonctionne. Ce n'est que lorsque vous obtenez des codes d'état dans la plage 4xx-5xx que vous pourriez remarquer un code d'état car vous verrez une page comme celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/E20Ry-1.png)
_Une page d'erreur 503 typique – Source : [Stack Overflow](https://stackoverflow.com/questions/27944151/asp-net-website-shows-503-service-unavailable-after-successful-publishing)_

Maintenant que vous avez une compréhension de base des codes d'état HTTP, creusons un peu plus l'erreur 503 Service Indisponible.

## Que signifie le code d'erreur 503 ?

Comme mentionné ci-dessus, les codes d'état 5xx signifient qu'il y a un problème avec le serveur lui-même.

Une erreur 503 Service Indisponible signifie que la page ou la ressource est indisponible. Il y a de nombreuses raisons pour lesquelles un serveur pourrait retourner une erreur 503, mais certaines raisons courantes sont la maintenance, un bug dans le code du serveur, ou un pic soudain de trafic qui fait que le serveur devient surchargé.

Le message envoyé avec l'erreur 503 peut varier en fonction du serveur d'où il provient, mais voici quelques-uns des messages courants que vous verrez :

> - 503 Service Indisponible  
> - 503 Service Temporairement Indisponible  
> - Erreur de Serveur HTTP 503  
> - Erreur HTTP 503  
> - Erreur 503 Service Indisponible  
> - Le serveur est temporairement incapable de traiter votre requête en raison d'une maintenance ou de problèmes de capacité. Veuillez réessayer plus tard.  
>   
> [Source](https://kinsta.com/blog/http-error-503/)

Quelle que soit la raison de l'erreur 503, elle est généralement temporaire – le serveur redémarrera, le trafic diminuera et le problème se résoudra de lui-même.

## Comment résoudre l'erreur 503 Service Indisponible

Lorsqu'on essaie de résoudre une erreur 503, il y a deux cas généraux.

Le premier est celui où vous êtes un utilisateur final et vous essayez de visiter un site que vous ne possédez pas. Dans le second cas, vous possédez le site et il renvoie des erreurs 503 aux personnes qui essaient de le visiter.

La méthode pour résoudre les erreurs 503 est différente selon le groupe auquel vous appartenez. Examinons quelques choses que vous pouvez faire en tant qu'utilisateur final si vous voyez une erreur 503.

### Comment résoudre une erreur 503 Service Indisponible en tant qu'utilisateur final

Puisque les codes d'état 5xx signifient que l'erreur est du côté serveur, il n'y a pas grand-chose que vous puissiez faire directement.

Même si les erreurs 503 sont généralement temporaires, il y a quelques choses que vous pouvez faire en attendant.

**#1 : Actualiser la page**

Parfois l'erreur est si temporaire qu'un simple rafraîchissement suffit. Avec la page ouverte, appuyez simplement sur Ctrl - R sous Windows et Linux, ou Cmd - R sous macOS pour actualiser la page.

**#2 : Voir si la page est inaccessible pour d'autres personnes**

La prochaine chose que vous pouvez faire est d'utiliser un service comme [Is It Down Right Now?](https://www.isitdownrightnow.com/) ou [Down For Everyone Or Just Me](https://downforeveryoneorjustme.com/) pour voir si d'autres personnes obtiennent la même erreur.

Rendez-vous simplement sur l'un de ces sites et entrez l'URL de la page que vous essayez de visiter.

Le service enverra une requête à l'URL que vous avez entrée pour voir s'il obtient une réponse. Ensuite, il vous montrera quelques statistiques et graphiques intéressants sur la page :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-44.png)
_Vérification de [freeCodeCamp](https://www.freecodecamp.org/) sur Is It Down Right Now?_

Si vous faites défiler un peu vers le bas, vous verrez quelques commentaires d'autres personnes. Souvent, les gens donnent leur localisation générale et d'autres données, donc cela peut être un bon moyen de déterminer si l'erreur n'affecte que certaines régions ou certains appareils.

**#3 : Redémarrer votre routeur**

Parfois le problème est lié à une défaillance du serveur DNS.

DNS signifie Domain Name System, et ils agissent essentiellement comme des traducteurs entre les adresses IP et les URL lisibles par les humains.

Par exemple, vous pouvez visiter Google en entrant directement son longue adresse IP (172.217.25.206), ou vous pouvez simplement entrer l'URL, www.google.com.

C'est un DNS, souvent hébergé sur un serveur, qui gère tout cela en arrière-plan.

Tout cela pour dire que de nombreux routeurs mettent en cache les réponses des serveurs DNS (www.google.com <==> 172.217.25.206). Mais parfois ce cache peut être corrompu et causer des erreurs.

Un moyen facile de réinitialiser ou de "vider" le cache est de redémarrer votre routeur. Il suffit de débrancher votre routeur pendant environ 5 secondes, puis de le rebrancher.

Il devrait redémarrer après une minute et tous vos appareils devraient se reconnecter automatiquement. Une fois qu'ils l'ont fait, essayez de visiter le site à nouveau.

### Comment résoudre une erreur 503 Service Indisponible en tant que propriétaire du site

Si vous êtes le propriétaire/développeur du site qui renvoie des erreurs 503, il y a un peu plus que vous pouvez faire pour diagnostiquer et résoudre le problème.

Voici quelques conseils généraux pour vous aider à démarrer :

**#1 : Redémarrer le serveur**

Le développement est difficile – même une simple page statique peut avoir tant de parties mobiles qu'il peut être difficile de déterminer ce qui cause l'erreur 503.

Parfois, la meilleure chose à faire est de redémarrer le serveur et de voir si cela résout le problème.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/1rs7t0-1.jpg)
_Source : [imgflip](https://imgflip.com/i/1rs7t0)_

La méthode exacte pour redémarrer votre serveur peut varier, mais généralement vous pouvez y accéder depuis le tableau de bord de votre fournisseur ou en vous connectant via SSH au serveur et en exécutant une commande de redémarrage.

Le serveur devrait redémarrer après quelques minutes. Si vous avez configuré tout pour qu'il s'exécute automatiquement au démarrage, vous pouvez visiter votre site et voir s'il fonctionne.

**#2 : Vérifier les journaux du serveur**

La prochaine chose à faire est de vérifier les journaux.

L'emplacement des journaux du serveur peut varier en fonction du service que vous exécutez, mais ils se trouvent souvent dans `/var/log/...`.

Jetez un coup d'œil dans ce répertoire et voyez si vous pouvez trouver quelque chose. Si ce n'est pas le cas, consultez le manuel de vos programmes en exécutant `man nom_du_programme`.

**#3 : Vérifier s'il y a une maintenance automatisée en cours**

Certains fournisseurs de services offrent des mises à jour de packages et une maintenance automatisées. Normalement, c'est une bonne chose – elles se produisent généralement pendant les temps d'arrêt et aident à s'assurer que tout est à jour.

Occasionnellement, les erreurs 503 sont dues à ces sessions de maintenance planifiées.

Par exemple, certains fournisseurs d'hébergement spécialisés dans l'hébergement WordPress mettent automatiquement à jour WP dès qu'il y a une nouvelle version. WordPress renvoie automatiquement une erreur 503 Service Indisponible chaque fois qu'il est mis à jour.

Vérifiez auprès de vos fournisseurs de services si l'erreur 503 est causée par une maintenance planifiée.

**#4 : Vérifier les paramètres du pare-feu de votre serveur**

Parfois, les erreurs 503 Service Indisponible sont causées par un pare-feu mal configuré où les connexions peuvent entrer, mais échouent à ressortir vers le client.

Votre pare-feu peut également nécessiter des paramètres spéciaux pour un CDN, où plusieurs connexions provenant d'une poignée d'adresses IP peuvent être interprétées à tort comme une attaque DDoS.

La méthode exacte pour ajuster les paramètres de votre pare-feu dépend de nombreux facteurs. Jetez un coup d'œil à votre pipeline et aux tableaux de bord de votre fournisseur de services pour voir où vous pouvez configurer le pare-feu.

**#5 : Vérifier le code**

Les bugs, comme les erreurs, arrivent. Essayez autant que vous le pouvez, il est impossible de tous les attraper. Occasionnellement, l'un d'eux peut passer à travers et causer une erreur 503.

Si vous avez tout essayé et que votre site affiche toujours une erreur 503 Service Indisponible, la cause peut être quelque part dans le code.

Vérifiez tout code côté serveur, et portez une attention particulière à tout ce qui concerne les expressions régulières – [un petit bug regex](https://www.freecodecamp.org/news/freecodecamp-servers-update-october-2019/) est ce qui a causé un pic énorme dans l'utilisation du CPU, des pannes en cascade, et environ trois jours de panique pour nous chez freeCodeCamp.

Espérons que vous pourrez retrouver le coupable, déployer une correction, et tout sera de retour à la normale.

## En résumé

Cela devrait être tout ce que vous devez savoir sur les erreurs 503 Service Indisponible. Bien qu'il n'y ait généralement pas grand-chose que vous puissiez faire lorsque vous voyez une erreur 503, espérons que certaines de ces étapes vous aideront la prochaine fois que vous en rencontrerez une.

Restez en sécurité, et bon rafraîchissement-jusqu'à-ce-que-ça-marche 😊