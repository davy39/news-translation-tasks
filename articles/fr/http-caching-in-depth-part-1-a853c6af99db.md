---
title: 'Une introduction approfondie au cache HTTP : exploration du paysage'
subtitle: ''
author: Léo Jacquemin
co_authors: []
series: null
date: '2018-12-17T18:21:46.000Z'
originalURL: https://freecodecamp.org/news/http-caching-in-depth-part-1-a853c6af99db
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Phwh9Iozlntqjhc2
tags:
- name: https
  slug: https
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: web performance
  slug: web-performance
seo_title: 'Une introduction approfondie au cache HTTP : exploration du paysage'
seo_desc: 'Cache Me If You Can

  About 2 years ago, I remember witnessing a reunion that had a profound impact on
  my software developer life.

  The client, a former developer with decades of experience, a tech savvy product
  owner and another senior developer were t...'
---

### Cachez-moi si vous pouvez

Il y a environ 2 ans, je me souviens d'avoir assisté à une réunion qui a eu un impact profond sur ma vie de développeur logiciel.

Le client, un ancien développeur avec *des décennies* d'expérience, un chef de produit techno-savvy et un autre développeur senior parlaient d'un problème de cache. L'API répondait avec des fragments vidéo obsolètes qui faisaient que les clients visionnaient le mauvais contenu.

C'était grave. Très grave.

Bien que personne ne sache quoi faire pour résoudre le problème, ils semblaient tous d'accord sur une chose. Le problème était très probablement un problème de cache.

Je ne savais **rien** du cache HTTP à l'époque, donc tout ce que je pouvais faire était d'écouter leurs arguments sur ce qui avait pu mal se passer. Et chacun d'eux avait une explication différente.

*Les navigateurs dévient des spécifications !* disait le client. *Le CDN remplace nos directives de cache !* pensait le chef de produit techno. *Nous devons invalider tout le cache* répondit le tech lead.

Comme je voulais être utile aussi, même si je n'étais pas exactement sûr de comment, étant donné mon niveau de compréhension, j'ai commencé à poser des questions à mes collègues.

Je me souviens très bien du niveau de confiance que tout le monde semblait avoir en répondant à mes questions. Tout le monde agissait comme s'ils savaient tout sur le cache HTTP. Mais en même temps, toutes leurs réponses semblaient vraiment vagues et superficielles. C'était vraiment comme si tout le monde avait ce niveau élevé de compréhension de comment les choses fonctionnaient, mais que personne ne voulait entrer dans les détails.

Finalement, le problème s'est résolu comme par magie et l'équipe était plutôt satisfaite de la façon dont les choses se sont passées.

Mais pas moi.

Je me suis dit à moi-même, qu'est-ce qui vient de se passer ces derniers jours ? Pourquoi est-ce que personne n'était prêt à admettre qu'ils n'ont aucune idée de comment ce cache fonctionne ? Est-ce la malédiction du développeur logiciel d'être toujours tenté de prétendre que nous en savons plus sur un sujet que nous n'en savons réellement ?

Alors j'ai décidé de vérifier par moi-même. Et j'ai quelque peu compris pourquoi tout le monde faisait semblant. Le sujet n'était en aucun cas facile. Mais j'étais déterminé à aller au fond des choses.

Et c'est ainsi que ce qui était censé être quelques heures de recherche sur Google s'est transformé en des mois de lecture d'articles, de méditation sur les spécifications, et d'expérimentation avec des logiciels de cache.

Aujourd'hui, je réalise que la performance web (dont le cache HTTP est l'un des aspects les plus importants) est un sujet sur lequel nous ne sommes pas suffisamment formés. Trop peu d'articles en parlent, et la plupart d'entre eux ne vont pas assez loin.

Les articles suivants sont ma tentative de rectifier cela en partageant tout ce que j'ai appris au cours des deux dernières années sur le cache HTTP.

Je ne suis pas un expert en cache, et je ne vous transformerai pas en un. Mais cela vous donnera, je l'espère, une solide compréhension de comment les choses fonctionnent réellement.

### Commençons

Cette série d'articles traite du cache dans le contexte de HTTP. Lorsqu'il est bien fait, le cache peut augmenter la performance de votre application d'un ordre de grandeur.

Au contraire, lorsqu'il est négligé ou complètement ignoré, il peut conduire à des effets secondaires vraiment indésirables causés par des serveurs proxy malveillants qui, en l'absence d'instructions de cache claires, décident de mettre en cache quand même et de servir des ressources obsolètes.

Avant d'entrer dans les détails tactiques de comment le cache fonctionne, il est utile de comprendre le contexte et le paysage du problème auquel nous sommes confrontés. Pour cette raison, la première partie de cette série couvre **où** le cache devrait se produire et **pourquoi** nous en avons besoin.

Sans plus attendre, commençons par un aperçu des considérations clés à garder à l'esprit lorsque l'on traite du cache HTTP, et dans une moindre mesure, de la performance web en général.

### Le cache partout

#### Navigateurs

Le cache est une technique très populaire. L'idée est en effet assez attrayante : peu importe la durée de la requête I/O, l'intensité CPU du calcul, ou toute autre tâche de programmation, c'est toujours la même chose : stocker le résultat quelque part et le récupérer tel quel, pour son application ultérieure.

Prenons l'exemple du cache HTTP du navigateur que tous les navigateurs implémentent, les ressources web sont stockées sur le système de fichiers de l'utilisateur. Par conséquent, les requêtes ultérieures qui accéderont à ces mêmes ressources les obtiendront instantanément.

Aucune requête réseau, aucun aller-retour client/serveur, aucun accès à la base de données, et ainsi de suite. Pouvez-vous penser à une amélioration de performance qui donnerait de meilleurs résultats que zéro latence et un déchargement complet du serveur ? Ce n'est tout simplement pas possible.

On pourrait penser que cette situation est trop idéale et irréaliste. Si c'était vrai, comment se fait-il que la plupart des pages ne se chargent pas si vite ? Une raison à cela est que, même si toutes les ressources web sont cachables, elles ne doivent pas être mises en cache de la même manière.

Les fichiers HTML, par exemple, qui sont les premiers à être téléchargés et qui contiennent des références à d'autres actifs, sont notoirement dangereux à mettre en cache. Par conséquent, il est peu probable qu'ils trouvent leur chemin vers les caches des navigateurs sauf pour quelques minutes au maximum, comme nous le verrons dans un instant.

Mais une autre explication possible, que nous trouvons plus probable sur la base de notre expérience, est que les politiques de cache sont souvent complètement laissées de côté pour que les serveurs web décident.

Définir un drapeau dans le fichier de configuration d'un serveur web pour activer automatiquement la génération [ETag](https://developer.mozilla.org/fr/docs/Web/HTTP/Headers/ETag) et les en-têtes Last-Modified n'est pas chronophage et peut donner des résultats décents.

Pendant un certain temps au moins. Jusqu'à ce que l'on réalise que la fonctionnalité ne fonctionne pas comme prévu ou, pire encore, que les utilisateurs commencent à recevoir du contenu obsolète pour des raisons inconnues.

De plus, ces serveurs web ne feront pas grand bien en termes de cache de votre API. La plupart d'entre eux génèrent des en-têtes de cache basés sur les métadonnées des fichiers, ce qui peut avoir des [conséquences subtiles](https://github.com/sullo/nikto/issues/469). Mais avec les requêtes API, il n'y a pas de fichier à lire les métadonnées. Par conséquent, lorsqu'ils voient une ressource qui est générée dynamiquement, tout ce qu'ils peuvent faire est de regarder et de transmettre la requête.

Certes, aussi efficace que cela puisse être, le cache dans le navigateur n'est pas aussi facile qu'il en a l'air. Les principaux navigateurs implémentent différentes couches de cache, dont celui de HTTP dont nous parlons n'est qu'une partie. Et au cas où vous vous poseriez la question, [ils peuvent interagir](https://blog.yoav.ws/tale-of-four-caches/) de certaines manières qui ne sont pas toujours aussi prévisibles que nous le souhaiterions.

De plus, le cache dans le navigateur est notoirement dangereux, car les développeurs manquent de la capacité à invalider les ressources à volonté. Pour ce faire, il faudrait permettre à un serveur web de pousser des informations à chaque client qui a interagi avec lui, sans que les clients initient une connexion, ce qui n'est pas possible dans une architecture client/serveur.

De plus, du point de vue du cacheur, aussi puissant soit-il, le navigateur a d'autres défauts. Il utilise certaines heuristiques douteuses lorsqu'aucune instruction de cache n'est explicitement présente, ce qui est une raison de plus pour nous de l'aider à savoir exactement quoi faire.

Mais même si nous devions le faire, les utilisateurs ont la capacité de vider leur cache de toute façon ou de le désactiver. Pas l'outil de cache tout-puissant que l'on pourrait demander pour Noël, après tout.

Alors, sortons le navigateur de l'équation pour l'instant et demandons-nous : sans lui, le cache HTTP est-il toujours pertinent ? Est-il implémenté à d'autres endroits ? Comme il s'avère, le navigateur n'est qu'une pièce du puzzle du cache. Et si les navigateurs devaient soudainement arrêter de tout mettre en cache, soyez assuré : les CDN nous couvrent.

#### CDN

Les réseaux de diffusion de contenu (CDN) sont les champions unifiés du monde du cache HTTP. La plupart d'entre eux ont installé des tonnes de serveurs — Akamai en a ~[240 000](https://www.akamai.com/us/en/about/facts-figures.jsp) — tous géographiquement répartis dans le monde afin de servir notre contenu près de nos utilisateurs finaux.

Ces entreprises ont accumulé des décennies d'expérience sur la performance web. La plupart des personnes qui écrivent [les spécifications](https://tools.ietf.org/html/rfc7234) ou le logiciel qui alimente les spécifications travaillent généralement dans ces entreprises, ce qui est un peu une indication qu'ils savent ce qu'ils font. Faisons un rapide tour d'horizon de pourquoi ils sont si importants et comment ils fonctionnent.

Tout d'abord, il est crucial de comprendre que tous ces serveurs sont des serveurs HTTP. En termes HTTP, ce sont des serveurs proxy, ce qui signifie qu'ils parlent HTTP. Ils n'encapsulent pas nos requêtes dans un autre protocole d'application propriétaire obscur. Ils utilisent simplement ces proxys, dont la plupart sont même gratuits ou open source !

En conséquence directe, toute connaissance du cache HTTP est immédiatement exploitable pour tirer parti de l'infrastructure qu'ils mettent à notre disposition. En plus de milliards de navigateurs, nous avons maintenant des milliers de serveurs stratégiquement placés par des entreprises spécialisées attendant que nous leur disions comment mettre en cache notre contenu pour une efficacité maximale. De plus, selon vos priorités, ce n'est même pas la meilleure fonctionnalité.

La plupart des CDN modernes annoncent la capacité de purger programmatiquement les ressources du réseau du CDN instantanément. Répétons-le : *programmatiquement* et *instantanément*.

En ce qui concerne le cache HTTP, les [deux problèmes difficiles](https://martinfowler.com/bliki/TwoHardThings.html) en informatique pourraient bien avoir été réduits à un seul ! Mettre en cache n'importe quoi et invalider instantanément chaque fois que nous le voulons. Du point de vue d'un développeur soucieux de la performance web, cela ne peut guère être mieux.

Un mot d'avertissement : les CDN ne doivent pas être aveuglément dignes de confiance sur cette base. Nous avons déjà expérimenté quelques légères différences entre ce qui était commercialisé dans la brochure et ce que nous avions en production, où d'autres techniques de contournement de cache ont dû être utilisées pour s'assurer que le cache était effectivement vidé.

Avant de commencer à mettre en cache toutes vos ressources pour toujours sans précaution, expérimenter sur un petit échantillon en premier pourrait être une bonne idée. Cependant, si ce n'est pas ici aujourd'hui, cela finira par arriver de manière cohérente partout, rendant nos vies beaucoup plus faciles.

Un autre aspect à garder à l'esprit est qu'il est dans l'intérêt de chaque CDN que les développeurs les voient comme des outils efficaces et puissants. En conséquence, ils feront souvent de leur mieux pour se conformer à la spécification.

De plus, ils fournissent tous une interface web qui permet de donner des règles de cache qui remplaceront ou joueront bien avec les directives de cache en amont provenant des serveurs d'origine. La capacité à configurer votre politique de cache en dehors de votre base de code a deux conséquences intéressantes.

Premièrement, cela signifie que des personnes autres que les développeurs peuvent avoir le contrôle sur cela, ce qui peut être vu comme une force ou une faiblesse selon votre perspective. La capacité à avoir quelqu'un d'autre qu'un développeur logiciel pour ajuster finement les paramètres de cache au niveau du CDN lors d'occasions critiques peut s'avérer utile dans certaines situations.

Mais peut-être encore plus important, cela signifie que la partie performance de votre application, ou au moins une grande partie de celle-ci, peut être complètement externalisée au niveau de l'infrastructure.

Tous les développeurs qui ont expérimenté des problèmes de performance à un moment donné le savent : c'est rarement quelque chose que vous pouvez mutualiser dans un seul fichier appelé *performance* et est [souvent mieux planifié à l'avance](http://e-culture-de-la-performance-web-sur-son-projet/), tout comme le journalisation détaillée au niveau de l'application. Mais ce n'est pas nécessairement le cas avec le cache.

À condition que vos en-têtes de cache soient intelligemment définis et que votre CDN soit bien configuré, vous pourriez écrire un code serveur mal optimisé (bien que, s'il vous plaît, ne le faites pas) et avoir toujours la grande majorité de vos utilisateurs servis avec du contenu en moins de 300 millisecondes, en réutilisant des versions mises en cache qui sont toujours parfaitement fraîches.

En revanche, comme on pourrait s'y attendre, la mise en place et la maintenance d'un tel réseau de serveurs sont à la fois coûteuses et complexes. En conséquence, bien que certains d'entre eux aient des plans gratuits qui permettent déjà un sérieux gain de performance dans des zones géographiques assez larges, ils restent des solutions payantes. Si votre intention est de mettre en cache des millions de ressources, soyez prêt à payer plusieurs milliers de dollars. C'est là que les caches proxy privés entrent en jeu.

#### Proxy privé

Le troisième et dernier acteur du jeu du cache HTTP est simplement le même logiciel dont sont faits beaucoup des CDN dont nous venons de parler. Les noms [Varnish](https://varnish-cache.org/), [Squid](http://www.squid-cache.org/), [Traffic Server](http://trafficserver.apache.org/), ou même [Nginx](https://www.nginx.com/) vous disent-ils quelque chose ? Eh bien, ils le devraient certainement !

Étant donné ce que nous venons de dire sur la performance inégalée des caches des navigateurs web, et le cas que nous venons de plaider en faveur des CDN, on pourrait légitimement se demander : pourquoi se donner la peine de les mettre en place devant mes serveurs d'origine lorsque les CDN peuvent faire beaucoup plus, et que les navigateurs sont plus proches de mes utilisateurs finaux ?

Eh bien, cette troisième et dernière solution dans le paysage du cache HTTP vient également avec sa juste part d'avantages. En fait, nous soutiendrons que cela devrait souvent être la première solution à rechercher. Examinons quelques points bonus des solutions les plus populaires.

Tout d'abord, ces solutions sont gratuites et open source, ce qui peut être vu comme une épée à double tranchant. Combien de tels logiciels, autrefois loués par la communauté, ont soudainement [cessé](https://blog.npmjs.org/post/180565383195/details-about-the-event-stream-incident) d'être maintenus par leurs contributeurs principaux en raison d'un manque d'intérêt, de sponsoring, ou des deux ? La peur de voir une dépendance principale d'un projet (framework web, bibliothèque UI, etc.) partir au cimetière des logiciels est une préoccupation réelle.

Cependant, lors de l'évaluation de ce risque, on doit toujours considérer la maturité de la technologie, depuis combien de temps elle existe, quelle grande entreprise l'utilise ou la soutient — elles font généralement les deux — et à quel point elle est efficace pour résoudre un problème particulier. Heureusement pour nous, les proxys dont nous parlons obtiennent de très bonnes notes sur tous les niveaux.

Un autre aspect vient simplement du gain de performance. Comme mentionné précédemment, ces logiciels sont ce dont les CDN sont faits. Cela a deux conséquences.

Premièrement, cela réduit massivement les chances de cessation de leur utilisation, car toute l'infrastructure des CDN repose sur eux. Ce type de stabilité est plus grand que lorsqu'une entreprise utilise simplement une bibliothèque dans le cadre d'un système plus large. Dans ce cas, le logiciel *est* le système.

Deuxièmement, toute connaissance difficilement acquise sur leur installation, configuration et maintenance sera directement transférable le jour où vous déciderez de basculer ou de compléter votre infrastructure de cache avec un CDN, puisque ce sont les mêmes serveurs ! Dans le monde du développement logiciel, où tout change si vite, c'est toujours une bonne nouvelle.

C'est la même raison pour laquelle apprendre le cache HTTP est un bon pari, car il est pertinent dans de nombreux endroits différents. Et il est probable que cela reste ainsi pendant des décennies, nous verrons pourquoi à la fin de cet article.

Navigateurs, serveurs edge, serveurs proxy... c'est beaucoup d'intermédiaires de cache. Penser à tous ces caches en même temps peut être un peu accablant et difficile à visualiser. Heureusement pour nous, comme nous l'avons mentionné précédemment, tous ces caches parlent HTTP et se conforment à la même spécification.

En tant que serveurs proxy, ils agissent tous de manière transparente à la fois pour les clients et pour les serveurs. Les serveurs d'origine communiquent avec le proxy comme s'il s'agissait du client, et les navigateurs des utilisateurs finaux communiquent avec le proxy comme s'il s'agissait du serveur. Cela reste vrai même entre les serveurs proxy.

Ainsi, nous pouvons modéliser la réalité en considérant que toutes les infrastructures de cache sont équivalentes à une seule avec un proxy de cache en place.

Cela est mieux décrit par l'image suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/5GuIRyGlz1WcpwpckUPGHVzMQ9SKeMjt0g5E align="left")

Nous utiliserons cette simplification dans le reste de cette série d'articles. Cette abstraction est utile pour visualiser les mécanismes en jeu, mais elle vient avec certaines limitations. Mettre deux proxys l'un après l'autre peut avoir des [conséquences subtiles](https://community.akamai.com/customers/s/article/and-Beware-of-the-Age-header-too?language=en_US).

Jusqu'à présent, nous avons couvert beaucoup de terrain sans révéler quoi que ce soit sur les interactions détaillées entre un client et un serveur de cache. Le cache HTTP est un sujet complexe. Avant de passer aux véritables aspects techniques dans la partie 2, il y a un dernier aspect important qui doit être exploré.

### Le cache pour l'avenir

Avez-vous déjà dû attendre quelques *secondes* pour interagir avec une page web, ou pour voir quelque chose de significatif à l'écran ? Probablement. C'est en fait [pas improbable du tout](https://www.machmetrics.com/speed-blog/average-page-load-times-websites-2018/). Tout le monde a expérimenté le slow internet à un moment donné dans sa vie, même à la maison avec une connectivité fibre.

Des recherches UX passées ont en fait obtenu des [métriques effrayantes](https://www.nngroup.com/articles/response-times-3-important-limits/) à ce sujet. Des métriques qui sont restées les mêmes pendant plus de 40 ans, d'ailleurs, ce qui les rend peu susceptibles de changer dans un avenir proche. Leurs directives sont exprimées en termes de centaines de *millisecondes*, alors que nous sommes habitués à naviguer sur l'Internet et à attendre *plusieurs* *secondes*.

Alors pourquoi pensons-nous que le cache HTTP est pertinent aujourd'hui et le restera presque certainement pour les années à venir ?

Tout se résume à cette question de base : **pourquoi le web est-il si lent ?**

Cette question est sans aucun doute difficile, et un examen rigoureux nous mènerait trop loin et nous ferait perdre notre focus principal, qui est le cache HTTP. Cependant, si nous n'avons aucune idée de ce qui rend une page web lente, comment pouvons-nous être sûrs que le cache, malgré toutes ses vertus, est le bon outil pour le travail ?

Depuis sa conception, le web a certainement beaucoup changé. Les jours où les pages web consistaient en de simples fichiers HTML contenant principalement du texte et des hyperliens sont révolus.

De nos jours, de nombreux sites web sont étiquetés comme des applications web, car leur apparence et leur comportement ressemblent à ceux des applications de bureau. Mais malgré toutes les améliorations et innovations qui ont été faites au fil des ans, une chose est toujours restée la même : cela a toujours commencé par le téléchargement d'un fichier HTML.

Au fur et à mesure qu'il télécharge progressivement le HTML, le navigateur découvre toutes les autres ressources qui, combinées, donneront tout le code côté client qui est analysé et finalement, exécuté.

Dans le cas d'une SPA typique par exemple, le flux de requêtes continue. Lors de l'exécution, l'application commence à télécharger des données depuis le serveur, généralement sérialisées en JSON de nos jours, afin de rendre l'interface utilisateur. Chaque URL dans la charge utile JSON déclenchera, une fois référencée dans le code (elle n'a même pas besoin d'être ajoutée au DOM), un autre téléchargement afin qu'elle puisse être affichée à l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/Jfw5khEHRrGvCfKXH-TrrhzxeDjyDa3SzlQL align="left")

Ce modèle d'exécution, où tous les octets nécessaires à l'application pour faire son travail sont dispersés à différents endroits et doivent être téléchargés à chaque fois, est assez remarquable. Arguablement, c'est ce qui rend le web si unique dans le monde du développement logiciel.

Mais il y a un hic.

En effet, à ce jour, l'application web typique nécessite 75 requêtes et pèse 1,5 Mo, ce qui signifie que les navigateurs doivent initier beaucoup de requêtes de ~20 ko chacune. En d'autres termes, cela signifie qu'une application web typique est composée de nombreuses connexions de courte durée.

Et voici le hic : c'est l'exact opposé de ce pour quoi TCP est optimisé.

#### L'anatomie d'une requête web

En théorie, toutes ces 75 requêtes devraient passer par ces étapes :

* Résolution DNS
    
* Poignée de main TCP
    
* Poignée de main SSL
    
* Téléchargement de données contraint par le flux TCP et le contrôle de congestion
    

Parcourons chacune d'elles et tirons-en une conséquence contre-intuitive.

La résolution DNS est le processus de conversion d'un nom d'hôte lisible par l'homme tel que example.com en une adresse IP. Bien que le protocole DNS soit basé sur UDP plutôt que TCP, le voyage pour obtenir une adresse IP de nom d'hôte [peut être vraiment long](https://howdns.works), impliquant plusieurs serveurs DNS. Et il n'est pas rare que ces résolutions DNS prennent entre 50 et 250 millisecondes.

Ensuite, chaque requête doit initier une connexion TCP. HTTP a toujours eu besoin d'un protocole de transport fiable pour fonctionner. Si les octets ASCII représentant chaque requête HTTP devaient être livrés dans le désordre, une ligne d'état telle que

```typescript
GET /home.html HTTP/1.1
```

deviendrait :

```typescript
GTE /mohe.hmtl HTTP/1.1
```

et la requête n'aurait pas beaucoup de sens.

Afin de garantir l'ordre de livraison, TCP marque chaque octet des données de l'application avec un identifiant unique appelé numéro de séquence (SYN). Le problème est que ce nombre doit être choisi aléatoirement [pour des raisons de sécurité](https://tools.ietf.org/html/rfc7414#section-3.7).

Par conséquent, si un client demande une ressource, il ne peut pas le faire sans signaler au serveur son numéro de séquence initial (ISN). Ensuite, il doit attendre que le serveur accuse bonne réception de ce segment, avant de pouvoir envoyer des données d'application.

Eh bien, à moins que la requête ne soit sécurisée, ce qui est probablement le cas puisque [80%](https://httparchive.org/reports/state-of-the-web#pctHttps) des requêtes HTTP de nos jours sont en fait des requêtes HTTPS sécurisées. Ce sont des requêtes HTTP normales, sauf qu'elles sont chiffrées afin de garantir (au moins, jusqu'à ce jour) la confidentialité, l'intégrité et l'authenticité.

Pour y parvenir, le client et les serveurs doivent maintenant convenir d'une version du protocole TLS, sélectionner des fonctions cryptographiques, s'authentifier mutuellement en échangeant et en validant des certificats x509... pour pas moins de [~10](https://tools.ietf.org/html/rfc8446#section-4) messages de protocole qui peuvent être regroupés dans un minimum de 2 échanges TCP, et autant d'allers-retours.

Une fois la connexion établie et sécurisée, TCP peut enfin commencer à envoyer des segments transportant nos données d'application, telles que notre requête HTTP. Malheureusement pour nous, TCP nous empêche d'envoyer toutes nos données en une seule fois dans un seul lot de plusieurs segments.

Cette restriction est un mal nécessaire, afin que nous ne provoquions pas accidentellement un débordement de tampon sur le récepteur. Lorsqu'une application qui a initié une connexion demande à la socket TCP sous-jacente des données, TCP refusera de donner un morceau qui serait incomplet ou composé de morceaux plus petits non ordonnés. D'où la nécessité d'un tampon.

La façon dont cela fonctionne est que TCP envoie N segments dans le premier lot, et, si tous les segments ont été reçus par le serveur, enverra deux fois plus de segments (2N) dans le lot suivant, et ainsi de suite, conduisant à une croissance exponentielle. Ce mécanisme est communément connu sous le nom d'algorithme [slow-start](https://hpbn.co/building-blocks-of-tcp/#slow-start) et est l'un des deux seuls modes possibles dans lesquels TCP fonctionne, avec l'évitement de congestion.

Nous ne discuterons pas de l'évitement de congestion dans cette série. Mais s'il n'y avait qu'une seule chose à savoir, ce serait que une fois que TCP sent que le réseau sous-jacent peut être congestionné, le protocole commence à agir beaucoup plus prudemment. Prolongeant ainsi encore plus le temps nécessaire pour transmettre les données.

#### La conséquence

Avec toutes ces étapes en tête, faisons un simple calcul pour réaliser quelque chose d'important. Aux débuts du web, le paramètre N (connu sous le nom de fenêtre de congestion dans les termes de TCP) était égal à 1. Avec une telle fenêtre et une ressource moyenne de 20 ko, nous pouvons déterminer combien d'allers-retours sont nécessaires pour qu'une requête moyenne soit entièrement transmise.

En effet, dans des circonstances normales, la taille maximale du segment ([MSS](https://tools.ietf.org/html/rfc879)) est de 1460 octets. Cela équivaut à 20 000 / 1460 = 14 segments TCP. Lorsqu'ils sont dispatchés selon le schéma exponentiel que nous venons de décrire, cela équivaut à 4 allers-retours vers le serveur.

Maintenant, si nous approximons une requête DNS basée sur UDP à une requête TCP vers les serveurs d'origine, nous pouvons estimer un nombre total d'allers-retours (RT) qui nécessitent le démarrage d'une application web moderne :

* Requête DNS : ~1 RT
    
* Établissement de la connexion TCP : 1 RT
    
* Poignée de main SSL : 2 RT
    
* Téléchargement de la ressource : 4 RTT
    
* **Total : 8 RT**
    

75 requêtes qui nécessitent toutes 8 allers-retours chacune résultent en un total de 600 allers-retours vers le serveur. Un RTT typique entre l'Europe et les États-Unis est de 50 ms, ce qui nous donne la quantité de temps que l'information passe à circuler sur Internet lorsque nous demandons une application web typique : 30 secondes. Et cela pourrait être pire.

La page d'accueil d'Amazon, par exemple, une [MPA](https://blog.octo.com/a-la-decouverte-des-architectures-du-front-2-4-les-multiple-page-applications/) typique, pèse actuellement 6,3 Mo et nécessite 339 requêtes. Cela se traduirait par un temps de chargement de page saillant de 2 minutes et 15 secondes. À titre d'exercice, essayez de faire de même pour la page d'accueil de Facebook Messenger, une [SPA](https://blog.octo.com/a-la-decouverte-des-architectures-du-front-3-4-les-single-page-applications/) typique.

Comment interpréter ce nombre ? Ce serait le temps de chargement réel de la page si chaque ressource devait être téléchargée séquentiellement, la congestion initiale de TCP était réduite à sa valeur minimale de 1, et si les requêtes DNS, TCP et les poignées de main SSL devaient être refaites à chaque fois. Le web serait un endroit très différent, c'est sûr.

Heureusement, de nombreuses améliorations ont été apportées au fil des ans. Les résolutions DNS sont mises en cache à différents endroits, les résultats des poignées de main TLS sont réutilisés.

Les connexions TCP ont été autorisées [à être persistantes](https://tools.ietf.org/html/rfc2616#page-44) entre plusieurs requêtes, évitant le coût de l'établissement de la connexion et du slow-start à chaque requête.

La fenêtre de congestion initiale de TCP a été augmentée deux fois, passant de 1 à [4](https://tools.ietf.org/html/rfc3390) et plus récemment, à [10](https://tools.ietf.org/html/rfc6928). Les navigateurs ont commencé à ouvrir des connexions parallèles (6) ainsi que certaines stratégies vraiment [avancées](https://www.igvita.com/posa/high-performance-networking-in-google-chrome/#predictor) pour accélérer les temps de chargement des pages.

Certaines [propositions](https://tools.ietf.org/html/rfc7413) ont tenté de se libérer de l'établissement de la connexion, bien qu'aucune d'entre elles ne soit largement implémentée.

Certains CDN ont même acquis des [algorithmes brevetés](https://developer.akamai.com/legacy/learn/Optimization/TCP_Optimizations.html) pour ajuster certains aspects de TCP tels que l'évitement de congestion, toujours pour la même raison : accélérer la livraison.

Quelle conséquence pouvons-nous tirer de tous ces allers-retours entre le navigateur et les serveurs d'origine ?

**Que la bande passante a cessé d'être le goulot d'étranglement** [**il y a de nombreuses années**](https://docs.google.com/a/chromium.org/viewer?a=v&pid=sites&srcid=Y2hyb21pdW0ub3JnfGRldnxneDoxMzcyOWI1N2I4YzI3NzE2)**.**

Cela est quelque peu contre-intuitif pour la plupart d'entre nous, car la bande passante a incarné la vitesse de navigation pendant des années. Après tout, elle a exactement la dimension d'une vitesse, des bits par unité de temps, et c'est la seule chose que les FAI annoncent lorsqu'ils essaient de nous attirer pour devenir leurs clients.

De plus, naviguer sur le 3G est clairement plus lent que sur le 4G. Mais c'est parce que le seuil auquel la bande passante cesse d'être le goulot d'étranglement est de 5 Mb/s, et le 3G atteint au maximum 2 Mb/s dans des conditions idéales !

Et si les technologies sans fil telles que le Wi-Fi ou le 5G sont effectivement plus lentes que leur homologue filaire d'une certaine sorte, c'est aussi parce que dans les systèmes sans fil, les pertes de paquets causées par les interférences sont monnaie courante, rendant ainsi la latence beaucoup plus élevée et volatile.

La dernière version du protocole HTTP, HTTP/2, nommée H2, était une continuation du protocole SPDY qui lui-même avait été initialement conçu suivant cette observation très précise : la bande passante n'a plus beaucoup d'importance. La latence, oui. Mais la latence est fondamentalement une fonction de deux choses : la vitesse de la lumière dans la fibre optique, et la distance entre les clients et les serveurs.

Des [recherches actives](https://www.extremetech.com/computing/151498-researchers-create-fiber-network-that-operates-at-99-7-speed-of-light-smashes-speed-and-latency-records) pour augmenter la vitesse de la lumière dans la fibre optique ont déjà été menées, mais elles ne nous ont menés que jusqu'à un certain point. Dans la plupart des déploiements, la lumière voyage déjà à 60 % de sa limite théorique maximale.

Mais même si nous devions atteindre 99 %, cela n'aurait un impact significatif sur votre site web que s'il se charge déjà en quelques secondes au maximum. S'il se charge en plus de 5 secondes, même si l'augmentation de performance serait perceptible, il semblerait toujours lent.

Par conséquent, il nous reste un choix évident : **réduire la distance**.

Et la seule façon d'y parvenir est en tirant parti des navigateurs et des réseaux de diffusion de contenu avec le cache HTTP.

### Conclusion

Tout au long de cet article, nous avons soutenu que le cache HTTP est l'un des moyens, sinon le plus efficace, d'améliorer la performance de votre application web. Et comme de nombreuses études continuent de le souligner, le temps de chargement des pages est un sujet important qui peut être directement traduit en satisfaction des utilisateurs et, en fin de compte, en rentabilité.

Nous avons vu que le cache peut se produire pratiquement partout, du navigateur, au CDN, en passant par les serveurs proxy privés situés juste devant vos serveurs d'origine. Mais aussi que, contrairement à de nombreuses décisions de performance, il peut être complètement externalisé en dehors de la base de code principale, ce qui est à la fois précieux et pratique.

Enfin, nous avons examiné de plus près l'anatomie d'une application web moderne, pour comprendre pourquoi la latence est le nouveau goulot d'étranglement, rendant le cache pertinent aujourd'hui et pour les années à venir, même avec le [déploiement régulier de H2](https://httparchive.org/reports/state-of-the-web#h2).

Dans le prochain article de cette série, nous plongerons en profondeur dans le *Comment*.

En un sens, cette première partie n'était qu'un échauffement ! Nous apprendrons comment tout cela fonctionne réellement : fraîcheur des ressources, révalidation, représentations, en-têtes de contrôle de cache... et bien plus encore !

Restez à l'écoute !

#### Pour aller plus loin :

Ilya Grigorik High Performance Browser Applications (un must read) :  
[https://hpbn.co/](https://hpbn.co/)

Mike Belshe paper qui a servi de base au protocole SPDY : [https://docs.google.com/a/chromium.org/viewer?a=v&pid=sites&srcid=Y2hyb21pdW0ub3JnfGRldnxneDoxMzcyOWI1N2I4YzI3NzE2](https://docs.google.com/a/chromium.org/viewer?a=v&pid=sites&srcid=Y2hyb21pdW0ub3JnfGRldnxneDoxMzcyOWI1N2I4YzI3NzE2)

Blogs actifs de CDN avec des tonnes de grands articles :  
[https://www.fastly.com/blog](https://www.fastly.com/blog)  
https://blogs.akamai.com/web-performance/