---
title: Building the React Image Optimization Component for Tueri.io
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
seo_title: null
seo_desc: 'By Dane Stevens


  Let’s face it, image optimization is hard. We want to make it effortless.

  When we set out to build our React Component there were a few problems we wanted
  to solve:


  Automatically decide image width for any device based on the parent...'
---

By Dane Stevens

![Low-quality Image Placeholder](https://cdn.tueri.io/274877906967/low-quality-image-placeholder-example.png)

Let’s face it, image optimization is hard. We want to make it effortless.

When we set out to build our React Component there were a few problems we wanted to solve:

* Automatically decide image width for any device based on the parent container.

* Use the best possible image format the user’s browser supports.

* Automatic image lazy loading.

* Automatic low-quality image placeholders (LQIP).

Oh, and it had to be effortless for React Developers to use.

## This is what we came up with:

```jsx
<Img src={ tueriImageId } alt='Alt Text' />

```

Easy right? Let’s dive in.

## Calculating the image size:

Create a `<figure />` element, detect the width and build an image URL:

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

        // Destructure props and state
        const { src, alt, options = {}, ext = 'jpg' } = this.props
        const { width } = this.state

        // Create an empty query string
        let queryString = ''        

        // If width is specified, otherwise use auto-detected width
        options['w'] = options['w'] || width

        // Loop through option object and build queryString
        Object.keys(options).map((option, i) => {
            return queryString +=  `${i < 1 ? '?' : '&'}${option}=${options[option]}`
        })

        return(
            <figure ref={this.imgRef}>
                { 
                    // If the container width has been set, display the image else null
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

This returns the following HTML:

```jsx
<figure>
    <img 
        src="https://cdn.tueri.io/tueriImageId/alt-text.jpg?w=autoCalculatedWidth" 
        alt="Alt Text" 
    />
</figure>

```

## Use the best possible image format:

Next, we needed to add support for detecting WebP images and having the Tueri service return the image in the WebP format:

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

        // If a format has not been specified, detect webp support
        // Set the fm (format) option in the image URL
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

This returns the following HTML:

```jsx
<figure>
    <img 
        src="https://cdn.tueri.io/tueriImageId/alt-text.jpg?w=autoCalculatedWidth&fm=webp" 
        alt="Alt Text" 
    />
</figure>

```

## Automatic image lazy loading:

Now, we need to find out if the `<figure />` element is in the viewport, plus we add a little buffer area so the images load just before being scrolled into view.

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
       // Only run if the image has not already been loaded
       if (this.imgRef.current && !this.state.lqipLoaded) {
           // Get the viewport height
           const windowHeight = this.window.innerHeight
           // Get the top position of the <figure /> element
           const imageTopPosition = this.imgRef.current.getBoundingClientRect().top
           // Multiply the viewport * buffer (default buffer: 1.5)
           const buffer = typeof this.props.buffer === 'number' && this.props.buffer > 1 && this.props.buffer < 10 ? this.props.buffer : 1.5
           // If <figure /> is in viewport
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

       // Destructure props and state
       // ...
       const { isInViewport, width } = this.state
       
       // ...
       
       return (
           <figure ref={this.imgRef}>
               { 
                   // If the container width has been set, display the image else null
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

## Automatic low-quality image placeholders (LQIP):

Finally, when an image is in the viewport, we want to load a 1/10 size blurred image, then fade out the placeholder image when the full-size image is loaded:

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

        // Destructure props and state
        // ...
        const { isInViewport, width, fullsizeLoaded } = this.state

        // ...
        
        // Modify the queryString for the LQIP image: replace the width param with a value 1/10 the fullsize
        const lqipQueryString = queryString.replace(`w=${ width }`, `w=${ Math.round(width * 0.1) }`)

        // Set the default styles. The full size image should be absolutely positioned within the <figure /> element
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

        // When the fullsize image is loaded, fade out the LQIP
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

                            {/* Load fullsize image in background */}
                            <img 
                                onLoad={ () => { this.setState({ fullsizeLoaded: true }) } }
                                style={ styles.fullsize }
                                src={`https://cdn.tueri.io/${ src }/${ kebabCase(alt) }.${ ext }${ queryString }`}
                                alt={ alt }
                            />

                            {/* Load LQIP in foreground */}
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

## Putting it all together:

Image optimization made effortless. Just swap out your regular `<img />` elements for the Tueri `<Img />` and never worry about optimization again.

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

        // Destructure props and state
        const { src, alt, options = {}, ext = 'jpg' } = this.props
        const { isInViewport, width, fullsizeLoaded } = this.state

        // Create an empty query string
        let queryString = ''

        // If width is specified, otherwise use auto-detected width
        options['w'] = options['w'] || width

        // If a format has not been specified, detect webp support
        if (!options['fm'] && this.isWebpSupported) {
            options['fm'] = 'webp'
        }

        // Loop through option prop and build queryString
        Object.keys(options).map((option, i) => {
            return queryString +=  `${i < 1 ? '?' : '&'}${option}=${options[option]}`
        })

        // Modify the queryString for the LQIP image: replace the width param with a value 1/10 the fullsize
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

        // When the fullsize image is loaded, fade out the LQIP
        if (fullsizeLoaded) {
            styles.lqip.opacity = 0
        }

        const missingALt = 'ALT TEXT IS REQUIRED'

        return(
            // Return the CDN domain from the TueriProvider
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

                                    {/* Load fullsize image in background */}
                                    <img 
                                        onLoad={ () => { this.setState({ fullsizeLoaded: true }) } }
                                        style={ styles.fullsize }
                                        src={`${ domain }/${ src }/${ kebabCase(alt || missingALt) }.${ ext }${ queryString }`}
                                        alt={ alt || missingALt }
                                    />

                                    {/* Load LQIP in foreground */}
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

## See it in action:

Try out a live demo on CodeSandbox:

%[https://codesandbox.io/s/qjzqw7w3q?fontsize=14]

---

_Originally published at [Tueri.io](https://tueri.io/blog/2019-03-21-building-the-react-image-optimization-component/?utm_source=Freecodecamp&utm_medium=Post&utm_campaign=)_

