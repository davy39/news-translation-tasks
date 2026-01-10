---
title: Si le code fonctionne, ne le réparez pas... Ou peut-être si ? Quand refactoriser
  votre code et quand le laisser tel quel.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-30T18:51:06.000Z'
originalURL: https://freecodecamp.org/news/advice-to-programmers-if-it-works-dont-fix-it-or
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/1_ShTnBApvIxNlKjTItTAAiw.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: software development
  slug: software-development
- name: web
  slug: web
seo_title: Si le code fonctionne, ne le réparez pas... Ou peut-être si ? Quand refactoriser
  votre code et quand le laisser tel quel.
seo_desc: 'By Huseyin Polat Yuruk

  Imagine software that you work on. It was written by programmers before you joined
  the team and the software works properly. There are some bugs that need to be fixed
  but it does what it’s supposed to do. Nothing else. This is ...'
---

Par Huseyin Polat Yuruk

Imaginez un logiciel sur lequel vous travaillez. Il a été écrit par des programmeurs avant que vous ne rejoigniez l'équipe et le logiciel fonctionne correctement. Il y a quelques bugs à corriger, mais il fait ce qu'il est censé faire. Rien de plus. C'est ce que les autres voient de l'extérieur du code : un logiciel qui résout les problèmes des clients et fonctionne comme prévu.

Mais qu'en est-il du code ? Et des programmeurs ? Que pensent-ils de leur logiciel ?

En tant que l'un des programmeurs qui ont construit ce logiciel, vous voyez des choses totalement différentes de l'intérieur du code.

Tout d'abord, vous pensez que la base de code est trop grande. Vous savez certainement que ce logiciel aurait pu être écrit avec beaucoup moins de code tout en fournissant les mêmes fonctionnalités. La base de code vous semble si complexe. Vous savez que le code aurait pu être écrit de manière meilleure, plus simple et mieux structurée.

Ajouter de nouvelles fonctionnalités ou implémenter quelque chose de nouveau est difficile et douloureux parce que vous devez prendre en compte les autres parties qui sont connectées les unes aux autres. Les modules ne sont pas faiblement couplés, donc apporter des modifications prend trop de temps. Et qu'en est-il du débogage ? Trouver des bugs et les corriger prend également trop de temps.

En dehors du mauvais design et du code laid, le logiciel fonctionne correctement et les clients sont satisfaits. Maintenant, vous êtes à la croisée des chemins. Il y a deux voies possibles pour vous : l'une vous dit que vous devriez suivre l'ancien adage de l'ingénierie, « Si ça marche, ne le réparez pas. » L'autre vous dit que vous devriez faire un peu de refactorisation pour faciliter votre travail sur votre base de code afin d'avoir un code plus lisible et compréhensible.

Quelle voie préféreriez-vous ? Suivriez-vous l'ancien adage de l'ingénierie « Si ça marche, ne le réparez pas » ?

## Deux mentalités différentes de programmeurs

La réponse à cette question peut être simple. Mais avant d'expliquer la réponse appropriée, je veux vous présenter deux mentalités différentes de programmeurs lorsqu'il s'agit de corriger un mauvais code qui fonctionne correctement.

La première mentalité croit en l'ancien adage de l'ingénierie : « **Si ça marche, ne le réparez pas.** » Pour eux, leur style de code n'a pas d'importance. Ils sont des programmeurs axés sur les résultats. Cela peut être un code complexe, mal structuré, complètement opposé aux principes de programmation importants, mais ils ne se soucient pas de la qualité de l'écriture du code. Ils se soucient seulement de ce qu'il fait.

Ainsi, pour ces programmeurs, corriger un code mal écrit est une perte de temps. Il fonctionne simplement. Pourquoi devraient-ils y toucher ?! Et de plus, il y a un grand risque d'introduire de nouveaux bugs en corrigeant le mauvais code. Alors, que feront-ils ? Ils ne toucheront pas au code et continueront à suivre l'ancien adage de l'ingénierie.

D'un autre côté, les autres programmeurs qui voient le code comme une œuvre d'art seront mal à l'aise dans ce genre de situation. Ils se sentiront dégoûtés en lisant un code mal écrit. Ils essaieront de corriger chaque morceau de code dans le projet parce qu'ils se soucient beaucoup du style de code, et chaque morceau de code dans leur projet devrait être traité comme une œuvre d'art.

Ils sont trop obsessionnels quant à leur style de code. Même si d'autres programmeurs écrivent un code bien structuré, ils essaieront de changer ce code pour le rendre conforme à leur propre style. Donc, en gros, ils ne suivent pas l'ancien adage « si ça marche, ne le réparez pas ». Ils corrigeront tout selon leur propre mentalité. En fin de compte, peu importe pour eux si ça marche ou non.

## Quelle serait la meilleure solution qui fonctionne pour vous ?

Trouvez les parties du code sur lesquelles vous travaillez activement et corrigez ces parties pour les rendre plus compréhensibles et lisibles. Ne touchez pas aux autres parties si elles fonctionnent comme prévu et qu'elles sont exemptes de bugs.

Pourquoi ce noyau est-il si important ? Les parties centrales de votre logiciel sont celles sur lesquelles vous travaillerez le plus. Vous lirez ces parties plus souvent et y apporterez des modifications plus souvent que le reste. S'il y a besoin d'ajouter des fonctionnalités supplémentaires ou d'implémenter de nouvelles fonctionnalités, elles seront directement connectées au noyau.

La plupart des bugs seront introduits à partir de ce noyau, ce qui signifie que vous passerez la plupart de votre temps à déboguer ces parties. Souvenez-vous de la [règle 80/20 (Principe de Pareto)](https://en.wikipedia.org/wiki/Pareto_principle), « **20 pour cent du code contient 80 pour cent des erreurs. Trouvez-les, corrigez-les !** »

Et les autres parties ?

Ces parties sont celles sur lesquelles vous travaillerez rarement. Elles sont exemptes de bugs. Elles ont peut-être été écrites il y a des mois ou des années et elles fonctionnent comme prévu. Elles peuvent être écrites de manière laide, même si elles auraient pu être écrites de manière plus simple, plus lisible et compréhensible. Cela ne signifie pas que vous devez les corriger aussi. Dieu sait quand vous devrez les relire ou les modifier à nouveau. Donc, ces parties peuvent rester telles qu'elles sont. Oubliez-les. Pas besoin de les corriger. Vous pouvez passer votre temps à travailler sur des choses plus importantes.

## Pourquoi est-il si important de corriger les parties centrales même si elles fonctionnent comme prévu ?

Si vous voulez servir vos clients pendant de nombreuses années, vous devriez avoir un produit maintenable. Un produit maintenable signifie que apporter des modifications n'est pas une lutte. Le débogage et la correction des bugs ne devraient pas prendre trop de temps et l'ajout de nouvelles fonctionnalités devrait également être facile. Ainsi, en fin de compte, vos programmeurs sont heureux et vos clients sont heureux aussi.

Comme l'a dit [Martin Fowler](https://martinfowler.com/) dans son livre [Refactoring](https://www.amazon.com/Refactoring-Improving-Existing-Addison-Wesley-Signature/dp/0134757599/ref=pd_sbs_14_img_0/147-2543130-6817650?_encoding=UTF8&pd_rd_i=0134757599&pd_rd_r=3126d0ac-cc44-40ab-874c-dd6a2817a30a&pd_rd_w=NxgDY&pd_rd_wg=nvdiq&pf_rd_p=5cfcfe89-300f-47d2-b1ad-a4e27203a02a&pf_rd_r=AB27YQ6VJP9RM58D8HBD&psc=1&refRID=AB27YQ6VJP9RM58D8HBD) :

> « Lorsque vous pensez aux programmeurs, la plupart d'entre nous penseront qu'ils passent la plupart de leur temps à écrire du code. En réalité, c'est une assez petite fraction. Les programmeurs passent la plupart de leur temps à lire le code et à le déboguer. Chaque programmeur peut raconter une histoire d'un bug qui a pris une journée entière (ou plus) à trouver. Corriger le bug est généralement assez rapide, mais le trouver est un cauchemar. »

Plus votre code est bien écrit, plus il est facile à comprendre. Plus votre code est compréhensible, plus votre travail est facile.

C'est la raison pour laquelle ne pas suivre l'ancien adage de l'ingénierie (si ça marche, ne le réparez pas) pour les parties centrales de votre logiciel est une décision importante que vous pouvez prendre.