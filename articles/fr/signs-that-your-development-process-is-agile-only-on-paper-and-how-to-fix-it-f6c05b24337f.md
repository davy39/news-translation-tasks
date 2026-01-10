---
title: Signes que votre processus de développement est Agile seulement sur le papier
  — et comment le corriger
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-05T21:24:37.000Z'
originalURL: https://freecodecamp.org/news/signs-that-your-development-process-is-agile-only-on-paper-and-how-to-fix-it-f6c05b24337f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6IeFjtwx0cPgTRjcS_vS6w.jpeg
tags:
- name: agile
  slug: agile
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Signes que votre processus de développement est Agile seulement sur le
  papier — et comment le corriger
seo_desc: 'By Geshan Manandhar

  Agility comes with practice, not putting big words on paper. Using Jira does not
  make your software development process agile. Saying we do “scrum” is not being
  agile.

  Being agile is having an agile mindset and putting it into pra...'
---

Par Geshan Manandhar

L'agilité vient avec la pratique, pas en mettant de grands mots sur le papier. Utiliser Jira ne rend pas votre processus de développement logiciel agile. Dire que nous faisons du "scrum" ne signifie pas être agile.

Être agile, c'est avoir un état d'esprit agile et le mettre en pratique chaque jour. Il s'agit de penser à la valeur que vous apportez au client et à la manière de le faire mieux.

Cet article révélera cinq signes que votre pratique n'est pas vraiment agile, et comment résoudre ces problèmes. Les signes et solutions concerneront plusieurs rôles comme Product Manager, Ingénieur logiciel, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/QsoP-waDxNwWENV8yaNFopJLAAHUEZvEdBg5)
_Image de tableau Agile provenant de [Unsplash](https://unsplash.com/photos/zoCDWPuiRuA" rel="noopener" target="_blank" title=")_

### TLDR;

* Si vous écrivez des documents > 5 pages, vous pouvez vous améliorer.
* Il devrait y avoir une définition claire de Prêt pour le développement et Terminé.
* Une Story/Problème devrait être basée sur la valeur apportée au client, pas seulement sur l'aspect technique.
* Sortir une nouvelle version de logiciel une fois par mois et dire que nous sommes agiles devrait être un crime.
* Ne pas se soucier de l'équipe, ce n'est pas faire de l'agile correctement.

Maintenant, examinons ces signes qui expliquent pourquoi les pratiques agiles sur papier ne fonctionneront pas et comment les corriger.

### Documents de plus de 5 pages

Il y aura de grandes fonctionnalités (épics) et elles doivent être expliquées. Cela ne vous donne pas une licence pour écrire des documents de 50 pages. Si un document est plus long que 5 pages, de nombreux membres de l'équipe ne le liront pas. Acceptez ce fait.

> _Un beau lundi matin, vous recevez un mémo de 30 pages de texte sur la nouvelle fonctionnalité que l'entreprise veut que nous développons. Allez-vous le lire attentivement ? La réponse est Non._

Vous pourriez le parcourir pour vous en sortir lors de la réunion et ce sera à peu près tout. Les documents deviennent obsolètes rapidement. Lorsque les exigences changent, personne ne se donne la peine de mettre à jour la documentation.

#### Solution

Écrivez des documents qui font moins de ou égal à 5 pages. Soyez concis et précis. Commencez à créer des aides visuelles pour le processus afin de l'expliquer. Créez des maquettes et utilisez des outils comme [Balsamiq](https://balsamiq.com/). Exprimez les exigences de manière à ce qu'elles soient comprises par tous avec moins ou pas de lecture impliquée. Ensuite, selon les besoins, créez un design UI et discutez. Après cela, implémentez-le en code.

### Définition floue de Prêt pour le développement et Terminé

Une définition claire de prêt pour le développement et terminé est cruciale pour le succès de l'équipe. Ne pas avoir ces définitions ou avoir des définitions floues nuira à la performance de l'équipe.

> _Un ingénieur logiciel devrait être clair sur le moment où la story est prête à être prise pour le développement. Il en va de même pour terminé._

Est-elle prête pour le développement lorsque la story est créée mais que la description n'existe pas ? Est-elle terminée dès que je la déploie en production et que je déplace ma tâche vers la colonne "terminé" ? Si il y a une confusion comme celle-ci, c'est un problème qui doit être abordé.

#### Solution

Ayez une définition claire point par point de "Définition de Prêt" et "Définition de Terminé". Cela vous aidera à mesurer et à améliorer la performance de l'équipe. Cela aidera également tous les membres impliqués à comprendre la signification de ces choses de la même manière.

### Stories basées sur les aspects techniques, pas sur la valeur pour le client

Le développement logiciel agile consiste toujours à apporter de la valeur au client. De la valeur sous forme de logiciel fonctionnel, pas une pile de documents.

Disons qu'il y a une story comme "En tant que responsable du service client, j'ai besoin de savoir qui a créé un remboursement afin que je puisse suivre et auditer les remboursements à l'avenir". Cette tâche peut impliquer l'ajout d'un champ "created_by" dans la table des remboursements, par exemple. Mais cela ne devrait pas aboutir à une "story" qui dit "Ajouter un champ created_by dans la table des remboursements". Bien sûr, cela peut être une tâche/sous-tâche dans le cadre de la story principale. La story principale apporte de la valeur, mais cette tâche de base de données est quelque chose qui aide le processus.

![Image](https://cdn-media-1.freecodecamp.org/images/bEDuLU1nTvT3YZAeZaxaIVHshWGUXbVjNg5X)
_Une story a de la valeur et des points, les tâches font partie d'une story._

#### Solution

Ayez des définitions et des limites claires pour Épic, Story et tâche. Chaque story devrait apporter une certaine valeur au client (comme dans l'image ci-dessus). Si vous suivez Scrum, vous aurez également des points de story pour des choses comme la vélocité de l'équipe. Les tâches techniques sont nécessaires. Cependant, seule la bonne somme de tâches techniques apporte de la valeur au client.

> _L'essentiel ici est "toujours se concentrer sur la valeur apportée au client"._

### Sortir une nouvelle version de logiciel une fois par mois

La première chose à considérer ici est :

> _Le déploiement est une tâche technique et la sortie d'une nouvelle version de logiciel est une activité commerciale._

[Le déploiement n'est pas une sortie](https://geshan.com.np/blog/2018/10/deployment-is-not-release/). Si vous n'êtes pas capable de faire cette distinction, il y a quelque chose qui doit être corrigé. En plus de cela, si vous sortez à peine une nouvelle version chaque mois, vous faites mal l'agile. [Sortir tôt, sortir souvent](https://en.wikipedia.org/wiki/Release_early,_release_often) est une excellente philosophie pour obtenir des retours précoces. Avec des retours précoces, vous pouvez apporter un nouvel ensemble de modifications dans la prochaine version pour améliorer le logiciel.

Cela peut ne pas s'appliquer aux applications mobiles car elles peuvent avoir un long processus d'approbation par le fournisseur. Pour les applications web, déployer et sortir plusieurs fois par jour devrait être la norme.

#### Solution

Construisez une culture et un processus technique qui vous permettent de déployer et/ou de sortir en production plusieurs fois par jour.

> _Appliquez une bonne qualité de code et d'excellentes pratiques d'ingénierie logicielle. Suivez les meilleures pratiques éprouvées comme les revues de code, les tests automatisés, CI/CD, [logging](https://geshan.com.np/blog/2015/08/importance-of-logging-in-your-applications/), la surveillance et le [déploiement automatisé](https://geshan.com.np/blog/2015/08/the-best-automated-deployment-tool-the-one-that-fits-your-needs/)._

Appelez cela DevOps, SRE ou Platforms engineering — peu importe. Mais faites-le et déployez sans crainte quand vous le souhaitez.

### Ne pas être attentif à la motivation de l'équipe

Le développement logiciel est un sport d'équipe. Si un joueur est blessé, l'équipe couvre ce joueur. Si un membre de l'équipe manque de certaines compétences, l'équipe couvre et aide à enseigner cette compétence au membre de l'équipe. Une équipe auto-organisée qui réfléchit à la manière d'améliorer le processus est au cœur de l'agile.

> _La motivation de l'équipe et des membres heureux sont essentiels à une haute productivité._

Si vous êtes traité comme des exécutants de stories sans voix et sans place pour l'amélioration, c'est un très mauvais signe.

#### Solution

Construisez une culture d'amélioration continue. Réfléchissez aux choses qui ont été faites et à la manière dont le processus peut être amélioré. Par exemple, si faire 60 % de nouvelles fonctionnalités et 40 % de bugs n'a pas bien fonctionné, trouvez un meilleur ratio. Faites des activités d'équipe et des choses qui élèvent l'esprit d'équipe.

### Conclusion

Être agile sur le papier et être agile en pratique sont deux choses différentes. Ne laissez pas votre processus de développement logiciel agile être comme un modèle en cascade avec la soi-disant peau agile. Soyez agile et corrigez ces signes pour avoir une production d'équipe élevée avec des performances fantastiques.

> _L'agile devrait être mis en œuvre pour résoudre les problèmes de personnes et de communication, ce qui entraîne la stabilisation des problèmes techniques._

_Vous pouvez lire plus de mes articles de blog sur [geshan.com.np](https://geshan.com.np/blog/2018/11/5-signs-that-reveal-your-software-development-process-is-agile-only-on-paper-and-solutions-for-them/)._