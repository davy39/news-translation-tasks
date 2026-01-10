---
title: Qu'est-ce que l'UTF-8 ? Tutoriel sur l'encodage des caractères UTF-8
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2022-04-03T04:01:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-utf-8-character-encoding
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/brett-jordan-M9NVqELEtHU-unsplash--1-.jpg
tags:
- name: HTML
  slug: html
- name: typography
  slug: typography
seo_title: Qu'est-ce que l'UTF-8 ? Tutoriel sur l'encodage des caractères UTF-8
seo_desc: 'UTF-8 is a character encoding system. It lets you represent characters
  as ASCII text, while still allowing for international characters, such as Chinese
  characters.

  As of the mid 2020s, UTF-8 is one of the most popular encoding systems.

  To start usin...'
---

L'UTF-8 est un système d'encodage de caractères. Il vous permet de représenter des caractères sous forme de texte ASCII, tout en permettant l'utilisation de caractères internationaux, tels que les caractères chinois.

Depuis le milieu des années 2020, l'UTF-8 est l'un des systèmes d'encodage les plus populaires.

Pour commencer à utiliser l'UTF-8, vous voudrez d'abord vous familiariser avec le jeu de caractères ASCII de base.

### Qu'est-ce que le jeu de caractères ASCII ?

L'ASCII utilise des points de code de 7 bits pour représenter 128 caractères différents. Ces points de code sont divisés en 95 caractères imprimables, qui comprennent les 26 lettres de l'alphabet anglais (A à Z, en majuscules et minuscules), les 10 chiffres (0 à 9), ainsi qu'une variété de ponctuation et d'autres symboles.

Il existe également 33 caractères non imprimables, qui incluent des caractères de contrôle tels que le retour chariot et le saut de ligne, ainsi que divers autres caractères utilisés pour des éléments tels que la mise en forme du texte.

### UTF-8 vs ASCII – Quelle est la différence ?

L'UTF-8 étend le jeu de caractères ASCII pour utiliser des points de code de 8 bits, ce qui permet d'utiliser jusqu'à 256 caractères différents.

Cela signifie que l'UTF-8 peut représenter tous les caractères ASCII imprimables, ainsi que les caractères non imprimables.

L'UTF-8 inclut également une variété de caractères internationaux supplémentaires, tels que les caractères chinois et les caractères arabes.

## Comment utiliser l'UTF-8 dans vos pages Web – Exemple HTML UTF-8

Et maintenant, la partie facile. Vous n'avez pas réellement besoin de savoir comment cela fonctionne (bien que je vous l'expliquerai dans un instant). Vous pouvez configurer l'encodage des caractères UTF-8 dans votre code HTML avec une seule ligne de HTML située dans la section `<head>` de votre code :

```html
<!DOCTYPE html>
<html>
<head>
    <!-- Définir l'encodage des caractères en utf-8 -->
    <meta charset="utf-8">
</head>
</html>

```

Ceci étant dit, laissez-moi vous expliquer comment l'UTF-8 fonctionne et pourquoi c'est un schéma d'encodage si brillant.

## Comment fonctionne l'encodage UTF-8 et combien d'espace de stockage chaque caractère utilise

Lors de la représentation de caractères en UTF-8, chaque point de code est représenté par une séquence d'un ou plusieurs octets. Le nombre d'octets utilisés dépend du point de code représenté par le caractère. Voici une ventilation de la plage d'utilisation :

* les points de code dans la plage ASCII (0-127) sont représentés par un seul octet
* les points de code dans la plage (128-2047) sont représentés par deux octets
* les points de code dans la plage (2048-65535) sont représentés par trois octets
* et les points de code dans la plage (65536-1114111) sont représentés par quatre octets. (Cela peut sembler être beaucoup de caractères possibles, mais gardez à l'esprit que rien qu'en chinois, il existe des centaines de milliers de caractères.)

Le premier octet d'une séquence UTF-8 est appelé l'"octet de tête" (leader byte). L'octet de tête fournit des informations sur le nombre d'octets présents dans la séquence et sur la valeur du point de code du caractère.

L'octet de tête pour une séquence d'un seul octet est toujours dans la plage (0-127). L'octet de tête pour une séquence de deux octets est dans la plage (194-223). L'octet de tête pour une séquence de trois octets est dans la plage (224-239). Et l'octet de tête pour une séquence de quatre octets est dans la plage (240-247).

Les octets restants dans la séquence sont appelés des "octets de queue" (trailing bytes). Les octets de queue pour une séquence de deux octets sont dans la plage (128-191). Les octets de queue pour une séquence de trois octets sont dans la plage (128-191). Et les octets de queue pour une séquence de quatre octets sont dans la plage (128-191).

Vous pouvez calculer la valeur du point de code d'un caractère en examinant l'octet de tête et les octets de queue. Pour une séquence d'un seul octet, la valeur du point de code est égale à la valeur de l'octet de tête.

Pour une séquence de deux octets, la valeur du point de code est égale à ((octet de tête - 194) * 64) + (octet de queue - 128).

Pour une séquence de trois octets, la valeur du point de code est égale à ((octet de tête - 224) * 4096) + ((octet de queue1 - 128) * 64) + (octet de queue2 - 128).

Pour une séquence de quatre octets, la valeur du point de code est égale à ((octet de tête - 240) * 262144) + ((octet de queue1 - 128) * 4096) + ((octet de queue2 - 128) * 64) + (octet de queue3 - 128).

## L'UTF-8 est un choix judicieux pour l'encodage

Encore une fois, l'UTF-8 est un système d'encodage extrêmement efficace. Il peut représenter une large gamme de caractères tout en restant compatible avec l'ASCII. Cela en fait un choix judicieux pour une utilisation dans les logiciels internationalisés.

J'espère que vous avez trouvé cela utile. Si vous voulez en apprendre davantage sur la programmation et la technologie, essayez le [programme de codage fondamental de freeCodeCamp](https://www.freecodecamp.org/learn). C'est gratuit.