---
title: Comment ajouter des boutons personnalisés à un sélecteur de date dans Flatpickr
subtitle: ''
author: Idris Abdul-Lateef
co_authors: []
series: null
date: '2024-01-17T16:34:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-custom-buttons-to-flatpickr
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/b01117c062c14a0d7f54f256baf09808482b6505_2_1024x512.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: User Interface
  slug: user-interface
seo_title: Comment ajouter des boutons personnalisés à un sélecteur de date dans Flatpickr
seo_desc: "If you've ever had to use a date picker in a web frontend project, chances\
  \ are that you've used flatpickr. \nFor the unacquainted, flatpickr is one of the\
  \ most popular date picker libraries in the open source-verse. It's framework-agnostic,\
  \ highly cus..."
---

Si vous avez déjà dû utiliser un sélecteur de date dans un projet de frontend web, il est probable que vous ayez utilisé flatpickr. 

Pour ceux qui ne connaissent pas, [flatpickr](https://flatpickr.js.org/) est l'une des bibliothèques de sélecteurs de date les plus populaires dans l'univers open source. Elle est indépendante des frameworks, hautement personnalisable et légère.

J'ai récemment dû l'utiliser dans une base de code Next.js et il y avait un cas d'utilisation particulier que j'avais. Le comportement intégré est que les dates sont appliquées immédiatement lorsqu'elles sont sélectionnées, et ensuite le sélecteur de date disparaît. 

Ce que je voulais vraiment, cependant, c'était de pouvoir choisir des dates et de ne pas voir la modale disparaître dès que je le faisais. Je voulais pouvoir continuer à choisir des dates et ne les appliquer que lorsque je cliquais sur un bouton "Appliquer". Je voulais aussi un bouton "Effacer" pour effacer les dates appliquées.

Normalement, l'API de flatpickr dispose de méthodes avec lesquelles vous pouvez travailler pour obtenir ces fonctionnalités, mais vous n'aurez pas de boutons sur le sélecteur de date lui-même. 

Même s'il existe un [plugin](https://flatpickr.js.org/plugins/#confirmdate) qui ajoute un bouton au sélecteur de date pour appliquer manuellement les dates, il ne fonctionne pas pour les plages de dates (ce dont j'avais besoin) et l'apparence du bouton ne s'harmonisait pas vraiment avec le thème général de l'application que je construisais. 

Je n'avais pas d'autre option que de trouver ma propre solution. Mais comment faire apparaître vos propres boutons sur le sélecteur de date de flatpickr ?

## Comment installer flatpickr
Tout d'abord, installez le package :
```bash
npm install flatpickr
```

Ensuite, vous avez besoin d'un composant `DatePicker` qui encapsulera le sélecteur de date personnalisé et le rendra réutilisable. Ce composant doit avoir une prop `onChange` à laquelle sera passée une fonction de rappel qui sera appelée chaque fois qu'une date est appliquée :
```tsx
// DatePicker.tsx

const DatePicker: React.FC<DatePickerProps> = ({ onChange }) => {
  return <div></div>
}

export default DatePicker

interface DatePickerProps {
  onChange: (date: Date[]) => void
}
```

Ensuite, vous devez configurer flatpickr lui-même. Vous allez importer certaines exportations du package flatpickr. Dans le balisage, vous allez ajouter un élément d'entrée de texte, qui sera l'entrée du sélecteur de date, et lui passer une variable de référence d'élément qui sera utilisée pour instancier l'instance flatpickr avec quelques options de configuration :
```tsx
// DatePicker.tsx

import { ElementRef, useEffect, useRef, useState } from "react"
import flatpickr from "flatpickr"

import { Instance as Flatpickr } from "flatpickr/dist/types/instance"
import "flatpickr/dist/flatpickr.min.css"

const DatePicker: React.FC<DatePickerProps> = ({ onChange }) => {
  const [flatpickrInstance, setFlatpickrInstance] = useState<Flatpickr>()
  const datePickerRef = useRef<ElementRef<"input">>(null)

  useEffect(() => {
    if (datePickerRef.current) {
      const flatpickrInstance = flatpickr(datePickerRef.current, {
        static: true,
        closeOnSelect: false,
      })
      
      setFlatpickrInstance(flatpickrInstance)
    }
    
    return () => flatpickrInstance?.destroy()
  }, [])

  return (
    <div>
      <input ref={datePickerRef} type="text" placeholder="Sélectionner une date..." />
    </div>
  )
}
...
```

Pour les options de configuration, `static` est défini sur true pour que la modale du sélecteur de date soit ancrée à l'entrée du sélecteur de date et `closeOnSelect` est false pour que la modale du sélecteur de date ne disparaisse pas lorsqu'une date est sélectionnée. 

Voici à quoi ressemble le sélecteur de date jusqu'à présent :
![Screenshot-2024-01-14-153953](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-14-153953.png)

## Comment ajouter les boutons
Nous arrivons à l'attraction principale du jour. Dans l'extrait ci-dessous, vous remarquerez deux nouvelles importations : `createPortal` de react-dom et un composant `Button` pré-stylisé. `createPortal` va jouer un rôle très spécial comme vous le verrez.
```tsx
// DatePicker.tsx

import { ElementRef, useEffect, useRef, useState } from "react"
import { createPortal } from "react-dom"
import flatpickr from "flatpickr"
import Button from "./Button"

import { Instance as Flatpickr } from "flatpickr/dist/types/instance"
import "flatpickr/dist/flatpickr.min.css"

...
```

En passant au corps du composant `DatePicker`, vous remarquerez également quelques changements. 

Il y a `dates` qui stockera la ou les dates sélectionnées (ou un tableau vide si aucune date n'est sélectionnée) et `applyDate` qui contiendra la fonction de rappel à appeler lorsque le bouton "Appliquer" est cliqué. 

Dans l'objet de configuration, vous trouverez deux hooks flatpickr : `onChange` qui est déclenché chaque fois qu'une date est choisie et reçoit un tableau des dates actuellement sélectionnées, et `onClose` qui est déclenché lorsque la modale du sélecteur de date est fermée. 

Dans le corps de ces hooks se trouvent des implémentations qui spécifient le comportement du sélecteur de date.
```tsx
// DatePicker.tsx

...
const DatePicker: React.FC<DatePickerProps> = ({ onChange }) => {
  const [flatpickrInstance, setFlatpickrInstance] = useState<Flatpickr>()
  const datePickerRef = useRef<ElementRef<"input">>(null)
  const dates = useRef<Date[]>([])
  const [applyDate, setApplyDate] = useState(() => () => {})

  useEffect(() => {
    if (datePickerRef.current) {
      const flatpickrInstance = flatpickr(datePickerRef.current, {
        static: true,
        closeOnSelect: false,
        onChange: (selectedDates) => {
          if (selectedDates.length === 0) {
            onChange([])
            dates.current = []
          }

          setApplyDate(() => {
            return () => {
              dates.current = selectedDates
              onChange(selectedDates)
              flatpickrInstance.close()
            }
          })
        },
        onClose: () => {
          flatpickrInstance.setDate(dates.current)
        },
      })

      setFlatpickrInstance(flatpickrInstance)
    }

    return () => flatpickrInstance?.destroy()
  }, [])
  
  
  return (
    <div>  
...
```

Nous en arrivons à la partie où vous placez enfin les boutons personnalisés à l'intérieur du sélecteur de date. C'est là que `createPortal` entre en jeu. 

L'instance `flatpickrInstance` possède une propriété, `calendarContainer`, qui contient une référence à l'élément `div` contenant le sélecteur de date. C'est ici que vous allez projeter les boutons personnalisés, juste en dessous de la partie calendrier du sélecteur de date, en utilisant [react portal](https://react.dev/reference/react-dom/createPortal).
```tsx
// DatePicker.tsx

...
  return (
    <div>
      <input ref={datePickerRef} type="text" placeholder="Sélectionner une date..." />
      {flatpickrInstance &&
        createPortal(
          <div className="flex justify-center gap-3 py-2">
            <Button
              text="Effacer"
              bgColor="#F8F8F8"
              textColor="#292A2E"
              onClick={() => {
                flatpickrInstance.clear(true)
                flatpickrInstance.close()
              }}
            />
            <Button
              text="Appliquer"
              bgColor="#569ff7"
              textColor="#FFF"
              onClick={applyDate}
            />
          </div>,
          flatpickrInstance.calendarContainer
        )}
    </div>
  )
}

export default DatePicker
...
```

Ensemble, voici le code final produit :
```tsx
// DatePicker.tsx

import { ElementRef, useEffect, useRef, useState } from "react"
import { createPortal } from "react-dom"
import flatpickr from "flatpickr"
import Button from "./Button"

import { Instance as Flatpickr } from "flatpickr/dist/types/instance"
import "flatpickr/dist/flatpickr.min.css"

const DatePicker: React.FC<DatePickerProps> = ({ onChange }) => {
  const [flatpickrInstance, setFlatpickrInstance] = useState<Flatpickr>()
  const datePickerRef = useRef<ElementRef<"input">>(null)
  const dates = useRef<Date[]>([])
  const [applyDate, setApplyDate] = useState(() => () => {})

  useEffect(() => {
    if (datePickerRef.current) {
      const flatpickrInstance = flatpickr(datePickerRef.current, {
        static: true,
        closeOnSelect: false,
        onChange: (selectedDates) => {
          if (selectedDates.length === 0) {
            onChange([])
            dates.current = []
          }

          setApplyDate(() => {
            return () => {
              dates.current = selectedDates
              onChange(selectedDates)
              flatpickrInstance.close()
            }
          })
        },
        onClose: () => {
          flatpickrInstance.setDate(dates.current)
        },
      })

      setFlatpickrInstance(flatpickrInstance)
    }

    return () => flatpickrInstance?.destroy()
  }, [])

  return (
    <div>
      <input ref={datePickerRef} type="text" placeholder="Sélectionner une date..." />
      {flatpickrInstance &&
        createPortal(
          <div className="flex justify-center gap-3 py-2">
            <Button
              text="Effacer"
              bgColor="#F8F8F8"
              textColor="#292A2E"
              onClick={() => {
                flatpickrInstance.clear(true)
                flatpickrInstance.close()
              }}
            />
            <Button
              text="Appliquer"
              bgColor="#569ff7"
              textColor="#FFF"
              onClick={applyDate}
            />
          </div>,
          flatpickrInstance.calendarContainer
        )}
    </div>
  )
}

export default DatePicker

interface DatePickerProps {
  onChange: (date: Date[]) => void
}
```

Et voici à quoi ressemble maintenant le sélecteur de date avec les boutons personnalisés :
![Screenshot-2024-01-16-085906](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-16-085906.png)

## Conclusion
Le sélecteur de date est maintenant entièrement fonctionnel et peut fonctionner pour toutes les options de `mode`. Il existe de nombreuses personnalisations potentielles que vous pourriez faire en utilisant cette technique. Espérons que cet article a bien montré comment la personnalisation de flatpickr peut être réalisée.


### 💖Aimez cet article ?
**Voir plus de mon contenu !** Vous pouvez trouver plus d'articles sur mon [blog](https://blog.eedris.dev).

**Vous voulez vous connecter ?** Contactez-moi sur [Twitter](https://twitter.com/eedrxs) ou [LinkedIn](https://linkedin.com/in/eedris).