---
title: Une introduction à ROUGE et comment l'utiliser pour évaluer les résumés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-26T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-rouge-and-how-it-works-for-evaluation-of-summaries-e059fb8ac840
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aOZ8uDUscHo0oRipuqKPBg.jpeg
tags:
- name: education
  slug: education
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Une introduction à ROUGE et comment l'utiliser pour évaluer les résumés
seo_desc: 'By Kavita Ganesan

  ROUGE stands for Recall-Oriented Understudy for Gisting Evaluation. It is essentially
  a set of metrics for evaluating automatic summarization of texts as well as machine
  translations.

  It works by comparing an automatically produced ...'
---

Par Kavita Ganesan

ROUGE signifie Recall-Oriented Understudy for Gisting Evaluation. Il s'agit essentiellement d'un ensemble de métriques pour évaluer la summarisation automatique de textes ainsi que les traductions automatiques.

Il fonctionne en comparant un **résumé produit automatiquement** ou une **traduction** avec un ensemble de **résumés de référence** (généralement produits par des humains). Supposons que nous ayons les résumés système et de référence suivants :

**Résumé Système (ce que la machine a produit) :**

```
the cat was found under the bed
```

**Résumé de Référence (standard de référence — généralement par des humains) :**

```
the cat was under the bed
```

Si nous considérons simplement les mots individuels, le nombre de mots chevauchants entre le résumé système et le résumé de référence est de 6. Cela, cependant, ne vous en dit pas beaucoup en tant que métrique. Pour obtenir une bonne valeur quantitative, nous pouvons en fait calculer la **précision** et le **rappel** en utilisant le chevauchement.

Simplement, le rappel (dans le contexte de ROUGE) fait référence à la quantité de **résumé de référence** que le **résumé système** récupère ou capture. Si nous considérons simplement les mots individuels, il peut être calculé comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/0*yhcByAEK3i1SVRhu.)

Dans cet exemple, le rappel serait donc :

![Image](https://cdn-media-1.freecodecamp.org/images/0*WD9JP4MkFvMsjYBS.)

Cela signifie que tous les mots du **résumé de référence** ont été capturés par le **résumé système**, ce qui est effectivement le cas pour cet exemple. Voila !

Cela semble vraiment bien pour un système de résumé de texte. Mais cela ne vous raconte pas l'autre côté de l'histoire. Un résumé généré par une machine (résumé système) peut être extrêmement long, capturant tous les mots du résumé de référence. Mais, beaucoup de mots dans le résumé système peuvent être inutiles, rendant le résumé inutilement verbeux.

C'est là que la précision entre en jeu. En termes de précision, ce que vous mesurez essentiellement, c'est **combien du résumé système était en fait pertinent ou nécessaire** ? La précision est mesurée comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/0*DttHG7bvoji8eQY3.)

Dans cet exemple, la Précision serait donc :

![Image](https://cdn-media-1.freecodecamp.org/images/0*lZmp28lCclAPTqJ-.)

Cela signifie simplement que 6 des 7 mots du résumé système étaient en fait pertinents ou nécessaires. Si nous avions le résumé système suivant, par opposition à l'exemple ci-dessus —

**Résumé Système 2 :**

```
the tiny little cat was found under the big funny bed
```

La Précision devient maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/0*EM9Q_uVgC3O7rlBE.)

Maintenant, cela ne semble pas si bien, n'est-ce pas ? C'est parce que nous avons assez de mots inutiles dans le résumé. L'aspect **précision** devient vraiment crucial lorsque vous essayez de générer des résumés qui sont concis par nature. Par conséquent, il est toujours préférable de calculer à la fois la **précision** et le **rappel**, puis de rapporter la **F-Mesure**.

Si vos résumés sont d'une certaine manière contraints à être concis par certaines contraintes, alors vous pourriez envisager d'utiliser uniquement le **rappel**, puisque la précision est moins préoccupante dans ce scénario.

ROUGE-N, ROUGE-S et ROUGE-L peuvent être considérés comme la granularité des textes comparés entre les résumés système et les résumés de référence.

* ROUGE-N — mesure le chevauchement des **unigrams**, **bigrams**, **trigrams** et des n-grams d'ordre supérieur
* ROUGE-L — mesure la **plus longue séquence correspondante** de mots en utilisant LCS. Un avantage de l'utilisation de LCS est qu'il ne nécessite pas de correspondances consécutives mais des correspondances en séquence qui reflètent l'ordre des mots au niveau de la phrase. Puisqu'il inclut automatiquement les n-grams communs les plus longs en séquence, vous n'avez pas besoin d'une longueur de n-gram prédéfinie.
* ROUGE-S — Est toute paire de mots dans une phrase dans l'ordre, permettant des écarts arbitraires. Cela peut également être appelé concurrence de skip-gram. Par exemple, **skip-bigram** mesure le chevauchement des paires de mots qui peuvent avoir un maximum de deux écarts entre les mots. Par exemple, pour la phrase _"cat in the hat"_, les skip-bigrams seraient _"cat in, cat the, cat hat, in the, in hat, the hat"_.

Par exemple, **ROUGE-1** fait référence au chevauchement des **_unigrams_** entre le résumé système et le résumé de référence. **ROUGE-2** fait référence au chevauchement des **_bigrams_** entre les résumés système et de référence.

Prenons l'exemple ci-dessus. Supposons que nous voulons calculer les scores de **précision et de rappel ROUGE-2**.

**Résumé Système :**

```
the cat was found under the bed
```

**Résumé de Référence :**

```
the cat was under the bed
```

**Bigrams du Résumé Système :**

```
the cat, cat was, was found, found under, under the, the bed
```

**Bigrams du Résumé de Référence :**

```
the cat, cat was, was under, under the, the bed
```

Sur la base des bigrams ci-dessus, le rappel ROUGE-2 est le suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/0*V6mnVSY3SvTY0jaz.)

Essentiellement, le résumé système a récupéré 4 bigrams sur 5 bigrams du résumé de référence, ce qui est assez bien ! Maintenant, la précision ROUGE-2 est la suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/0*zOxldvQLkQRENv1w.)

La précision ici nous indique que parmi tous les bigrams du résumé système, il y a un chevauchement de 67 % avec le résumé de référence. Ce n'est pas trop mal non plus. Notez que lorsque les résumés (à la fois les résumés système et de référence) deviennent de plus en plus longs, il y aura moins de bigrams chevauchants. Cela est particulièrement vrai dans le cas de la summarisation abstraite, où vous ne réutilisez pas directement des phrases pour la summarisation.

La raison pour laquelle on utiliserait ROUGE-1 plutôt que ou en conjonction avec ROUGE-2 (ou d'autres mesures ROUGE de granularité plus fine), est également de montrer la fluidité des résumés ou de la traduction. L'intuition est que si vous suivez plus étroitement les ordonnancements de mots du résumé de référence, alors votre résumé est en fait plus fluide.

Pour plus d'informations approfondies sur ces métriques d'évaluation, vous pouvez vous référer à [l'article de Lin](http://www.aclweb.org/anthology/W04-1013). La mesure à utiliser dépend de la tâche spécifique que vous essayez d'évaluer. Si vous travaillez sur la summarisation extractive avec des résumés système et de référence assez verbeux, il peut être judicieux d'utiliser ROUGE-1 et ROUGE-L. Pour des résumés très concis, ROUGE-1 seul peut suffire, surtout si vous appliquez également la radicalisation et la suppression des mots vides.

### Articles à lire

* [ROUGE : Un package pour l'évaluation automatique des résumés](http://www.aclweb.org/anthology/W04-1013)