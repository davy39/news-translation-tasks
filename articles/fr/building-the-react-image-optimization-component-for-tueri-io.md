---
title: Construction du composant d'optimisation d'image React pour Tueri.io
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-11T18:37:17.000Z'
originalURL: https://freecodecamp.org/news/building-the-react-image-optimization-component-for-tueri-io
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/progressive.png
tags:
- name: Image Placeholder
  slug: image-placeholder
- name: 'image optimization '
  slug: image-optimization
- name: React
  slug: reactjs
- name: responsive images
  slug: responsive-images
seo_title: Construction du composant d'optimisation d'image React pour Tueri.io
seo_desc: 'By Dane Stevens


  Let’s face it, image optimization is hard. We want to make it effortless.

  When we set out to build our React Component there were a few problems we wanted
  to solve:


  Automatically decide image width for any device based on the parent...'
---

Par Dane Stevens

![Placeholder d'image de faible qualité](https://cdn.tueri.io/274877906967/low-quality-image-placeholder-example.png)

Admettons-le, l'optimisation d'image est difficile. Nous voulons la rendre sans effort.

Lorsque nous nous sommes lancés dans la construction de notre composant React, il y avait quelques problèmes que nous voulions résoudre :

* Décider automatiquement de la largeur de l'image pour tout appareil en fonction du conteneur parent.

* Utiliser le meilleur format d'image possible que le navigateur de l'utilisateur supporte.

* Chargement paresseux automatique des images.

* Placeholders d'image de faible qualité automatiques (LQIP).

Oh, et il fallait que ce soit sans effort pour les développeurs React à utiliser.

## Voici ce que nous avons conçu :

```jsx
<Img src={ tueriImageId } alt='Texte alternatif' />

```

Facile, non ? Plongeons-nous.

## Calcul de la taille de l'image :

Créez un élément `<figure />`, détectez la largeur et construisez une URL d'image :

```jsx
class Img extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            width: 0
        }
        this.imgRef = React.createRef()
    }

    componentDidMount() {
        const width = this.imgRef.current.clientWidth
        this.setState({
            width
        })
    }

    render() {

        // Déstructurer les props et le state
        const { src, alt, options = {}, ext = 'jpg' } = this.props
        const { width } = this.state

        // Créer une chaîne de requête vide
        let queryString = ''        

        // Si la largeur est spécifiée, sinon utiliser la largeur détectée automatiquement
        options['w'] = options['w'] || width

        // Parcourir l'objet option et construire queryString
        Object.keys(options).map((option, i) => {
            return queryString +=  `${i < 1 ? '?' : '&'}${option}=${options[option]}`
        })

        return(
            <figure ref={this.imgRef}>
                { 
                    // Si la largeur du conteneur a été définie, afficher l'image sinon null
                    width > 0 ? (
                        <img
                            src={`https://cdn.tueri.io/${ src }/${ kebabCase(alt) }.${ ext }${ queryString }`}
                            alt={ alt }
                        />
                    ) : null 
                }
            </figure>
        )

    }
}

export default Img

```

Cela retourne le HTML suivant :

```jsx
<figure>
    <img 
        src="https://cdn.tueri.io/tueriImageId/alt-text.jpg?w=autoCalculatedWidth" 
        alt="Alt Text" 
    />
</figure>

```

## Utiliser le meilleur format d'image possible :

Ensuite, nous devions ajouter la prise en charge de la détection des images WebP et faire en sorte que le service Tueri retourne l'image au format WebP :

```jsx
class Img extends React.Component {

    constructor(props) {
        // ...
        this.window = typeof window !== 'undefined' && window
        this.isWebpSupported = this.isWebpSupported.bind(this)
    }

    // ...
    
    isWebpSupported() {
        if (!this.window.createImageBitmap) {
            return false;
        }
        return true;
    }

    render() {

        // ...

        // Si un format n'a pas été spécifié, détecter la prise en charge de webp
        // Définir l'option fm (format) dans l'URL de l'image
        if (!options['fm'] && this.isWebpSupported) {
            options['fm'] = 'webp'
        }

        // ...
        
        return (
            // ...
        )

    }
}

// ...

```

Cela retourne le HTML suivant :

```jsx
<figure>
    <img 
        src="https://cdn.tueri.io/tueriImageId/alt-text.jpg?w=autoCalculatedWidth&fm=webp" 
        alt="Alt Text" 
    />
</figure>

```

## Chargement paresseux automatique des images :

Maintenant, nous devons déterminer si l'élément `<figure />` est dans la fenêtre d'affichage, plus nous ajoutons une petite zone tampon pour que les images se chargent juste avant d'être défilées dans la vue.

```jsx
   class Img extends React.Component {

   constructor(props) {
       // ...
       this.state = {
           // ...
           isInViewport: false
           lqipLoaded: false
       }
       // ...
       this.handleViewport = this.handleViewport.bind(this)
   }

   componentDidMount() {
       // ...
       this.handleViewport()
       this.window.addEventListener('scroll', this.handleViewport)
   }
   
   handleViewport() {
       // Ne s'exécute que si l'image n'a pas déjà été chargée
       if (this.imgRef.current && !this.state.lqipLoaded) {
           // Obtenir la hauteur de la fenêtre d'affichage
           const windowHeight = this.window.innerHeight
           // Obtenir la position supérieure de l'élément <figure />
           const imageTopPosition = this.imgRef.current.getBoundingClientRect().top
           // Multiplier la fenêtre d'affichage * tampon (tampon par défaut : 1,5)
           const buffer = typeof this.props.buffer === 'number' && this.props.buffer > 1 && this.props.buffer < 10 ? this.props.buffer : 1.5
           // Si <figure /> est dans la fenêtre d'affichage
           if (windowHeight * buffer > imageTopPosition) {
               this.setState({
                   isInViewport: true
               })
           }
       }
   }
   
   // ...
   
   componentWillUnmount() {
       this.window.removeEventListener('scroll', this.handleViewport)
   }

   render() {

       // Déstructurer les props et le state
       // ...
       const { isInViewport, width } = this.state
       
       // ...
       
       return (
           <figure ref={this.imgRef}>
               { 
                   // Si la largeur du conteneur a été définie, afficher l'image sinon null
                   isInViewport && width > 0 ? (
                       <img 
                           onLoad={ () => { this.setState({ lqipLoaded: true }) } }
                           // ...
                       />
                   ) : null 
               }
           </figure>
       )

   }
}

export default Img

```

## Placeholders d'image de faible qualité automatiques (LQIP) :

Enfin, lorsqu'une image est dans la fenêtre d'affichage, nous voulons charger une image floue de taille 1/10, puis faire disparaître l'image de placeholder lorsque l'image en pleine taille est chargée :

```jsx
class Img extends React.Component {

    constructor(props) {
        // ...
        this.state = {
            // ...
            fullsizeLoaded: false
        }

        // ...

    }

    // ...

    render() {

        // Déstructurer les props et le state
        // ...
        const { isInViewport, width, fullsizeLoaded } = this.state

        // ...
        
        // Modifier la queryString pour l'image LQIP : remplacer le paramètre de largeur par une valeur 1/10 de la taille réelle
        const lqipQueryString = queryString.replace(`w=${ width }`, `w=${ Math.round(width * 0.1) }`)

        // Définir les styles par défaut. L'image en pleine taille doit être positionnée absolument dans l'élément <figure />
        const styles = {
            figure: {
                position: 'relative',
                margin: 0
            },
            lqip: {
                width: '100%',
                filter: 'blur(5px)',
                opacity: 1,
                transition: 'all 0.5s ease-in'
            },
            fullsize: {
                position: 'absolute',
                top: '0px',
                left: '0px',
                transition: 'all 0.5s ease-in'
            }
        }

        // Lorsque l'image en pleine taille est chargée, faire disparaître le LQIP
        if (fullsizeLoaded) {
            styles.lqip.opacity = 0
        }

        return(
            <figure
                style={ styles.figure }
                // ...
            >
                {
                    isInViewport && width > 0 ? (
                        <React.Fragment>

                            {/* Charger l'image en pleine taille en arrière-plan */}
                            <img 
                                onLoad={ () => { this.setState({ fullsizeLoaded: true }) } }
                                style={ styles.fullsize }
                                src={`https://cdn.tueri.io/${ src }/${ kebabCase(alt) }.${ ext }${ queryString }`}
                                alt={ alt }
                            />

                            {/* Charger le LQIP en premier plan */}
                            <img 
                                onLoad={ () => { this.setState({ lqipLoaded: true }) } }
                                style={ styles.lqip }
                                src={`https://cdn.tueri.io/${ src }/${ kebabCase(alt) }.${ ext }${ lqipQueryString }`} 
                                alt={ alt } 
                            />
                        </React.Fragment>
                    ) : null
                }            
            </figure>
        )

    }
}

// ...

```

## Mettre le tout ensemble :

L'optimisation d'image rendue sans effort. Il suffit de remplacer vos éléments `<img />` réguliers par le `<Img />` de Tueri et ne vous souciez plus jamais de l'optimisation.

```jsx
import React from 'react'
import PropTypes from 'prop-types'
import { TueriContext } from './Provider'
import kebabCase from 'lodash.kebabcase'

class Img extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            isInViewport: false,
            width: 0,
            height: 0,
            lqipLoaded: false,
            fullsizeLoaded: false
        }

        this.imgRef = React.createRef()
        this.window = typeof window !== 'undefined' && window 
        this.handleViewport = this.handleViewport.bind(this)       
        this.isWebpSupported = this.isWebpSupported.bind(this)

    }

    componentDidMount() {

        const width = this.imgRef.current.clientWidth

        this.setState({
            width
        })
        
        this.handleViewport()

        this.window.addEventListener('scroll', this.handleViewport)

    }

    handleViewport() {
        if (this.imgRef.current && !this.state.lqipLoaded) {
            const windowHeight = this.window.innerHeight
            const imageTopPosition = this.imgRef.current.getBoundingClientRect().top
            const buffer = typeof this.props.buffer === 'number' && this.props.buffer > 1 && this.props.buffer < 10 ? this.props.buffer : 1.5
            if (windowHeight * buffer > imageTopPosition) {
                this.setState({
                    isInViewport: true
                })
            }

        }
    }

    isWebpSupported() {
        if (!this.window.createImageBitmap) {
            return false;
        }
        return true;
    }

    componentWillUnmount() {
        this.window.removeEventListener('scroll', this.handleViewport)
    }

    render() {

        // Déstructurer les props et le state
        const { src, alt, options = {}, ext = 'jpg' } = this.props
        const { isInViewport, width, fullsizeLoaded } = this.state

        // Créer une chaîne de requête vide
        let queryString = ''

        // Si la largeur est spécifiée, sinon utiliser la largeur détectée automatiquement
        options['w'] = options['w'] || width

        // Si un format n'a pas été spécifié, détecter la prise en charge de webp
        if (!options['fm'] && this.isWebpSupported) {
            options['fm'] = 'webp'
        }

        // Parcourir la prop option et construire queryString
        Object.keys(options).map((option, i) => {
            return queryString +=  `${i < 1 ? '?' : '&'}${option}=${options[option]}`
        })

        // Modifier la queryString pour l'image LQIP : remplacer le paramètre de largeur par une valeur 1/10 de la taille réelle
        const lqipQueryString = queryString.replace(`w=${ width }`, `w=${ Math.round(width * 0.1) }`)

        const styles = {
            figure: {
                position: 'relative',
                margin: 0
            },
            lqip: {
                width: '100%',
                filter: 'blur(5px)',
                opacity: 1,
                transition: 'all 0.5s ease-in'
            },
            fullsize: {
                position: 'absolute',
                top: '0px',
                left: '0px',
                transition: 'all 0.5s ease-in'
            }
        }

        // Lorsque l'image en pleine taille est chargée, faire disparaître le LQIP
        if (fullsizeLoaded) {
            styles.lqip.opacity = 0
        }

        const missingALt = 'LE TEXTE ALTERNATIF EST OBLIGATOIRE'

        return(
            // Retourner le domaine CDN du TueriProvider
            <TueriContext.Consumer>
                {({ domain }) => (
                    <figure
                        style={ styles.figure }
                        ref={this.imgRef}
                    >
                        {
                            // 
                            isInViewport && width > 0 ? (
                                <React.Fragment>

                                    {/* Charger l'image en pleine taille en arrière-plan */}
                                    <img 
                                        onLoad={ () => { this.setState({ fullsizeLoaded: true }) } }
                                        style={ styles.fullsize }
                                        src={`${ domain }/${ src }/${ kebabCase(alt || missingALt) }.${ ext }${ queryString }`}
                                        alt={ alt || missingALt }
                                    />

                                    {/* Charger le LQIP en premier plan */}
                                    <img 
                                        onLoad={ () => { this.setState({ lqipLoaded: true }) } }
                                        style={ styles.lqip }
                                        src={`${ domain }/${ src }/${ kebabCase(alt || missingALt) }.${ ext }${ lqipQueryString }`} 
                                        alt={ alt || missingALt } 
                                    />
                                </React.Fragment>
                            ) : null
                        }            
                    </figure>
                )}
                
            </TueriContext.Consumer>
        )

    }
}

Img.propTypes = {
    src: PropTypes.string.isRequired,
    alt: PropTypes.string.isRequired,
    options: PropTypes.object,
    ext: PropTypes.string,
    buffer: PropTypes.number
}

export default Img

```

## Voir en action :

Essayez une démonstration en direct sur CodeSandbox :

%[https://codesandbox.io/s/qjzqw7w3q?fontsize=14]

---

_Publié à l'origine sur [Tueri.io](https://tueri.io/blog/2019-03-21-building-the-react-image-optimization-component/?utm_source=Freecodecamp&utm_medium=Post&utm_campaign=)_