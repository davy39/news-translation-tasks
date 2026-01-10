---
title: Meilleures pratiques React – Conseils pour écrire un meilleur code React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-03T16:41:47.000Z'
originalURL: https://freecodecamp.org/news/best-practices-for-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/React-Best-Practices-Thumbnail.png
tags:
- name: best practices
  slug: best-practices
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Meilleures pratiques React – Conseils pour écrire un meilleur code React
seo_desc: 'By Jean-Marc Möckel

  Two years ago, I started to learn and use React. And today I''m still using it at
  my day job as a Software Developer and in my own side projects.

  During that time I''ve come across a lot of "typical" issues. So I searched around
  and...'
---

Par Jean-Marc Möckel

Il y a deux ans, j'ai commencé à apprendre et à utiliser React. Et aujourd'hui, je l'utilise toujours dans mon travail de développeur logiciel et dans mes propres projets personnels.

Pendant cette période, j'ai rencontré beaucoup de problèmes "typiques". J'ai donc cherché et trouvé quelques bonnes pratiques que j'ai intégrées à mon flux de travail, et j'ai élaboré des choses qui ont facilité ma vie ou celle des membres de ma équipe.

J'ai également rencontré des défis en cours de route que je n'ai pas résolus de la meilleure façon à l'époque, et je veux les aborder de manière plus efficace à l'avenir.

C'est la raison pour laquelle j'ai écrit ce guide. Je le considère comme une collection de conseils que je me serais donnés il y a deux ans lorsque j'ai commencé.

## Table des matières :

* [Trois grands défis auxquels les développeurs React sont confrontés](#heading-trois-grands-defis-auxquels-les-developpeurs-react-sont-confrontes)

* [Apprendre les bases de React](#heading-apprendre-les-bases-de-react)

* [Apprendre à construire des composants React propres, performants et maintenables](#heading-apprendre-a-construire-des-composants-react-propres-performants-et-maintenables)

* [Conseils pour vous aider à écrire un meilleur code React – La cerise sur le gâteau](#heading-conseils-pour-vous-aider-a-ecrire-un-meilleur-code-react-la-cerise-sur-le-gateau)

* [Mots de la fin](#heading-mots-de-la-fin)

Tout d'abord, vous allez découvrir les **trois grands défis** auxquels chaque développeur React doit faire face. C'est important car lorsque vous êtes conscient des défis potentiels, vous comprendrez les raisons derrière ces bonnes pratiques de manière plus approfondie. Avoir cet état d'esprit dès le début vous aide également lors de la conception de vos composants ou de l'organisation de votre projet.

Après cette première étape importante, je vous présenterai les **trois meilleures pratiques**. Elles sont un mélange de conseils théoriques et pratiques avec des exemples de code. J'essaie de minimiser les *problèmes de hello world* et de venir avec du code que j'ai vu dans le *monde réel*.

## Trois grands défis auxquels les développeurs React sont confrontés

![Image](https://www.freecodecamp.org/news/content/images/2022/01/christian-erfurt-sxQz2VfoFBE-unsplash.jpg align="left")

Pendant mes deux années d'utilisation quotidienne de React, j'ai reconnu trois grands défis auxquels les développeurs React sont confrontés lors de la construction de leurs applications. Ignorer ces défis pourrait entraîner des moments difficiles qui nuisent à la croissance de votre application.

Gardez donc ces défis à l'esprit lorsque vous orchestrez votre application, car cela vous fera gagner du temps et de l'énergie.

### ⚒️ Maintenabilité

Cela va de pair avec la *réutilisabilité*. Au début, lorsque l'application et les composants sont très légers, ils sont faciles à maintenir. Mais une fois que les exigences commencent à croître, les composants tendent à devenir très complexes et donc moins maintenables.

J'ai souvent vu un composant qui a de nombreux cas différents, chacun représentant un résultat différent. Le JSX est inondé de rendus conditionnels (opérateurs ternaires et simples opérateurs `&&`), les classnames sont appliqués de manière conditionnelle, ou le composant utilise une énorme instruction `switch`. Il existe de nombreuses valeurs de props et d'état possibles, chacune responsable d'un résultat différent.

Il n'y a rien de mal avec ces techniques en elles-mêmes, à mon avis. Mais je pense que chacun devrait développer un sentiment pour savoir quand un composant commence à devenir moins maintenable et quand ces techniques deviennent surutilisées. Nous apprendrons plus tard dans l'article comment mieux contrôler cela.

Le problème (et j'en ai été coupable moi aussi) est que plus un composant a de complexité et de résultats différents (polymorphisme), plus il devient difficile à maintenir.

Pour être honnête, la cause profonde est souvent la paresse, le manque d'expérience, ou la pression du temps pour refactoriser correctement un composant afin de le rendre plus maintenable et plus propre.

Un autre facteur clé que j'ai observé est l'absence ou le peu de tests. Je sais, les tests ne sont pas un type de travail que beaucoup de développeurs aiment, mais cela peut vraiment vous aider à long terme. Les tests eux-mêmes ne seront pas un sujet majeur dans cet article, alors restez à l'affût pour un autre article de blog de ma part à ce sujet.

### 🧠 Compréhension solide de React

Une autre cause profonde des problèmes des développeurs React est une mauvaise compréhension de base du fonctionnement de React sous le capot. J'ai été là aussi.

J'ai vu beaucoup de gens sauter trop vite dans des concepts intermédiaires ou avancés sans avoir une base solide. Mais ce n'est pas seulement particulier à React. C'est un problème général en programmation.

Ne pas avoir une compréhension solide de React peut également causer des problèmes pour vous en tant que développeur. Je me souviens avoir eu des maux de tête lorsque je voulais utiliser différents cycles de vie des composants mais que je ne savais pas comment les utiliser. J'ai donc dû faire quelques pas en arrière et approfondir ce sujet.

Parce que je pense que c'est l'une des choses les plus importantes, j'ai dédié un chapitre entier à ce sujet dans cet article de blog ci-dessous.

### 📈 Évolutivité

Ce défi va de pair avec la *maintenabilité*. Il n'est pas seulement spécifique à React, mais s'applique généralement en logiciel.

J'ai appris que créer un excellent logiciel ne concerne pas seulement l'UX, les modèles de code propre, ou l'architecture intelligente, par exemple. Pour moi, la qualité d'un logiciel augmente ou diminue également avec sa capacité à évoluer.

À mon avis, de nombreuses choses entrent en jeu pour augmenter l'évolutivité du logiciel. Vous apprendrez mes conseils les plus importants dans cet article.

Je pense que lorsque vous gardez à l'esprit la *maintenabilité* et l'*évolutivité* lors de l'orchestration de vos composants et de l'organisation de votre structure de projet, vous aurez moins de chances de vous retrouver avec un désordre de code source qui nécessite une refactorisation majeure.

# Comment apprendre React

D'accord, plongeons maintenant plus profondément dans quelques bonnes pratiques pour apprendre React.

## Apprendre les bases de React

![Image](https://www.freecodecamp.org/news/content/images/2022/01/brett-jordan-Lzfxzip-pNI-unsplash.jpg align="left")

Comme nous l'avons brièvement discuté ci-dessus, manifester les bases n'est pas seulement pertinent pour apprendre React, mais aussi pour d'autres technologies ou langages de programmation. Vous ne pouvez pas construire un gratte-ciel sur une fondation sableuse et vous attendre à ce qu'il soit solide.

Cela peut sembler évident pour beaucoup d'entre vous, mais j'ai vu des développeurs qui ont sauté dans les concepts intermédiaires ou avancés de React sans vraiment comprendre les bases.

Cela est également vrai pour JavaScript en général. Je suis un grand croyant que l'apprentissage de React n'a pas de sens si vous n'avez pas une base solide en JavaScript Vanilla.

Donc, si cela vous semble familier et que vous pensez à apprendre React mais que vous ne vous sentez pas très à l'aise avec JavaScript Vanilla, passez un peu plus de temps à renforcer JavaScript d'abord. Cela vous fera gagner beaucoup de maux de tête et de temps à l'avenir.

Voici un guide utile sur les [concepts JavaScript essentiels à connaître avant de plonger dans React](https://www.freecodecamp.org/news/top-javascript-concepts-to-know-before-learning-react/) si vous souhaitez réviser.

Mais connaître les bases seules ne suffit pas pour moi. C'est un peu obligatoire de savoir comment React fonctionne sous le capot. Si vous voulez devenir un bon développeur React (ce que je suppose que vous voulez, puisque vous lisez cet article), vous devez connaître l'outil que vous utilisez. Cela est bénéfique pour vous en tant que développeur et pour vos clients également.

D'une part, cela peut vous faire gagner beaucoup de temps en débogant votre application. D'autre part, cela vous rend plus efficace car vous n'avez pas à faire quelques pas en arrière pour réapprendre les bases encore et encore. Vous savez essentiellement de quoi vous parlez.

Bien sûr, vous ne pouvez pas tout savoir et vous ne devriez pas vous stresser sur ce sujet. Vous apprendrez de plus en plus en passant par des problèmes pratiques et en construisant plus de projets. Mais avec une bonne connaissance solide, vous êtes bien équipé dès le début.

D'accord, cela a du sens. Mais vous vous demandez peut-être ce que vous devez exactement savoir pour avoir une base solide en React ?

En tant que minimum absolu, vous devriez comprendre tous les sujets à l'intérieur du chapitre [**Concepts principaux**](https://reactjs.org/docs/hello-world.html) à l'intérieur de la documentation officielle de React.

Un autre [chapitre que vous devriez bien connaître est celui sur les **Hooks**](https://reactjs.org/docs/hooks-intro.html) car ils sont devenus une convention et sont utilisés partout, surtout dans les packages React tiers.

Bien sûr, il y en a certains que vous utiliserez plus souvent comme `useState` et `useEffect`, mais comprendre les autres comme `useMemo`, `useCallback` ou `useRef` est également essentiel.

Il y a aussi [un autre chapitre appelé **Guides avancés**](https://reactjs.org/docs/accessibility.html) que je ne considérerais pas comme obligatoire au début, mais je vous recommande vivement de saisir ces concepts pendant votre parcours React.

Comme toujours, il est souvent plus facile de comprendre les sujets avancés lorsque vous avez déjà une certaine expérience pratique. Mais plus vous comprenez ces choses tôt, mieux c'est.

Bien sûr, vous ne devriez pas vous limiter à suivre uniquement la documentation React. Travailler à travers un cours en ligne qui couvre ces bases, regarder des tutoriels ou lire d'autres articles de blog fait également partie de la construction d'une base solide. Donc, testez ce qui fonctionne le mieux pour vous.

Si je devais choisir les concepts les plus importants à connaître au minimum, je suggérerais ceux-ci :

* qu'est-ce que l'« état » ?

* avantages et inconvénients des composants de classe et fonctionnels

* qu'est-ce que les re-rendus de composants et comment fonctionnent-ils ?

* comment déclencher des re-rendus

* différents cycles de vie des composants et comment interagir avec eux

* Virtual DOM

* Avantages du CSR (Client Side Rendering) et du SSR (Server Side Rendering) en général et dans React

* Composants contrôlés vs non contrôlés

* Élévation d'état

* au moins une technologie de gestion d'état global (Context API, Redux/Toolkit, Recoil)

* Modèles de composants (surtout comment choisir le bon modèle)

## Apprendre à construire des composants React propres, performants et maintenables

![Image](https://www.freecodecamp.org/news/content/images/2022/01/wesley-tingey-mvLyHPRGLCs-unsplash.jpg align="left")

Je sais – c'est le rêve de tout programmeur (ou du moins je l'espère). Et pour moi, cette capacité sépare un bon programmeur d'un excellent programmeur. La partie amusante est que ce n'est jamais vraiment terminé car il y a toujours quelque chose à apprendre et à améliorer.

Suivre ces bonnes pratiques ne facilitera pas seulement les choses pour vous, mais aussi pour vos coéquipiers. J'ai vu des équipes de développement qui ont créé un *guide de style* où elles ont défini des pierres angulaires importantes sur la façon dont elles écrivent du code. Très bonne idée si vous me le demandez.

Certains d'entre eux étaient :

* utiliser des composants fonctionnels (comme les fonctions fléchées)

* ne pas utiliser de styles en ligne

* maintenir une structure d'importation appropriée (importations tierces en premier --&gt; importations internes en dessous)

* formater votre code avant de commiter

Et ainsi de suite.

Bien sûr, vous pouvez être très détaillé à ce sujet. Cela dépend de votre équipe. Personnellement, je n'aime pas les guides de style très détaillés car je pense que vous devriez avoir une certaine liberté en tant que développeur qualifié et ne pas être trop restreint.

Mais un guide de style en général est un bon moyen de définir et de maintenir les meilleures pratiques et de s'assurer que votre équipe est sur la même longueur d'onde concernant certains domaines importants. Je pense que cela augmente considérablement le travail d'équipe et la production.

Examinons quelles sont ces meilleures pratiques pour créer des composants qui sont propres, performants et maintenables. Installez-vous confortablement, prenez quelque chose pour prendre des notes et profitez-en !

### 📁 Créer une bonne structure de dossiers

Organiser vos fichiers et dossiers à l'intérieur de votre application React est obligatoire pour la maintenabilité et l'évolutivité.

Une **bonne** structure de dossiers dépend de la taille de votre application et de votre équipe. Il n'y a donc pas de réponse générale à cela. Surtout parce que c'est un sujet très subjectif et dépend également des préférences personnelles.

Mais avec le temps, certaines bonnes pratiques pour différentes tailles d'application ont évolué.

[Cet excellent article de blog](https://www.robinwieruch.de/react-folder-structure/) passe en revue cinq tailles d'application différentes et présente de bonnes idées sur la façon d'organiser vos fichiers et dossiers. Avoir cela à l'esprit lors de la planification ou du démarrage de votre application peut faire une énorme différence à long terme.

Ne le sur-ingéniez pas, mais essayez de maintenir une structure appropriée qui convient le mieux à votre application actuelle et à la taille de votre équipe.

### 👆 Maintenir un ordre d'importation structuré

Si vous avez déjà une certaine expérience avec React, vous avez peut-être vu des fichiers qui sont gonflés avec beaucoup d'instructions d'importation. Ils peuvent également être mélangés avec des importations externes de packages tiers et des importations internes comme d'autres composants, des fonctions utilitaires, des styles et bien plus encore.

Exemple du monde réel (coupé) :

```javascript
import React, { useState, useEffect, useCallback } from "react";
import Typography from "@material-ui/core/Typography";
import Divider from "@material-ui/core/Divider";
import Title from "../components/Title";
import Navigation from "../components/Navigation";
import DialogActions from "@material-ui/core/DialogActions"
import { getServiceURL } from '../../utils/getServiceURL";
import Grid from "@material-ui/core/Grid";
import Paragraph from "../components/Paragprah";
import { sectionTitleEnum } from "../../constants";
import { useSelector, useDispatch } from "react-redux";
import Box from "@material-ui/core/Box";
import axios from 'axios';
import { DatePicker } from "@material-ui/pickers";
import { Formik } from "formik";
import CustomButton from "../components/CustomButton";
...
```

Vous reconnaissez probablement le problème ici. Il est difficile de distinguer ce qui est toutes les importations tierces et les importations locales (internes). Elles ne sont pas regroupées et semblent être partout.

Meilleure version :

```javascript
import React, { useState, useEffect, useCallback } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Formik } from "formik";
import axios from 'axios';
import Typography from "@material-ui/core/Typography";
import Divider from "@material-ui/core/Divider";
import Box from "@material-ui/core/Box";
import DialogActions from "@material-ui/core/DialogActions";
import Grid from "@material-ui/core/Grid";
import { DatePicker } from "@material-ui/pickers";

import { getServiceURL } from '../../utils/getServiceURL";
import { sectionTitleEnum } from "../../constants";
import CustomButton from "../components/CustomButton";
import Title from "../components/Title";
import Navigation from "../components/Navigation";
import Paragraph from "../components/Paragraph";
...
```

La structure est plus claire et il est très facile de distinguer où se trouvent les importations externes et internes. Bien sûr, vous pouvez l'optimiser davantage si vous utilisez plus d'importations nommées (si c'est possible ! :) ). Cela vous permet d'importer tous les composants provenant de material-ui en une seule ligne.

J'ai vu d'autres développeurs qui aiment diviser la structure d'importation en trois parties différentes :

Intégrées (comme 'react') --&gt; Externes (modules node tiers) --&gt; Internes.

Vous pouvez le gérer vous-même à chaque fois ou laisser un **linter** faire le travail. [Voici](https://dev.to/otamnitram/sorting-your-imports-correctly-in-react-213m) un excellent article sur la façon de configurer votre linter pour votre application React afin de maintenir une structure d'importation appropriée.

### 📖 Apprendre différents modèles de composants

Pour vous assurer de ne pas vous retrouver avec un code spaghetti non maintenable et non évolutif, apprendre différents modèles de composants est essentiel à mesure que vous devenez plus expérimenté dans React.

Mais ce n'est pas tout. Connaître les différents modèles est une bonne base. Mais l'aspect le plus important est que vous savez **quand** utiliser quel modèle pour votre problème.

Chaque modèle sert un but précis. Par exemple, le **modèle de composant composé** évite le *prop-drilling* inutile de nombreux niveaux de composants. Donc, la prochaine fois que vous commencez à passer des props à travers cinq niveaux de composants pour enfin atteindre le composant qui est intéressé par les props, vous commencez à orchestrer les composants différemment.

Une petite note ici sur le prop-drilling, car j'ai eu beaucoup de discussions à ce sujet dans le passé. Il y a beaucoup d'opinions sur le fait que c'est mauvais ou non. Pour ma part, j'essaie de penser à une autre façon / un autre modèle si je commence à passer des props à travers plus de deux niveaux de composants.

Ce fait vous rend plus efficace en tant que développeur et rend les composants que vous écrivez plus maintenables ou évolutifs. Avoir ces modèles dans votre boîte à outils vous distingue également des autres développeurs React. Je vous encourage vivement à faire vos propres recherches, mais [ce](https://www.udemy.com/course/the-complete-guide-to-advanced-react-patterns/) cours Udemy m'a beaucoup aidé.

### 🔍 Utiliser un linter et suivre ses règles

Un linter ne vous aide pas seulement à maintenir un ordre d'importation distinguable de vos dépendances. Il vous aide à écrire un meilleur code en général.

Lorsque vous utilisez *create-react-app*, ESLint est déjà configuré, mais vous pouvez également le configurer complètement par vous-même ou étendre les règles d'un ensemble de règles préconfiguré.

Un linter observe essentiellement le code JavaScript que vous écrivez et vous rappelle les erreurs que vous attraperiez plus probablement lors de l'exécution du code. Il m'a fallu un certain temps pour vraiment apprécier l'utilisation d'un linter, mais aujourd'hui je ne peux plus imaginer travailler sans lui.

Avoir le linter est une chose, mais suivre ses règles en est une autre. Bien sûr, vous pouvez le désactiver. Soit pour une ligne de code spécifique, soit pour le fichier entier. Il peut y avoir des cas où cela a du sens, mais selon mon expérience, ils sont assez rares.

Un autre grand avantage est que vous pouvez également ajuster la vérification du style. Cela est particulièrement utile pour les équipes. Une fois que vous avez convenu de certaines conventions sur la façon dont vous écrivez votre code et comment il doit être formaté, vous pouvez facilement combiner ESLint avec quelque chose comme JSPrettify.

### 🧪 Tester votre code

Je sais, les tests ne sont probablement pas votre tâche préférée en tant que développeur. J'étais comme ça. Au début, cela semblait être une tâche inutile et perturbatrice. Cela peut être vrai à court terme. Mais à long terme – et lorsque l'application grandit – c'est vital.

Pour moi, les tests sont devenus une pratique qui garantit que je fais mon travail de manière plus professionnelle et que je livre des logiciels de meilleure qualité.

En principe, il n'y a rien de mal avec les tests manuels par un humain et cela ne devrait pas être évité complètement. Mais imaginez que vous intégrez une nouvelle fonctionnalité et que vous voulez vous assurer que rien n'est cassé. Cela peut être une tâche chronophage et sujette à l'erreur humaine.

Pendant que vous écrivez des tests, vous êtes déjà dans le processus de réflexion sur la façon d'organiser votre code afin de passer ce test. Pour moi, cela est toujours utile car je reconnais les pièges qui peuvent survenir et que je dois surveiller.

Vous ne sautez pas directement dans l'écriture de votre code non plus (ce que je ne recommande pas du tout), mais vous réfléchissez d'abord à l'objectif.

Par exemple, "Que devrait faire ce composant particulier ? Quels cas limites importants peuvent survenir que je dois tester ? Puis-je rendre le composant plus pur pour qu'il ne serve qu'un seul but ? ..."

Avoir une vision pour le code que vous êtes sur le point d'écrire vous aide également à maintenir une concentration aiguë sur la réalisation de cette vision.

Les tests peuvent également servir de documentation, car pour un nouveau développeur qui découvre la base de code, cela peut être très utile pour comprendre les différentes parties du logiciel et comment elles sont censées fonctionner.

Donc, n'évitez pas les tests parce que cela semble être un *travail supplémentaire*. La réalité est que cela peut vous éviter un travail supplémentaire à l'avenir lorsque vous le configurez correctement.

Jetez un coup d'œil au chapitre ["Testing"](https://reactjs.org/docs/testing.html) dans la documentation React, parcourez quelques tutoriels sur les tests dans React, et commencez simplement à écrire votre première petite application TDD ou implémentez des tests dans une application sur laquelle vous travaillez actuellement.

### 🤖 Intégrer TypeScript (ou au moins utiliser des props par défaut et des types de props)

Je me souviens de mon premier projet React en tant que développeur logiciel où notre équipe a reçu un projet qui était déjà essentiellement écrit par une autre entreprise. Ensuite, nous avons dû construire le projet du client sur celui-ci, et TypeScript avait déjà été intégré.

Jusqu'à ce moment-là, mes coéquipiers et moi n'avions pas beaucoup d'expérience en TypeScript puisque nous venions tous d'un arrière-plan JavaScript vanilla.

Après quelques semaines de travail sur ce projet, nous avons senti que TypeScript n'était pas un avantage, mais plutôt un obstacle qui nous bloquait dans notre flux de travail. Nous n'utilisions pas non plus vraiment les avantages de celui-ci car nous définissions tout avec le type *any* pour supprimer les avertissements TypeScript.

Cela nous a conduit à la décision de supprimer TypeScript du projet et de travailler sur notre terrain connu avec JavaScript vanilla. Cela s'est bien passé au début, mais plus notre projet devenait complexe, plus les erreurs de type émergeaient. Nous avons donc beaucoup douté de notre décision de nous débarrasser complètement de TypeScript. Mais ces choses peuvent arriver et nous ont donné des expériences précieuses pour l'avenir.

Cette circonstance m'a conduit à donner une autre chance à TypeScript, et je l'ai appris pendant mon temps libre. Après avoir construit quelques projets secondaires avec celui-ci, je ne peux plus imaginer une vie sans lui.

L'utilisation de TypeScript présente de nombreux avantages comme la vérification de type statique, une meilleure complétion de code dans votre IDE (intellisense), une expérience développeur améliorée, et la détection d'erreurs de type pendant que vous écrivez le code – pour n'en nommer que quelques-uns.

D'autre part, cela peut présenter certains défis, bien sûr, car si vous ne venez pas d'un arrière-plan avec des langages fortement typés (comme Java ou C#), cela peut être plus difficile au début pour le comprendre.

Mais je peux dire que cela vaut vraiment la peine de l'apprendre et de l'intégrer. [Voici](https://blog.bitsrc.io/5-strong-reasons-to-use-typescript-with-react-bc987da5d907) un bel article qui peut vous aider à obtenir un aperçu des avantages et des inconvénients de l'utilisation de TypeScript dans les applications React. Et [voici un tutoriel](https://www.freecodecamp.org/news/how-to-code-your-react-app-with-typescript/) sur la façon de coder vos applications React en TypeScript.

Il peut y avoir des raisons pour lesquelles vous ne souhaitez pas utiliser TypeScript dans votre application React. C'est bien. Mais au minimum, je recommande d'utiliser **prop-types** et **default-props** pour vos composants afin de vous assurer de ne pas mélanger vos props.

### 🧩 Utiliser le chargement paresseux / la division de code

Si vous avez passé du temps dans l'univers JavaScript et React, vous avez probablement rencontré le **bundling**. Pour ceux d'entre vous qui entendent ce terme pour la première fois, voyons ce que disent les docs React officielles :

> La plupart des applications React auront leurs fichiers "bundled" en utilisant des outils comme Webpack, Rollup ou Browserify. Le bundling est le processus de suivi des fichiers importés et de leur fusion en un seul fichier : un "bundle". Ce bundle peut ensuite être inclus sur une page web pour charger une application entière en une seule fois.

En principe, c'est une excellente technique, mais avec la croissance de votre application vient un défi. Votre bundle commence également à croître. Surtout lorsque vous utilisez de grandes bibliothèques tierces comme three.js.

Le piège est que ce bundle doit toujours être chargé complètement, même lorsque l'utilisateur n'a besoin que d'une fraction du code. Cela conduit à des problèmes de performance car cela peut prendre un temps inutilement long pour charger votre application.

Pour éviter cela, il existe une technique appelée **code splitting** où vous divisez votre bundle en morceaux de code dont votre utilisateur a besoin. Cela est pris en charge par les bundlers les plus courants comme Webpack, Rollup et Browserify. Le grand avantage est que vous pouvez créer plusieurs bundles et les charger dynamiquement.

Diviser votre bundle vous aide à **charger paresseusement** uniquement les choses dont l'utilisateur a besoin.

Pour illustrer cela, imaginez que vous entrez dans une épicerie et que vous voulez simplement prendre des bananes, des pommes et du pain. Dans ce cas, vous n'achetez pas toute la gamme du magasin et puis vous prenez vos bananes, pommes et pain. Vous n'êtes intéressé que par une fraction de la gamme. Alors pourquoi acheteriez-vous tout ? Cela prendrait beaucoup plus de temps et est bien sûr plus cher.

Je pense qu'il est important d'être conscient des défis potentiels qui peuvent survenir à mesure que votre application grandit, et qu'il existe certaines techniques pour se débarrasser de ces problèmes. Pour plus de lectures, consultez la [documentation React](https://reactjs.org/docs/code-splitting.html).

### 🔧 Extraire la logique réutilisable dans des hooks personnalisés

Selon la documentation React,

> *Les Hooks nous permettent de réutiliser la logique avec état sans changer notre hiérarchie de composants.*

En principe, ils sont une meilleure solution aux techniques qui étaient utilisées auparavant en combinaison avec les composants de classe. Si vous avez codé pendant un certain temps, vous vous souvenez peut-être de l'utilisation des **Higher Order Components** ou des **render props.**

Chaque fois que vous vous trouvez dans une situation où vous devez réutiliser la même logique avec état qui est déjà utilisée dans un autre composant fonctionnel, c'est le moment idéal pour créer un hook personnalisé. À l'intérieur, vous encapsulez la logique et n'avez qu'à appeler le hook en tant que fonction à l'intérieur de vos composants.

Prenons un exemple rapide où nous devons mettre à jour notre UI en fonction de la taille de l'écran et voulons suivre la taille actuelle de la fenêtre lors du redimensionnement manuel de la fenêtre du navigateur.

```jsx
const ScreenDimensions = () => {
  const [windowSize, setWindowSize] = useState({
    width: undefined,
    height: undefined,
  });
  
  useEffect(() => {
    function handleResize() {
      setWindowSize({
        width: window.innerWidth,
        height: window.innerHeight,
      });
    }
    window.addEventListener('resize', handleResize);
    handleResize();
    return () => window.removeEventListener('resize', handleResize);
  }, []);
  
  return (
  	<>
    	<p>Current screen width: {windowSize.width}</p>
        <p>Current screen height: {windowSize.height}</p>
    </>
  )
}
```

Comme vous pouvez le voir, la solution est assez simple et il n'y a rien de mal à la définir comme ceci.

Maintenant vient la partie délicate. Imaginez que nous aimerions utiliser la logique exacte dans un autre composant, où nous allons rendre une UI différente (une pour les smartphones et une pour les ordinateurs de bureau) en fonction de la taille actuelle de l'écran.

Bien sûr, nous pourrions simplement copier la logique, la coller et nous avons terminé. Mais ce n'est pas une bonne pratique, comme vous le savez peut-être du principe DRY.

Si nous voulions ajuster notre logique, nous devrions le faire dans les deux composants. Et lorsque nous collons notre logique dans encore plus de composants, cela devient moins maintenable et plus sujet aux erreurs.

Alors, que feriez-vous normalement dans un projet JavaScript vanilla ? Vous définiriez probablement une fonction qui encapsule la logique et peut être utilisée à de nombreux endroits différents. C'est exactement ce que nous allons réaliser avec les hooks. Ils ne sont rien de plus que des fonctions JavaScript mais avec quelques particularités React car ils utilisent des hooks React.

Voyons à quoi ressemblerait notre hook personnalisé :

```jsx
const useWindowSize = () => {
  const [windowSize, setWindowSize] = useState({
    width: undefined,
    height: undefined,
  });
  
  useEffect(() => {
    function handleResize() {
      setWindowSize({
        width: window.innerWidth,
        height: window.innerHeight,
      });
    }
    window.addEventListener('resize', handleResize);
    handleResize();
    return () => window.removeEventListener('resize', handleResize);
  }, []);
  
  return windowSize;
}
```

Maintenant, appelons-le simplement à l'intérieur de notre composant **ScreenDimensions** :

```jsx
const ScreenDimensions = () => {
  const windowSize = useWindowSize()
  
  return (
  	<>
    	<p>Current screen width: {windowSize.width}</p>
        <p>Current screen height: {windowSize.height}</p>
    </>
  )
}
```

Cela nous permet de simplement appeler le hook personnalisé dans n'importe quel autre composant et de sauvegarder la valeur de retour (qui est la taille actuelle de la fenêtre) dans une variable que nous pouvons utiliser à l'intérieur du composant.

```jsx
const ResponsiveView = () => {
  const windowSize = useWindowSize()
  
  return (
  	<>
    	{windowSize.width <= 960 ? (
          <SmartphoneView />
        ) : (
          <DesktopView />	
        )}
    </>
  )
}
```

### 🛠️ Gérer les erreurs efficacement

La gestion efficace des erreurs est souvent négligée et sous-estimée par de nombreux développeurs. Comme beaucoup d'autres bonnes pratiques, cela semble être une réflexion après coup au début. Vous voulez faire fonctionner le code et ne voulez pas "perdre" de temps à réfléchir aux erreurs.

Mais une fois que vous êtes devenu plus expérimenté et que vous avez été dans des situations désagréables où une meilleure gestion des erreurs aurait pu vous faire économiser beaucoup d'énergie (et de temps précieux bien sûr), vous réalisez que c'est obligatoire à long terme d'avoir une gestion des erreurs solide à l'intérieur de votre application. Surtout lorsque l'application est déployée en production.

Mais que signifie exactement *gestion des erreurs* dans le monde React ? Il y a quelques parties différentes qui jouent un rôle. L'une est de **capturer** les erreurs, une autre de **gérer** l'UI en conséquence, et la dernière de les **journaliser** correctement.

#### Limite d'erreur React

C'est un composant de classe personnalisé qui est utilisé comme un wrapper de votre application entière. Bien sûr, vous pouvez également envelopper le composant ErrorBoundary autour de composants qui sont plus profonds dans l'arbre des composants pour rendre une UI plus spécifique, par exemple. En principe, c'est aussi une bonne pratique d'envelopper l'ErrorBoundary autour d'un composant qui est sujet aux erreurs.

Avec la méthode de cycle de vie `componentDidCatch()` vous êtes en mesure de capturer les erreurs pendant la phase de rendu ou tout autre cycle de vie des composants enfants. Donc, lorsqu'une erreur survient pendant cette phase, elle remonte et est capturée par le composant ErrorBoundary.

Si vous utilisez un service de journalisation (que je recommande également vivement), c'est un excellent endroit pour s'y connecter.

La fonction statique `getDerivedStateFromError()` est appelée pendant la phase de rendu et est utilisée pour mettre à jour l'état de votre composant ErrorBoundary. Sur la base de votre état, vous pouvez rendre conditionnellement une UI d'erreur.

```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    // journaliser l'erreur vers un service de rapport d'erreurs
    errorService.log({ error, errorInfo });
  }

  render() {
    if (this.state.hasError) {
      return <h1>Oups, quelque chose s'est mal passé.</h1>;
    }
    return this.props.children; 
  }
}
```

Le grand inconvénient de cette approche est qu'elle ne gère pas les erreurs dans les rappels asynchrones, sur le rendu côté serveur, ou dans les gestionnaires d'événements car ils sont en dehors de la limite.

#### Utiliser try-catch pour gérer les erreurs au-delà des limites

Cette technique est efficace pour capturer les erreurs qui peuvent survenir à l'intérieur des rappels asynchrones. Imaginons que nous récupérons les données de profil d'un utilisateur à partir d'une API et que nous voulons les afficher à l'intérieur d'un composant de profil.

```jsx
const UserProfile = ({ userId }) => {
	const [isLoading, setIsLoading] = useState(true)
	const [profileData, setProfileData] = useState({})
    
    useEffect(() => {
    	// Fonction séparée pour utiliser async
        const getUserDataAsync = async () => {
        	try {
            	// Récupérer les données de l'utilisateur depuis l'API
            	const userData = await axios.get(`/users/${userId}`)
                // Lancer une erreur si les données de l'utilisateur sont falsy (sera capturé par catch)
                if (!userData) {
                	throw new Error("Aucune donnée utilisateur trouvée")
                }
                // Si les données de l'utilisateur sont truthy, mettre à jour l'état
                setProfileData(userData.profile)
            } catch(error) {
            	// Journaliser toute erreur capturée dans le service de journalisation
            	errorService.log({ error })
                // Mettre à jour l'état 
                setProfileData(null)
            } finally {
            	// Réinitialiser l'état de chargement dans tous les cas
                setIsLoading(false)
            }
        }
        
        getUserDataAsync()
    }, [])
    
    if (isLoading) {
    	return <div>Chargement ...</div>
    }
    
    if (!profileData) {
    	return <ErrorUI />
    }
    
    return (
    	<div>
        	...Profil de l'utilisateur
        </div>
    )
}
```

Lorsque le composant est monté, il commence une requête GET vers notre API pour recevoir les données de l'utilisateur correspondant à l'userId que nous obtiendrons des props.

L'utilisation de try-catch nous aide à capturer toute erreur qui pourrait survenir lors de cet appel API. Par exemple, cela pourrait être une réponse 404 ou 500 de l'API.

Une fois qu'une erreur est capturée, nous sommes dans le bloc catch et recevons l'erreur en tant que paramètre. Maintenant, nous sommes en mesure de la journaliser dans notre service de journalisation et de mettre à jour l'état en conséquence pour afficher une UI d'erreur personnalisée.

#### Utiliser la bibliothèque react-error-boundary (recommandation personnelle)

Cette bibliothèque fusionne essentiellement ces deux techniques ci-dessus. Elle simplifie la gestion des erreurs dans React et surmonte les limitations du composant ErrorBoundary que nous avons vues ci-dessus.

```jsx
import { ErrorBoundary } from 'react-error-boundary'

const ErrorComponent = ({ error, resetErrorBoundary }) => {
  
  return (
    <div role="alert">
      <p>Quelque chose s'est mal passé :</p>
      <pre>{error.message}</pre>
    </div>
  )
}

const App = () => {
  const logError = (error, errorInfo) => {
  	errorService.log({ error, errorInfo })
  }
  

  return (
    <ErrorBoundary 
       FallbackComponent={ErrorComponent}
       onError={logError}
    >
       <MyErrorProneComponent />
    </ErrorBoundary>
  );
}
```

La bibliothèque exporte un composant qui est constitué de la fonctionnalité ErrorBoundary que nous connaissons déjà et y ajoute quelques nuances. Elle vous permet de passer un `FallbackComponent` en tant que prop qui doit être rendu une fois qu'une erreur a été capturée.

Elle expose également une prop `onError` qui fournit une fonction de rappel lorsqu'une erreur survient. C'est idéal pour l'utiliser afin de journaliser l'erreur vers un service de journalisation.

Il y a quelques autres props qui sont assez utiles. Si vous souhaitez en savoir plus, n'hésitez pas à consulter [la documentation](https://www.npmjs.com/package/react-error-boundary?activeTab=readme).

Cette bibliothèque fournit également un hook appelé `useErrorHandler()` qui est destiné à capturer toute erreur qui est en dehors des limites comme les gestionnaires d'événements, dans le code asynchrone et dans le rendu côté serveur.

#### Journalisation des erreurs

Capturer et gérer les erreurs efficacement est une partie, les journaliser correctement en est une autre. Une fois que vous avez configuré votre gestion des erreurs à l'intérieur de votre application, vous devez les journaliser de manière persistante.

La manière la plus fréquemment utilisée est le bon vieux **console.log**. Cela peut être bien pendant le développement lorsque vous voulez un journal rapide, mais une fois que votre application est déployée en production, cela devient inutile. Cela est dû au fait que vous ne voyez l'erreur que dans le navigateur de l'utilisateur, ce qui n'est pas efficace du tout.

Lorsque vous journalisez des erreurs en production, **vous**, en tant que développeur, souhaitez voir les erreurs en un seul endroit dédié afin de les corriger.

Pour cette raison, nous avons besoin d'un service de journalisation créé par nous-mêmes ou par un tiers.

Lorsque vous utilisez des services de journalisation tiers, ma recommandation personnelle est définitivement **Sentry**. Je vous encourage donc vivement à le vérifier.

### ☝️ Gardez votre prop key unique dans toute votre application

Lorsque vous mappez sur un tableau pour rendre ses données, vous devez toujours définir une propriété **key** pour chaque élément. Une pratique courante que j'ai vue et utilisée moi-même est d'utiliser simplement l'**index** de chaque élément comme prop key.

L'utilisation de la prop key est importante car elle aide React à identifier l'élément exact qui a changé, est ajouté ou est supprimé. Imaginez que l'état de votre composant change et que l'UI doit être ré-rendue avec le nouvel état. React doit déterminer les différences entre l'UI précédente et la nouvelle UI afin de la mettre à jour.

"Quels éléments sont ajoutés/supprimés ou ont changé ?"

Par conséquent, la prop key doit être unique. L'utilisation de l'index de l'élément actuel garantit qu'il est uniquement unique dans cette fonction map particulière.

Cela pourrait ressembler à ceci, si nous prétensions montrer l'historique des scores d'une équipe de football de la saison en cours :

```jsx
const SeasonScores = ({ seasonScoresData }) => {
	
    return (
    	<>
        	<h3>Nos scores de cette saison :<h3>
        	{seasonScoresData.map((score, index) => (
    			<div key={index}>
        			<p>{score.oponennt}</p>
        			<p>{score.value}</p>
        		</div>
    		))}
        </>
    )
}
```

Bien que cela soit uniquement unique à l'intérieur de cette fonction map ici, cela pourrait entraîner des problèmes potentiels. Il est assez courant d'avoir plus d'une fonction map à l'intérieur de votre application React ou même dans un composant.

Supposons que nous avons une autre fonction map dans notre composant pour afficher l'effectif actuel :

```jsx
const SeasonScores = ({ seasonScoresData, currentRoster }) => {
	
    return (
    	<>
        	<h3>Nos scores de cette saison :<h3>
        	{seasonScoresData.map((score, index) => (
    			<div key={index}>
        			<p>{score.oponennt}</p>
        			<p>{score.value}</p>
        		</div>
    		))}
            </br>
			<h3>Notre effectif actuel :<h3>
        	{currentRoster.map((player, index) => (
            	<div key={index}>
                	<p>{player.name}</p>
                    <p>{player.position}</p>
                    <p>{player.jerseyNumber}</p>
                    <p>{player.totalGoals}</p>
                </div>
    		))}
        </>
    )
}
```

Maintenant, nous nous retrouvons dans la situation où nous avons utilisé de nombreuses clés deux fois à l'intérieur de notre composant. Supposons que nous avons **14** éléments à l'intérieur de `seasonScoresData` et **30** dans `currentRoaster`. Nous avons utilisé les nombres 0-13 deux fois comme prop key. Maintenant, nous ne servons plus le but d'avoir des props key uniques.

Cela pourrait entraîner des problèmes potentiels car React pourrait ne ré-rendre qu'un seul élément et omettre l'autre. Ou cela peut entraîner des inefficacités avec la mise à jour de l'arbre UI. Consultez l'article de blog recommandé à la fin de ce conseil pour obtenir un exemple plus approfondi.

Pour éviter ce comportement indésirable, assurez-vous d'utiliser toujours des **clés uniques dans toute votre application**. Idéalement, chaque élément du tableau a sa propre identité unique que vous pouvez utiliser. Mais ce n'est pas toujours le cas, donc vous pouvez utiliser une bibliothèque externe comme **uuidv4** pour générer des identifiants uniques.

En gardant cela à l'esprit et en supposant que chaque élément des deux tableaux a une propriété id, le composant ressemblerait à ceci :

```jsx
const SeasonScores = ({ seasonScoresData, currentRoster }) => {
	
    return (
    	<>
        	<h3>Nos scores de cette saison :<h3>
        	{seasonScoresData.map((score, index) => (
    			<div key={score.id}>
        			<p>{score.oponennt}</p>
        			<p>{score.value}</p>
        		</div>
    		))}
            </br>
			<h3>Notre effectif actuel :<h3>
        	{currentRoster.map((player, index) => (
            	<div key={player.id}>
                	<p>{player.name}</p>
                    <p>{player.position}</p>
                    <p>{player.jerseyNumber}</p>
                    <p>{player.totalGoals}</p>
                </div>
    		))}
        </>
    )
}
```

Si vous souhaitez approfondir, n'hésitez pas à consulter [cet excellent article](https://medium.com/swlh/understanding-the-importance-of-the-key-prop-in-react-f2b92ce65f45) sur ce sujet.

## Conseils pour vous aider à écrire un meilleur code React – La cerise sur le gâteau

![Image](https://www.freecodecamp.org/news/content/images/2022/01/joanna-kosinska-_xN7UbcZ33I-unsplash.jpg align="left")

J'aimerais comparer ce guide au processus de construction d'une maison. La première partie, *Apprendre les bases de React*, est la fondation solide sur laquelle vous construisez votre application. La deuxième, *Comment construire des composants React propres, performants et maintenables*, est pour construire les murs.

Cette section est essentiellement le toit qui vient par-dessus pour compléter la maison. C'est la raison pour laquelle j'aimerais l'appeler *La cerise sur le gâteau*. Ces conseils ici sont plus granulaires.

La plupart de ces pratiques sont plus optionnelles que celles précédentes, mais peuvent faire une différence si vous les utilisez correctement.

### 🦘 Implémenter le hook useReducer plus tôt

Probablement l'un des hooks les plus fréquemment utilisés dans React est **useState**. J'ai créé et vu des composants au fil du temps qui ont beaucoup d'états différents. Il est donc naturel qu'ils deviennent inondés de nombreux hooks useState.

```jsx
const CustomersMap = () => {
  const [isDataLoading, setIsDataLoading] = useState(false)
  const [customersData, setCustomersData] = useState([])
  const [hasError, setHasError] = useState(false)
  const [isHovered, setIsHovered] = useState(false)
  const [hasMapLoaded, setHasMapLoaded] = useState(false)
  const [mapData, setMapData] = useState({})
  const [formData, setFormData] = useState({})
  const [isBtnDisabled, setIsBtnDisabled] = useState(false)
  
  ...
  
  return ( ... )
}
```

Avoir beaucoup de hooks useState différents est toujours un bon signe que la taille et donc la complexité de votre composant augmente.

Si vous pouvez créer des sous-composants plus petits où vous pouvez transférer un peu d'état et de JSX, alors c'est une excellente façon de procéder. Vous nettoyez ainsi vos hooks useState et votre JSX en une seule étape.

Dans notre exemple ci-dessus, nous pourrions mettre les deux derniers états dans un composant séparé qui gère tout l'état et le JSX qui a à voir avec un formulaire.

Mais il existe des scénarios où cela n'a pas de sens, et vous devez garder ces nombreux états différents dans un seul composant. Pour augmenter la lisibilité de votre composant, il y a le hook **useReducer**.

La documentation officielle de React dit ceci à ce sujet :

> `useReducer` est généralement préférable à `useState` lorsque vous avez une logique d'état complexe qui implique plusieurs sous-valeurs ou lorsque l'état suivant dépend de l'état précédent. useReducer vous permet également d'optimiser les performances pour les composants qui déclenchent des mises à jour profondes car vous pouvez passer dispatch au lieu de callbacks.

En gardant cela à l'esprit, le composant ressemblerait à ceci lorsque vous utilisez `useReducer` :

```jsx
// ÉTAT INITIAL
const initialState = {
  isDataLoading: false,
  customerData: [],
  hasError: false,
  isHovered: false,
  hasMapLoaded: false,
  mapData: {},
  formdata: {},
  isBtnDisabled: false
}

// RÉDUCTEUR
const reducer = (state, action) => {
  switch (action.type) {
    case 'POPULATE_CUSTOMER_DATA':
      return {
        ...state,
        customerData: action.payload
      }
    case 'LOAD_MAP':
      return {
        ...state,
        hasMapLoaded: true
      }
    ...
    ...
    ...
    default: {
      return state
    }	
  }
}

// COMPOSANT
const CustomersMap = () => {
  const [state, dispatch] = useReducer(reducer, initialState)
  
  ...
  
  return ( ... )
}
```

Le composant lui-même semble plus propre et vient avec quelques grands avantages comme vous pouvez le voir dans la documentation. Si vous êtes habitué à Redux, le concept d'un réducteur et comment il est construit n'est pas nouveau pour vous.

Ma règle personnelle est d'implémenter le hook useReducer si mon composant dépasse quatre hooks useState, ou si l'état lui-même est plus complexe qu'un simple booléen, par exemple. Il pourrait s'agir d'un objet pour un formulaire avec quelques niveaux plus profonds à l'intérieur.

### 🔘 Utiliser la notation abrégée pour les props booléennes

Souvent, il y a des scénarios où vous passez des props booléennes à un composant. J'ai vu beaucoup de développeurs le faire comme ceci :

```jsx
<RegistrationForm hasPadding={true} withError={true} />
```

Mais vous n'avez pas besoin de le faire nécessairement comme ceci car l'occasion de la prop elle-même est soit truthy (si la prop est passée) soit falsy (si la prop est manquante).

Une approche plus propre serait :

```jsx
<RegistrationForm hasPadding withError />
```

### 📝 Éviter les accolades pour les props de chaîne de caractères

Un cas d'utilisation similaire à celui que nous avons vu dans le conseil précédent est l'utilisation de props de chaîne de caractères :

```jsx
<Paragraph variant={"h5"} heading={"A new book"} />
```

Vous n'avez pas besoin des accolades dans ce cas car vous êtes autorisé à utiliser directement des chaînes de caractères à l'intérieur de vos props. Lorsque vous souhaitez attacher une className à un élément JSX, vous l'utilisez également directement comme une chaîne de caractères.

Lorsque vous souhaitez utiliser une expression JavaScript différente d'une chaîne de caractères, vous devez utiliser les accolades. Par exemple, si vous souhaitez utiliser un nombre ou un objet. Cela est également vrai pour les chaînes de caractères de modèle (ne vous faites pas prendre comme je l'ai fait de nombreuses fois, haha).

Avec des chaînes de caractères simples, comme dans l'exemple, cela ressemblerait à ceci :

```jsx
<Paragraph variant="h5" heading="A new book" />
```

### 🧹 Effacer les attributs non-HTML lors de la propagation des props

Prenons un exemple rapide :

```jsx
const MainTitle = ({ isBold, children, ...restProps }) => {
	
  return (
    <h1 
      style={{ fontWeight: isBold ? 600 : 400 }}
      {...restProps}
    >
      {children}
    </h1>
  )
}
```

Nous venons de créer un composant qui rendra une balise h1, extrait certaines props, et propage toutes les autres props potentielles sur la balise h1. Jusqu'à présent, tout va bien.

Maintenant, nous sommes en mesure de l'utiliser dans d'autres composants et pouvons déclencher manuellement si le h1 doit être en gras ou non :

```jsx
// AVEC TITRE EN GRAS
const IndexPage = () => {
	
  return (
    <>
      <MainTitle isBold>
        Bienvenue sur notre nouveau site !
      </MainTitle>
      ...
    </>
  )
}
```

```jsx
// SANS TITRE EN GRAS
const AboutPage = () => {
	
  return (
    <>
      <MainTitle>
      	Quelques lignes rapides sur nous !
      </MainTitle>
      ...
    </>
  )
}
```

Jusqu'à présent, tout fonctionne parfaitement sans aucune erreur ou avertissement. La partie intéressante commence maintenant lorsque nous utilisons d'autres props qui sont directement propagées sur la balise h1.

Lorsque vous utilisez des attributs HTML valides comme id ou une classe, tout fonctionne sans aucune erreur (rappel --&gt; "className" deviendra "class") :

```jsx
const IndexPage = () => {
	
  return (
    <>
      <MainTitle isBold id="index-main-title" className="align-left">
        Bienvenue sur notre nouveau site !
      </MainTitle>
      ...
    </>
  )
}
```

Ainsi, toutes les props ci-dessus seront ajoutées en tant qu'attribut à la balise h1 car nous utilisons **{...restProps}** dessus. Peu importe ce que nous ajoutons et que nous n'extrayons pas, cela sera ajouté à la balise h1.

C'est génial pour de nombreux cas d'utilisation mais peut être un problème en même temps :

```jsx
// Composant de Page
const IndexPage = () => {
	
  return (
    <>
      <MainTitle isBold hasPadding>
        Bienvenue sur notre nouveau site !
      </MainTitle>
      ...
    </>
  )
}

// Composant MainTitle
const MainTitle = ({ isBold, children, ...restProps }) => {
	
  return (
    <h1 
      style={{ 
        fontWeight: isBold ? 600 : 400,
        padding: restProps.hasPadding ? 16 : 0
      }}
      {...restProps}
    >
      {children}
    </h1>
  )
}
```

Dans le code ci-dessus, nous avons ajouté une nouvelle prop appelée `hasPadding` au composant `MainTitle`, qui est optionnelle. À l'intérieur du composant, nous ne l'extrayons pas des props et l'appelons via `restProps.hasPadding`.

Le code fonctionne, mais lorsque vous ouvrez votre navigateur, vous recevrez un avertissement indiquant que `hasPadding` est un attribut non-HTML que vous essayez d'appliquer sur la balise h1. Cela est dû à `{...restProps}` sur la balise h1 et à ne pas extraire `hasPadding` comme `isBold` par exemple.

Pour éviter cela, extrayez toujours tous les attributs non-HTML des props en premier, pour vous assurer qu'il n'y a que des attributs HTML valides dans `restProps` que vous propagez sur un élément JSX.

Dans notre exemple, cela ressemblerait à ceci :

```jsx
// Composant de Page
const IndexPage = () => {
	
  return (
    <>
      <MainTitle isBold hasPadding>
        Bienvenue sur notre nouveau site !
      </MainTitle>
      ...
    </>
  )
}

// Composant MainTitle
const MainTitle = ({ isBold, children, hasPadding, ...restProps }) => {
	
  return (
    <h1 
      style={{ 
        fontWeight: isBold ? 600 : 400,
        padding: hasPadding ? 16 : 0
      }}
      {...restProps}
    >
      {children}
    </h1>
  )
}
```

De nombreux avertissements de ce type peuvent inonder inutilement la console de votre navigateur, ce qui peut être très désagréable. Surtout lorsque vous déboguez.

Pour obtenir plus d'informations sur ce sujet et d'autres façons de le résoudre, consultez [cette partie de la documentation React](https://reactjs.org/warnings/unknown-prop.html).

### ⏱️ Utiliser des extensions de snippets

Dans Visual Studio Code, par exemple, il existe certaines extensions disponibles qui augmentent considérablement votre productivité. L'un de ces types d'extensions sont les **extensions de snippets.**

Le grand avantage de celles-ci est que vous n'avez pas à écrire tout ce code de base à nouveau. Imaginez que vous construisez de nombreux nouveaux composants et que vous devez tout taper encore et encore :

```jsx
import React from 'react'

const GoogleMap = () => {

}

export default GoogleMap
```

Avec ces snippets, vous n'avez qu'à taper `rafce`, par exemple, appuyer sur tab et vous avez le même code de base. C'est un vrai gain de temps et rend le développement plus rapide.

**Mais utilisez-les avec prudence !** Je ne recommanderais pas d'utiliser des snippets à tous les développeurs. À mon avis, les débutants ne devraient pas utiliser de snippets et devraient taper le code de base à la main. Lorsque vous faites cela, vous obtenez une mémoire musculaire qui manifeste les choses que vous apprenez.

Si vous l'avez fait si souvent que vous pouvez le taper dans votre sommeil et que cela devient ennuyeux, c'est le bon moment pour utiliser des snippets.

Voici mes recommandations :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Bildschirmfoto-2022-02-01-um-14.55.02.png align="left")

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Bildschirmfoto-2022-02-01-um-15.05.01.png align="left")

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Bildschirmfoto-2022-02-01-um-15.06.59.png align="left")

### ❌ Écrire un fragment lorsqu'une div n'est pas nécessaire

Un composant React ne peut rendre qu'une seule balise HTML à sa racine. Donc, si vous souhaitez rendre deux éléments adjacents, vous obtiendrez la fameuse erreur appelée **Les éléments JSX adjacents doivent être enveloppés dans une balise englobante**.

```jsx
const InfoText = () => {
	
  // Cela lancera une erreur
  return (
    <h1>Bienvenue !</h1>
    <p>Ceci est notre nouvelle page, nous sommes heureux que vous soyez ici !</p>
  )
}
```

Alors, que pouvez-vous faire ? Vous enveloppez simplement la sortie rendue dans un fragment, ce qui satisfait React et ne rend pas de balise HTML supplémentaire dans le navigateur.

```jsx
const InfoText = () => {
	
  return (
  	<>
      <h1>Bienvenue !</h1>
      <p>Ceci est notre nouvelle page, nous sommes heureux que vous soyez ici !</p>
    </>
  )
}
```

Bien sûr, vous auriez pu résoudre cela avec une balise div également. Mais utiliser div après div créera ce que j'aime appeler **l'enfer des div** dans le navigateur où vous avez de nombreuses balises div profondément imbriquées sans aucun sens.

Donc, chaque fois que vous devez utiliser une balise wrapper dans React mais que vous n'avez pas nécessairement besoin d'une balise HTML, utilisez simplement un fragment.

### 👍 Intégrer des balises auto-fermantes lorsqu'aucun enfant n'est nécessaire

D'après mon expérience, ce conseil est souvent négligé, mais pourrait rendre votre code beaucoup plus propre avec peu d'effort.

Dans React, vous avez la possibilité de passer des éléments enfants à un composant, qui sont ensuite disponibles pour le composant via sa propriété children. Ces composants sont souvent appelés **composants composites.**

Dans ce cas, vous devez utiliser une balise d'ouverture et une balise de fermeture, bien sûr :

```jsx
<NavigationBar>
  <p>Accueil</p>
  <p>À propos</p>
  <p>Projets</p>
  <p>Contact</p>
</NavigationBar>
```

Mais lorsqu'aucun enfant n'est nécessaire, il n'y a aucun sens à utiliser une balise d'ouverture et de fermeture, n'est-ce pas ?

```jsx
<NavigationBar></NavigationBar>
```

Au lieu de faire cela, je recommande d'utiliser simplement le composant comme un élément auto-fermant comme la balise input en HTML, qui ne prend pas d'enfants non plus.

```jsx
<NavigationBar />
```

Cela semble beaucoup plus propre tout de suite, n'est-ce pas ?

### ✅ Suivre les conventions de nommage courantes

Le sens derrière les conventions de nommage est de reconnaître plus facilement le type d'élément avec lequel vous traitez et d'avoir quelque chose dans votre code qui est courant dans la communauté.

De mon point de vue, il y a deux conventions de nommage majeures impliquées dans React et JavaScript que vous devriez suivre :

#### Utiliser PascalCase dans les composants, interfaces ou alias de type

```jsx
// Composant React
const LeftGridPanel = () => {
  ...
}

// Interface TypeScript
interface AdminUser {
  name: string;
  id: number;
  email: string;
}

// Alias de type TypeScript
type TodoList = {
	todos: string[];
    id: number;
    name: string;
}
```

#### Utiliser camelCase pour les types de données JavaScript comme les variables, tableaux, objets, fonctions, etc.

```jsx
const getLastDigit = () => { ... }

const userTypes = [ ... ]
```

Nommer les composants React en PascalCase est particulièrement important. Parce que lorsque vous avez un linter configuré pour React, mais que vous avez nommé le composant en camelCase et que vous utilisez des hooks à l'intérieur, vous recevrez un message d'avertissement tout le temps que les hooks ne sont autorisés que dans les composants. C'est parce que le linter reconnaît un composant React s'il est écrit en PascalCase ou non.

Cela peut être désagréable, mais est rapidement corrigé en respectant les conventions de nommage établies.

### 🦠 Assainir votre code pour prévenir les attaques XSS

Peut-être vous êtes-vous retrouvé dans un scénario où vous devez utiliser la propriété `dangerouslySetInnerHTML` sur un élément dans React. En principe, c'est l'équivalent de React à `innerHTML` que vous connaissez peut-être de JavaScript.

Ainsi, en l'utilisant, vous pouvez définir du HTML directement depuis React.

Considérons l'exemple suivant, où nous aimerions rendre une chaîne HTML à l'intérieur d'une div. La chaîne pourrait provenir d'un éditeur de texte riche où elle est déjà formatée en HTML.

```jsx
const Markup = () => {
  const htmlString = "<p>Ceci est défini via dangerouslySetInnerHTML</p>"
  
  return (
    <div dangerouslySetInnerHTML={{ __html: htmlString }} />
  )
}
```

Le terme **dangerously** est choisi avec intention. L'utilisation de cette propriété peut vous exposer à une attaque de type cross-site-scripting (XSS). Il est donc obligatoire que le code qui est défini soit d'abord assaini.

Une excellente bibliothèque est [**dompurify**](https://www.npmjs.com/package/dompurify) qui peut vous aider avec cela.

## Mots de la fin

Wow, c'était amusant, n'est-ce pas ? J'ai fait de mon mieux pour tout sortir ce qui s'est accumulé dans ma tête au fil du temps. Ma motivation derrière ce guide est de partager mon expérience avec vous afin que vous puissiez éviter des moments plus difficiles pendant votre apprentissage et votre développement avec React.

Bien sûr, il peut y avoir des bonnes pratiques que vous considérez comme plus importantes et que j'ai manquées ici. C'est génial. J'adorerais entendre ce que vous aimeriez ajouter à ce guide.

Rappelez-vous, il s'agit toujours d'adapter ce qui est utile pour vous. Donc, ne prenez pas tout pour acquis et réfléchissez à ce qui pourrait être utile dans votre situation. Ensuite, vous pouvez simplement l'ajouter à votre propre ensemble de bonnes pratiques.

Vous pouvez également suivre mon parcours de développeur et obtenir de nombreuses autres informations utiles sur la vie d'un développeur sur mon [profil Instagram](https://www.instagram.com/jean_marc.dev/). Je suis toujours là pour vous aider et heureux de chaque retour que je peux obtenir. Donc, n'hésitez pas à me contacter.