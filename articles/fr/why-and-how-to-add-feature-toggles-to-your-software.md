---
title: Pourquoi et comment ajouter des bascules de fonctionnalités à votre logiciel
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-11-24T15:49:00.000Z'
originalURL: https://freecodecamp.org/news/why-and-how-to-add-feature-toggles-to-your-software
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/featuretoggles.png
tags:
- name: youtube
  slug: youtube
seo_title: Pourquoi et comment ajouter des bascules de fonctionnalités à votre logiciel
seo_desc: 'Feature Toggles (aka Feature Flags) are a technique used in software development
  in order to hide, enable or disable a particular feature during runtime. They allow
  teams to modify system behavior without changing code.

  We just published a course on ...'
---

Les bascules de fonctionnalités (ou Feature Flags) sont une technique utilisée en développement logiciel pour masquer, activer ou désactiver une fonctionnalité particulière lors de l'exécution. Elles permettent aux équipes de modifier le comportement du système sans changer le code.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp qui vous apprendra pourquoi et comment utiliser les bascules de fonctionnalités dans votre logiciel.

<style>
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

.switch input { 
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #2196F3;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
</style>
<label class="switch">
  <input type="checkbox" onclick="toggle()">
  <span class="slider round"></span>
</label>
<br>
<img src="https://www.freecodecamp.org/news/content/images/2021/03/comments-meme.jpeg" id="secretimg" style="display:none;">
<script>
function toggle() {
  var x = document.getElementById("secretimg");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script>

Fredrik Strand Oseberg a créé ce cours. Fredrik est ingénieur logiciel principal chez Unleash, un produit open-source qui simplifie l'ajout de bascules de fonctionnalités à votre logiciel. Unleash a fourni à freeCodeCamp une subvention qui a aidé à rendre ce cours possible.

Dans ce cours, vous apprendrez les bases des bascules de fonctionnalités, comment vous pouvez les utiliser et comment elles peuvent vous aider à améliorer le flux de travail de votre équipe de développement pour accélérer le temps de livraison.

Le cours commence par une interview d'Ivar Østhus, le fondateur d'Unleash, puis continue en examinant les cas d'utilisation de base des bascules de fonctionnalités et comment vous pouvez configurer Unleash open-source pour traiter des cas d'utilisation et des scénarios plus avancés.

Voici les sections couvertes dans ce cours :

* Introduction aux bascules de fonctionnalités avec Ivar Østhus
* Implémentation de base des bascules de fonctionnalités
* Pièges de base des bascules de fonctionnalités
* Implémentation d'une configuration externe de bascules de fonctionnalités
* Fournisseurs de bascules de fonctionnalités
* Architecture d'Unleash
* Configuration d'Unleash open-source avec Docker
* Création d'une clé API
* Configuration du proxy Unleash avec Docker
* Aperçu de l'application et création d'une bascule de fonctionnalités
* Utilisation des bascules de fonctionnalités dans une application réelle
* Connexion à Unleash avec le SDK proxy React
* Comprendre la persistance et le contexte d'Unleash
* Utilisation de stratégies pour la segmentation
* Introduction à l'expérimentation
* Comprendre les variantes
* Implémentation des variantes dans notre base de code
* Utilisation de fournisseurs d'analyse pour comprendre les données d'expérimentation
* Métriques d'utilisation
* Dette technique et nettoyage des bascules de fonctionnalités
* Conclusion

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://youtu.be/-yHZ9uLVSp4) (2 heures de visionnage).

%[https://youtu.be/-yHZ9uLVSp4]

Vous pourriez également trouver cet article utile : 11 principes pour construire un système de [feature flag](https://docs.getunleash.io/topics/feature-flags/feature-flag-best-practices) à grande échelle.