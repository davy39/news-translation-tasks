---
title: Comment effectuer un audit d'accessibilité web
subtitle: ''
author: Victoria Nduka
co_authors: []
series: null
date: '2024-10-19T00:31:00.636Z'
originalURL: https://freecodecamp.org/news/how-to-perform-a-web-accessibility-audit
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729112018927/8f769e94-9c4b-4651-a0f7-0c99d529c9c3.png
tags:
- name: Accessibility
  slug: accessibility
seo_title: Comment effectuer un audit d'accessibilité web
seo_desc: Learn step-by-step guidelines for performing a thorough web accessibility
  audit, including best practices and tools to use.
---

Plus d'[un milliard de personnes dans le monde vivent avec une forme de handicap](https://www.who.int/health-topics/disability#tab=tab_1). Cela représente environ 16 % de la population mondiale. Maintenant, imaginez combien de ces individus pourraient essayer d'accéder à votre site web. Navigueraient-ils facilement à travers votre site, ou rencontreraient-ils des barrières qui pourraient les éloigner ?

Un audit d'accessibilité web vous aide à identifier et à corriger les problèmes qui empêchent les utilisateurs d'interagir efficacement avec votre site web. Dans ce guide, vous apprendrez comment effectuer un audit d'accessibilité web et améliorer l'utilisabilité de votre site.

## Table des matières

* [Qu'est-ce que l'accessibilité web ?](#heading-quest-ce-que-laccessibilite-web)
    
* [Qu'est-ce qu'un audit d'accessibilité web ?](#heading-quest-ce-quun-audit-daccessibilite-web)
    
* [Que faire avant l'audit](#heading-que-faire-avant-laudit)
    
* [Comment auditer votre site web](#heading-comment-auditer-votre-site-web)
    
* [Que faire après l'audit](#heading-que-faire-apres-laudit)
    
* [L'accessibilité est un processus continu](#heading-laccessibilite-est-un-processus-continu)
    

## Qu'est-ce que l'accessibilité web ?

L'accessibilité web signifie que les sites web et les applications web sont conçus et développés de manière à ce que les personnes handicapées puissent les utiliser. Cela inclut les individus ayant des handicaps visuels, auditifs, moteurs, cognitifs et neurologiques. Un site web accessible offre une meilleure expérience utilisateur pour tous les utilisateurs, quelles que soient leurs capacités.

## Qu'est-ce qu'un audit d'accessibilité web ?

Un audit d'accessibilité web est le processus d'évaluation d'un site web ou d'une application web pour déterminer à quel point les personnes handicapées peuvent l'utiliser facilement. Cette évaluation est effectuée selon les normes établies par le World Wide Web Consortium (W3C). Ces normes, connues sous le nom de Web Content Accessibility Guidelines (WCAG), fournissent les critères pour évaluer l'accessibilité d'un site web.

Un audit d'accessibilité vous aide à identifier les barrières qui empêchent les personnes handicapées d'utiliser pleinement ou d'interagir avec votre site. À la fin de l'audit, vous aurez un rapport complet qui détaille les problèmes trouvés et les étapes à suivre pour améliorer l'accessibilité de votre site.

## Que faire avant l'audit

Avant de plonger dans l'audit proprement dit, il y a quelques étapes préparatoires que vous devez suivre pour établir les bases d'une révision d'accessibilité approfondie et organisée. Voici ce que vous devez faire :

### 1. Familiarisez-vous avec les directives d'accessibilité

La première étape de tout audit d'accessibilité est de comprendre les règles contre lesquelles vous auditez. Vous familiariser avec ces directives vous aidera à comprendre ce que vous devez rechercher et quels types de changements pourraient être nécessaires pour améliorer l'accessibilité de votre site.

Les [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/TR/WCAG22/) fournissent des recommandations détaillées sur la manière de rendre les sites web plus accessibles aux personnes handicapées. Elles sont versionnées, la WCAG 2.2 étant la version la plus récente. Les directives sont divisées en trois niveaux de conformité :

* **Niveau A** : Les exigences minimales pour l'accessibilité.
    
* **Niveau AA** : Aborde les barrières les plus courantes pour les utilisateurs handicapés.
    
* **Niveau AAA** : Le niveau le plus élevé et le plus rigoureux d'accessibilité.
    

Pour commencer, vous devriez viser la conformité au niveau AA.

### 2. Définissez l'objectif de votre audit

Pourquoi effectuez-vous l'audit en premier lieu, et que souhaitez-vous accomplir ? Votre objectif pourrait être de :

* Savoir où vous en êtes en termes d'accessibilité.
    
* Générer un [modèle de template d'accessibilité de produit volontaire (VPAT)](https://en.wikipedia.org/wiki/Voluntary_Product_Accessibility_Template).
    
* Identifier les problèmes qui doivent être corrigés.
    

Votre objectif déterminera l'approche que vous adopterez pour effectuer l'audit.

### 3. Définissez la portée de votre audit

Ensuite, décidez quelles parties de votre site web vous allez auditer. Bien qu'il soit idéal d'auditer l'ensemble du site, cela peut ne pas toujours être réalisable en raison de contraintes de temps ou de ressources. Dans ce cas, concentrez-vous sur les pages et fonctionnalités clés qui sont essentielles pour l'interaction des utilisateurs.

### 4. Rassemblez vos outils

Pour effectuer un audit d'accessibilité web approfondi, vous aurez besoin d'une combinaison d'outils de test automatisés et manuels.

Pour les tests automatisés, certains outils populaires incluent :

* WAVE
    
* Axe DevTools
    
* Lighthouse
    
* Analyseurs de contraste de couleurs
    

Pour les tests manuels, vous aurez besoin de :

* Un clavier (pour tester la navigation au clavier).
    
* Des lecteurs d'écran comme JAWS, NVDA ou VoiceOver.
    
* Différents navigateurs pour vérifier la compatibilité.
    
* Idéalement, un groupe de participants aux tests, en particulier des individus handicapés, pour fournir des retours en conditions réelles.
    

### 5. **Créez une liste de contrôle d'accessibilité**

Sur la base des directives WCAG, créez une liste de contrôle des éléments spécifiques à vérifier lors de votre audit. Cette liste de contrôle servira de feuille de route, garantissant que vous ne manquez aucun composant critique.

Avoir une liste de contrôle basée sur les normes WCAG assure la cohérence de votre audit et vous donne des étapes claires et actionnables à suivre. Cela vous permet également de suivre votre progression et de documenter les problèmes pour une revue ultérieure.

## Comment auditer votre site web

Il est maintenant temps de procéder à l'audit proprement dit. Une bonne approche consiste à commencer par un test rapide à l'aide d'un outil automatisé, suivi d'une revue manuelle approfondie pour détecter les problèmes que l'automatisation pourrait manquer.

### Étape 1 : Exécuter une analyse automatisée

Pour l'analyse automatisée, vous pouvez utiliser WAVE, axe DevTools, Lighthouse, ou une combinaison de ces outils pour une évaluation plus complète. Utilisez plusieurs outils pour détecter une gamme plus large de problèmes d'accessibilité et fournir une analyse plus équilibrée.

#### Utilisation de WAVE

1. Allez sur [wave.webaim.org](http://wave.webaim.org).
    
2. Entrez l'URL du site web que vous souhaitez vérifier.
    
Alternativement,

1. Installez l'[extension de navigateur WAVE](https://wave.webaim.org/extension/).
    
2. Allez sur la page que vous souhaitez auditer.
    
3. Faites un clic droit sur la page pour ouvrir le menu contextuel.
    
4. Cliquez sur "WAVE this page" pour analyser votre page.
    
    ![Capture d'écran du menu clic droit montrant l'option 'WAVE this page'](https://cdn.hashnode.com/res/hashnode/image/upload/v1729181600332/64b21e6a-42a9-458f-a3a4-f85a414be7cc.png align="center")
    
5. WAVE générera un rapport montrant :
    
    * Erreurs (icônes rouges)
        
    * Alertes (icônes jaunes)
        
    * Fonctionnalités (icônes vertes)
        
    * Éléments structurels (icônes bleues)
        
    * Éléments HTML5 et ARIA (icônes violettes)
        
        ![Résumé des résultats de l'outil d'évaluation d'accessibilité WAVE montrant 2 erreurs, 0 erreurs de contraste, 48 alertes, 26 fonctionnalités, 58 éléments structurels et 50 éléments ARIA](https://cdn.hashnode.com/res/hashnode/image/upload/v1729181301746/5e667a48-8ee7-4157-80ab-7334194cf3bd.png align="center")
        
6. Cliquez sur chaque icône pour obtenir plus d'informations sur le problème ou la fonctionnalité.
    

#### Utilisation de axe DevTools

1. Installez l'[extension axe DevTools](https://www.deque.com/get-started-axe-devtools-browser-extension/?_gl=1*30317n*_up*MQ..*_ga*ODc3NjIyNjgyLjE3MjkxODIyNTg.*_ga_C9H6VN9QY1*MTcyOTE4MjI1Ny4xLjEuMTcyOTE4MjMxMS4wLjAuMA..) pour votre navigateur.
    
2. Naviguez vers la page web que vous souhaitez tester.
    
3. Ouvrez les DevTools de votre navigateur (F12 ou Cmd+Option+I)
    
4. Allez dans l'onglet "axe DevTools".
    
    ![Capture d'écran de l'interface axe DevTools montrant les options pour Scan User Flow, Full Page Scan et Partial Page Scan](https://cdn.hashnode.com/res/hashnode/image/upload/v1729182512532/f9ea794b-9806-428e-93fe-2af843f4bb2e.png align="center")
    
5. Cliquez sur "Full Page Scan" pour démarrer la vérification d'accessibilité.
    
6. Passez en revue les résultats. Ils sont catégorisés par gravité (Critique, Sérieux, Modéré, Mineur).
    
7. Chaque problème inclut des détails sur :
    
    * En quoi consiste le problème
        
    * Pourquoi c'est important
        
    * Comment le corriger
        
    * Quels critères de succès WCAG il viole
        

#### Utilisation de Lighthouse

1. Ouvrez les DevTools de votre navigateur (F12 ou Cmd+Option+I).
    
2. Allez dans l'onglet "Lighthouse".
    
3. Sélectionnez "Accessibilité" sous "Catégories" (vous pouvez en sélectionner d'autres également).
    
    ![Panneau des paramètres Lighthouse, montrant les options pour générer un rapport, choisir le mode et l'appareil, et sélectionner les catégories à analyser](https://cdn.hashnode.com/res/hashnode/image/upload/v1729182964952/083f7f52-621c-492a-a821-0ff7ae71d45e.png align="center")
    
4. Cliquez sur "Analyser le chargement de la page".
    
5. Passez en revue le score d'accessibilité et les problèmes spécifiques trouvés.
    
6. Chaque problème renvoie à des explications plus détaillées et à des solutions pour les corriger.
    

### Étape 2 : Effectuer un test manuel

Les tests manuels complètent les outils automatisés en vérifiant les problèmes qui ne peuvent pas être détectés automatiquement. Cela implique de simuler comment les utilisateurs handicapés interagiraient avec votre site web. Voici quelques domaines clés sur lesquels se concentrer lors des tests manuels :

#### 1. Navigation au clavier

De nombreux utilisateurs dépendent d'un clavier pour naviguer sur le web, soit en raison de handicaps moteurs, soit parce qu'ils utilisent des technologies d'assistance comme les lecteurs d'écran. Pour tester cela :

* Assurez-vous que tous les éléments interactifs (liens, boutons, formulaires) peuvent être accessibles en utilisant la touche Tab.
    
* Utilisez la touche Entrée ou la barre d'espace pour activer les éléments.
    
* Vérifiez les pièges de clavier (endroits où un utilisateur peut se retrouver bloqué et ne peut pas naviguer pour en sortir).
    

#### 2. Compatibilité avec les lecteurs d'écran

Les lecteurs d'écran convertissent le contenu à l'écran en parole ou en braille. Pour tester l'accessibilité des lecteurs d'écran :

* Installez un lecteur d'écran comme NVDA (pour Windows) ou VoiceOver (pour macOS).
    
* Naviguez à travers le site web en utilisant uniquement le lecteur d'écran. Vérifiez si le contenu est lu dans un ordre logique et si tous les éléments sont correctement étiquetés.
    
* Portez une attention particulière aux problèmes comme les textes alternatifs manquants ou incorrects pour les images, une structure de titres impropre et des boutons non étiquetés.
    

#### 3. Alternatives textuelles

Vérifiez que le contenu non textuel tel que les images, les vidéos et les icônes dispose d'alternatives textuelles appropriées. Par exemple :

* Les images doivent avoir un texte alternatif descriptif qui transmet leur but ou leur fonction.
    
* Les vidéos doivent inclure des sous-titres et des transcriptions pour garantir l'accessibilité aux utilisateurs ayant des handicaps auditifs.
    

### Étape 3 : Passer en revue l'utilisation du HTML sémantique et de l'ARIA

Les éléments sémantiques comme `<header>`, `<nav>`, `<article>` et `<footer>` aident les lecteurs d'écran à comprendre la structure d'une page. Les attributs Accessible Rich Internet Applications (ARIA) peuvent être utilisés pour améliorer l'accessibilité du contenu dynamique. Cependant, il est important d'utiliser ARIA avec parcimonie et uniquement lorsque cela est nécessaire, car une utilisation incorrecte peut entraîner plus de problèmes.

Voici quelques bonnes pratiques :

* Utilisez le HTML sémantique partout où c'est possible avant de recourir à ARIA.
    
* Assurez-vous que les rôles, états et propriétés ARIA sont correctement implémentés. Une mauvaise utilisation de ARIA peut confondre les utilisateurs et les lecteurs d'écran.
    

### Étape 4 : Documenter les problèmes

Une fois que vous avez terminé les tests automatisés et manuels, il est temps de documenter les problèmes d'accessibilité que vous avez découverts. Catégorisez les problèmes par leur gravité :

* **Critique** : Problèmes qui bloquent les utilisateurs dans l'accès aux fonctionnalités essentielles, comme une navigation ou des formulaires non fonctionnels.
    
* **Modéré** : Problèmes qui dégradent l'expérience utilisateur, comme un mauvais contraste de couleurs.
    
* **Mineur** : Violations mineures qui n'impactent pas significativement l'expérience utilisateur mais qui doivent tout de même être traitées, comme des attributs ARIA mal utilisés.
    

Utilisez une feuille de calcul ou un outil de gestion de projet comme GitHub Issues pour documenter les problèmes. Vous pourriez également utiliser l'[outil de rapport WCAG-EM](https://www.w3.org/WAI/eval/report-tool) développé par l'initiative d'accessibilité web du W3C (WAI).

Dans votre rapport, assurez-vous d'inclure :

* La page où le problème se produit.
    
* Une description du problème.
    
* Les critères de succès WCAG qu'il viole.
    
* Des suggestions sur la manière de corriger le problème.
    

## Que faire après l'audit

Vous avez terminé votre audit. Vous disposez maintenant d'un rapport détaillé sur l'accessibilité avec les problèmes que vous avez identifiés. Que faire ensuite ?

### 1. Implémenter et tester les corrections

L'étape suivante consiste à travailler avec votre équipe de développement pour implémenter les corrections. Idéalement, vous devriez viser à résoudre tous les problèmes identifiés. Cependant, si vous travaillez sous des contraintes de temps, vous pourriez vouloir prioriser les problèmes qui sont plus faciles à corriger mais qui ont tout de même un impact significatif sur l'accessibilité.

Après avoir apporté ces modifications, relancez vos audits d'accessibilité — à la fois automatisés et manuels — pour vérifier que les problèmes ont été résolus avec succès.

### 2. Établir des directives d'accessibilité

Vos efforts en matière d'accessibilité seraient vains si de nouveaux développeurs dans votre équipe introduisaient des problèmes d'accessibilité sur votre site web. Pour éviter cela, créez un document complet décrivant vos normes d'accessibilité. Ce document doit détailler les bonnes pratiques que votre équipe suivra à l'avenir. De cette manière, toutes les futures mises à jour ou modifications maintiennent les améliorations d'accessibilité que vous avez apportées.

## L'accessibilité est un processus continu

Effectuer un audit d'accessibilité web est une étape importante pour rendre votre site web plus inclusif. Mais cela signifie-t-il que votre travail est terminé et que vous pouvez vous détendre ? Pas tout à fait. L'accessibilité n'est pas une tâche ponctuelle. C'est un processus continu.

À mesure que vous ajoutez de nouvelles fonctionnalités ou du contenu, vous devrez tester et améliorer continuellement votre site pour maintenir les normes d'accessibilité. Cela ne profite pas seulement aux utilisateurs handicapés, cela améliore l'expérience utilisateur globale pour tout le monde.

Prioriser constamment l'accessibilité conduit à un site web plus convivial, fonctionnel et inclusif.