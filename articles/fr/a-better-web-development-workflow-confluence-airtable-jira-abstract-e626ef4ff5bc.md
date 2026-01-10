---
title: 'Un meilleur flux de travail pour le développement web : Confluence, Airtable
  et plus'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-04T17:38:58.000Z'
originalURL: https://freecodecamp.org/news/a-better-web-development-workflow-confluence-airtable-jira-abstract-e626ef4ff5bc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*K3DXpE4GwzoHTtFrrvF6Rw.png
tags:
- name: Design
  slug: design
- name: management
  slug: management
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: workflow
  slug: workflow
seo_title: 'Un meilleur flux de travail pour le développement web : Confluence, Airtable
  et plus'
seo_desc: 'By Vince MingPu Shao

  Working as a front-end developer for nearly two years, I’ve got helpful experience
  from being part of several web development projects of design/digital agencies.

  One obvious but valuable lesson I’ve learnt is that collaborating ...'
---

Par Vince MingPu Shao

En tant que développeur front-end depuis près de deux ans, j'ai acquis une expérience précieuse en participant à plusieurs projets de développement web au sein d'agences de design/digitales.

Une leçon évidente mais précieuse que j'ai apprise est que la collaboration entre chaque groupe avec un objectif commun mais des responsabilités et des buts distincts n'est pas facile. Il existe différents aspects et niveaux de difficultés en termes de collaboration, et la partie spécifique que je souhaite aborder ici est le processus de flux de travail.

Sur la base de mon expérience, et avec l'aide de mes amis designers et développeurs, j'ai construit un flux de travail de développement web conçu pour les petites équipes (5 à 15 personnes). Le système est composé de [Confluence](https://www.atlassian.com/software/confluence), [Jira](https://www.atlassian.com/software/jira), [Airtable](https://airtable.com/) et [Abstract](https://www.abstract.com/). Dans cet article, je vais partager le pourquoi et le comment de ce flux de travail.

### **Motivation pour la création d'un nouveau flux de travail**

Pour livrer un site web personnalisé sans utiliser de modèles fournis par des [constructeurs de sites web](https://www.wpbeginner.com/beginners-guide/how-to-choose-the-best-website-builder/), les exigences minimales en termes de talents incluent un designer, un développeur et un chef de projet. Après avoir participé à quelques cas, j'ai eu le sentiment que quelque chose n'allait pas avec notre flux de travail : les informations importantes n'étaient jamais alignées, tant en interne entre les différents rôles qu'en externe avec le client. Cette communication inefficace ralentissait clairement le cycle de développement et nuisait à l'équipe.

J'ai donc commencé à résoudre ce problème.

![Image](https://cdn-media-1.freecodecamp.org/images/OvSIwKWcr0uLNPIPbzpIfRHQS9zaHGbsbAbi)
_Recherche Google sur les ressources de flux de travail : [définition du flux de travail](https://medium.com/eightshapes-llc/system-features-step-by-step-e69c90982630" rel="noopener" target="_blank" title="">Fonctionnalités des systèmes de design</a>, <a href="http://styleguides.io/" rel="noopener" target="_blank" title="">ressources de guides de style</a> et <a href="https://www.projectmanager.com/training/define-workflow-process" rel="noopener" target="_blank" title=")_

J'ai recherché sur Google des ressources sur l'établissement et l'amélioration d'un flux de travail. Bien que j'aie appris beaucoup de choses grâce à toutes ces excellentes ressources, j'ai trouvé que presque aucune d'entre elles n'était destinée aux projets de développement web dans une agence de design/digitale. Il s'agissait soit d'un système de design, soit de directives de codage qui se limitaient aux rôles de design ou de front-end, soit d'un flux de travail conçu pour une équipe ayant son propre produit.

En conséquence, j'ai décidé de sélectionner les parties dont j'avais besoin pour résoudre nos problèmes et de former un flux de travail personnalisé pour le développement de sites web.

### **Problèmes et objectifs**

Voici les problèmes que j'ai identifiés dans notre flux de travail existant, ainsi que les objectifs d'amélioration correspondants :

#### **1. Méthodologie en cascade**

![Image](https://cdn-media-1.freecodecamp.org/images/DoyhUSqgX3dzSOt-H13itXsiXmdgnBidIS0V)
_démonstration abstraite du modèle en cascade_

**Problème :** D'après mon expérience, les projets de sites web adoptent une approche en cascade parce que les clients n'ont pas le concept de produit minimum viable (MVP). Au lieu de diviser les fonctionnalités des vues et de les modulariser, les clients ont tendance à penser au site de manière traditionnelle, page par page, ce qui oblige les designers et les développeurs à travailler page par page en séquence. Cela les empêche d'avoir une perspective universelle sur l'ensemble du projet. Cette situation entraîne de nombreuses révisions redondantes et des allers-retours entre les pages.

**Objectif :** Changer l'état d'esprit des clients est à la fois arrogant et irréaliste. L'objectif est de trouver un moyen de séparer les exigences des vues dès que possible et de développer de manière aussi modulaire que possible en interne, sur la base du modèle page par page.

#### **2. Jetons de design universels et composants gérés par les designers et les développeurs**

![Image](https://cdn-media-1.freecodecamp.org/images/vvgm0WaDEKF0T2cOXCKFxtTvQU8cv1542eZe)
_jetons de design de [Salesforce](https://www.lightningdesignsystem.com/design-tokens/" rel="noopener" target="_blank" title=")_

**Problème :** Il s'agit d'un problème courant pour lequel de nombreux articles ont partagé d'excellentes solutions, qui proposent principalement de construire un système de design géré par des [générateurs de guides de style/bibliothèques](https://github.com/davidhund/styleguide-generators#user-content-nodejs). Bien que ce soit une excellente solution, la gestion d'un site supplémentaire qui offre à peine des permissions d'édition aux designers n'était pas appropriée dans notre situation.

**Objectif :** En plus de créer des jetons de design universels et des langages que les designers, les développeurs et les chefs de projet peuvent tous comprendre, construire un système qui permet à chacun de gérer les actifs de manière synchrone.

#### **3. Tableau de bord de progression précis et à jour**

![Image](https://cdn-media-1.freecodecamp.org/images/FwCH5YpT2UsHNFtkhBFjwA0X5EYvii65dZ2G)
_nous avons besoin d'un tableau de bord de progression éditable et accessible_

**Problème :** Bien que les suiveurs de problèmes, les kanbans et autres modèles de gestion de projet soient utiles et pratiques, la plupart d'entre eux ont échoué à agir comme un tableau de bord de progression simple, flexible et convivial. Ce type de tableau de bord ferait gagner beaucoup de temps à l'équipe car il éviterait aux membres de l'équipe de devoir rapporter activement ou de demander la situation actuelle de tâches spécifiques. Il facilite également la vie des chefs de projet s'ils ont une connaissance claire de l'ensemble du projet sans trop d'efforts.

**Objectif :** Construire un système de tableau de bord qui offre des permissions d'édition pour les individus responsables de tâches spécifiques.

### **Diagramme du flux de travail**

Avant de plonger dans l'introduction détaillée de la pile d'outils de gestion, jetons un coup d'œil au flux de travail abstrait simplifié que j'ai organisé. Il s'agit essentiellement d'une visualisation d'un flux de travail normal que la plupart des agences ont, mais il y a deux points à noter ici.

![Image](https://cdn-media-1.freecodecamp.org/images/KJYSglCts4eVtawsVirn4A5Yk0q9uX0mb8kL)
_diagramme du flux de travail que j'ai conçu_

#### **1. Évaluation du développeur**

Tout d'abord, lorsque les exigences ou les problèmes provenant du client sont approuvés et documentés par le chef de projet, en plus d'envoyer la tâche à un designer, ils sont également envoyés à un développeur pour évaluation. Dans ce processus, le développeur examine les spécifications de la tâche, vérifiant s'il y a des fonctions ou des caractéristiques plutôt compliquées incluses. Si c'est positif, le développeur peut commencer à travailler dessus ou informer le designer des problèmes potentiels au préalable.

#### **2. Source unique de vérité**

Remarquez également qu'après l'approbation du livrable de design par le client, et avant de transmettre la tâche au développeur, elle passe par un processus d'**enregistrement/modification/suppression dans le magasin de design** effectué par le designer. Cela est dû au fait que le développeur doit toujours être exposé à une seule et unique source de magasin de design, qui contient des actifs constamment maintenus et mis à jour, prêts pour le développement.

Maintenant, nous pouvons plonger dans la pile d'outils de gestion que j'ai préparée et voir comment les outils nous aident à résoudre nos problèmes.

### **La pile d'outils**

Après avoir expérimenté diverses options sur le marché, la pile que je propose ici est composée de [Confluence](https://www.atlassian.com/software/confluence), [Jira](https://www.atlassian.com/software/jira), [Airtable](https://airtable.com/) et [Abstract](https://www.abstract.com/). En plus de l'introduction de base et de quelques exemples clés d'application, je ne couvrirai pas tous les détails de l'utilisation des outils.

![Image](https://cdn-media-1.freecodecamp.org/images/gsTUQmkRJBddtnziPdjtqnVDMbVjnhBXhPTU)
_[ABEM](http://atomicdesign.bradfrost.com/" rel="noopener" target="_blank" title="">design atomique</a> et <a href="https://css-tricks.com/abem-useful-adaptation-bem/" rel="noopener" target="_blank" title=")_

Note : le système suppose que l'équipe de développement adopte la [méthodologie de design atomique](http://atomicdesign.bradfrost.com/) et le système de nommage [ABEM](https://css-tricks.com/abem-useful-adaptation-bem/).

### **1. Confluence**

**Rôle :** centre d'information et de ressources

Bien qu'il soit intimidant au premier abord, [Confluence](https://www.atlassian.com/software/confluence) offre un espace de travail puissant et facile à organiser, avec des tonnes de fonctionnalités, d'intégrations d'applications et de modèles personnalisés. Ce n'est définitivement pas une solution universelle à tous les problèmes, mais c'est parfait pour la documentation des spécifications, des exigences, des comptes-rendus de réunion et plus encore.

Par conséquent, Confluence dans cette pile fonctionne comme un centre d'information et de ressources, ce qui signifie que chaque lien et détail lié à ce projet doit être documenté correctement ici.

Mon avantage préféré de Confluence est la capacité à personnaliser les modèles de documents. Cette fonctionnalité rend vraiment pratique la standardisation du flux de travail.

![Image](https://cdn-media-1.freecodecamp.org/images/zukI9t8HsDbd772oHP5IU5AYp0FdmHsLxccu)
_étape d'évaluation du développeur_

#### **Exemple :** Revue de la fonctionnalité des composants

J'ai mentionné le **processus d'évaluation du développeur** ci-dessus, qui est en fait un travail compliqué. Cela est dû au fait que ce processus inclut des informations de base sur le composant, une [revue FSM](https://www.vinceshao.com/blog/how-to-design-ui-states-and-communicate-with-developers-using-fsm-table) du développeur (si nécessaire), un espace FAQ et plus encore. Mais la flexibilité du modèle et des outils que Confluence fournit rend cela super facile. Il suffit de construire un modèle dans les paramètres de configuration et vous êtes prêt à partir.

![Image](https://cdn-media-1.freecodecamp.org/images/S58FbHZlVK5HY-YykmaxzZIb51ggDDM2gvzu)
_modèle personnalisé pour la revue des composants dans Confluence_

### **2. Jira**

**Rôle :** suivi des problèmes et gestion des types d'actions

Également un membre de la famille Atlassian, [Jira](https://www.atlassian.com/software/jira) est un logiciel super puissant de suivi des problèmes et de planification de projets. Ma partie préférée est la création de flux de travail personnalisés pour les problèmes. Puisqu'il existe de nombreux tutoriels sur la façon d'utiliser la puissance de Jira, la seule chose que je veux souligner ici est l'utilisation du type de problème comme mentionné ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/qoZ5zv8GbyTHSKRLnEj8g2oI6ybCj6xreaTG)
_le designer met à jour le magasin de design_

#### **Exemple :** Mettre à jour le développeur sur les changements du magasin de design par [type de problème](https://confluence.atlassian.com/jiraportfolioserver024/configuring-initiatives-and-other-hierarchy-levels-934716034.html)

Pour s'assurer que les développeurs construisent les composants sur la base de vues de design correctes, ils doivent être informés chaque fois que quelque chose dans le magasin de design est mis à jour, ce qui inclut des actions comme **enregistrer, modifier et supprimer**. Ainsi, lorsqu'un composant est mis à jour, le designer doit ouvrir un problème avec le développeur responsable assigné et le type de problème/action correct sélectionné.

![Image](https://cdn-media-1.freecodecamp.org/images/T7JTRAHQx4Pix-oLPoiMXbQP2weMpxoskBFv)
_[Fonction des types de problèmes Jira](https://confluence.atlassian.com/jiraportfolioserver024/configuring-initiatives-and-other-hierarchy-levels-934716034.html" rel="noopener" target="_blank" title=")_

### **3. Airtable**

**Rôle :** gestion des composants et tableau de bord de progression

[Airtable](https://airtable.com), un mélange de feuille de calcul et de base de données, est l'élément qui fait fonctionner cette pile. Il y a deux fonctionnalités incroyables qui soutiennent mon flux de travail : quatre types de transition de vue dans une seule table et le lien de contenu lié. Je vais présenter deux exemples d'utilisation de ces deux fonctionnalités ici.

![Image](https://cdn-media-1.freecodecamp.org/images/peF16s69oSsbNSBglXcfYq5EepGzbXF9HNi8)
_le développeur commence à travailler sur la tâche_

#### **Exemple 1 :** Gestion des composants

Comment gérez-vous votre bibliothèque de composants ? Nous avons choisi de ne pas utiliser un générateur de guide de style, car il n'est pas accessible pour les designers à éditer. L'utilisation de la bibliothèque de composants Sketch n'était pas non plus appropriée, car elle a trop de limitations si nous essayions de l'utiliser en dehors du cadre du logiciel lui-même.

Je ne dirais pas qu'Airtable est une solution parfaite, mais c'est l'option la plus facile et la plus flexible à laquelle j'ai pu penser. Jetez un coup d'œil au modèle de démonstration du tableau de gestion des composants ici :

![Image](https://cdn-media-1.freecodecamp.org/images/h825KA9cEz3P3tgn911Lq8GHP9nXGDp8RSGc)
_tableau des composants_

Une fois qu'une nouvelle vue de design enregistrée et prête à être développée de manière programmatique est soumise au développeur, celui-ci évalue la vue en fonction du système ABEM et l'enregistre dans le tableau. Il y a 9 colonnes dans le tableau, incluant :

**1. Nom :** nom du composant selon le principe ABEM

**2. Aperçu :** capture d'écran ou image exportée du composant

**3. Page liée :** lien vers la page contenant ce composant

**4. Composant enfant :** lien vers les composants enfants contenant celui-ci

**5. Modificateur :** vérifie s'il y a des variations de style (ex : --active, --red)

**6. Catégorie de composant :** une classification générale de catégorie (ex : texte, hero, sidebar)

**7. Statut de développement :** statut de la progression du développement (en attente, assigné, en cours, terminé, en révision)

**8. Responsable :** développeur responsable de ce composant

**9. Niveau atomique :** catégorie atomique de ce composant (atome, molécule, organisme)

Le meilleur aspect ici est que vous pouvez référencer des données dans les mêmes tables et dans d'autres tables. Cette connexion des points empêche les choses de devenir plus désordonnées à mesure que l'échelle grandit. Remarquez également que vous pouvez filtrer, trier et changer les vues facilement.

#### **Exemple 2 :** Statut de développement des pages

Étant donné que l'hypothèse ici est que nous évaluerons inévitablement la progression du développement page par page, un modèle de tableau conçu à cet effet est nécessaire. Ce tableau peut être un tableau de bord de progression pour les équipes internes et partagé avec le client en même temps.

![Image](https://cdn-media-1.freecodecamp.org/images/UBnBd4zGsyJu7Yeiq01oSwuvSB8J1R39muZx)
_tableau de la liste des pages_

Toutes les informations concernant la page, y compris la date limite, le lien du prototype InVision, le responsable et les composants enfants, peuvent être organisées ici. Notez qu'il est très pratique de documenter et de mettre à jour le statut de développement du design, du front-end et du back-end en même temps.

### **4. Abstract**

**Rôle :** source unique de vérité et contrôle de version des actifs de design

[Abstract](https://www.abstract.com/) est [GitHub](https://github.com/) pour les actifs [Sketch](https://www.sketchapp.com/) qui sauve les designers de l'enfer de la copie et du collage de fichiers. Il est hors du cadre de cet article de démontrer les détails de la gestion du flux de contrôle de version. Le point clé à retenir ici est qu'Abstract est le magasin de design qui agit comme la **source unique de vérité**. Les designers doivent continuer à mettre à jour la branche principale vers la dernière version du design confirmé, puis informer les développeurs. D'autre part, les développeurs ne doivent prendre que les actifs de design dans la branche principale comme référence.

![Image](https://cdn-media-1.freecodecamp.org/images/gyVsOvJOSx72uhwZNAPIV0nrHNh5DfuZsrMa)
_[Modèle de branche Abstract](https://www.abstract.com/how-it-works/" rel="noopener" target="_blank" title=")_

### Plus de travail à faire

D'après ma propre expérience, le développement de l'ensemble du projet après l'adoption de ce nouveau flux de travail a été au moins deux fois plus rapide qu'avant. Ce n'est pas une solution parfaite, car elle nécessite encore beaucoup de travail manuel pour la mise à jour et la maintenance.

Mais je pense que cela pourrait être une référence utile pour les équipes de développement web à la recherche d'un meilleur flux de travail, et j'espère que plus de personnes pourront partager leurs flux de travail à l'avenir !

---

_?[ 4e2d 6587](https://medium.com/as-a-product-designer/a-better-web-development-workflow-confluence-airtable-jira-abstract-zh-24fc8d5b8329)_[_ 7248 9020 (Version chinoise)_](https://medium.com/as-a-product-designer/a-better-web-development-workflow-confluence-airtable-jira-abstract-zh-24fc8d5b8329)  _/ Article original publié sur_ [_vinceshao.com_](https://www.vinceshao.com/blog/a-better-web-development-workflow-confluence-airtable-jira-and-abstract)