---
title: Qu'est-ce que l'Amélioration Progressive, et pourquoi c'est important
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-26T22:15:02.000Z'
originalURL: https://freecodecamp.org/news/what-is-progressive-enhancement-and-why-it-matters-e80c7aaf834a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*cs42aEkypTZorYk6
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que l'Amélioration Progressive, et pourquoi c'est important
seo_desc: 'By Praveen Dubey

  Progressive Enhancement (PE) is a powerful methodology for developing web applications.

  Here is a formal definition:


  Progressive enhancement is a strategy for web design that emphasizes core web page
  content first. This strategy the...'
---

Par Praveen Dubey

L'Amélioration Progressive (AP) est une méthodologie puissante pour développer des applications web.

Voici une définition [formelle](https://en.wikipedia.org/wiki/Progressive_enhancement) :

> **L'amélioration progressive** est une stratégie de conception web qui met l'accent sur le contenu principal de la page web en premier. Cette stratégie ajoute ensuite progressivement des couches de présentation et de fonctionnalités plus nuancées et techniquement rigoureuses par-dessus le contenu, en fonction des capacités du navigateur/connexion Internet de l'utilisateur final. — Wikipédia

Les avantages proposés de cette stratégie sont qu'elle permet à tout le monde d'accéder au contenu de base et aux fonctionnalités d'une page web, en utilisant n'importe quel navigateur ou connexion Internet, tout en fournissant une version améliorée de la page à ceux qui disposent d'un logiciel de navigateur plus avancé ou d'une bande passante plus grande.

Et en un mot...

...elle nous offre une expérience utilisateur de base et une compatibilité multi-navigateurs pour assurer la **stabilité**.

```
let AP = "Amélioration Progressive";
```

La stratégie AP se compose des principes de base suivants :

* Le **contenu** de base doit être accessible à **tous les navigateurs web**
* Les **fonctionnalités** de base doivent être accessibles à **tous les navigateurs web**
* Un balisage sémantique et épuré contient tout le contenu
* La mise en page améliorée est fournie par du CSS lié externement
* Le comportement amélioré est fourni par du JavaScript non intrusif, lié externement
* Les préférences de l'utilisateur final pour le navigateur web sont respectées

Ainsi, lorsque vous construisez votre prochain site web avec des frameworks JavaScript/CSS de nouvelle génération qui ne fonctionnent que dans l'environnement le **plus favorable** pour votre code et qui se cassent lorsqu'ils ne l'obtiennent pas... ce n'est pas une stratégie d'Amélioration Progressive.

Au lieu de cela, fixez-vous un objectif où le développement doit commencer par la fourniture de fonctionnalités de base, une stabilité sur tous les navigateurs et appareils, et une expérience transparente pour l'utilisateur avant d'introduire de la complexité.

### Exemples d'AP

Examinons quelques exemples qui montrent comment la stratégie AP fonctionne.

#### **Polices Web**

Les polices web sont magnifiques, mais lorsque l'utilisateur est sur un réseau lent avec un site lourd, elles dégradent certainement l'expérience utilisateur. Même dans cette situation, la police système doit être utilisée comme solution de repli pour rendre le contenu et peut être changée en police web dès qu'elles sont chargées.

Montrer du contenu est mieux que d'attendre les polices web — ou de ne rien obtenir.

#### **HTML Initial**

Les sites sont chargés avec des scripts. Il peut s'agir d'Angular, React ou d'un autre framework. Lorsque ces scripts sont responsables de l'affichage initial du contenu, votre utilisateur verra une page blanche sur le navigateur ou l'appareil lorsque quelque chose ne va pas avec les scripts ou lorsque l'utilisateur est sur un réseau lent.

Il est toujours bon de considérer le chargement du contenu initial à partir du HTML pour offrir une meilleure expérience utilisateur, plutôt que de dépendre entièrement des scripts qui ne sont pas encore chargés.

#### **Vérification des Fonctionnalités**

Les bons sites font toujours cette partie. Lorsque vous utilisez une fonctionnalité qui n'est pas supportée en fonction des différents navigateurs ou appareils, assurez-vous toujours de vérifier si la fonctionnalité est disponible dans le navigateur avant de l'utiliser dans votre JavaScript.

[Modernizr](https://modernizr.com/) est une bibliothèque populaire pour la détection des fonctionnalités qui peut vous aider.

Vous pouvez charger des scripts supplémentaires pour charger le support de repli uniquement lorsqu'il n'est pas disponible dans le navigateur ou l'appareil. De cette façon, vous pouvez éviter de charger des scripts supplémentaires lorsqu'ils ne sont pas nécessaires.

### Maintenant, Pourquoi l'AP ?

Raisons importantes de se concentrer sur la stratégie AP avant de construire votre prochaine application :

#### **Fondation Solide**

L'AP se concentre sur le début de votre projet en utilisant uniquement les technologies web les plus basiques avant d'introduire certaines des fonctionnalités les plus complexes. Ainsi, dans tous les cas, vous avez une fondation pour soutenir vos fonctionnalités complexes afin de vous assurer qu'elles fonctionnent.

Une fois que l'équipe est convaincue que l'expérience principale du site est stable et fonctionnera sans dépendre fortement de la vitesse du réseau, du navigateur et de l'appareil, vous pouvez alors commencer à introduire des couches de fonctionnalités plus complexes ou des éléments de science-fiction.

#### **Stabilité**

`Équipe Qualité` : « L'icône de recherche ne fonctionne pas dans Safari pour la page Offres »

`Équipe Dev` : « Eh bien, ça marche sur _ma machine_, videz le cache, rechargez ou mourrez »

`Équipe Qualité` (du ciel) : « Ça ne fonctionne toujours pas, vous vérifiez sur Chrome, ça se casse sur Safari »

`Équipe Dev` : « Quand avons-nous commencé à supporter Safari ? attendez... patching patching... »

```
if(getBrowsers() == 'safari') {
```

```
Patch.magicHelpers.searchIconMagic()
```

```
}
```

```
Patch.magicHelpers = {
```

```
searchIconMagic: function() {
```

```
// Ne peut pas partager la magie, faire quelque chose
```

```
   }};
```

« après 1 heure... vérifiez maintenant ».

`Équipe Qualité` : « Fonctionne bien pour Chrome et Safari mais cassé pour Mozilla maintenant... Ahhhhh !!!!! »

Eh bien, nous avons tous été dans cette situation au moins une fois.

Le coût de la stabilité et de la maintenance d'un projet dépend également de la manière dont le projet commence. Configurer un projet avec des frameworks et le patcher ne fonctionnera pas à long terme.

La stratégie AP vous aide à construire une fondation solide pour votre projet où votre HTML, CSS et JS sont alignés et visent à fournir des solutions de repli. Ils essaient de s'assurer que vous ne dépendez pas fortement des fonctionnalités spécifiques au navigateur.

#### **SEO et Accessibilité**

Tout le monde veut voir son application listée dans la première page des moteurs de recherche, mais cela prend _un travail et une planification constants_ pour construire de telles applications incroyables. La fondation solide de votre projet garantit que votre application se concentre sur une approche de contenu d'abord.

Les pages construites avec la stratégie AP s'assurent que le **contenu de base** est **toujours** accessible pour les araignées des moteurs de recherche et est prêt à être indexé. Évitez tout rendu de contenu dynamique qui pourrait entraver l'exploration de votre contenu par les araignées.

Les Applications Web Progressives (PWA) sont conçues pour fonctionner pour tous les utilisateurs, quel que soit leur choix de navigateur, car elles sont construites avec l'amélioration progressive comme principe de base.

### **Réflexions Finales**

La stratégie AP se concentre sur une fondation solide pour votre projet. Cette fondation solide vous aide dans votre vision pour votre produit pour un plan à long terme.

Il est facile de s'accrocher à un nouveau framework JavaScript/CSS pour votre nouveau projet et de commencer à coder, mais cela peut conduire à une Dégradation Gracieuse. Vous continuerez à patcher votre code avec des solutions de repli pour les navigateurs ou appareils qui ne supportent pas les frameworks.

Bien que la stratégie AP nécessite un peu plus de planification dans les étapes initiales, elle garantit que votre utilisateur est capable d'expérimenter au moins les fonctionnalités de base même dans le pire des cas. L'AP n'est pas applicable dans les situations qui dépendent fortement de JavaScript pour atteindre certaines présentations ou comportements d'interface utilisateur, mais pour un projet à long terme, il vaut la peine de considérer certains aspects de la stratégie AP.

J'espère que cela a donné un aperçu de la Stratégie d'Amélioration Progressive.

N'hésitez pas à laisser un commentaire ci-dessous.

Merci d'avoir lu cet article ! Si vous avez des questions, envoyez-moi un email (praveend806 [at] gmail [dot] com).

Ressources qui parlent plus de l'AP et des études de cas :

[**Concevoir avec l'Amélioration Progressive : Construire le Web qui fonctionne pour tout le monde**](https://www.oreilly.com/library/view/designing-with-progressive/9780321659477/)  
[_L'amélioration progressive est une approche du développement web qui vise à offrir la meilleure expérience possible aux..._www.oreilly.com](https://www.oreilly.com/library/view/designing-with-progressive/9780321659477/)[**Unboring.net | Workflow : Appliquer l'Amélioration Progressive sur un projet WebVR**](https://unboring.net/workflows/progressive-enhancement/)  
[_Comment j'ai créé un contenu interactif à intégrer sur weather.com_unboring.net](https://unboring.net/workflows/progressive-enhancement/)