---
title: 'Comment et pourquoi vous devriez vous équiper : le temps passé à aiguiser
  votre hache n''est jamais perdu'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-20T16:56:37.000Z'
originalURL: https://freecodecamp.org/news/how-and-why-you-should-tool-up-time-spent-sharpening-your-axe-is-never-wasted-ef74e05e85d0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*sT3OymCpylqi6csy.
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Comment et pourquoi vous devriez vous équiper : le temps passé à aiguiser
  votre hache n''est jamais perdu'
seo_desc: 'By Harshdeep S Jawanda

  There is this old anecdote about two friends who went to the forest to chop up some
  firewood for their homes. The first friend kept at it without a break for four hours,
  whereas the other friend would rest for 5 minutes or so e...'
---

Par Harshdeep S Jawanda

Il y a cette vieille anecdote sur deux amis qui sont allés dans la forêt pour couper du bois de chauffage pour leurs maisons. Le premier ami a continué sans pause pendant quatre heures, tandis que l'autre ami se reposait pendant 5 minutes ou plus chaque heure. Lorsqu'ils ont terminé, le premier ami a été surpris de voir que le tas de bois de l'autre était beaucoup plus grand que le sien.

Incrédule, il a demandé : « Comment as-tu coupé plus de bois que moi ?! J'ai travaillé sans arrêt tandis que tu as pris tant de pauses. »

Son ami a répondu : « Pendant que je me reposais, j'aiguisais ma hache, afin de pouvoir couper du bois plus efficacement le reste du temps. »

C'est ce que je veux dire par « Équipez-vous ! » : vous équiper des bons outils pour vous rendre plus productif tout en assurant une meilleure qualité de travail.

Ce qui suit est destiné aux développeurs et utilise Java pour illustrer des exemples. Mais **les conseils généraux s'appliquent à tout le monde**.

### Soyez intelligent

L'exemple ci-dessus n'est pas meant à vous faire courir vers votre clavier pour commencer à taper des classes/librairies d'utilitaires qui vous aideront supposément. Pas du tout ! Soyez intelligent quant à ce dont vous avez exactement besoin. Maximisez le retour sur votre investissement (en temps) (ROI). Une partie importante d'être intelligent signifie que vous...

#### Préférez les solutions pré-construites à la création des vôtres

Pour les développeurs, le bon outil est souvent une bibliothèque qui vous fournit la fonctionnalité requise. Qu'il s'agisse de la classe `Optional<T>` de la bibliothèque Guava (pour une utilisation dans le code pré-Java 8) ou de son implémentation `ImmutableList<T>`, ces outils ont été développés pour couvrir de nombreux cas d'utilisation. Ils ont également généralement plusieurs générations d'évolution derrière eux et ont été minutieusement testés, à la fois par les développeurs et par les utilisateurs. Ainsi, ils offrent les avantages d'un bon design et d'implémentations matures.

Rappelez-vous : ne réinventez pas la roue !

#### Utilisez vos outils de manière cohérente

Si vous utilisez un outil ou une technique, essayez de l'utiliser de manière cohérente dans tout votre travail autant que vous le pouvez. Cela aidera à réduire la charge mentale de devoir faire un **changement de contexte** entre différents paradigmes et situations.

Souvent, cela signifie refactoriser du code hérité. Dans de telles situations, vous devriez sérieusement envisager de planifier du temps pour cela. Si le temps est un facteur limitant — comme c'est souvent le cas — essayez de prioriser les parties à fort impact de votre base de code.

### Quand il est temps de le faire vous-même

Le moment viendra probablement (comme c'est presque toujours le cas) où les solutions pré-construites ne seront pas suffisantes, ou elles ne combleront pas certaines des lacunes très spécifiques dont vous avez besoin. Ne vous sentez pas pressé de créer des bibliothèques énormes, parfaitement conçues, tout-en-un. **Commencez petit**. Créez **une solution qui est juste suffisante** pour vos besoins actuels. Peut-être qu'au lieu de créer une bibliothèque, pensez seulement à créer une classe utilitaire, puis avancez à partir de là.

#### Un peu peut aller loin

Vous serez surpris de voir combien d'utilité et de commodité même 3 à 4 lignes de code ordinaire peuvent offrir.

Il y avait un certain nombre d'endroits dans mon code où je devais obtenir des valeurs spécifiques à partir d'indices spécifiques dans des `List`. Qu'y a-t-il de plus simple que :

```
Object listValue = myList.get(index)
```

N'est-ce pas ? Pas si vite ! Cette simple ligne de code peut potentiellement lancer deux exceptions différentes (pouvez-vous déterminer lesquelles et pourquoi ?). D'accord, alors vous enveloppez votre code avec un peu de `try-catch` et maintenant vous avez terminé, n'est-ce pas ? Quelle valeur allez-vous assigner à `listValue` en cas d'exception ? Votre code commence maintenant à ressembler à quelque chose comme :

```
Object listValue = null; // assignation de valeur par défauttry {    listValue = myList.get(index);} catch (Exception e) {    // Ne rien faire (si c'est ce que vous voulez faire)}
```

Code simple et direct — mais ce n'est pas exactement une belle vue ou très pratique. Sans parler du fait que des fragments similaires seront éparpillés dans tout votre code. Tôt ou tard, vous oublierez également de prévoir toutes les éventualités. Et puis : **boum !!**

Comparez cela à :

```
Object listValue = Lists.get(myList, index, null);
```

où la classe utilitaire `Lists` contient la méthode de commodité suivante :

```
public static <T> T get(List<T> list, int position, T defaultValue) {    if (null != list && position >= 0 && position < list.size())        return list.get(position);    return defaultValue;}
```

C'est une méthode extrêmement simple, mais très utile (pour un cas d'utilisation spécifique).

Bien sûr, cela peut ne pas être exactement ce dont vous avez besoin. Vous pourriez également argumenter qu'au lieu de lancer une exception `ArrayIndexOutOfBounds`, ce code masque les indices incorrects et pourrait conduire à des erreurs insidieuses, et c'est pourquoi vous ne trouvez pas de code comme celui-ci dans les bibliothèques à usage général (où l'échec précoce est une vertu)... Tout cela est valable, mais c'est aussi pourquoi j'ai écrit cette méthode utilitaire particulière pour **mon cas d'utilisation.**

Cela illustre mon propos : au-delà du point où vous pouvez/allez/devez écrire du code utilitaire pour vos cas d'utilisation spécifiques, soyez simplement conscient des pièges potentiels, le cas échéant.

### Recherchez les motifs répétitifs

Comme je l'ai mentionné auparavant, il n'y a pas besoin de se précipiter dans quoi que ce soit. Une bonne et facile façon d'identifier les scénarios où un niveau d'abstraction plus élevé serait utile est de rechercher les choses qui sont :

* encombrantes
* ont une utilisation répétée
* sont sujettes aux erreurs

Que cela soit votre guide. Basiquement, **recherchez les motifs répétitifs** dans votre code ou vos actions pour obtenir le meilleur rapport qualité-prix.

Alors que vous commencez à améliorer les scénarios les plus évidents, d'autres — souvent de niveau supérieur — motifs commenceront à émerger. Les choses qui ne semblaient pas si inconfortables auparavant commenceront soudainement à sembler maladroites/sujettes aux erreurs en comparaison. Cela vous guidera automatiquement vers le prochain outil/abstraction que vous devriez développer.

Rincez, répétez.

### Ne forcez pas

Laissez l'utilisation/adoption de vos outils croître de manière organique alors que vous traitez vos points de douleur et vos goulots d'étranglement (état d'esprit Agile ?). Ne fixez pas une limite codée en dur de X heures passées par semaine pour satisfaire une métrique externement imposée de ce qui constitue une « bonne pratique ».

**L'utilisation forcée d'outils peut parfois être contre-productive** : vous obtiendrez de bien meilleurs résultats lorsque vous et vos collaborateurs **ressentez le besoin de vous améliorer**. Le niveau de motivation et la perception de la récompense (lorsque l'amélioration se produit) sont simplement beaucoup plus élevés.

### Dernier point mais non des moindres...

Pratiquez l'apprentissage continu et l'amélioration de soi.

Ce sont les deux outils les plus importants que vous pouvez vous équiper. Une fois que vous aurez inculqué ces habitudes, elles auront l'impact le plus durable sur votre vie et votre carrière.

### Enfin...

Si vous avez trouvé cet article utile, n'oubliez pas d'applaudir ;-) !

Les discussions constructives et les corrections sont les bienvenues.