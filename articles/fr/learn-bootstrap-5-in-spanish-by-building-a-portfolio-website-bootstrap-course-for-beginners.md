---
title: Apprendre Bootstrap 5 en espagnol en créant un site portfolio – Cours Bootstrap
  pour débutants
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2022-11-10T05:30:10.000Z'
originalURL: https://freecodecamp.org/news/learn-bootstrap-5-in-spanish-by-building-a-portfolio-website-bootstrap-course-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/thumbnail-2.png
tags:
- name: Bootstrap 5
  slug: bootstrap-5
- name: Español
  slug: espanol-2
- name: freeCodeCamp.org
  slug: freecodecamp
- name: online courses
  slug: online-courses
seo_title: Apprendre Bootstrap 5 en espagnol en créant un site portfolio – Cours Bootstrap
  pour débutants
seo_desc: 'Welcome! If you speak Spanish and you want to practice your HTML and CSS
  skills, create responsive websites with Bootstrap 5, and build your portfolio website,
  then this course is for you.

  In this article, you will find a brief introduction to respon...'
---

Bienvenue ! Si vous parlez espagnol et que vous souhaitez pratiquer vos compétences en HTML et CSS, créer des sites web responsives avec Bootstrap 5, et construire votre site portfolio, alors ce cours est fait pour vous.

Dans cet article, vous trouverez une brève introduction au développement web responsive et à Bootstrap 5. Vous apprendrez également pourquoi vous devriez les apprendre si votre objectif est de devenir développeur front-end.

Ensuite, vous trouverez un cours de 5 heures sur Bootstrap 5 sur la chaîne YouTube freeCodeCamp en espagnol. Dans ce cours, vous pouvez apprendre les fondamentaux en espagnol et construire votre site portfolio étape par étape en utilisant les composants, icônes et la grille de Bootstrap.

Si vous avez des amis hispanophones, vous êtes les bienvenus pour partager la [version espagnole de cet article](https://www.freecodecamp.org/espanol/news/aprende-bootstrap-5-en-espanol-creando-tu-portafolio-personal-curso-de-bootstrap-desde-cero) avec eux.

**💡 Astuce :** pour suivre le cours, vous devez avoir des connaissances préalables en HTML et CSS. Si vous devez réviser ces sujets, je vous invite à suivre nos cours complets sur la [chaîne YouTube en espagnol](https://www.youtube.com/freecodecampespanol).

Commençons ! ✨

## 🔹 Qu'est-ce que Bootstrap ?

Commençons par une introduction à Bootstrap. La [documentation officielle de Bootstrap](https://getbootstrap.com/) le définit comme :

> Un outil puissant, extensible et riche en fonctionnalités pour le développement front-end.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Boostrap.png)
_Bootstrap 5 - Site officiel_

Examinons de plus près les mots clés de cette définition :

* Bootstrap est **puissant** car il dispose de nombreuses fonctionnalités, y compris des classes CSS prédéfinies que vous pouvez appliquer à vos éléments HTML pour leur attribuer un style instantanément. Avec Bootstrap, vous pouvez également utiliser des plugins JavaScript puissants pour créer des éléments comme des carrousels, des modales, des infobulles, et plus encore.
* Bootstrap est **extensible** car vous pouvez étendre ou personnaliser les classes CSS prédéfinies qui accompagnent Bootstrap pour répondre à vos besoins. Si vous devez changer une couleur, vous pouvez le faire avec des sélecteurs, identifiants et classes CSS personnalisés. Vous pouvez également personnaliser le code JavaScript qui alimente certains composants Bootstrap.
* Bootstrap est utilisé pour le développement **front-end** car cette partie du développement web se concentre sur la conception et le développement de l'interface utilisateur, la partie du site web que les utilisateurs voient et avec laquelle ils interagissent directement.

**💡 Astuce :** en gros, Bootstrap vous fournit tous les outils nécessaires pour développer des sites web responsives avec des composants, icônes et styles prédéfinis.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Snippets.png)
_Exemples de composants Bootstrap ([source](https://getbootstrap.com/docs/5.2/examples/))_

## 🔶 Importance de créer un portfolio de développeur

Développer votre site portfolio est très important pour mettre en avant vos connaissances, compétences et les projets sur lesquels vous avez travaillé pendant votre parcours d'apprentissage.

Réfléchissez-y...

Quel est le meilleur moyen de prouver vos connaissances et compétences ?

La réponse est : **créer des projets concrets.**

C'est exactement ce que recherchent les employeurs – des développeurs capables d'apprendre de nouvelles technologies et de les appliquer à de nouveaux scénarios.

Créer un projet est un excellent moyen de montrer que vous avez les bonnes compétences et la motivation pour travailler en tant que développeur web.

Super. Maintenant que vous savez pourquoi il est important de créer votre portfolio de développeur, voyons le site portfolio que vous allez créer. 👁🏻

## 🔸 Projet du cours

Voici la structure principale du projet de site portfolio que nous allons construire pendant le cours :

### Section Hero et Section À propos de moi

Cette section aura une barre de navigation et une image de profil. La barre de navigation sera responsive. Une icône de menu burger sera affichée sur les petits appareils (au lieu de la barre de navigation) et le texte sera masqué automatiquement.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-06-at-9.21.20-AM.png)

### **Section Expérience**

Cette section inclura trois domaines de connaissances différents et des badges pour mettre en avant des compétences spécifiques. Cette section sera responsive et aura un effet de survol pour ajouter de l'interactivité.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-06-at-9.22.27-AM.png)

### **Section Projets**

Cette section inclura des liens vers les dépôts GitHub et les versions en direct des projets. Nous créerons cette section avec la grille Bootstrap, elle sera donc entièrement responsive et vous apprendrez à travailler avec les points de rupture de la grille.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-11-at-2.27.55-PM.png)

### **Section Articles**

Une liste d'articles ou de billets de blog. Ceux-ci seront des cartes et des groupes de listes Bootstrap. Chaque article sera représenté par un lien qui s'ouvrira dans un nouvel onglet.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-11-at-2.28.12-PM.png)

### **Section Témoignages**

Un carrousel de témoignages de clients. Ce sera un composant carrousel Bootstrap avec trois témoignages et des contrôleurs pour passer à l'élément précédent ou suivant dans le carrousel.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-06-at-9.23.28-AM.png)

### **Section Contactez-moi et Pied de page**

Cette section aura des liens vers les profils de réseaux sociaux et affichera les droits d'auteur du site web. Les liens de réseaux sociaux seront des icônes Bootstrap personnalisées.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-11-at-2.28.47-PM.png)

### **Dans les coulisses**

Nous travaillerons avec :

* La grille Bootstrap pour adapter le site web à des appareils de différentes tailles.
* Les composants Bootstrap, y compris les boutons, carrousel, barre de navigation responsive, images responsives, cartes, groupes de listes, et plus encore.
* Les icônes Bootstrap pour ajouter des liens vers les profils de réseaux sociaux (Twitter, GitHub, LinkedIn et Instagram).
* Les balises HTML sémantiques telles que `<header>`, `<section>`, et `<footer>`.
* Les requêtes média pour adapter les éléments HTML à des appareils de différentes tailles et orientations.
* Les sélecteurs CSS
* Google Fonts
* Et plus encore !

Vous pratiquerez de nombreuses compétences différentes en construisant ce projet et, une fois terminé, vous aurez un portfolio professionnel entièrement responsive pour mettre en avant vos compétences.

Cela semble génial, n'est-ce pas ?

💡 **Astuce :** après avoir créé la structure de base du site web, vous pouvez la personnaliser avec votre image de profil unique, vos compétences et vos projets.

## 🔹 Outils de développement

Nous travaillerons avec plusieurs outils que les développeurs utilisent dans leur travail quotidien.

### [Visual Studio Code](https://code.visualstudio.com/)

Un éditeur de code puissant et populaire créé par Microsoft. Vous pouvez le télécharger et l'installer gratuitement depuis son site officiel.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-11-at-2.47.40-PM.png)
_Visual Studio Code - Site officiel_

### [Extension Live Server pour Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

Une extension très utile qui nous aidera à améliorer notre productivité en actualisant le navigateur lorsque nous modifions nos fichiers HTML ou CSS.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-11-at-2.48.32-PM.png)
_Live Server - Documentation dans la Place de marché des extensions_

### [Outils de développement Chrome](https://developer.chrome.com/docs/devtools/)

Un ensemble d'outils de développement intégrés au navigateur Google Chrome. Ils sont très utiles pour tester la réactivité du site web, sélectionner des éléments dans la structure HTML et prévisualiser les modifications dans les fichiers HTML et CSS.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-10-11-at-2.50.32-PM.png)
_Outils de développement Chrome - freeCodeCamp_

💡 **Astuce :** nous téléchargerons et installerons tous les outils nécessaires pendant le cours et vous apprendrez à travailler avec eux étape par étape.

## 🔸 Cours sur YouTube

Super. Maintenant que vous en savez plus sur Bootstrap 5 et sur l'importance de créer un portfolio professionnel, vous avez également vu ce que vous apprendrez pendant le cours.

Si vous êtes prêt, nous vous invitons à commencer à suivre le cours sur la chaîne YouTube [freeCodeCamp Español](https://www.youtube.com/freecodecampespanol) :

%[https://www.youtube.com/watch?v=QCw0L6FupQ0]

💻 Dans ce lien, vous pouvez accéder au [projet en direct](https://estefaniacn.github.io/portafolio-adaptable-bootstrap/) (en espagnol) et pratiquer l'utilisation des outils de développement Chrome.

✍️  Cours créé par **Estefania Cassingena Navone** (Twitter : [@EstefaniaCassN](https://twitter.com/EstefaniaCassN), YouTube : [Coding with Estefania](https://youtube.com/codingwithestefania)).

J'espère vraiment que vous aimerez le cours et que vous le trouverez utile pour créer votre portfolio de développeur.

Vous êtes également les bienvenus pour continuer à apprendre avec nos cours en **espagnol** :

%[https://www.youtube.com/watch?v=XqFR2lqBYPs]

%[https://www.youtube.com/watch?v=ivdTnPl1ND0]

%[https://www.youtube.com/watch?v=DLikpfc64cA]

%[https://www.youtube.com/watch?v=6Jfk8ic3KVk]

%[https://www.youtube.com/watch?v=1hpc70_OoAg]