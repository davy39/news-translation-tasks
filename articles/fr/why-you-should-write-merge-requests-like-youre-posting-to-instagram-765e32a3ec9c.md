---
title: Pourquoi vous devriez rédiger des demandes de fusion comme si vous publiiez
  sur Instagram
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2019-05-02T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-write-merge-requests-like-youre-posting-to-instagram-765e32a3ec9c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BW0h4oGKEJaPmSbE2z-o1w.jpeg
tags:
- name: coding
  slug: coding
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Pourquoi vous devriez rédiger des demandes de fusion comme si vous publiiez
  sur Instagram
seo_desc: Merge requests (or pull requests) are a huge part of a team’s development
  process. It’s the main gatekeeper preventing developers from throwing whatever they
  want into the default branch. It’s also a reference to the history and understanding
  of the ...
---

Les demandes de fusion (ou pull requests) sont une partie importante du processus de développement d'une équipe. C'est le principal gardien qui empêche les développeurs de jeter n'importe quoi dans la branche par défaut. C'est aussi une référence à l'historique et à la compréhension des changements qu'une personne apporte à une application. Cela donne aux réviseurs de code et aux testeurs plus de confiance pour vraiment savoir ce qui se passe.

![Image](https://cdn-media-1.freecodecamp.org/images/YgdjhAHTChoj8uhrbINlzctXz1SyGeCWEHBY)
_Gandalf : tu ne fusionneras pas ce code !_

Alors, quel est le rapport avec Instagram ? Accordez-moi un peu de patience, cela a du mérite.

### Les fondements d'une publication Instagram

Cela peut s'appliquer à n'importe quelle plateforme de médias sociaux, mais nous allons nous en tenir à Instagram ici. Commençons par un exemple de publication de la NASA. La publication peut être décomposée en quelques composants vitaux : une image, une description et des hashtags.

![Image](https://cdn-media-1.freecodecamp.org/images/22w7-FHEtT7b8VUmP6o0k0S4uDQ7-pHsBcUf)
_[https://www.instagram.com/p/BwH0GRAjL5i/](https://www.instagram.com/p/BwH0GRAjL5i/" rel="noopener" target="_blank" title=")_

### Quel est le rapport avec le code ?

J'y viens ! En regardant chaque partie, nous pouvons commencer à les relier à notre demande de fusion. Commençons par les 3 bases :

* Image => Code
* Description => Quelle est votre fonctionnalité ?
* Hashtags => Quelles parties de votre application cela impacte-t-il ?

#### Code

Tout comme l'image ou la vidéo est l'aspect le plus important d'une publication, votre code l'est aussi. C'est le contenu principal qui alimente la conversation et l'intérêt. Bien qu'il soit solide en lui-même, sans contexte, il peut créer son propre ensemble de problèmes.

#### Description

Dans la publication de la NASA ci-dessus, sans voir la description, cela pourrait très bien être une illustration floue de l'Étoile de la Mort. Au lieu de cela, grâce à la description, nous découvrons qu'il s'agit de Jupiter. L'imagerie infrarouge nous permet de mieux voir son atmosphère.

![Image](https://cdn-media-1.freecodecamp.org/images/2jgyZaOM9IPXhInSF6AoSEMBTofSb0CydA7L)
_Ce n'est pas une lune ! Exact, c'est Jupiter._

Ne pas savoir ce que fait le code que vous regardez ou ce qu'il impacte peut entraîner de la confusion et un manque de compréhension pour ceux qui ne sont pas déjà familiers avec votre application. Même pour les vétérans, ne pouvoir voir qu'un petit segment d'un diff par rapport à une base de code gigante change complètement ce que vous regardez.

#### Zones d'impact

Tout comme les hashtags permettent aux gens de taguer du contenu pour montrer les sujets auxquels il est lié, fournir une zone d'impact aide à donner à votre réviseur une idée de l'endroit où il devrait porter son attention. Si le réviseur ou le testeur ne connaît qu'un seul endroit où un composant modifié est utilisé (alors qu'il est utilisé plus largement dans l'application), il pourrait manquer des cas d'utilisation importants qui pourraient avoir des changements cassants en dehors de cette instance.

### Apprendre de l'histoire

Je suis sûr que Jupiter sera là pour les deux prochaines années. Regarder en arrière notre code dans ce laps de temps peut sembler un paysage complètement différent. Des morceaux de code sur lesquels ont travaillé des développeurs depuis longtemps partis peuvent ne pas être complètement compris. Cela pourrait être crucial pour l'intégrité d'une application.

![Image](https://cdn-media-1.freecodecamp.org/images/TK-wVHMdMdlwkREfBQumX1K6H3f7CG-Rocs1)
_[https://www.instagram.com/p/BveREmPD9Vb/](https://www.instagram.com/p/BveREmPD9Vb/" rel="noopener" target="_blank" title=")_

Chacun de ces composants de demande de fusion joue un rôle clé dans la prévention de la perte de connaissances et de contexte des changements apportés à une application. Pourquoi la logique métier a-t-elle été configurée pour gérer une situation particulière de cette manière ? Trouver le commit et le relier à la demande de fusion pourrait très bien prévenir une situation où votre application perd de l'argent en raison d'un bug auquel vous n'auriez pas pensé sans ce contexte.

### Bonus : Commentaires

Les retours sont cruciaux pour les Instagrammers et les développeurs. Pouvoir apprendre des autres et gagner une perspective différente est la clé non seulement pour grandir en tant qu'individu, mais aussi pour pouvoir tirer les meilleurs morceaux et la sagesse de toutes les parties de votre équipe. Prendre et comprendre ces retours est crucial pour renforcer votre application.

### Comment l'équipe E84 rédige-t-elle les demandes de fusion ?

Sur des projets plus importants, nous faisons un effort supplémentaire pour aider à guider notre équipe dans la rédaction de demandes de fusion de qualité. En particulier, nous utilisons des modèles de demande de fusion pour accomplir le travail.

Nous avons essayé de le décomposer en 2 sujets principaux, un aperçu du travail et comment tester.

```
## Aperçu

### Quelle est la fonctionnalité ?
(Décrivez ce qu'est la fonctionnalité)

### Quelle est la solution ?
(Décrivez à un niveau élevé comment la fonctionnalité a été implémentée)

### Quelles parties du site cela impacte-t-il ?
(Décrivez quelles parties du site sont impactées et *si* le code a touché d'autres zones)

## Test

### Quels sont les tests requis ?
(Décrivez les prérequis pour les étapes de test)

### Quelles sont les étapes pour reproduire ?
(Décrivez et listez les étapes pour reproduire - distinguez si les instructions sont pour un développeur ou un testeur QA)

## Autres notes
(Ajoutez toute information supplémentaire qui serait utile au développeur ou au testeur QA)
```

Disponible également ici : [https://gist.github.com/colbyfayock/086038bc5e38fd7edf4e73e1602de71c](https://gist.github.com/colbyfayock/086038bc5e38fd7edf4e73e1602de71c)

Depuis l'ajout de ce modèle, nous avons pu voir une tendance clairement ascendante dans la qualité de nos demandes de fusion. Par conséquent, de meilleures références historiques aux changements de code.

### Comment ajouter des modèles ?

Nous sommes une maison à la saveur Gitlab pour nos projets internes. La plupart des logiciels Git devraient pouvoir fournir l'option d'ajouter un modèle de demande de fusion. Pour aider à commencer :

* Gitlab : [https://docs.gitlab.com/ee/user/project/description_templates.html#creating-merge-request-templates](https://docs.gitlab.com/ee/user/project/description_templates.html#creating-merge-request-templates)
* Github : [https://help.github.com/en/articles/creating-a-pull-request-template-for-your-repository](https://help.github.com/en/articles/creating-a-pull-request-template-for-your-repository)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f60a Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">f4e8f60a Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

_Publié à l'origine sur [https://www.element84.com/blog/write-merge-requests-like-youre-posting-to-instagram](https://www.element84.com/blog/write-merge-requests-like-youre-posting-to-instagram)._