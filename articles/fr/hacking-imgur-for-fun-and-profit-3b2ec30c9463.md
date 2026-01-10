---
title: Pirater Imgur pour le plaisir et le profit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-29T12:03:06.000Z'
originalURL: https://freecodecamp.org/news/hacking-imgur-for-fun-and-profit-3b2ec30c9463
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kACKGoXyE6b-f0aelUSF4Q.jpeg
tags:
- name: bug bounty
  slug: bug-bounty
- name: imgur
  slug: imgur
- name: information security
  slug: information-security
- name: Security
  slug: security
- name: Web Development
  slug: web-development
seo_title: Pirater Imgur pour le plaisir et le profit
seo_desc: 'By Nathan

  So you think your memes are safe…


  Sorry not sorry.

  I’ve been meaning to write about this for a while. It all started back in July 2015
  when I decided to look for vulnerabilities in Imgur, an incredibly popular image
  sharing platform.

  The r...'
---

Par Nathan

Alors vous pensez que vos memes sont en sécurité…

![Image](https://cdn-media-1.freecodecamp.org/images/R2XhuRff6Qm04ONevEE3yQWiCljMUNY7irD-)
_Désolé, pas désolé._

J'avais l'intention d'écrire à ce sujet depuis un moment. Tout a commencé en juillet 2015 lorsque j'ai décidé de chercher des vulnérabilités sur [Imgur](http://imgur.com/), une plateforme de partage d'images incroyablement populaire.

La raison pour laquelle j'ai choisi Imgur est que je visitais fréquemment le site et que je connaissais déjà son fonctionnement. Après une rapide enquête, j'ai réussi à identifier quelques vulnérabilités courantes : XSS, clickjacking et toute une série de problèmes CSRF.

Signaler les problèmes s'est avéré un peu difficile. La seule façon que j'ai trouvée pour contacter Imgur était via leur système de support, qui n'était pas adapté pour signaler des problèmes de sécurité. Finalement, le 1er août, j'ai rédigé un rapport détaillant les problèmes, j'ai envoyé un email à security@imgur.com et j'ai attendu. Mais pas longtemps.

Quelques heures plus tard, j'ai reçu un email du fondateur et PDG d'Imgur, Alan Schaaf, me remerciant et m'offrant quelques goodies en récompense. Au cours des jours suivants, j'ai continué à leur transmettre des rapports sur les vulnérabilités que j'ai découvertes, dont une qui me rapporterait plus tard plus de 5 000 $.

Les choses sont restées calmes pendant un moment. Je vérifiais occasionnellement si certains des problèmes avaient été résolus, et effectivement, beaucoup l'avaient été. C'était rassurant de savoir qu'ils prenaient les problèmes au sérieux et que j'aidais à sécuriser la plateforme.

Puis, fin septembre, [Imgur s'est fait pirater](https://www.reddit.com/r/technology/comments/3lw2g6/imgur_is_being_used_to_create_a_botnet_and_ddos/). Quelqu'un a pu télécharger un fichier HTML avec du JavaScript malveillant sur Imgur et a procédé à cibler les utilisateurs de 8chan.

Cela a été rapidement [corrigé,](http://blog.imgur.com/2015/09/22/imgur-vulnerability-patched/) cependant, cela a été largement rapporté et clairement quelque chose qu'Imgur aurait souhaité ne pas voir arriver. En réponse, Imgur a finalement lancé leur [programme de bug bounty](http://blog.imgur.com/2015/09/30/imgurs-security-bug-bounty-program/) une semaine plus tard.

C'était une excellente nouvelle, car les gens avaient maintenant un moyen de signaler les problèmes de manière sécurisée. J'ai contacté Alan une fois de plus pour lui demander si certains de mes rapports étaient éligibles pour une récompense, et il m'a mis en contact avec l'un des développeurs d'Imgur, qui a confirmé que j'étais éligible et m'a demandé de créer un rapport sur [HackerOne](https://hackerone.com/imgur). Pour toutes les vulnérabilités que j'avais signalées — plus de 20 au total — 50 $ était ma récompense. La raison étant « pour la plupart, nous offrons des goodies pour les rapports CSRF, donc vous êtes plus une exception ici ».

Avant qu'Imgur ne crée leur programme de bug bounty, Imgur était truffé de vulnérabilités CSRF. Certaines, qui ont maintenant été corrigées, incluent : la possibilité de mettre à jour la bio de l'utilisateur, la possibilité de générer un nouveau secret client pour une [application Imgur](https://imgur.com/account/settings/apps), et la possibilité de changer l'URL de redirection pour une application Imgur donnée. Ce sont quelques-uns des problèmes que j'avais initialement signalés, donc être récompensé avec seulement 50 $ était assez décourageant.

Cependant, le développeur était clair : le programme était nouveau, et ils étaient encore en train d'apprendre et d'essayer de l'améliorer. Avec cela à l'esprit, je lui ai donné une liste des problèmes que j'avais signalés et il a confirmé qu'il y avait beaucoup plus dans les rapports qu'il ne l'avait réalisé.

Dans les quelques semaines entre la discussion des problèmes et l'obtention d'une récompense supplémentaire, j'ai découvert autre chose d'intéressant.

Lors de ma recherche initiale, j'ai examiné le code source HTML d'Imgur et j'ai trouvé le snippet suivant :

```
$(function() { if(!/^([^:]+:)\/\/([^.]+\.)*imgur(-dev)?\.com(\/.*)?$/.test(document.referrer)) { Imgur.Util.jafoLog({ event: 'galleryDisplay', meta: { gallerySort: 'viral', galleryType: 'hot' }}); } });
```

Cela m'a conduit à effectuer une reconnaissance sur imgur-dev.com, qui s'est avéré être le domaine qu'Imgur utilise pour le développement interne. Une rapide recherche Google pour site:imgur-dev.com a révélé que Google avait indexé le sous-domaine « alan.imgur-dev.com » qui contenait une version de développement d'Imgur. Le serveur, cependant, était hors ligne à ce moment-là. J'ai pu voir une copie mise en cache de la page qui révélait des informations intéressantes, y compris des tables de base de données et des noms de colonnes dans des requêtes SQL générées par [le profileur de Kohana](https://kohanaframework.org/3.1/guide/kohana/profiling).

Avance rapide jusqu'en novembre, j'ai décidé de jeter un autre coup d'œil à imgur-dev.com. Boom ! alan.imgur-dev.com était en ligne et accessible. Qu'ai-je trouvé ? C'était essentiellement Imgur tel que vous le connaissez avec quelques utilisateurs et quelques publications de test. Ce qui est notable, c'est que c'est un environnement de développeur — je pouvais voir des traces de pile qui incluaient des parties du code source d'Imgur, des avertissements et notices PHP, des détails sur l'environnement, des requêtes de base de données et des chemins complets vers des fichiers de configuration.

Avec ces détails, j'ai créé un autre rapport sur HackerOne et j'ai attendu une réponse. Deux jours plus tard, j'ai jeté un autre coup d'œil à alan.imgur-dev.com. Cette fois, j'ai décidé d'utiliser [SubBrute](https://github.com/TheRook/subbrute) sur alan.imgur-dev.com pour voir s'il y avait des sous-sous-domaines qui pourraient être intéressants.

Peu de temps après avoir commencé le scan, j'ai obtenu un hit : es.alan.imgur-dev.com. Une rapide visite a montré qu'il s'agissait d'un serveur Elasticsearch qui n'avait pas été mis à jour depuis un moment. En fait, après avoir cherché une vulnérabilité Elasticsearch, j'ai découvert [CVE-2014-3120](https://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2014-3120).

```
La configuration par défaut dans Elasticsearch avant la version 1.2 active le scripting dynamique, ce qui permet aux attaquants distants d'exécuter des expressions MVEL arbitraires et du code Java via le paramètre source vers _search.
```

Naturellement, j'ai pris un script de preuve de concept et j'ai essayé de lire /etc/passwd. Bingo. Lecture du fichier réussie. Maintenant, la chose sûre à faire ici aurait été de signaler le problème et de passer à autre chose. Pas cette fois. Imgur était à l'étape d'offrir des récompenses de 50 $ et des goodies. Je n'étais pas satisfait de cela. J'ai décidé d'aller plus loin et de voir à quel point je pouvais pirater Imgur si je le voulais.

Un fichier de configuration que j'avais remarqué plus tôt s'appelait « keys.php ». J'ai décidé d'essayer de le lire comme je l'avais fait pour /etc/passwd, et une fois de plus, c'était un succès. Ce fichier contenait tout ce dont j'avais besoin. Des clés API pour Fastly et MailChimp, des clés API pour les applications mobiles, même des clés API reCAPTCHA. Sweet. Mais ce n'est pas tout… le fichier contenait également les identifiants utilisés pour se connecter aux serveurs MySQL locaux et distants. Oups.

Le problème maintenant était que je ne connaissais pas le nom d'hôte du serveur MySQL distant, et je ne peux pas me connecter au serveur local à distance. Wat do ?

Je suis retourné au scan des sous-domaines, et il y avait un autre hit. sql.alan.imgur-dev.com. Oh oui, vous savez ce qui va se passer…

J'ai visité le domaine et j'ai été accueilli par phpMyAdmin. Maintenant, habituellement, vous vous attendriez à entrer uniquement le nom d'utilisateur et le mot de passe pour vous connecter. Heureusement pour moi, on m'a donné le choix des hôtes auxquels se connecter. L'un était le serveur local, et l'autre était un serveur distant hébergé sur Amazon AWS. J'ai sélectionné le serveur distant, entré les identifiants, et j'avais un accès complet à la base de données de production d'Imgur.

Eh bien, voilà, c'était amusant à écrire… Oh, vous pensiez que c'était tout ? Ce n'est pas tout, les gens.

Le fichier de configuration contenait également deux ensembles de clés d'accès Amazon [AWS](https://aws.amazon.com/developers/access-keys/) — un ensemble pour le développement et un ensemble pour la production. Alors, qu'ai-je fait ensuite ?

Rien.

Bien que je sache que j'aurais pu utiliser les clés pour lancer de nouveaux serveurs, me connecter en SSH à des serveurs existants, ou les détruire complètement, j'ai décidé de ne pas même tester s'ils fonctionnaient.

Une partie importante de la recherche en sécurité est de savoir quand s'arrêter.

Je suis allé assez loin pour prouver à quel point le problème est sérieux, et démontrer ce qu'un attaquant malveillant pourrait faire, sans être trop négligent ou intrusif.

Cela devait être corrigé, et rapidement. J'ai mis à jour le rapport HackerOne avec mes nouvelles découvertes, et j'ai envoyé un email urgent à Alan pour attirer son attention. En moins d'une demi-heure, le serveur était hors ligne. Le lendemain matin, Alan a répondu en me faisant savoir que l'accès au serveur était désactivé pendant qu'ils déterminent les prochaines étapes. J'ai été incroyablement impressionné par la façon dont ils l'ont géré.

```
Une erreur de configuration du groupe de sécurité a permis aux environnements de développement d'Imgur de faire face à l'internet public. Typiquement, ces environnements étaient protégés derrière un endpoint spécial qui ouvrait l'accès aux employés authentifiés d'Imgur pendant une courte fenêtre de temps. Puisque les environnements de développement étaient configurés de manière à faciliter le développement, certaines clés et variables d'environnement étaient exposées. Bien que la plupart de ces informations sensibles étaient limitées aux environnements de développement, certaines informations de production étaient également exposées. Depuis la publication de ce rapport, la sécurité autour des environnements de développement a été complètement repensée et ils résident maintenant derrière un VPN.
```

En avançant jusqu'à début décembre, pour les multiples vulnérabilités et le problème à haut risque que j'avais signalés, j'ai été récompensé par 500 $. Inutile de dire que je n'étais pas impressionné. J'ai décidé d'écrire un email à Alan pour lui donner mon avis sur le programme jusqu'à présent, et aussi expliquer pourquoi 500 $ n'étaient pas suffisants.

```
Les primes de bug sont comme l'embauche de mercenaires. Moins cher qu'une armée permanente de pentesters. Mais ne vous plaignez pas quand ils changent de côté pour plus d'or.
```

Une semaine plus tard, Alan a répondu, en accord avec les points que j'avais soulevés, et a dit que l'équipe aurait une réunion sur le programme bientôt. J'étais heureux d'apprendre que mon avis était pris au sérieux. Parfois, il est utile de parler directement au PDG pour que des changements réels se produisent.

Encore une fois, en janvier 2016, Alan m'a envoyé un dernier email.

```
Hey Nathan, Bonne année ! J'ai enfin pu me synchroniser avec mon équipe et parvenir à une conclusion sur ce sujet. Puisque votre exploit est allé au-delà (contenait plusieurs exploits tous enchaînés, accès aux données de production, etc.), nous voulons aussi aller au-delà pour vous, et avons convenu de vous offrir 5 000 $ supplémentaires. C'est tellement plus que tout ce que nous avons jamais offert auparavant, mais encore une fois, cet exploit était tellement plus que tout ce qui a été trouvé auparavant, donc je pense qu'il le mérite et j'espère qu'il est suffisant pour vous. Merci beaucoup de nous avoir protégés et de nous l'avoir signalé correctement. Bonne chance pour la nouvelle année. Cordialement, Alan
```

C'était une excellente nouvelle à recevoir. Non seulement Imgur a changé leur programme de bug bounty pour payer équitablement les chercheurs, mais les 5 000 $ supplémentaires ont énormément aidé moi et d'autres. La moitié de cette somme est allée à des personnes dans le besoin, y compris [Lauri Love,](https://freelauri.com/) un hacker faisant face à une extradition vers les États-Unis, et un ami proche qui s'est récemment retrouvé sans abri. Diverses œuvres caritatives et chercheurs en ont également bénéficié.

J'ai continué à participer au programme de bug bounty d'Imgur, et bien qu'il ne soit pas parfait, il a répondu et payé généreusement à moi et à d'autres. J'espère que d'autres équipes pourront apprendre de la volonté d'Imgur de prendre en compte les retours et de s'améliorer, car la communication autour de la sécurité est si importante.

Qu'est-ce qui m'attend ensuite ? J'espère continuer à apprendre et travailler pour rendre Internet un environnement plus sûr et plus sécurisé pour les générations futures. Internet est minuscule par rapport à ce qu'il sera dans 10 ans. La bataille n'est pas terminée, et la guerre est encore à venir.

Si vous cherchez un défi, je vous recommande vivement de consulter le programme de bug bounty d'Imgur et d'autres sur [HackerOne](https://hackerone.com/imgur).

Vous pouvez me suivre sur [Twitter](https://twitter.com/NathOnSecurity) où je tweete sur la sécurité, le terrible temps britannique et les memes. Oui. Vous savez que vous voulez… :-)