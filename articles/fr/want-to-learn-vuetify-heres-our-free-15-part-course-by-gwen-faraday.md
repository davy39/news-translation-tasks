---
title: Vous voulez apprendre Vuetify ? Voici notre cours gratuit en 15 parties par
  Gwen Faraday
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-23T16:02:00.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-vuetify-heres-our-free-15-part-course-by-gwen-faraday
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-23-at-17.06.55.png
tags:
- name: Scrimba
  slug: scrimba
- name: vue
  slug: vue
- name: Vuetify
  slug: vuetify
seo_title: Vous voulez apprendre Vuetify ? Voici notre cours gratuit en 15 parties
  par Gwen Faraday
seo_desc: 'By Per Harald Borgen

  If you love building apps in Vue.js but struggle to know where to start with UI
  design, look no further than Vuetify. It''s a UI library containing handcrafted
  material components which give apps a beautiful finish and professiona...'
---

Par Per Harald Borgen

Si vous adorez créer des applications en Vue.js mais que vous avez du mal à savoir par où commencer avec la conception d'interface utilisateur, ne cherchez pas plus loin que Vuetify. Il s'agit d'une bibliothèque d'interface utilisateur contenant des composants matériels artisanaux qui donnent aux applications une belle finition et un aspect professionnel.

## Pourquoi apprendre Vuetify ?

Vuetify est la bibliothèque de composants la plus populaire pour Vue.js, vous permettant de créer des applications magnifiques et accessibles même si la conception d'interface utilisateur n'est pas votre domaine.

Bien que la bibliothèque dispose de plus de 80 éléments prêts à l'emploi, elle vous permet également de créer des éléments personnalisés, donnant à vos applications un aspect propre et sur mesure.

Cet article vous guide à travers le cours gratuit [de deux heures sur Vuetify](https://scrimba.com/course/gvuetify?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article) de Gwen Faraday sur Scrimba. Le cours vous enseigne toutes les compétences de base nécessaires pour commencer avec Vuetify, y compris :

- Typographie
- Espacement
- Boutons
- Navigation
- Grille
- Carte

Dans la première moitié, Gwen introduit tous les éléments Vuetify nécessaires pour construire une grande application. Comme pour tous les cours Scrimba, vous pouvez mettre en pause les scrims et explorer le code.

La deuxième moitié vous permet de mettre la main à la pâte en construisant une boutique en ligne. Cela met vos nouvelles compétences à bonne utilisation et vous permet d'appliquer vos nouvelles connaissances.

À la fin, vous serez parfaitement versé dans la construction d'applications stylisées professionnellement avec Vuetify.

## Introduction à l'instructrice

Gwen Faraday est une ingénieure logicielle, auteure, conférencière et créatrice de contenu qui gère également une chaîne YouTube, [the Faraday Academy](https://www.youtube.com/channel/UCxA99Yr6P_tZF9_BgtMGAWA/featured), où elle enseigne une large gamme de sujets, y compris Vue.js et Vuetify. Cela fait d'elle l'enseignante parfaite pour vous guider à travers ce voyage d'apprentissage et faire passer vos compétences Vuetify au niveau supérieur.

## Prérequis

Pour tirer le meilleur parti de ce tutoriel, vous aurez besoin d'une bonne compréhension de HTML, CSS, Javascript et Vue.js. Si vous n'en êtes pas encore là, consultez les excellents cours gratuits de Scrimba pour vous mettre à niveau :

- [HTML et CSS](https://scrimba.com/course/ghtmlcss?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
- [Javascript](https://scrimba.com/course/gintrotojavascript?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
- [Vue.js](https://scrimba.com/course/glearnvue?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)

Si vous êtes prêt à vous lancer avec Vuetify, commençons !

## Introduction à Vuetify

[Dans le premier cast](https://scrimba.com/p/pP4xZu3/cEKyEkuB?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), Gwen nous présente Vuetify et partage les deux dépôts Github où elle a stocké tout le code, [basic-components](https://github.com/gwenf/vuetify-basic-components) et [vuetify-responsive](https://github.com/gwenf/vuetify-responsive). Cela nous permet de télécharger le code et de l'essayer nous-mêmes.

## Qu'est-ce que le Material Design ?

[Ensuite](https://scrimba.com/p/pP4xZu3/c4PDDZtg?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), nous apprenons le Material Design, une norme développée par Google pour la mise en œuvre d'interfaces accessibles et conviviales.

La norme Material fournit un ensemble de règles pour les éléments les plus courants trouvés sur les pages web, y compris les boutons, le texte, la navigation et des fonctionnalités plus avancées telles que le mouvement et l'élévation.

Vuetify simplifie la mise en œuvre de cette norme en fournissant un ensemble d'éléments d'interface utilisateur prêts à l'emploi et conformes, que nous pouvons ajouter directement à notre application Vue.js.

## Premier regard sur le code Vuetify

[Dans le prochain cast](https://scrimba.com/p/pP4xZu3/ckPbepSM?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), Gwen nous donne un premier aperçu du code Vuetify en instantiant une application Vue, en ajoutant une propriété Vuetify et en créant un nouvel objet Vuetify :

```js
new Vue({
	el: "#app",
	vuetify: new Vuetify({}),
	data: {
		message: "Using Single File Components",
	},
});
```

Ensuite, Gwen nous montre l'élément `<v-app>`, qui est le composant racine de tous les éléments Vuetify (les composants Vuetify doivent être à l'intérieur de `<v-app>`) :

```vue
<v-app>
     <v-content>
          <playground></playground>
     </v-content>
</v-app>
```

## Typographie

[![Typographie Vuetify](https://dev-to-uploads.s3.amazonaws.com/i/lrmuhh5orzx32c4jdlsd.png)](https://scrimba.com/p/pP4xZu3/cMqPmeTG?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
_Cliquez sur l'image pour accéder au cours._

Dans [le prochain scrim](https://scrimba.com/p/pP4xZu3/cMqPmeTG?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), nous voyons certaines des options que Vuetify offre pour gérer la typographie, y compris les titres, les sous-titres et le texte du corps. Nous voyons également comment changer la couleur du texte et la couleur de fond.

```vue
<v-card-text>
     <h1 class="display-4 purple yellow--text">Titre 1</h1>
     <h2 class="display-3">Titre 2</h2>
     <h3 class="display-2">Titre 3</h3>
     <h4 class="title">Titre</h4>
     <h5 class="subtitle-1">Sous-titre</h5>
     <p class="body-1">Corps</p>
</v-card-text>
```

Enfin, nous voyons comment utiliser les classes Vuetify pour ajuster le poids et le style de la police :

```vue
<h1 class="font-italic font-weight-light">Titre 1</h1>
```

**Note :** Les classes Vuetify remplacent tous les autres styles que le navigateur applique aux balises HTML.

## Espacement

[Ensuite](https://scrimba.com/p/pP4xZu3/cD7pnzSw?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), nous explorons certaines des classes d'espacement dans Vuetify, qui nous permettent d'ajouter des marges et des rembourrages. Nous voyons également comment changer la taille de l'espacement.

```vue
<h3 class="ml-5">Espacement</h3>
```

Le meilleur de tout, Gwen nous montre également comment les classes Vuetify peuvent aider avec ce graal du style d'application - centrer un élément ! Cliquez sur le cours pour en savoir plus.

## Boutons

[![Boutons Vuetify](https://dev-to-uploads.s3.amazonaws.com/i/ollkzqisck44bqdnc1r9.png)](https://scrimba.com/p/pP4xZu3/crmrBwtP?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
_Cliquez sur l'image pour accéder au cours._

Dans [le prochain scrim](https://scrimba.com/p/pP4xZu3/crmrBwtP?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), nous examinons certaines des options disponibles avec le composant de bouton de Vuetify, y compris les boutons avec du texte, des icônes ou les deux.

```vue
<v-btn large block>Submit</v-btn>
```

Enfin, nous voyons comment créer des boutons personnalisés en utilisant les classes des sections précédentes.

```vue
<button v-ripple class="elevation-2 py-2 px-4">
     Submit
</button>
```

## Navigation

[![Navigation Vuetify](https://dev-to-uploads.s3.amazonaws.com/i/je40l0odaw1l68pi8a71.png)](https://scrimba.com/p/pP4xZu3/czkwwQCw?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
_Cliquez sur l'image pour accéder au cours._

[Ensuite](https://scrimba.com/p/pP4xZu3/czkwwQCw?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), nous examinons les deux principales options de navigation disponibles dans Vuetify, `<v-app-bar>` et `<v-toolbar>`. Les deux éléments de navigation fournissent un redimensionnement automatique des boutons et des icônes, des icônes de navigation et la capacité de gérer les listes déroulantes.

```vue
<v-toolbar color="deep-purple accent-4" dense dark>
    <v-app-bar-nav-icon></v-app-bar-nav-icon>
<v-toolbar-title>Titre de l'application</v-toolbar-title></v-toolbar>
```

[Cliquez ici](https://scrimba.com/p/pP4xZu3/czkwwQCw?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article) pour voir tout cela en action !

## Grille

[![Grille Vuetify](https://dev-to-uploads.s3.amazonaws.com/i/hddtxtqh91j6z9gjb1up.png)](https://scrimba.com/p/pP4xZu3/cWKBnPSV?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
_Cliquez sur l'image pour accéder au cours._

Dans [le prochain scrim](https://scrimba.com/p/pP4xZu3/cWKBnPSV?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), Gwen nous guide à travers le système de grille de Vuetify, qui est divisé en 12 colonnes, avec cinq points de rupture média intégrés pour gérer différentes tailles d'écran.

```vue
<v-row>
    <v-col cols="12" sm="6">
        <v-card
        class="pa-2"
        outlined
        tile
        >
        Colonne
        </v-card>
    </v-col>
</v-row>
```

## Carte

[![Carte Vuetify](https://dev-to-uploads.s3.amazonaws.com/i/dbh0863c4we6t4sncpf2.png)](https://scrimba.com/p/pP4xZu3/cdNW42t8?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
_Cliquez sur l'image pour accéder au cours._

Dans [ce cast](https://scrimba.com/p/pP4xZu3/cdNW42t8?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), Gwen explique que Vuetify utilise un composant `<v-card>` comme enveloppe pour toute carte d'interface utilisateur. Ce composant peut prendre des props, des classes et des slots et dispose d'événements personnalisés, permettant des cartes bien alignées et soignées dans n'importe quel cas d'utilisation.

```vue
 <v-card-title>
    <v-icon
        large
        left
    >
        mdi-twitter
    </v-icon>
    </v-card-title>

    <v-card-text class="headline font-weight-bold">
    "Vue Rocks!"
    </v-card-text>

</v-card>
```

Gwen nous présente également l'élément `<v-spacer>`, qui nous permet d'ajouter facilement de l'espace blanc entre les éléments.

Enfin, nous vérifions le fichier `Playground.vue` - un espace pour nous permettre d'explorer les fonctionnalités de Vuetify que Gwen nous a montrées jusqu'à présent. Rendez-vous [au cours](https://scrimba.com/p/pP4xZu3/cdNW42t8?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article) pour l'essayer vous-même et voir ce que Vuetify peut faire.

## Navigation de la boutique

[![Navigation de la boutique en ligne Vuetify](https://dev-to-uploads.s3.amazonaws.com/i/tc2s63qss1f3tc7vyyhu.png)](https://scrimba.com/p/pP4xZu3/cMZMQbu9?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
_Cliquez sur l'image pour accéder au cours._

[Ensuite](https://scrimba.com/p/pP4xZu3/cMZMQbu9?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), il est temps de commencer à construire notre application de boutique. Gwen nous commence par ajouter une barre de navigation incluant la réactivité et un menu de tiroir. Nous passons également en revue certaines options de style, y compris les icônes et un menu dense.

## Page d'accueil

[Ensuite](https://scrimba.com/p/pP4xZu3/c33vv6fz?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), il est temps d'ajouter une page d'accueil. Gwen ajoute l'en-tête et un pied de page, puis nous lance le défi de coder la section centrale en utilisant les maquettes fournies. Rendez-vous [au screencast](https://scrimba.com/p/pP4xZu3/c33vv6fz?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article) pour tester vos nouvelles compétences Vuetify et comparer votre travail à la solution de Gwen.

Pour terminer, Gwen nous montre l'élément `<v-snackbar>`, qui peut être utilisé pour notifier un utilisateur lorsqu'un produit a été ajouté au panier.

```vue
<v-snackbar
	v-model="$store.state.snackbar.show"
	:multi-line="true"
	:right="true"
	:top="true"
	:timeout="6000"
	:color="$store.state.snackbar.variant"
>
    {{ $store.state.snackbar.message }}
    <v-btn
    dark
    text
    @click="$store.commit('updateSnackbar', { show: false })"
    >
    Fermer
    </v-btn>
</v-snackbar>
```

## Page de la boutique

[![Page de la boutique en ligne Vuetify](https://dev-to-uploads.s3.amazonaws.com/i/m1d909j9guwo0q1da9jj.png)](https://scrimba.com/p/pP4xZu3/cvdrn6Ar?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
_Cliquez sur l'image pour accéder au cours._

[Dans le prochain Scrim](https://scrimba.com/p/pP4xZu3/cvdrn6Ar?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), nous construisons notre page de boutique en utilisant les éléments de grille Vuetify. Tout d'abord, nous ajoutons des cartes de produit en réutilisant les cartes que nous avons construites pour notre page d'accueil. Ensuite, Gwen nous lance le défi de construire une barre latérale avec les éléments `<v-sheet>` et `<v-expansion-panels>`.

Rendez-vous [au cast](https://scrimba.com/p/pP4xZu3/cvdrn6Ar?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article) pour essayer le défi.

## Page du panier

[![Page du panier Vuetify](https://dev-to-uploads.s3.amazonaws.com/i/drbsnxpy6p95kzj3aph5.png)](https://scrimba.com/p/pP4xZu3/caZyp7um?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article)
_Cliquez sur l'image pour accéder au cours._

[Ensuite](https://scrimba.com/p/pP4xZu3/caZyp7um?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article), nous ajoutons une page de panier à notre application. Une fois de plus, Gwen nous lance le défi de coder la page selon ses maquettes, ce qui est une excellente pratique pour le codage en conditions réelles et renforce la mémoire musculaire nécessaire pour devenir un expert de Vuetify.

Cliquez ici pour donner le meilleur de vous-même avant de comparer votre travail avec le code final de Gwen. N'oubliez pas que vous pouvez toujours revenir aux scrims précédents ou consulter la documentation Vuetify si vous avez des difficultés.

## Écran de paiement

Dans le dernier scrim de code, nous construisons un flux de paiement simple en utilisant l'élément `<v-stepper>`.

```vue
<v-stepper-header>
    <v-stepper-step
        step="1"
        :complete="step > 1"
    />
    <v-divider />
    <v-stepper-step
        step="2"
        :complete="step > 2"
    />
    <v-divider />
    <v-stepper-step
        step="3"
    />
    </v-stepper-header>
```

Pour terminer le cours, Gwen souligne qu'il y a quelques fonctionnalités dans les maquettes que nous n'avons pas couvertes et nous encourage à essayer de les coder nous-mêmes en utilisant l'interface interactive de Scrimba.

## Conclusion

Un énorme bravo pour avoir terminé le cours ! J'espère que vous l'avez trouvé utile et que vous avez maintenant la confiance nécessaire pour construire des applications magnifiques en utilisant Vuetify. Pourquoi ne pas continuer votre voyage d'apprentissage en explorant la large gamme d'autres sujets disponibles sur [Scrimba](https://scrimba.com/?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_launch_article) ?

Où que vous alliez ensuite, bon codage :)


%[https://www.youtube.com/watch?v=rJIRv-_oYnA]