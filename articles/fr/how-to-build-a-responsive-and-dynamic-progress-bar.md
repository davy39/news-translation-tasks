---
title: Comment créer une barre de progression réactive et dynamique avec HTML, CSS
  et JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-15T17:43:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-responsive-and-dynamic-progress-bar
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/Screen-Shot-2020-09-12-at-2.35.47-PM.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: vue
  slug: vue
- name: Web Development
  slug: web-development
seo_title: Comment créer une barre de progression réactive et dynamique avec HTML,
  CSS et JavaScript
seo_desc: "By Michael Xavier\nA couple years back I wrote a short article on building\
  \ a responsive progress bar. My techniques have developed since then, and so an\
  \ update is in order. \nThe biggest change is that pseudo-elements (before, after)\
  \ are no longer requ..."
---

Par Michael Xavier

Il y a quelques années, j'ai écrit un court [article](https://medium.com/@beyondborders/building-a-responsive-progress-bar-ea5a0ecabe91) sur la création d'une barre de progression réactive. Mes techniques ont évolué depuis, et une mise à jour s'impose donc.

Le plus grand changement est que les pseudo-éléments (before, after) ne sont plus nécessaires. Maintenant, le CSS est plus simple, le DOM est plus facile à lire, et c'est beaucoup plus dynamique.

Alors essayons à nouveau.

Notre objectif est de créer une barre de progression réactive simple et efficace qui fait ce qui suit :

* A quatre étapes jusqu'à la complétion.
* Chaque étape a un état `default`, `active` et `complete`.
* Peut progresser d'étape en étape jusqu'à la complétion.

[Consultez le CodePen ici pour un exemple en direct.](https://codepen.io/lookininward/pen/LYpxPPo)

## Le HTML

Pour réduire la redondance et augmenter la réutilisabilité, nous suivons tous les états dans un composant Vue. Dans le DOM, cela génère dynamiquement le nombre requis d'étapes.

**Note** : _Le JavaScript natif (ECMAScript) ou tout autre framework peut accomplir cela. L'utilisation de Vue est à des fins démonstratives._

La barre de progression utilise un balisage de base. Il y a :

* un conteneur avec des classes calculées en fonction de l'étape actuelle : `progressClasses`
* une piste de fond statique : `progress__bg`
* une boucle qui itère à travers chaque étape et applique `stepClasses` en fonction de l'étape actuelle.

Chaque étape a :

* un `progress__indicator` qui contient une icône de vérification visible si l'étape est complète.
* un `progress__label` qui contient le texte de l'étiquette pour cette étape.

```html vue
<div
  id="app"
  :class="progressClasses"
>
  <div class="progress__bg"></div>
  
  <template v-for="(step, index) in steps">
    <div :class="stepClasses(index)">
      <div class="progress__indicator">
        <i class="fa fa-check"></i>
      </div>
      <div class="progress__label">
        {{step.label}}
      </div>
    </div>
  </template>
  
  <div class="progress__actions">
    <div
      class="btn"
      v-on:click="nextStep(false)"
    >
      Retour
    </div>
    <div
      class="btn"
      v-on:click="nextStep"
    >
      Suivant
    </div>
    <div>
      Étape :
      {{currentStep ? currentStep.label : "Début"}}
    </div>
  </div>
</div>

```

Pour simplifier, les `progress__actions` qui contrôlent la direction du déplacement sont imbriquées dans la barre de progression elle-même.

## Le CSS (SCSS)

C'est ici que nous faisons le gros du travail. Les classes définies ici seront appliquées dynamiquement par le JS en fonction de l'étape actuelle.

Tout d'abord, choisissons quelques couleurs à utiliser :

```scss
$gray:  #E5E5E5;
$gray2: #808080;
$blue:  #2183DD;
$green: #009900;
$white: #FFFFFF;
```

Maintenant, définissons la classe `.progress` : le conteneur qui maintient ensemble le contenu de la barre de progression.

```scss
.progress {
  position: absolute;
  top: 15vh;
  width: 0%;
  height: 10px;
  background-color: $blue;
  transition: width .2s;
}
```

Notre barre de progression a besoin d'un `.progress__bg` sur lequel les étapes de progression vont s'exécuter comme une piste. Cela sera gris, recouvert par la barre colorée à mesure qu'elle avance vers l'étape suivante.

```scss
.progress__bg {
  position: absolute;
  width: 100vw;
  height: 10px;
  background-color: $gray;
  z-index: -1;
}
```

Chaque `.progress__step` contient l'étape ronde qui va se mettre en évidence et se remplir à mesure que la barre de progression avance.

```scss
.progress__step {
  position: absolute;
  top: -8px;
  left: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  
  @for $i from 1 through 5 {
    &.progress__step--#{$i} {
      left: calc(#{$i * 20}vw - 9px);
    }
  }
}
```

Il contient également l'indicateur rond `.progress__indicator` et le texte de l'étiquette `.progress__label`. Leurs styles par défaut sont définis en dehors de `.progress__step`.

```scss
.progress__indicator {
  width: 25px;
  height: 25px;
  border: 2px solid $gray2;
  border-radius: 50%;
  background-color: $white;
  margin-bottom: 10px;
  
  .fa {
    display: none;
    font-size: 16px;
    color: $white;
  }
}

.progress__label {
  position: absolute;
  top: 40px;
}
```

Continuons maintenant à imbriquer dans `.progress__step` et définissons l'étape dans son état **actif**.

```scss
&.progress__step--active {
  color: $blue;
  font-weight: 600;
}
```

Ensuite, définissons l'étape dans son état **complet**. **Note** : les styles par défaut pour `.progress__indicator` et `.progress__label` sont écrasés lorsqu'ils sont dans l'état complet.

```scss
&.progress__step--complete {
  .progress__indicator {
    background-color: $green;
    border-color: $blue;
    color: $white;
    display: flex;
    align-items: center;
    justify-content: center;
  }
    
  .progress__indicator .fa {
    display: block;
  }
  
  .progress__label {
    font-weight: 600;
    color: $green;
  }
}
```

## Le JavaScript

Comme mentionné précédemment, cela différera en fonction de la manière dont vous implémentez la logique des étapes, du contexte plus large dans lequel elle est implémentée, des frameworks et des motifs que vous utilisez, et ainsi de suite.

Cet exemple utilise un composant Vue pour démontrer :

* le calcul des classes pour la barre de progression en fonction de l'état actuel.
* le calcul des classes pour chaque étape en fonction de l'état actuel.

```javascript vue
var app = new Vue({
  el: '#app',
  
  data: {
    currentStep: null,
    steps: [
      {"label": "un"},
      {"label": "deux"},
      {"label": "trois"},
      {"label": "complet"}
    ]
  },
  
  methods: {
    nextStep(next=true) {
      const steps = this.steps
      const currentStep = this.currentStep
      const currentIndex = steps.indexOf(currentStep)
      
      // gérer le retour
      if (!next) {
        if (currentStep && currentStep.label === 'complet') {
          return this.currentStep = steps[steps.length - 1]           
        }

        if (steps[currentIndex - 1]) {
          return this.currentStep = steps[currentIndex - 1] 
        }

        return this.currentStep = { "label": "debut" }   
      }
      
      // gérer le suivant
      if (this.currentStep && this.currentStep.label === 'complet') {
        return this.currentStep = { "label": "debut" }
      }
      
      if (steps[currentIndex + 1]) {
        return this.currentStep = steps[currentIndex + 1]
      }

      this.currentStep = { "label": "complet" }   
    },
    
    stepClasses(index) {
      let result = `progress__step progress__step--${index + 1} `
      if (this.currentStep && this.currentStep.label === 'complet' ||
          index < this.steps.indexOf(this.currentStep)) {
        return result += 'progress__step--complete'
      }
      if (index === this.steps.indexOf(this.currentStep)) {
        return result += 'progress__step--active'
      }
      return result
    }
  },
  
  computed: {
     progressClasses() {
      let result = 'progress '
      if (this.currentStep && this.currentStep.label === 'complet') {
        return result += 'progress--complete'
      }
      return result += `progress--${this.steps.indexOf(this.currentStep) + 1}`
    }
  }
})
```

## Conclusion

À la fin, vous obtenez ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/progress-1.gif)

[Consultez le CodePen pour un exemple en direct.](https://codepen.io/lookininward/pen/LYpxPPo)

Si vous trouvez mes articles utiles, envisagez de devenir membre de [mon Patreon](https://www.patreon.com/michaelxavier) :)

Ou si vous voulez simplement m'offrir un café (j'adore le café) :

<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick" />
<input type="hidden" name="hosted_button_id" value="AYXCQNZ3CL39Y" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_CA/i/scr/pixel.gif" width="1" height="1" />
</form>