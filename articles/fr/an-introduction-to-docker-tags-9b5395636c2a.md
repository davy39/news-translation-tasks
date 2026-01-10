---
title: Une introduction rapide aux tags Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-12T18:22:09.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-docker-tags-9b5395636c2a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*KBn45TeUMJZSbz9n.png
tags:
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Une introduction rapide aux tags Docker
seo_desc: 'By Shubheksha Jalan

  If you’ve worked with Docker even for a little while, I bet you’ve come across tags.
  They often look like “my_image_name:1” where the part after the colon is known as
  a tag. The tag is not always specified when tagging images, but...'
---

Par Shubheksha Jalan

Si vous avez travaillé avec Docker ne serait-ce qu'un peu, je parie que vous avez déjà rencontré des tags. Ils ressemblent souvent à « my_image_name:1 » où la partie après les deux points est connue sous le nom de tag. Le tag n'est pas toujours spécifié lors du taggage des images, mais nous y reviendrons plus tard.

Depuis que j'ai commencé à utiliser Docker, j'ai été très confus à propos des tags. La documentation ne les explique pas très bien, et il n'y a vraiment pas d'explications approfondies sur le sujet. C'est pourquoi j'ai décidé d'écrire cet article.

### Qu'est-ce que les tags Docker ?

Alors, que sont exactement les tags Docker ? En termes simples, les tags Docker transmettent des informations utiles sur une version spécifique ou une variante d'une image. Ce sont des alias pour l'ID de votre image qui ressemblent souvent à ceci : `f1477ec11d12`. C'est juste une façon de faire référence à votre image. Une bonne analogie est la façon dont les tags Git font référence à un commit particulier dans votre historique.

Les deux cas les plus courants où les tags entrent en jeu sont :

1. Lors de la construction d'une image, nous utilisons la commande suivante :

```
docker build -t username/image_name:tag_name .
```

Essayons de décomposer ce que fait cette commande. Nous disons au démon Docker de récupérer le fichier Docker présent dans le répertoire courant (c'est ce que fait le `.` à la fin). Ensuite, nous disons au démon Docker de construire l'image et de lui donner le tag spécifié. Si vous exécutez `docker images`, vous devriez voir une image dont le dépôt est `username/image_name` et le tag est `tag_name`.

`username/image_name` n'est pas un format obligatoire pour spécifier le nom de l'image. C'est juste une convention utile pour éviter de tagger à nouveau votre image lorsque vous devez la pousser vers un registre.

Votre image peut être nommée comme vous le souhaitez. Pour le registre Docker public, vous êtes limité à une hiérarchie à deux niveaux lors de la nomination des images. Par exemple, votre image ne peut pas avoir le nom `a/b/c:1`. Cette restriction n'existe généralement pas dans les registres privés. Comme indiqué précédemment, il n'est pas obligatoire de spécifier un `tag_name`. Nous verrons ce qui se passe dans ce cas bientôt.

2. Taggage explicite d'une image via la commande `tag`.

```
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
```

Cette commande crée simplement un alias (une référence) sous le nom de `TARGET_IMAGE` qui fait référence à `SOURCE_IMAGE`. C'est tout ce qu'elle fait. C'est comme attribuer à une image existante un autre nom pour y faire référence. Remarquez comment le tag est spécifié comme optionnel ici aussi, par `[:TAG]`.

### Que se passe-t-il lorsque vous ne spécifiez pas de tag ?

D'accord, découvrons maintenant ce qui se passe lorsque vous ne spécifiez pas de tag lors du taggage d'une image. C'est là que le tag `latest` entre en jeu. Chaque fois qu'une image est taggée sans tag explicite, elle reçoit le tag `latest` par défaut. C'est un choix de nom malheureux qui cause beaucoup de confusion. Mais j'aime à penser que c'est le **tag par défaut** qui est donné aux images lorsque vous n'en spécifiez pas.

Beaucoup de confusion autour de `latest` est causée par l'attente qu'il s'agisse de la dernière version de l'image, surtout dans les Dockerfiles. Considérons les différents scénarios avec un exemple :

#### Scénario 1 :

Supposons que l'instruction suivante soit présente dans notre Dockerfile :

```
FROM debian
```

Puisque nous n'avons pas spécifié de tag, Docker ajoutera le tag `latest` et essaiera de tirer l'image `debian:latest`.

#### Scénario 2 :

```
FROM debian:9.3
```

Puisque le tag est explicitement mentionné ici, Docker tirera l'image Debian taggée 9.3

Une autre chose à garder à l'esprit est qu'il n'y a pas de règle qui stipule qu'une image doit avoir un seul tag. Une image peut avoir plusieurs tags et ils sont généralement utilisés pour spécifier les versions majeures et mineures. Par exemple, considérons ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/bOvBoIYQodn8oPnc9D39cLmXRwp4i-vcgIUc)
_[Page Docker Hub pour Debian](https://hub.docker.com/r/library/debian/" rel="noopener" target="_blank" title=")_

Au moment de la rédaction de cet article, le tag `latest` pour l'image Debian pointe vers la version `9.3` **et** la version `9`. Cela changera probablement à l'avenir chaque fois que la version majeure ou mineure de l'image sera augmentée.

Veuillez noter que l'utilisation de tags pour la version sémantique est une convention qui est suivie, mais les tags n'ont pas été conçus **uniquement** à cette fin.

### En conclusion, latest n'est pas un tag spécial

Le principal point à retenir de ce que nous avons couvert jusqu'à présent est que **latest est comme n'importe quel autre tag**. La responsabilité incombe au développeur de tagger correctement les images de sorte que `latest` pointe toujours vers la dernière version stable de l'image.

Par conséquent, nous ne spécifions pas explicitement un tag dans nos Dockerfiles lors du tirage d'images, car nous pourrions nous retrouver avec une version complètement différente de l'image de base que celle que nous avions utilisée auparavant. Il n'y a aucune garantie quant à savoir s'il s'agira d'une augmentation majeure ou mineure. Même une ancienne version peut être taggée comme `latest`.

P.S. Si vous avez trouvé des idées fausses/erreurs dans l'article, n'hésitez pas à me tweeter [@ScribbingOn](https://twitter.com/ScribblingOn).

Merci à [Jérôme Petazzoni](https://twitter.com/jpetazzo) pour m'avoir aidé à comprendre certaines de ces choses.