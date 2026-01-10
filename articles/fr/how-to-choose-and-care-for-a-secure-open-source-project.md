---
title: Comment choisir et entretenir un projet open source sécurisé
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-05-28T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-choose-and-care-for-a-secure-open-source-project
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/cover-2.png
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: dependency management
  slug: dependency-management
- name: information security
  slug: information-security
- name: open source
  slug: open-source
- name: Security
  slug: security
- name: Web Security
  slug: web-security
seo_title: Comment choisir et entretenir un projet open source sécurisé
seo_desc: "A few tricks for assessing the security of an open source project.\nThere\
  \ is a rather progressive sect of the software development world called the open\
  \ source community. \nThis community believes that most people would be a lot happier\
  \ and get a lot m..."
---

### Quelques astuces pour évaluer la sécurité d'un projet open source.

Il existe une secte plutôt progressive dans le monde du développement logiciel appelée la communauté open source.

Cette communauté croit que la plupart des gens seraient beaucoup plus heureux et accompliraient beaucoup plus de travail s'ils arrêtaient de construire des choses que quelqu'un d'autre a déjà construites et offertes pour une utilisation gratuite. Ils veulent que vous utilisiez leurs outils.

![Une bande dessinée que j'ai dessinée sur l'utilisation des outils des autres, avec la roue comme exemple.](https://victoria.dev/blog/how-to-choose-and-care-for-a-secure-open-source-project/wheels.png)

Outre le fait qu'ils existent sans que vous ayez à lever le petit doigt, les outils et logiciels open source présentent certains avantages distincts. Surtout dans le cas de projets bien établis, il est très probable que quelqu'un d'autre ait déjà résolu tous les bugs les plus ennuyeux pour vous.

Grâce à la facilité avec laquelle les utilisateurs peuvent consulter et modifier le code source, il est également plus probable qu'un programme ait été amélioré et sécurisé au fil du temps.

Lorsque de nombreux développeurs contribuent, ils apportent leur propre expertise et expériences uniques. Cela peut aboutir à un produit bien plus robuste et capable que ce qu'un seul développeur peut produire.

Bien sûr, étant aussi variés que les personnes qui les construisent, tous les projets open source ne sont pas créés égaux, ni maintenus pour être également sécurisés.

Il existe de nombreux facteurs qui affectent l'adéquation d'un projet à votre cas d'utilisation. Voici quelques considérations générales qui constituent un bon point de départ lors du choix d'un projet open source.

## Comment choisir un projet open source

Dans ses exigences les plus basiques, un bon projet logiciel est fiable, facile à comprendre, et dispose de composants et de sécurité à jour. Il existe plusieurs indicateurs qui peuvent vous aider à faire une supposition éclairée sur le fait qu'un projet open source satisfait ces critères.

### Qui l'utilise

Pris dans son contexte, le nombre de personnes utilisant déjà un projet open source peut être indicatif de sa qualité.

Si un projet compte une centaine d'utilisateurs, par exemple, il est raisonnable de penser que quelqu'un a essayé de l'utiliser au moins une centaine de fois avant que vous ne le trouviez. Ainsi, selon les anciennes coutumes de "Je ne sais pas ce qu'il y a dans cette grotte, tu passes d'abord", il est plus probable qu'il soit correct.

Vous pouvez tirer des conclusions sur la base d'utilisateurs d'un projet en examinant les statistiques disponibles. Selon votre plateforme, celles-ci peuvent inclure le nombre de téléchargements, de critiques, de problèmes ou de tickets, de commentaires, de contributions, de forks, ou d'étoiles, quelle que soit leur signification.

Évaluez les statistiques sociales sur des plateformes comme GitHub avec un grain de sel. Elles peuvent vous aider à déterminer la popularité d'un projet, mais seulement de la même manière que les applications de critiques de restaurants peuvent vous aider à déterminer si vous devriez manger chez Foo's Grill & Bar.

Selon l'endroit où se trouve Foo's Grill & Bar, quand il a ouvert, et la probabilité que les gens soient à proximité lorsqu'une envie irrésistible de steak se fait sentir, avoir vingt-six critiques peut être un bon signe ou un terrible signe.

Bien que vous ne vous attendriez pas à ce qu'un projet qui traite d'un cas d'utilisation ou d'une technologie très obscure ait des centaines d'utilisateurs, avoir quelques utilisateurs actifs est, dans un tel cas, tout aussi inspirant confiance.

La validation externe peut également être utile. Par exemple, les paquets inclus dans une distribution (distro) de système d'exploitation Linux doivent se conformer à des normes strictes et subir un examen. Choisir un logiciel inclus dans les dépôts par défaut d'une distro peut signifier qu'il est plus susceptible d'être sécurisé.

Peut-être l'un des meilleurs indicateurs à rechercher est de savoir si l'équipe de développement d'un projet utilise son propre projet. Recherchez des problèmes, des discussions ou des articles de blog montrant que les créateurs et mainteneurs du projet utilisent ce qu'ils ont construit eux-mêmes. Communément appelé ["manger sa propre nourriture pour chien"](https://en.wikipedia.org/wiki/Eating_your_own_dog_food), ou "dogfooding", c'est un indicateur que le projet est très probablement bien maintenu par ses développeurs.

### Qui le construit

Le principal ennemi des bons logiciels open source est généralement un manque d'intérêt. Les parties impliquées dans un projet open source peuvent faire la différence entre une bibliothèque éphémère et un utilitaire respecté à long terme. Plusieurs mainteneurs engagés, même contribuant sur leur temps libre, ont un taux de réussite beaucoup plus élevé pour soutenir un projet et générer de l'intérêt.

Les projets avec un intérêt sain sont généralement soutenus par, et à leur tour cultivent, une communauté de contributeurs et d'utilisateurs.

Les nouveaux contributeurs peuvent être activement accueillis, des guides clairs sont disponibles expliquant comment aider, et les mainteneurs du projet sont disponibles et abordables lorsque les gens ont des questions inévitables.

Certaines communautés ont même des salons de discussion ou des forums où les gens peuvent interagir en dehors des contributions. Les communautés actives aident à maintenir l'intérêt, la pertinence et la qualité du projet.

De manière moins organique, un projet peut également être soutenu par des organisations qui le sponsorisent. Les gouvernements et les entreprises avec un intérêt financier sont également des mécènes de l'open source, et un projet qui bénéficie d'une utilisation dans le secteur public ou d'un soutien financier a une incitation supplémentaire à rester pertinent et utile.

### À quel point est-il actif

La récence et la fréquence de l'activité d'un projet open source sont peut-être le meilleur indicateur de l'attention portée à sa sécurité. Examinez les versions, l'historique des commits, les journaux de modifications ou les révisions de la documentation pour déterminer si un projet est actif. Comme les projets varient en taille et en portée, voici quelques éléments généraux à rechercher.

Maintenir la sécurité est un effort continu qui nécessite une surveillance et des mises à jour régulières, surtout pour les projets avec des composants tiers. Ceux-ci peuvent être des bibliothèques ou toute partie du projet qui dépend de quelque chose en dehors de lui-même, comme une intégration de passerelle de paiement.

Un projet inactif est plus susceptible d'avoir un code obsolète ou d'utiliser des versions obsolètes de composants. Pour une détermination plus concrète, vous pouvez rechercher les composants tiers d'un projet et comparer leurs derniers correctifs ou mises à jour avec les dernières mises à jour du projet.

Les projets sans composants tiers peuvent ne pas avoir de mises à jour externes à appliquer. Dans ces cas, vous pouvez utiliser l'activité récente et les notes de version pour déterminer l'engagement des mainteneurs d'un projet.

Généralement, les projets actifs doivent montrer des mises à jour dans les derniers mois, avec une version notable dans la dernière année. Cela peut être une bonne indication que le projet utilise une version à jour de son langage ou de son framework.

Vous pouvez également juger de l'activité d'un projet en regardant les mainteneurs du projet eux-mêmes. Les mainteneurs actifs répondent rapidement aux retours ou aux nouveaux problèmes, même si c'est juste pour dire : "Nous nous en occupons."

Si le projet a une communauté, ses mainteneurs en font partie. Ils peuvent avoir un site web dédié ou écrire des blogs réguliers. Ils peuvent offrir des moyens de les contacter directement et en privé, surtout pour soulever des préoccupations de sécurité.

### Pouvez-vous le comprendre

Avoir une documentation est une exigence de base pour un projet destiné à être utilisé par quelqu'un d'autre que son créateur. Les bons projets open source ont une documentation facile à suivre, honnête et complète.

Avoir une [documentation bien écrite](https://victoria.dev/blog/word-bugs-in-software-documentation-and-how-to-fix-them/) est l'une des façons dont un projet peut se démarquer et démontrer la réflexion et le dévouement de ses mainteneurs.

Une section "Pour commencer" peut détailler toutes les exigences et la configuration initiale pour exécuter le projet. Une liste précise des sujets dans la documentation permet aux utilisateurs de trouver rapidement les informations dont ils ont besoin. Une déclaration de licence claire ne laisse aucun doute sur la manière dont le projet peut être utilisé et à quelles fins.

Ce sont des aspects caractéristiques d'une documentation qui sert ses utilisateurs.

Un projet qui suit de bonnes pratiques de codage a probablement un code aussi lisible que sa documentation. Un code facile à lire se prête à être compris. Généralement, il a des fonctions et des variables clairement définies et nommées de manière appropriée, un flux logique et un but apparent. Un code lisible est plus facile à corriger, à sécuriser et à construire.

### À quel point est-il compatible

Quelques facteurs détermineront la compatibilité d'un projet avec vos objectifs. Ce sont des qualités objectives et peuvent être déterminées en examinant les fichiers du dépôt d'un projet. Ils incluent :

* Langage de code
* Technologies ou frameworks spécifiques
* Compatibilité de la licence

La compatibilité ne signifie pas nécessairement une correspondance directe. Différents langages de code peuvent interagir les uns avec les autres, tout comme diverses technologies et frameworks. Vous devez lire attentivement la licence d'un projet pour comprendre si elle permet une utilisation pour votre objectif, ou si elle est compatible avec une licence que vous souhaitez utiliser.

En fin de compte, un projet qui satisfait tous ces critères peut ne pas encore tout à fait convenir à votre cas d'utilisation. Cependant, l'un des avantages de l'open source est que vous pouvez toujours en bénéficier en apportant des modifications qui conviennent mieux à votre utilisation. Si ces modifications améliorent le projet pour tout le monde, vous pouvez rendre la pareille et faire avancer les choses en contribuant votre travail au projet.

## Entretien et alimentation appropriés d'un projet open source

Une fois que vous adoptez un projet open source, un peu d'attention est nécessaire pour vous assurer qu'il continue d'être un atout pour vos objectifs.

Bien que ses mainteneurs s'occupent des fichiers du projet en amont, vous seul êtes responsable de votre propre copie. Comme tout logiciel, votre projet open source doit être bien entretenus pour rester aussi sécurisé et utile que possible.

Ayez un système qui vous fournit des notifications lorsque des mises à jour pour votre logiciel sont disponibles. Mettez à jour le logiciel rapidement, en traitant chaque correctif comme s'il était vital pour la sécurité - il peut bien l'être.

Gardez à l'esprit que les créateurs et mainteneurs de projets open source agissent, dans la plupart des cas, uniquement par la bonté de leur cœur. Si vous en avez un particulièrement génial, ses développeurs peuvent rendre des mises à jour et des correctifs de sécurité disponibles sur une base régulière. C'est à vous de surveiller les mises à jour et de les appliquer rapidement.

Comme pour la plupart des choses dans le logiciel, garder vos ajouts open source modulaires peut être utile. Vous pourriez utiliser des [sous-modules git](https://git-scm.com/book/en/v2/Git-Tools-Submodules), des branches ou des environnements pour isoler vos ajouts. Cela peut faciliter l'application des mises à jour ou l'identification de la source de tout bug qui pourrait survenir.

Ainsi, bien qu'un projet open source puisse ne coûter aucun argent, _caveat emptor_, ce qui signifie : "Jimmy, si nous t'obtenons un chiot, c'est ta responsabilité de t'en occuper."