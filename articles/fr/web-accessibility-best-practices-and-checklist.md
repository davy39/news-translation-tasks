---
title: Accessibilité Web – Bonnes Pratiques et Liste de Contrôle pour les Développeurs
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2022-11-30T18:40:47.000Z'
originalURL: https://freecodecamp.org/news/web-accessibility-best-practices-and-checklist
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/WebAccessibility.png
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: Web Development
  slug: web-development
seo_title: Accessibilité Web – Bonnes Pratiques et Liste de Contrôle pour les Développeurs
seo_desc: "The World Health Organization reports that about 15% (1.2 billion) of the\
  \ world's population lives with some form of disability. \nThis means that as developers,\
  \ our focus on making websites and applications accessible helps more people use\
  \ these reso..."
---

L'Organisation Mondiale de la Santé [rapports](https://www.who.int/teams/noncommunicable-diseases/sensory-functions-disability-and-rehabilitation/world-report-on-disability) qu'environ **15% (1,2 milliard)** de la population mondiale vit avec une forme de handicap. 

Cela signifie qu'en tant que développeurs, notre concentration sur la création de sites web et d'applications accessibles aide davantage de personnes à utiliser ces ressources. 

Dans cet article, je vais souligner les barrières à l'accessibilité web, discuter des Web Content Accessibility Guidelines (WCAG), et partager une liste de contrôle de base que tous les développeurs peuvent utiliser lors de la construction de leurs sites web et applications.

> « Le pouvoir du Web réside dans son universalité. L'accès par tous, indépendamment du handicap, est un aspect essentiel. » – Tim Berners-Lee, Directeur du W3C et inventeur du World Wide Web.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/a11y.png)
_Crédit image : [Interactive Schools](https://blog.interactiveschools.com/)_

## Qu'est-ce que l'Accessibilité Web ?

Une personne est considérée comme handicapée lorsqu'elle est confrontée à une condition – permanente ou temporaire – qui rend difficile ou impossible l'accomplissement d'une tâche souhaitée. 

En effet, l'accessibilité web consiste à supprimer toutes les barrières qui empêchent les utilisateurs d'accéder au web de manière égale.

## Quelles sont les Barrières à l'Accessibilité ?

Les barrières à l'accessibilité incluent les barrières **visuelles, auditives, cognitives** et **motrices**. 

Les barrières visuelles constituent des conditions qui rendent difficile pour les personnes de voir des images, des vidéos et des gifs. Ces conditions peuvent inclure une basse vision, le daltonisme, ou même une perte totale de la vision. 

Les barrières auditives constituent des conditions qui rendent difficile ou impossible pour les personnes de consommer du contenu audio. 

Ceux qui ont des difficultés à se concentrer, à apprendre ou à se souvenir de nouvelles choses sont confrontés à des barrières cognitives. 

Et les personnes qui ont une perte partielle ou totale de fonction dans une partie du corps et qui trouvent difficile de naviguer sur les sites web en utilisant des dispositifs tels qu'une souris rencontrent des barrières motrices.

Pour résoudre ces barrières d'accessibilité web ou numérique, l'Initiative pour l'Accessibilité Web (WAI) du World Wide Consortium (W3C) a créé les **Web Content Accessibility Guidelines** (WCAG). 

## Quelles sont les Web Content Accessibility Guidelines ? 

Ce sont des normes mondialement acceptées qui guident les développeurs et les organisations dans la création d'un web accessible.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/pour-accessibility.png)
_Crédit image : [Site Improve](https://www.siteimprove.com/)_

La plupart des barrières à l'accessibilité web rencontrées par les personnes handicapées peuvent être classées en quatre catégories. Les WCAG abordent chaque catégorie pour garantir que l'accessibilité est atteinte.

**Perceptible :** Il est nécessaire que les utilisateurs puissent identifier le contenu et les éléments d'interface en utilisant leurs sens. La plupart des utilisateurs s'appuient principalement sur les sens visuels, tandis que d'autres s'appuient sur le son.

**Utilisable :** Il est nécessaire que les utilisateurs puissent utiliser les contrôles, les boutons, la navigation et autres éléments interactifs par eux-mêmes. Il prend en considération que les utilisateurs handicapés utiliseront des technologies d'assistance comme la reconnaissance vocale, les claviers, les lecteurs d'écran, etc.

**Compréhensible :** Il est nécessaire que les utilisateurs puissent comprendre le contenu et apprendre et se souvenir de l'utilisation de votre site. Le site doit avoir un format cohérent, une conception et des modèles d'utilisation prévisibles, ainsi qu'un ton approprié.

**Robuste :** Il est nécessaire que les utilisateurs de capacités et de conditions variées puissent interpréter et interagir de manière fiable avec le contenu en utilisant une technologie ou un dispositif de leur choix.

## Liste de Contrôle pour l'Accessibilité Web

En tant que développeurs, voici quelques éléments à surveiller lors de la création de sites web ou d'applications afin de garantir que les personnes de capacités variées puissent y accéder de manière égale.  

### Comment rendre les images accessibles

Toutes les images doivent avoir des textes alternatifs descriptifs sous forme de phrases plutôt que simplement un mot ou une clause. Par exemple, l'image ci-dessous doit avoir un texte alternatif comme montré dans le code sous celle-ci.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/pizza.jpg)
_Photo par [Unsplash](https://unsplash.com/@hybridstorytellers?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Hybrid Storytellers</a> sur <a href="https://unsplash.com/t/food-drink?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)_

```html
<img alt="une main droite retirant une part d'une pizza entière" src="https://unsplash.com/photos/XYyUxXw_oQw"/>
```

Le code ci-dessus montre un texte alternatif descriptif sous forme de phrase pour l'image. L'objectif du texte alternatif doit être de décrire l'image de manière à ce que les personnes utilisant des lecteurs d'écran aient l'impression de pouvoir visualiser ou imaginer exactement quelle image est décrite.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/ImageAlt-1.png)
_Sortie du texte alternatif de l'image_

Le niveau suivant d'accessibilité, comme vu dans l'image ci-dessus, est d'écrire des textes alternatifs de sorte que les utilisateurs qui pourraient rencontrer des problèmes de connectivité aient une idée de l'image avant de la voir.

### Comment rendre les liens accessibles

Les liens doivent être descriptifs et suggestifs, et vous devez étiqueter tous les liens avec exactement ce qu'ils font. 

Évitez d'intégrer vos liens dans des textes vagues tels que 'ici'. Par exemple, si nous voulions faire référence à mon article le plus récent, pour le bien des utilisateurs qui dépendent des lecteurs d'écran, voici comment faire.

```html
<p>
Consultez mon article le plus récent sur <a href="https://www.freecodecamp.org/news/web-layouts-use-css-grid-and-flex-to-create-responsive-webpages/">Web Layouts – Comment utiliser CSS Grid et Flex pour créer une page web responsive</a>
</p>
```

Dans le code ci-dessus, la balise de lien est enveloppée autour du titre complet de l'article au lieu de simplement faire du texte de lien un vague 'ici'. De cette manière, tout le monde qui voit, lit ou entend cela sait exactement quelle ressource sera trouvée lorsque le lien est cliqué.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/AccessibilityLink.png)
_Image de sortie du lien_

Lorsque les lecteurs d'écran arrivent à un lien aussi descriptif que celui que nous avons dans l'image ci-dessus, cela facilite grandement la tâche des utilisateurs malvoyants pour savoir ce que fait le lien et, par conséquent, décider s'ils veulent ou non le visiter. 

### **Comment rendre les formulaires accessibles**

Lors de la création de formulaires web, vous devez prendre en compte les utilisateurs ayant des limitations visuelles ou motrices. Facilitez la navigation dans votre formulaire avec le clavier pour les utilisateurs qui ne peuvent pas utiliser la souris et pour les utilisateurs dépendant des lecteurs d'écran afin qu'ils sachent exactement quelles informations sont nécessaires pour chaque entrée.

Assurez-vous que vos formulaires sont accessibles en utilisant `<label>` ou `aria-label` pour communiquer le but d'une entrée ou les informations qu'elle nécessite aux lecteurs d'écran. 

Les balises `<fieldset>` indiquent au formulaire que les groupes d'entrées appartiennent ensemble et les balises `<legend>` agissent comme des étiquettes pour les groupes d'entrées. Cela devient particulièrement nécessaire lors de la gestion de questions impliquant des cases à cocher ou des boutons radio.

```html
<fieldset class="first-section">
      <legend>Coordonnées</legend>
      <label for="name">Nom</label>
      <input type="text" id="name" name="name" autofocus placeholder="Ophy Boamah" autocomplete="on" required> <br><br>
      <label for="email">Email</label>
      <input type="email" id="email" placeholder="ob2@hotmail.com"> <br><br>
      <label for="tel">Téléphone</label>
      <input type="tel" id="tel" placeholder="+233 200001212"> <br><br>
</fieldset>
```

Dans le code ci-dessus, j'ai implémenté toutes les meilleures pratiques de formulaire que j'ai mentionnées. La balise fieldset crée un groupe initial "first-section". La balise legend contient du texte qui fournit une description pour le groupe d'éléments. Enfin, la balise label identifie chacune des entrées et leur but.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Fieldset.png)
_Sortie du formulaire accessible_

L'image ci-dessus est le résultat du code. Pour en savoir plus sur la création de formulaires modernes et accessibles, consultez mon article précédent sur [Comment Créer et Valider des Formulaires Web Modernes avec HTML5](https://www.freecodecamp.org/news/create-and-validate-modern-web-forms-html5/). 

### Accessibilité vidéo et audio

Toutes les vidéos doivent avoir des sous-titres et des légendes. De même, tous les contenus audio doivent avoir des transcriptions, afin que les personnes ayant des déficiences auditives puissent suivre et comprendre.

```html
 <video id="video" controls preload="metadata">
     <source src="assets/samplevideo.mp4" type="video/mp4" />
     <track
     label="Anglais"
     kind="subtitles"
     srclang="en"
     src="assets/samplevideo-en.srt"
     default />
 </video>
```

Le code ci-dessus montre un élément vidéo qui introduit la balise track pour ajouter des sous-titres afin que les utilisateurs qui ne peuvent pas entendre l'audio accompagnant puissent lire pour suivre.

%[https://vimeo.com/776769878#t=0]

### Comment sélectionner des couleurs pour l'accessibilité 

Lors de la sélection des couleurs pour vos sites web, prenez en compte les personnes daltoniennes et celles qui ont des problèmes de vue. 

Lorsque nous utilisons des couleurs avec un mauvais contraste, cela rend difficile pour les utilisateurs de lire ou de naviguer dans le contenu d'une page web. Cela signifie que nous devons toujours nous assurer que même dans de mauvaises conditions d'éclairage, nos couleurs de premier plan et d'arrière-plan ont suffisamment de contraste entre elles pour les boutons, les liens, les images, les icônes, les textes, etc. 

Si vous n'êtes pas sûr que deux couleurs se complètent de manière accessible, vérifiez en utilisant cet [outil de vérification de couleur en ligne](https://accessibleweb.com/color-contrast-checker/).

![Image](https://www.freecodecamp.org/news/content/images/2022/11/wcagcolorcheceker.png)
_Utilisez un outil de vérification de couleur pour vérifier le contraste des couleurs_

Vous pouvez également ajouter cette [Extension Chrome de Vérification d'Accessibilité Web](https://chrome.google.com/webstore/detail/accessible-web-helper/gdnpkbipbholkoaggmlblpbmgemddbgb) à votre navigateur pour des vérifications d'accessibilité sur site.

### Comment rendre les transitions et animations accessibles

Utilisez les transitions et animations avec parcimonie et uniquement lorsque cela est extrêmement nécessaire afin de ne pas déclencher certains utilisateurs. 

Certains deviennent étourdis ou subissent des crises lorsqu'ils rencontrent des éléments qui bougent rapidement. Fournissez un moyen pour que ces utilisateurs puissent mettre en pause, masquer ou arrêter l'animation en rendant ces contrôles disponibles. 

### Comment créer une structure de page et une navigation accessibles

Utilisez les balises HTML appropriées pour structurer sémantiquement les sites web. Votre site doit être facile à naviguer, surtout avec des technologies d'assistance. 

Les titres de page doivent être descriptifs afin que les utilisateurs puissent facilement différencier les onglets.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Site d'Accessibilité Web | Liste de Contrôle pour les Développeurs</title>
</head>
<body>
  <header>
  <nav>
    <ul>
      <li>Accueil</li>
      <li>À propos</li>
      <li>Contact</li>
    </ul>
  </nav>
  </header>
  <main>
    <section>
      <div>
        <h1>
          Bienvenue sur l'Accessibilité Web
        </h1>
        <p>
          Ceci est une structuration sémantique avec des balises HTML
        </p>
      </div>
    </section>
  </main>
  <footer>
    <a href="https://codehemaa.com">Mon site web</a>
  </footer>
</body>
</html>
```

Le code ci-dessus montre une page web avec un titre descriptif. J'ai utilisé les bonnes balises sémantiques pour structurer correctement la page en distinguant l'en-tête du corps principal et du pied de page. 

J'ai également correctement étiqueté les sections, les divs et les en-têtes. Cela aide les enregistreurs d'écran à épeler correctement exactement quel élément et quel contenu est présent sur la page.

## Conclusion

Si l'inventeur du web a déclaré avec emphase « l'accès par tous, indépendamment du handicap, est un aspect essentiel » du web, alors en tant que développeurs, nous devons nous efforcer d'atteindre cet objectif. De plus, c'est simplement la bonne chose à faire.

Vous devriez considérer l'accessibilité même avant de commencer à construire vos sites – et non pas après, en tant que contrôle des dommages. À l'avenir, nous devons nous efforcer d'inclure en contribuant à construire un web plus conscient et plus convivial en matière d'accessibilité. 

Merci d'avoir lu 👋🏾. J'espère que vous l'avez trouvé utile.