---
title: Arrêtez d'appeler PostgREST « MAGIQUE » !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-18T20:01:07.000Z'
originalURL: https://freecodecamp.org/news/stop-calling-postgrest-magic-8f3e1d5e5dd1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yj04j1w-TajB2vgwbWBHnQ.png
tags:
- name: database
  slug: database
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Arrêtez d'appeler PostgREST « MAGIQUE » !
seo_desc: 'By Ruslan Talpă

  While it’s flattering for developers to have “magic” associated with their work,
  it might be damaging to the adoption of PostgREST. Magic means unknown and people
  fear the unknown. Let’s take 10 minutes to understand how it works inte...'
---

Par Ruslan Talpă

Bien que ce soit flatteur pour les développeurs d'avoir le terme « magique » associé à leur travail, cela pourrait nuire à l'adoption de [PostgREST](https://github.com/begriffs/postgrest). La magie signifie l'inconnu et les gens craignent l'inconnu. Prenons 10 minutes pour comprendre comment cela fonctionne en interne.

J'ai [commencé à contribuer](https://github.com/begriffs/postgrest/graphs/contributors?from=2015-08-22&to=2017-06-27&type=a) au cœur de PostgREST il y a 2 ans. Depuis, j'ai vérifié ce que les gens en disent. Il y a deux camps. Les fans inconditionnels qui l'appellent « magique » et sont prêts à s'en prendre aux non-croyants. Et puis il y a les sceptiques.

Ce récit s'adresse au camp des sceptiques. Il découle du fait que les gens ne comprennent pas comment PostgREST fonctionne !

Tout est simple, et beau.

### Qu'y a-t-il dans une URL (REST) ?

Prenons cet exemple

```
GET /items/1
```

Si vous enlevez tout, comme l'authentification et l'autorisation, l'essence qui reste est celle-ci

```
SELECT * FROM items WHERE id=1
```

PostgREST prend une requête HTTP, la regarde, la traduit en SQL et l'exécute. C'est presque tout ce qu'il y a à faire. C'est une grande fonction pure. J'espère que je ne me ferai pas crucifier par les gens de Haskell pour avoir abusé de la notation et ignoré qu'il y a en réalité des IO en cours.

```
postgrest :: Schema -> HTTP -> SQL
```

Voici un exemple un peu plus compliqué :

```
GET /items?select=id,name&id=gt.10&order=name
```

est traduit par

```
SELECT id, name FROM items WHERE id > 10 ORDER BY name
```

### Les trois ingrédients magiques ✨

Il y a trois concepts fondamentaux sur lesquels PostgREST est construit, tout le reste n'est que des clochettes et des sifflets. Si vous les comprenez, vous comprenez PostgREST.

#### Encodage JSON

La première idée brillante que [Joe Nelson](https://github.com/begriffs) a eue a été de reconnaître que PostgreSQL peut encoder la réponse en JSON. Vous pourriez vous demander : « Pourquoi voudrait-on faire cela, mettre plus de charge sur le composant qui est le plus difficile à mettre à l'échelle ? »

Eh bien, voici les raisons.

L'encodeur JSON de PostgreSQL est rapide, il est rapide en C. Plus votre réponse est grande, plus le gain est important. Il peut être 2x/10x plus rapide que [ActiveRecord](https://dockyard.com/blog/2014/05/27/avoid-rails-when-generating-json-responses-with-postgresql) ou même 160x pour les grandes réponses.

Réfléchissons un instant. Quelles sont les implications de faire en sorte que la base de données retourne la réponse finale, en plus de lui faire faire plus de travail ?

Tout ce qui se trouve devant la base de données n'a plus besoin de désérialiser la réponse provenant de la base de données, et de la transformer en représentation interne du langage pour ces données. Ensuite, après que les données sont en mémoire, il n'est pas nécessaire de les resérialiser en JSON. Cela signifie que sur le chemin de sortie, votre code n'a rien à faire, il suffit de transmettre ce qu'il reçoit de la base de données.

Nous avons déplacé une partie de la charge vers la base de données depuis le code de l'application. Ce n'est rien pour le puissant PostgreSQL, ce n'est pas là que se trouve le travail lourd. Si nous regardons l'ensemble du système, nous avons réduit la quantité totale de travail à faire en supprimant une étape de sérialisation/désérialisation. C'est l'un des secrets de la rapidité de PostgREST. Il laisse le grand faire son travail.

Regardons à quoi cela ressemble réellement en SQL. Cette requête est similaire à celles que PostgREST génère.

```
WITH essence AS (  SELECT id, name FROM items WHERE id > 10 ORDER BY name)SELECT   coalesce(    array_to_json(array_agg(row_to_json(response))),    '[]'  )::character varying AS BODYFROM (SELECT * FROM essence) response
```

Nous avons enveloppé la requête `essence`. À l'autre extrémité, nous obtenons notre résultat sous forme d'une seule ligne avec une colonne appelée `BODY` qui contient la réponse JSON. Facile !

#### Authentification / Autorisation

C'est la partie avec laquelle la plupart des nouveaux arrivants ont des difficultés lorsqu'ils rencontrent PostgREST pour la première fois. Ils ont la question (parfaitement naturelle) : « Comment PostgREST implémente-t-il l'authentification/autorisation ? ».

La réponse courte est, **il ne le fait pas**.

Encore une fois, l'une des idées brillantes de Joe, et je dirais même qu'elle est plus fondamentale que l'encodage JSON.

PostgreSQL dispose d'un système de [rôles](https://www.postgresql.org/docs/current/static/user-manag.html) riche. En conjunction avec des fonctionnalités telles que les vues et la [Sécurité au Niveau des Lignes](https://www.postgresql.org/docs/9.6/static/ddl-rowsecurity.html) (RLS), vous pouvez avoir un contrôle fin sur l'accès à vos données jusqu'à une cellule individuelle. Pourtant, les gens traitent leurs bases de données comme des « magasins de données stupides ». Et ce qui est encore pire, ils s'y connectent en utilisant des rôles avec des privilèges d'administrateur.

Quel serait l'intérêt d'une attaque par injection SQL si le rôle avec lequel l'application se connecte à la base de données n'a des privilèges que sur des tables et des lignes spécifiques ? Au pire, l'attaquant supprimerait ses propres données. Mais je m'égare...

Lorsque PostgREST se connecte pour la première fois à la base de données, il utilise un rôle que nous appelons généralement `authenticator`. Ce rôle n'a aucun privilège attaché à part la capacité de se connecter.

Chaque fois qu'une requête authentifiée arrive, et qu'il y a un en-tête `Authorization` contenant un jeton JWT, PostgREST décodera le jeton, vérifiera qu'il est valide en utilisant la clé secrète, et regardera sa charge utile pour un champ particulier appelé `role`. Supposons que `role` ait la valeur `alice`.

Cela signifie que cette requête doit être exécutée avec les privilèges de `alice`. Pour ce faire, nous utilisons un petit tour de PostgreSQL. Vous pouvez **changer** l'utilisateur actuel, un peu comme faire `sudo alice`. Et encore mieux, vous pouvez le faire dans le contexte d'une transaction afin qu'il n'y ait aucune chance qu'une requête interfère avec une autre. Nous ne créons pas de nouvelle connexion à la base de données, cela se produit dans la même connexion. Et bien que `alice` soit un rôle de base de données, il n'a pas de privilèges de connexion.

Voici l'ordre dans lequel les choses se passent :

```
BEGIN;SET LOCAL role TO 'alice';-- la requête principale va iciCOMMIT;
```

Cela ne signifie pas que PostgREST passe à ce qu'il veut. Pour que cela fonctionne, vous devez explicitement dire que le rôle `authenticator` a le droit d'assumer le rôle `alice` par :

```
GRANT alice TO authenticator;
```

Ainsi, PostgREST a acquis la capacité de faire de l'autorisation en exploitant le système de rôles de la base de données sous-jacente. Les implications et les avantages de cette approche sont énormes.

Le code de PostgREST reste petit et simple. Vous pouvez déclarer les privilèges pour chaque utilisateur en utilisant SQL sans avoir de code impératif laid partout. Et, peu importe quel code futur accède à la base de données, les règles sont appliquées de manière cohérente.

Il y a aussi un autre grand avantage qui n'est pas immédiatement évident.

Dans la manière traditionnelle de construire des API, lorsqu'une requête arrive, vous commencez à vérifier si l'utilisateur actuel a le droit d'accéder à cette information. Cela signifie des requêtes supplémentaires. Ces types de requêtes jouent un grand rôle dans la latence globale de la requête, et la charge sur la base de données. Cela donne l'impression que les bases de données sont lentes et ne s'adaptent pas très bien.

En donnant à PostgreSQL une vue complète de qui émet la requête (rôle), quels sont ses privilèges (autorisations) et ses restrictions (RLS), le planificateur de requêtes peut faire un bien meilleur travail, utiliser tous les index et même devenir plus rapide avec le temps.

La première objection soulevée est que l'on aurait besoin d'un rôle de base de données pour chaque utilisateur de l'application et que ce n'est pas un très bon design. Ils auraient raison, mais ce n'est pas ce que PostgREST vous demande de faire. Vous pouvez utiliser les rôles de base de données pour définir des groupes d'utilisateurs (admin, employé, client) et ensuite utiliser RLS pour spécifier des [règles utilisateur](https://blog.2ndquadrant.com/application-users-vs-row-level-security/) basées sur leur nom d'utilisateur, leur identifiant ou leur email.

#### Intégration des ressources

Vous pourriez avoir l'impression que bien que PostgREST ait une solution agréable pour l'authentification et l'exposition des points de terminaison REST, ce ne sont que vos capacités CRUD de base. Et cela ne suffit pas pour une API moderne. Après tout, c'est pourquoi nous avons des choses comme GraphQL.

Vous avez raison, si tout ce qu'il faisait était le CRUD de base, alors ce serait un bon outil pour le prototypage ou les projets simples. Mais PostgREST a un dernier tour dans sa manche, et je suis fier d'appeler cela ma plus grande [contribution](https://github.com/begriffs/postgrest/issues/218). Le tour est le paramètre `&select=`. Il ne permet pas seulement de spécifier les colonnes que vous voulez retourner de votre table, mais vous pouvez aussi demander des ressources liées :

```
GET /items?select=id,name,subitems(id,name)
```

Si vous remplacez `()` par `{}` et que vous plissez un peu les yeux, vous pouvez presque voir GraphQL. L'interface de PostgREST est comparable en pouvoirs expressifs à GraphQL lorsqu'il s'agit de récupérer des données de votre base de données.

Il nous a fallu une réécriture complète du [cœur](https://github.com/begriffs/postgrest/pull/295) et ensuite une année pour rendre l'interface uniforme pour tous les chemins. Mais nous y sommes enfin arrivés.

Alors, comment cela fonctionne-t-il ?

Au premier démarrage, PostgREST exécute un ensemble de [requêtes](https://github.com/begriffs/postgrest/blob/master/src/PostgREST/DbStructure.hs) sur votre base de données. Cela permet de comprendre quelles entités y vivent et les relations entre elles, en fonction des clés étrangères que vous avez définies. Après cela, chaque fois que vous dites `subitems(...)` il sait que la table `items` est liée à la table `subitems` par une clé étrangère appelée `item_id`. Sur la base de ces informations, il sait comment générer la requête de jointure correcte. Cela fonctionne de manière similaire pour les relations parent et plusieurs-à-plusieurs.

Une requête simplifiée (essence) de cela ressemble à ceci

```
SELECT    items.id, items.name,    COALESCE(         (            SELECT array_to_json(array_agg(row_to_json(subitems)))            FROM (                SELECT subitems.id, subitems.name                FROM subitems                WHERE subitems.item_id = items.id             ) subitems         ),         '[]'    ) AS subitemsFROM items
```

Au premier regard, on pourrait penser que cela est très inefficace car il semble faire une sous-sélection pour chaque ligne d'élément, mais nous utilisons PostgreSQL et son planificateur de requêtes impressionnant, il sait ce que vous demandez réellement et il vous couvre. N'ayez pas peur des jointures et des sous-sélections.

Une fois, après avoir montré cette requête et expliqué que le planificateur de requêtes sait comment la gérer correctement, j'ai reçu une réponse comme

_« Ha-ha, oui, vous comptez sur la miséricorde d'un optimiseur de requêtes. »_

Je prendrai cela n'importe quel jour, merci beaucoup !

Je compterai sur un logiciel développé sur une période de [20 ans](https://en.wikipedia.org/wiki/PostgreSQL#History) par des personnes avec des [PHD](https://www.postgresql.org/community/contributors/). Je n'ai pas l'arrogance de penser que d'une manière ou d'une autre ma boucle `for` est une technologie supérieure à l'optimiseur de requêtes [PostgreSQL](https://momjian.us/main/writings/pgsql/optimizer.pdf).

### Mais pourquoi (avons-nous besoin de PostgREST) ? ?

Maintenant, si vous avez suivi et compris comment les choses s'emboîtent, vous pourriez penser :

> _« Tout ce que fait PostgREST est de générer une requête SQL, de l'envelopper dans une transaction avec un certain contexte et de l'exécuter. Pourquoi ne pas sauter l'intermédiaire, écrire un script qui prend du SQL brut en entrée et fait la même chose ? »_

Vous pourriez faire cela. En effet, personne ne pourrait accéder aux donnéesqu'ils ne sont pas censés voir et les choses iront bien pendant un certain temps. Et puis, une nuit, vous vous réveillerez à cause d'une alerte indiquant que votre base de données est hors service. Après une certaine investigation, vous trouverez comme coupable cette requête :

```
SELECT   crypt(    encode(digest(gen_random_bytes(1024), 'sha512'), 'base64'),       gen_salt('bf', 20)  )FROM   generate_series(1, 1000000)
```

WT#!

Ce qui est pire, je n'ai besoin d'aucun privilège sur aucune table pour exécuter cette requête !

Pour tout son pouvoir, PostgreSQL n'a pas été conçu pour dévier les attaques par déni de service (DoS). C'est là que PostgREST vous sauve. Il trouve un équilibre entre l'exposition de beaucoup de flexibilité SQL aux clients pour être utile, mais limite cette puissance pour prévenir les requêtes malveillantes. Il ne permettra pas les jointures **à volonté**, seulement celles définies par les clés étrangères qui devraient avoir les index appropriés.

### Faire une chose bien ?

Alors vous êtes convaincu ! Vous avez téléchargé le binaire, vous l'avez pointé vers votre base de données et BAM ! Vous avez une API REST ! Les choses avancent bien. La plupart de vos besoins en API sont couverts. Ensuite, vous arrivez à quelques derniers détails à implémenter et soudain vous vous arrêtez !

« Comment puis-je envoyer un email avec cette chose ? Comment puis-je appeler cette API tierce lorsqu'un utilisateur se connecte ? Comment puis-je écrire mes tests ?

Mince, je savais que c'était une mauvaise idée ! Hé, les développeurs de PostgREST, pouvez-vous m'aider et implémenter cette fonctionnalité ? »

Et la réponse que vous obtiendrez probablement est « Vous n'en aurez pas besoin » (YAGNI). Ce n'est pas parce que nous sommes des #$%#. C'est parce que PostgREST est un composant de votre stack, ce n'est pas « la stack ». Il a un seul travail et il essaie de le faire bien. À lui seul, il ne remplacera pas complètement votre framework MVC backend préféré. Mais avec un peu d'aide d'amis comme PostgreSQL, OpenResty, RabbitMQ, il le fera pour vous et avec de grands résultats. Jetez un coup d'œil au [Starter Kit](https://github.com/subzerocloud/postgrest-starter-kit) pour voir comment il s'intègre dans la stack.

Vous n'écrirez plus d'API, vous les définirez et les configurerez.

### Au-delà de REST ?

Récemment, la communauté front-end a été prise d'assaut par la frénésie React & GraphQL, et pour une bonne raison. Il pourrait sembler que REST sera bientôt laissé de côté, emportant PostgREST avec lui. Pourtant, les idées ici transcendent REST, c'est le protocole que vous utilisez pour parler à PostgREST.

Vous avez peut-être entendu parler de [PostGraphQL](https://github.com/postgraphql/postgraphql). Il est basé sur les mêmes idées avec une implémentation complètement différente. L'[auteur](https://github.com/calebmer) est également l'un des principaux contributeurs de PostgREST. Inspiré par PostgREST et les discussions sur GraphQL au sein de la communauté PostgREST, il a décidé d'y mettre sa propre touche.

J'ai décidé de prendre une route différente. J'ai utilisé PostgREST et construit GraphQL par-dessus, au lieu de réimplémenter la même logique dans un autre langage. Après tout, c'était mon objectif dès le [début](https://github.com/begriffs/postgrest/issues/218). Développer les capacités de PostgREST à un point où il peut supporter GraphQL.

Cela a été un long voyage pour développer mon idée originale pour [subZero](https://subzero.cloud/), une API GraphQL & REST pour votre base de données. Mais j'ai beaucoup appris en cours de route.

Essayez subZero. J'espère que le [logiciel](https://github.com/subzerocloud) supplémentaire que nous avons développé en cours de route vous sera utile.

Profitez !

Si vous avez des questions sur PostgREST ou subZero, vous pouvez toujours me joindre par [email](https://github.com/ruslantalpa) ou [slack](https://slack.subzero.cloud/).