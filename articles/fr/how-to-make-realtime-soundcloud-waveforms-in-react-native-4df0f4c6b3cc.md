---
title: Comment créer des formes d'onde SoundCloud en temps réel dans React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-05T21:38:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-realtime-soundcloud-waveforms-in-react-native-4df0f4c6b3cc
coverImage: https://cdn-media-1.freecodecamp.org/images/0*j5GlB8Rv63-BazDF
tags:
- name: music
  slug: music
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer des formes d'onde SoundCloud en temps réel dans React Native
seo_desc: 'By Pritish Vaidya

  Introduction

  SoundCloud is a music and podcast streaming platform for listening to millions of
  authentic tracks. They have a really interactive interface for playing / listening
  to the tracks.

  The most important feature in their int...'
---

Par Pritish Vaidya

### **Introduction**

SoundCloud est une plateforme de streaming de musique et de podcasts pour écouter des millions de pistes authentiques. Ils ont une interface vraiment interactive pour jouer/écouter les pistes.

La fonctionnalité la plus importante de leur interface est d'afficher la progression de la piste basée sur sa _forme d'onde de fréquence_. Cela aide les utilisateurs à identifier la nature de celle-ci.

Ils ont également un [article de blog](https://developers.soundcloud.com/blog/waveforms-let-s-talk-about-them) qui décrit comment utiliser la forme d'onde basée sur son image. Il est difficile d'utiliser les mêmes techniques pour générer la forme d'onde dans une application _React Native_. Leur **SDK** [**Waveform.js**](https://github.com/soundcloud/waveformjs) _traduit une forme d'onde en points flottants à rendre sur une toile HTML5_ et n'est actuellement _plus opérationnel_.

Dans cet article, nous discuterons de la manière d'utiliser la même forme d'onde pour nos applications React Native.

### Pourquoi devrais-je utiliser les formes d'onde de SoundCloud ?

![Image](https://cdn-media-1.freecodecamp.org/images/kB4RbN318B8fU2hED2jFXFaXDB8G8--O9HfB)
_Crédits image — [KnowYourMeme](https://knowyourmeme.com/photos/1269398-arthurs-headphones" rel="noopener" target="_blank" title=")_

* La forme d'onde de SoundCloud est plus impressionnante que l'ancienne manière ennuyeuse d'afficher la _barre de progression_.
* La forme d'onde préchargée donnera à l'utilisateur une idée des différentes fréquences présentes dans la chanson.
* Il est également beaucoup plus facile d'afficher le _pourcentage de piste mis en mémoire tampon_ sur une forme d'onde plutôt que de l'afficher sur une barre de progression vide.

### En savoir plus sur les formes d'onde de SoundCloud

![Image](https://cdn-media-1.freecodecamp.org/images/LQ0a-DVQtUZJ8LmuJEqNenemVj10ylCPKzxJ)
_Crédits image — [Backstage Blog par les développeurs de SoundCloud](http://img.svbtle.com/inline_leemartin_24131769094098_raw.png" rel="noopener" target="_blank" title=")_

SoundCloud fournit une `waveform_url` dans son API de pistes.

* Chaque piste a sa propre `waveform_url` unique.
* La `waveform_url` contient un lien vers l'image hébergée dans le cloud.

**Exemple —** [https://w1.sndcdn.com/PP3Eb34ToNki_m.png](https://w1.sndcdn.com/PP3Eb34ToNki_m.png)

![Image](https://cdn-media-1.freecodecamp.org/images/ngCp52SzK2q5vYwSAyokRu5nsw8rs8PZdLAj)
_Crédits image — [Forme d'onde de SoundCloud pour la piste « Megadeth — Sweating Bullets » par mauriciohaensch](https://w1.sndcdn.com/PP3Eb34ToNki_m.png" rel="noopener" target="_blank" title=")_

Pour l'instant, tous les arguments sont statiques, donc ils sont inutilisables dans cet état actuel. Par conséquent, nous devons recréer la forme d'onde basée sur celle-ci en utilisant les _conteneurs_ de **React Native** afin d'avoir accès aux _événements tactiles, styles, etc._

### Prise en main

![Image](https://cdn-media-1.freecodecamp.org/images/g9wt8pkrRv-xcPBH8AhI4e-oZcJcUEst0bcc)
_Crédits image — [ImgFlip](https://imgflip.com/memegenerator/4081988/What-if-i-told-you" rel="noopener" target="_blank" title=")_

Voici une liste de ce dont vous aurez besoin :

* [d3-scale](https://github.com/d3/d3-scale)
* [d3-array](https://github.com/d3/d3-array)

Tout d'abord, nous avons besoin de l'échantillonnage de la forme d'onde. L'astuce consiste à remplacer `.png` par `.json` pour la `waveform_url`. Un appel `GET` à celle-ci nous donnerait un objet de réponse qui contient

* **width** (Largeur de la forme d'onde)
* **height** (Hauteur de la forme d'onde)
* **samples** (Tableau)

Pour plus d'informations, vous pouvez essayer le lien suivant [https://w1.sndcdn.com/PP3Eb34ToNki_m.json](https://w1.sndcdn.com/PP3Eb34ToNki_m.json).

### Plongez dans le code

![Image](https://cdn-media-1.freecodecamp.org/images/bdodPYaqbZeIjm8lEuNdAIXa9BFywxEkmY3C)
_Crédits image — [Unsplash](https://images.unsplash.com/photo-1466477234737-8a3b3faed8c3?ixlib=rb-0.3.5&amp;s=919a7e046d85dc25ac72f4c3070228b6&amp;auto=format&amp;fit=crop&amp;w=800&amp;q=60" rel="noopener" target="_blank" title=")_

#### Ajouter un composant SoundCloudWave personnalisé

```jsx
function percentPlayed (time, totalDuration) {
 return  Number(time) / (Number(totalDuration) / 1000)
}

<SoundCloudWave
  waveformUrl={waveform_url}
  height={50}
  width={width}
  percentPlayable={percentPlayed(bufferedTime, totalDuration)} 
  percentPlayed={percentPlayed(currentTime, totalDuration)}
  setTime={this.setTime}
/>
```

Il serait préférable de créer un composant personnalisé _SoundCloudWave_ qui peut être utilisé à plusieurs endroits selon les besoins. Voici les `props` requis :

* **waveformUrl** — L'objet URL de la forme d'onde (accessible via l'API des pistes)
* **height** — Hauteur de la forme d'onde
* **width** — Largeur du composant de la forme d'onde
* **percentPlayable** — La durée de la piste mise en mémoire tampon en secondes
* **percentPlayed** — La durée de la piste jouée en secondes
* **setTime** — Le gestionnaire de rappel pour changer l'heure actuelle de la piste.

#### Obtenir les échantillons

```jsx
fetch(waveformUrl.replace('png', 'json'))
  .then(res => res.json())
  .then(json => {
    this.setState({
      waveform: json,
      waveformUrl
    })
  });
```

Obtenez les échantillons en utilisant un simple appel d'API `GET` et stockez le résultat dans le `state`.

#### Créer un composant Waveform

```jsx
import { mean } from 'd3-array';

const ACTIVE = '#FF1844',
  INACTIVE = '#424056',
  ACTIVE_PLAYABLE = '#1b1b26'
  
const ACTIVE_INVERSE = '#4F1224',
  ACTIVE_PLAYABLE_INVERSE = '#131116',
  INACTIVE_INVERSE = '#1C1A27'

function getColor(
    bars,
    bar,
    percentPlayed,
    percentPlayable,
    inverse
) {
  if(bar/bars.length < percentPlayed) {
    return inverse ? ACTIVE : ACTIVE_INVERSE
  } else if(bar/bars.length < percentPlayable) {
    return inverse ? ACTIVE_PLAYABLE : ACTIVE_PLAYABLE_INVERSE
  } else {
    return inverse ? INACTIVE : INACTIVE_INVERSE
  }
}

const Waveform =
  (
   {
     waveform,
     height,
     width,
     setTime,
     percentPlayed,
     percentPlayable,
     inverse
   }
  ) => 
  {
    const scaleLinearHeight = scaleLinear().domain([0, waveform.height]).range([0, height]);
    const chunks = _.chunk(waveform.samples, waveform.width/((width - 60)/3))
      return (
        <View style={[{
          height,
          width,
          justifyContent: 'center',
          flexDirection: 'row',
         },
         inverse && {
          transform: [
            { rotateX: '180deg' },
            { rotateY: '0deg'},
          ]
         }
        ]}>
         {chunks.map((chunk, i) => (
           <TouchableOpacity key={i} onPress={() => {
             setTime(i)
           }}>
            <View style={{
              backgroundColor: getColor
               (
                 chunks,
                 i,
                 percentPlayed,
                 percentPlayable,
                 inverse
               ),
              width: 2,
              marginRight: 1,
              height: scaleLinearHeight(mean(chunk))
             }}
            />
          </TouchableOpacity>
         ))}
        </View>
      )
  }
```

Le **composant Waveform** fonctionne comme suit :

* Les Chunks divisent l'objet `samples` en fonction de la `width` que l'utilisateur souhaite rendre à l'écran.
* Les Chunks sont ensuite mappés dans un événement `Touchable`. Les styles sont `width:2` et `height: scaleLinearHeight(mean(chunk))`. Cela génère la `moyenne` à partir de `d3-array`.
* La `backgroundColor` est passée en tant que méthode avec différents paramètres à la méthode `getColor`. Cela déterminera ensuite la couleur à retourner en fonction des conditions définies.
* L'événement `Touchable onPress` appellera le gestionnaire personnalisé passé dans celui-ci, pour définir le nouveau _temps de recherche_ de la piste.

Ce composant sans état peut maintenant être rendu dans votre composant enfant comme suit :

```jsx
render() {
  const {height, width} = this.props
  const { waveform } = this.state
  if (!waveform) return null;
  return (
     <View style={{flex: 1, justifyContent: 'center'}}>
       <Waveform
         waveform={waveform}
         height={height}
         width={width}
         setTime={this.setTime}
         percentPlayed={this.props.percent}
         percentPlayable={this.props.percentPlayable}
         inverse
       />
       <Waveform
         waveform={waveform}
         height={height}
         width={width}
         setTime={this.setTime}
         percentPlayed={this.props.percent}
         percentPlayable={this.props.percentPlayable}
         inverse={false}
       />
     </View>
    )
}
```

Ici, l'un des composants de forme d'onde est original et l'autre est inversé comme dans le lecteur de SoundCloud.

### Conclusion

Voici les liens vers _react-native-soundcloud-waveform_

* [Github](https://github.com/pritishvaidya/react-native-soundcloud-waveform)
* [npm](https://www.npmjs.com/package/react-native-soundcloud-waveform)

J'ai également créé une application en react-native — **MetalCloud** pour les fans de **musique Metal** où vous pouvez voir le composant ci-dessus en action.

Voici les liens :

* [IOS](https://itunes.apple.com/us/app/metalcloud/id1319945253?mt=8)
* [Android](https://play.google.com/store/apps/details?id=com.metalcloud)

Merci d'avoir lu. Si vous avez aimé cet article, montrez votre soutien en applaudissant pour partager avec d'autres personnes sur Medium.

_D'autres choses intéressantes peuvent être trouvées sur mes profils [StackOverflow](https://stackoverflow.com/users/6606831/pritish-vaidya) et [GitHub](https://github.com/pritishvaidya)._

_Suivez-moi sur [LinkedIn](https://www.linkedin.com/in/pritish-vaidya-506686128/), [Medium](https://medium.com/@pritishvaidya94), [Twitter](https://twitter.com/PritishVaidya) pour des mises à jour sur les nouveaux articles._