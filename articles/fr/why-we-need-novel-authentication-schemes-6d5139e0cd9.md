---
title: Pourquoi avons-nous besoin de nouveaux schémas d'authentification ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-26T09:24:26.000Z'
originalURL: https://freecodecamp.org/news/why-we-need-novel-authentication-schemes-6d5139e0cd9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9NyXeoNrQoKQoWY7ZuMXew.jpeg
tags:
- name: '#infosec'
  slug: infosec
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Pourquoi avons-nous besoin de nouveaux schémas d'authentification ?
seo_desc: 'By Cossack Labs Dev Stories

  Revealing security holes in 5 main methods of authentication

  Introduction: A Word To Pass

  Passwords are ultimate keepers of diversity and security. Since Ancient Roman times
  until now, they are used for one to prove being ...'
---

Par Cossack Labs Dev Stories

Révélation des failles de sécurité dans 5 méthodes principales d'authentification

### Introduction : Un Mot À Passer

Les mots de passe sont les gardiens ultimes de la diversité et de la sécurité. Depuis l'époque de la Rome antique jusqu'à aujourd'hui, ils sont utilisés pour prouver qu'une personne est digne d'obtenir un privilège que les autres ne possèdent pas, mais qu'ils désirent fortement obtenir. Un « mot magique », que l'on connaît et que les autres ne connaissent pas, ouvre la porte à une opportunité et diversifie un individu en le sélectionnant parmi une foule énorme.

Nous pouvons dire que le mot de passe est le plus ancien et le plus largement utilisé des piliers de l'authentification, qui est extensivement utilisé sur l'Internet du 21e siècle. Son importance est encore plus grande qu'avant, car de nos jours, de plus en plus de personnes communiquent à distance sans se voir ni s'entendre, utilisant des moyens à distance pour accéder à des systèmes automatisés. Par conséquent, ils doivent se fier uniquement aux mots de passe pour vérifier la partie distante et prouver leur propre identité. Il suffit de connaître le mot de passe d'une autre personne pour devenir cette personne aux yeux des autres, faire tout ce que vous voulez en leur nom, obtenir leurs privilèges dans les systèmes automatisés. C'est pourquoi il est si crucial de protéger correctement les mots de passe.

Cependant, la plupart des schémas utilisés pour l'authentification aujourd'hui ont leurs propres faiblesses — bien que certaines d'entre elles soient assez théoriques, dans un monde en rapide évolution, les menaces théoriques deviennent fréquemment très pratiques.

#### La communication comme principale menace pour les secrets

La manière idéaliste de garder un secret en sécurité est de ne pas l'utiliser : si vous ne l'utilisez jamais, personne ne l'interceptera. Cependant, cela rend de tels secrets inutiles. Puisque les secrets vous donnent des privilèges, vous voulez obtenir et exercer ces privilèges de temps en temps.

Pour ce faire, vous devez prouver que vous connaissez le secret. Ce processus implique de communiquer le secret à une autre partie, ce qui expose finalement tout ou partie du secret. L'exercice d'un secret implique au moins 2 parties : un prouveur (vous) et un vérificateur (une entité qui décide finalement si votre secret est le bon et si vous méritez les privilèges que vous revendiquez). Cependant, si vous ne pouvez pas communiquer directement avec le vérificateur, vous devez utiliser une ou plusieurs entités intermédiaires, auquel cas ces entités connaissent également le secret.

Revenons maintenant au monde réel du 21e siècle et d'Internet : lors de la communication, vous pouvez utiliser des milliers de liens intermédiaires pour livrer vos données, donc une fois que vous envoyez un secret au vérificateur — ce n'est plus un secret.

### Méthodes existantes d'authentification

Les méthodes existantes offrent un certain niveau de protection, meilleur ou pire, mais chacune d'entre elles présente des inconvénients significatifs. Jusqu'à présent, la plupart des systèmes actuels et des protocoles sécurisés n'ont utilisé que trois types de primitives cryptographiques : le chiffrement, l'accord de clé et les signatures numériques. Des tâches de plus haut niveau, comme l'authentification, sont réalisées en combinant ces primitives de quelque manière que ce soit dans un protocole.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GRHd9iKAhL5A_3_XopGOlg.jpeg)

L'authentification Internet a commencé avec des mots de passe assez basiques : un utilisateur entrait le mot de passe dans le formulaire web, le mot de passe était envoyé via HTTP au serveur, le serveur vérifiait le mot de passe et laissait l'utilisateur entrer. C'était au début du petit Internet. À cette époque, les attaquants étaient limités par leur très faible expérience sur le fonctionnement d'Internet. Même si certains avaient des connaissances de base en réseau, ils n'avaient pas l'équipement, les outils ou les logiciels (qui étaient très coûteux à l'époque) pour mener les attaques. De plus, les attaques elles-mêmes étaient sans but en raison de la faible valeur commerciale des informations qui transitaient par Internet à cette époque. Finalement, la croissance d'Internet et la disponibilité des connaissances, des logiciels et des outils ont créé le premier attaquant réseau : les mots de passe HTTP étaient facilement volés par les renifleurs de réseau passifs les plus simples et les analyseurs de protocole.

L'étape suivante a été de changer les mots de passe en certaines valeurs qui étaient inutiles pour les écouteurs passifs : les gens ont commencé à hacher le mot de passe. Puisque le serveur et l'utilisateur avaient le même mot de passe, ils pouvaient produire des hachages identiques de ceux-ci et les comparer, l'utilisateur envoyant le hachage au serveur. Il semblait que les attaquants ne pouvaient pas obtenir le mot de passe, car l'inversion d'une fonction de hachage est calculatoirement « presque impossible ». Cette solution a sauvé la journée... pour juste un petit moment ! Les attaquants ont utilisé deux moyens pour surmonter cela :

_Premièrement :_ beaucoup de gens rendent leurs mots de passe « faciles à retenir », donc les attaquants ont haché un grand ensemble de mots populaires et, en connaissant le hachage, pouvaient facilement « rechercher » le mot de passe original s'il se trouvait être dans le « dictionnaire » produit : une attaque par dictionnaire a été inventée.

_Deuxièmement :_ même si quelqu'un utilisait un mot de passe complexe, les attaquants utilisaient simplement le hachage directement pour s'authentifier avec le serveur avec un « navigateur modifié ». Ils n'entraient pas le mot de passe dans le formulaire, mais injectaient le hachage directement dans le flux HTTP : une attaque active a été inventée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kf2NQd5Ak3cE6wJH0tfH_g.jpeg)

Il était maintenant clair que le trafic HTTP devait être chiffré. Cependant, puisque les parties communicantes étaient situées loin l'une de l'autre, un accord de clé a été utilisé et a finalement été rompu par les attaquants : l'homme du milieu a été proposé.

L'histoire continue : plus les schémas sophistiqués pour protéger la transmission des mots de passe sont proposés, meilleures et plus intelligentes sont les attaques conçues pour les vaincre. Ne serait-il pas formidable d'éviter de transmettre les mots de passe du tout ?

#### 1. Protocoles d'échange de hachage personnalisés

La plupart des ingénieurs qui commencent à développer des outils cryptographiques semblent très satisfaits lorsqu'ils ont leur premier succès à transformer un morceau de données en une chaîne aléatoire en utilisant une clé et à récupérer les données originales. Le problème est que la plupart des ingénieurs s'arrêtent à ce stade. Comme nous le savons de la loi de Schneier :

_N'importe qui, du plus ignorant des amateurs au meilleur cryptographe, peut créer un algorithme qu'il ne peut pas lui-même casser._

Ils pensent que si la sortie est effectivement aléatoire et que personne ne connaît la clé, ils sont en sécurité. Ainsi, on peut toujours trouver des schémas de chiffrement de faible sécurité, des clés ou des vecteurs initiaux codés en dur, une utilisation impropre des modes de chiffrement, etc., même dans les logiciels de production. Et, bien que votre sortie semble aléatoire, un attaquant sophistiqué avec les bons outils et une formation mathématique trouvera sûrement des motifs, des fuites de canaux auxiliaires, effectuera une cryptanalyse et récupérera finalement les données. Même les grandes entreprises ont des problèmes avec cela, alors qu'est-ce qui vous rend spécial ?

Différents schémas impliquant bcrypt, pbkdf2 ou tout cadre 'encrypt then compare' ne fournissent qu'un fragment du système de sécurité au lieu d'une solution complète. Cela ne fournit pas un niveau de sécurité suffisant du tout.

#### 2. Authentification HTTP

Les mots de passe sont encore largement utilisés en HTTP pour donner aux utilisateurs l'accès à des ressources restreintes. Cependant, malgré la longue histoire des mises à jour des protocoles d'authentification, il reste encore une certaine marge pour les attaques. Un utilisateur soucieux de la sécurité ne tentera jamais d'entrer son mot de passe sur un site web si ce site ne fournit pas de connexion HTTPS pour entrer de telles informations d'identification. Cela signifie que même aujourd'hui, les mécanismes d'authentification HTTP en eux-mêmes sont assez faibles. Vérifions le schéma simplifié de haut niveau de l'authentification HTTP :

![Image](https://cdn-media-1.freecodecamp.org/images/0*JmW8cRdAO4lnDK5_.png)
_À première vue, cela semble correct, mais si l'on y réfléchit davantage, de nombreuses préoccupations peuvent venir à l'esprit :_

* Tout d'abord, le serveur authentifie le client, mais le client n'authentifie pas le serveur. Ainsi, le client ne sait pas à qui il envoie ses informations d'identification. De plus, l'authentification HTTP ne définit pas la confidentialité, donc n'importe qui peut au moins savoir qu'une certaine ressource web a une certaine base d'utilisateurs simplement en observant le trafic.
* Bien que dans les protocoles d'authentification récents, les utilisateurs n'envoient pas directement les mots de passe, envoyant des hachages (qui est une fonction irréversible à sens unique) de leurs mots de passe à la place, les écouteurs passifs peuvent encore collecter ces informations et utiliser des techniques plus complexes (comme les [attaques par dictionnaire](https://en.wikipedia.org/wiki/Dictionary_attack) pour récupérer le mot de passe).
* Les mécanismes d'authentification précédents n'utilisaient pas de nonces de serveur, donc une simple [attaque par rejeu](https://en.wikipedia.org/wiki/Replay_attack) était possible. Même aujourd'hui, de nombreux navigateurs supportent de tels mécanismes plus anciens pour des raisons de compatibilité, donc un [homme du milieu](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) peut forger des messages entre le client et le serveur et effectuer une [attaque par rétrogradation](https://en.wikipedia.org/wiki/Downgrade_attack).

#### 3. Kerberos

Une approche paresseuse : au lieu de s'authentifier mutuellement, pourquoi ne pas faire faire cela par quelqu'un d'autre ? Ainsi, une entité est créée, tous les clients et services y enregistrent leurs clés et lorsque la communication entre un client et un serveur particulier est nécessaire, ils demandent simplement « le service ». Cela semble bien au début, mais il y a quelques inconvénients et le principal d'entre eux est que tous les inconvénients deviennent de plus en plus graves à mesure que votre infrastructure grandit :

* méthodes mal développées pour obtenir la confiance initiale dans le serveur Kerberos (enregistrement initial du client et du service)
* principalement le chiffrement symétrique est utilisé pour les informations de protocole et, puisque le protocole est connu, il y a une possibilité ouverte d'attaques à texte clair connu
* le développement et les tests sont difficiles sous Kerberos : un domaine séparé et une configuration Kerberos séparée sont nécessaires pour les environnements de développement et de production
* possibles mauvaises configurations et utilisation de la cryptographie faible pour les administrateurs inexpérimentés
* le plus important : tout va bien jusqu'à ce que votre serveur Kerberos soit sécurisé. Lorsqu'il est compromis, tout l'écosystème de sécurité explose. Et puisque tôt ou tard des violations de sécurité se produisent, avoir Kerberos est similaire à avoir une bombe à retardement de sécurité dans votre jardin.

#### 4. SSL/TLS

[SSL/TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) est le protocole standard de facto pour l'authentification Internet. En utilisant TLS, un client (par exemple, un navigateur) authentifie le serveur et, éventuellement, le serveur peut authentifier le client. Le protocole est bien établi, mais présente certains inconvénients :

* nécessite une [infrastructure à clé publique](https://en.wikipedia.org/wiki/Public_key_infrastructure) établie, qui est difficile à configurer et à maintenir techniquement ainsi que coûteuse
* le protocole est complexe, donc il a une mauvaise auditabilité en termes de mise en œuvre (de nombreuses attaques de mise en œuvre le prouvent)
* a une longue histoire de mises à jour et d'améliorations, qui sont motivées par des raisons de compatibilité ainsi que par des attaques de protocole découvertes
* a encore des faiblesses (en partie à cause de ce qui précède)

Bien que la version actuelle soit considérée comme sécurisée (pourtant les gens utilisent rarement la dernière version de TLS, se noyant plutôt dans les anciens chiffrements et versions vulnérables comme SSLv3), il y a encore de nombreuses informations qu'un observateur passif peut collecter à partir du résultat du protocole :

* si le protocole a réussi ou non
* quelles parties communiquent (en vérifiant les champs du certificat)
* à quel point le logiciel sur le client et le serveur est moderne (en examinant la version TLS communiquée et la liste des suites de chiffrement supportées)
* éventuellement si les parties utilisent du matériel dédié pour le stockage des clés privées

#### 5. OAuth

On pourrait penser que nous avons omis OAuth, le protocole d'autorisation déléguée populaire fréquemment utilisé pour l'authentification de nos jours.

Cependant, c'est un protocole qui :

* l'un de ses principaux concepteurs [démissionne avec un retour négatif](http://hueniverse.com/2012/07/26/oauth-2-0-and-the-road-to-hell/) concernant le niveau de sécurité
* [multiples](http://www.thread-safe.com/2012/01/problem-with-oauth-for-authentication.html) [failles](http://leastprivilege.com/2013/03/15/common-oauth2-vulnerabilities-and-mitigation-techniques/) trouvées dans sa conception de base
* [nombreuses](http://homakov.blogspot.com/2012/07/saferweb-most-common-oauth2.html) [erreurs](http://homakov.blogspot.com/2013/03/oauth1-oauth2-oauth.html) [de](http://insanecoding.blogspot.com/2013/03/oauth-great-way-to-cripple-your-api.html) [mise en œuvre](https://conference.hitb.org/hitbsecconf2013ams/materials/D2T1%20-%20Andrey%20Labunets%20and%20Egor%20Homakov%20-%20OAuth%202.0%20and%20the%20Road%20to%20XSS.pdf)
* ... flottant parmi les déploiements aussi grands que [Github](http://homakov.blogspot.com/2014/02/how-i-hacked-github-again.html) et [Facebook](https://www.facebook.com/IHAverified/posts/632698623426949)

En bref, vous pourriez prendre tous les pires points des méthodes précédentes (clients non authentifiés, mauvaise sécurité de transport), en ajouter de nouveaux (attaques actives latérales !) et avoir cela comme protocole « d'authentification ».

Si, par un quelconque caprice du sort, vous devez finir par utiliser OAuth pour l'authentification, veuillez investir un peu de temps pour [le renforcer autant que possible](https://github.com/homakov/oauthsecurity).

### Avec l'augmentation de la complexité, de nouveaux problèmes surgissent.

Outre les problèmes avec les protocoles eux-mêmes, de nouvelles topologies de réseau et de nouveaux schémas de relation apparaissent, avec des dispositions de réseau ad-hoc, des rôles mixtes et peu de capacité à supporter une infrastructure de confiance lourde du passé. De nouveaux types de vulnérabilités et de nouvelles techniques de détection de vulnérabilités rendent de nouveaux vecteurs d'attaque efficaces.

Que faisons-nous pour relever ces défis ?

Pas grand-chose. Nous augmentons encore la complexité en introduisant l'authentification multifactorielle. Nous ajoutons des jetons d'authentification avec de très mauvaises propriétés (comme les empreintes digitales, photographiées par une caméra spéciale dans votre iPhone). Nous introduisons des dispositifs physiques.

Cependant, chacun de ces canaux d'authentification ayant ses propres failles, bien que la force générale de l'ensemble du schéma soit meilleure lorsque chaque partie est suffisamment forte, lorsque l'un des canaux d'authentification est compromis, la sécurité se dégrade considérablement. Et, comme l'infrastructure pour ces nouveaux canaux d'authentification est encore à stabiliser, vous pourriez même ne pas comprendre que votre jeton est compromis, ainsi que l'ensemble du schéma d'authentification.

### Existe-t-il une solution ?

Toutes les méthodes mentionnées ci-dessus sont fortes à un certain degré et ont certaines faiblesses différentes. Si vous êtes prêt à vous en tenir à ces méthodes, mettez au moins un peu d'effort à les protéger de leurs faiblesses en appliquant les meilleures pratiques disponibles. En tant que cryptographes, nous nous efforçons de trouver des méthodes qui sont [théoriquement sécurisées, et non seulement 'jamais prouvées comme étant non sécurisées', ce qui est connu comme étant pratiquement sécurisé](https://books.google.com.ua/books?id=1NHli2uzt_EC&pg=PA76&lpg=PA76&dq=practical+vs+theoretical+security&source=bl&ots=tWHzZvyCNE&sig=ZDHHwhcYADzUoaTUoelbsyOx6dI&hl=uk&sa=X&ved=0ahUKEwj4p4mxo67JAhUHjiwKHat9Df8Q6AEIOjAE#v=onepage&q=practical%20vs%20theoretical%20security&f=false).

Cependant, nous avons quelque chose de plus intéressant pour les personnes prêtes à essayer de nouvelles choses. Quelque chose qui n'est pas seulement pratiquement fort, mais aussi mathématiquement fort.

Chez Cossack Labs, nous avons travaillé sur un nouveau schéma d'authentification de requête, efficace lorsqu'il y a un identifiant d'objet (A) et une propriété unique de l'objet (B). Parmi ces objets, sans surprise, se trouvent les paires login/mot de passe. Cette méthode ne repose pas sur les propriétés cryptographiques traditionnelles, qui incluent encore l'envoi de mots de passe sous une forme ou une autre sur le réseau (et ayant une certaine probabilité théorique d'être compromis), mais plutôt une mise en œuvre pratique de nouvelles mathématiques cryptographiques, qui ne fuite pas les informations d'identification du tout, que ce soit sous forme directe ou hachée.

Restez à l'écoute pour les prochains articles éducatifs et le document scientifique sur Secure Authenticator, une nouvelle façon de vérifier le mot de passe de l'utilisateur avec 0 chance d'interception.

P.S. Cet article a été initialement publié sur notre [blog](https://cossacklabs.com/why-we-need-novel-authentication-methods.html).