---
title: Comment mettre à jour des objets à l'intérieur de tableaux JSONB avec PostgreSQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-15T15:48:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-update-objects-inside-jsonb-arrays-with-postgresql-5c4e03be256a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*TyYEPUBI96D1NDh4
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: SQL
  slug: sql
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment mettre à jour des objets à l'intérieur de tableaux JSONB avec PostgreSQL
seo_desc: 'By Leandro Cesquini Pereira

  How to update a specific value on a JSONB array

  Let’s say you decided to store data in the database as json or jsonb and discovered
  that you just created new problems for yourself that you didn’t have before. You’re
  not al...'
---

Par Leandro Cesquini Pereira

### Comment mettre à jour une valeur spécifique dans un tableau JSONB

Disons que vous avez décidé de stocker des données dans la base de données sous forme de json ou jsonb et que vous avez découvert que vous veniez de créer de nouveaux problèmes pour vous-même que vous n'aviez pas avant. Vous n'êtes pas seul.

JSONB est un outil puissant, mais il a un coût car vous devez adapter la manière dont vous interrogez et manipulez les données.

Et il n'est pas rare de charger l'objet jsonb entier en mémoire, de le transformer en utilisant votre langage de programmation préféré, puis de le sauvegarder à nouveau dans la base de données. Mais vous venez de créer un autre problème : des goulots d'étranglement de performance et un gaspillage de ressources.

Dans cet article, voyons comment mettre à jour une valeur spécifique d'un objet à l'intérieur d'un tableau avec une seule requête.

**TL;DR** : la requête finale se trouve à la fin de l'article, et vous pouvez consulter un exemple en direct sur [DB Fiddle](https://www.db-fiddle.com/f/e8aeGk7cRNYnpjsqi1ncrs/1) pour copier-coller et jouer avec.

Supposons que vous implémentez un écran client pour stocker des contacts dynamiques pour chaque client. Vous avez alors l'idée de stocker les contacts sous forme de colonne JSONB car ils sont dynamiques, et ainsi utiliser une structure de données non relationnelle a du sens.

Vous créez ensuite une table customers avec une colonne contacts JSONB et y insérez des données :

![Image](https://cdn-media-1.freecodecamp.org/images/gfE87Cd6J1Jg8NG-SoiqfVGz1J8JN8rC6Fnj)

Plutôt facile, non ? Mais comment pouvez-vous mettre à jour un contact spécifique pour un client spécifique ? Comment changer l'email de Jimi ou le téléphone de Janis ? ?

Heureusement, PostgreSQL est votre ami et fournit la fonction _jsonb_set_ :

_jsonb_set(target jsonb, path text[], new_value jsonb[, create_missing boolean])_

Étant donné une colonne jsonb, vous pouvez définir une nouvelle valeur sur le chemin spécifié :

![Image](https://cdn-media-1.freecodecamp.org/images/NsMb3UL3fPutaYFB4ebdOGq7rFVCqjJmiJPd)
_Référence : [Fonctions Json de PostgreSQL](https://www.postgresql.org/docs/9.5/functions-json.html" rel="noopener" target="_blank" title=")_

Les sélections ci-dessus retourneront :

```
[{"type": "phone", "value": "+1–202–555–0105"}, {"type": "email", "value": "jimi.hendrix@gmail.com"}]

[{"type": "email", "value": "janis.joplin@gmail.com"}]
```

Pour changer l'email de Jimi dans la liste des contacts, vous indiquez le chemin "**1, value**" qui signifie le deuxième objet du tableau (en commençant à 0) et la clé **value**. C'est le _path_. La même chose s'applique pour changer l'email de Janis, mais son objet email est à l'index 0.

Vous pensez peut-être : je dois simplement utiliser jsonb_set dans une instruction de mise à jour et c'est tout ? C'est l'idée, mais ce n'est pas encore suffisant.

Le problème avec les données non relationnelles est qu'elles sont dynamiques. Eh bien, c'est l'une des raisons d'utiliser JSONB, mais cela apporte un problème : voyez que l'objet email de Jimi est à l'index 1 et l'objet email de Janis est à l'index 0 dans le tableau, et un autre client pourrait avoir un tableau très différent avec des index différents. Alors, comment pouvez-vous découvrir l'index de chaque type de contact ? ?

La réponse est de trier les éléments du tableau et d'obtenir son index :

![Image](https://cdn-media-1.freecodecamp.org/images/KoTlVXRd73a57XhyrIfVj0QnZfqRK8KguWoZ)

Cette requête retourne **1**, qui est l'_index_ de l'_objet email (type email)_ à l'intérieur du tableau des contacts du client Jimi.

Nous avons maintenant toutes les pièces du puzzle : nous savons comment mettre à jour une valeur jsonb et comment découvrir l'index de l'objet à mettre à jour.

La seule étape restante est la mise à jour elle-même. En mettant tout ensemble, nous avons :

![Image](https://cdn-media-1.freecodecamp.org/images/ysGG240RTX8t9rLeuMv4KdubaDVpzVMfjnEb)

La partie la plus importante de cette requête est le bloc _with_. C'est une ressource puissante, mais pour cet exemple, vous pouvez le considérer comme un "moyen de stocker une variable" qui est le _path_ du contact que vous devez mettre à jour, qui sera dynamique en fonction de l'enregistrement.

Permettez-moi d'expliquer un peu cette partie :

```
('{'||index-1||',value}')::text[] as path
```

Il construit simplement le chemin comme _'{1, value}'_, mais nous devons le convertir en _text[]_ car c'est le type attendu par la fonction _jsonb_path_.

#### Conclusion

JSONB est un outil formidable et précieux pour résoudre de nombreux problèmes. Mais gardez à l'esprit que vous devez également interroger et mettre à jour ce type de données. Cela entraîne un coût que vous devez prendre en compte lors du choix des outils que vous utilisez.

_Note de bas de page : cette solution est issue d'une session de programmation en binôme avec [Lucas Cegatti](https://www.freecodecamp.org/news/how-to-update-objects-inside-jsonb-arrays-with-postgresql-5c4e03be256a/undefined)._

_Vous cherchez une entreprise créative pour implémenter votre prochaine idée ? Consultez [LNA Systems](https://lnasystems.com.br) et parlons-en._