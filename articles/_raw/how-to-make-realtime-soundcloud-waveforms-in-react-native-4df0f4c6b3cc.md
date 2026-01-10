---
title: How to make realtime SoundCloud Waveforms in React Native
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
seo_title: null
seo_desc: 'By Pritish Vaidya

  Introduction

  SoundCloud is a music and podcast streaming platform for listening to millions of
  authentic tracks. They have a really interactive interface for playing / listening
  to the tracks.

  The most important feature in their int...'
---

By Pritish Vaidya

### **Introduction**

SoundCloud is a music and podcast streaming platform for listening to millions of authentic tracks. They have a really interactive interface for playing / listening to the tracks.

The most important feature in their interface is showing the progress of the track based on its _frequency waveform._ This helps the users to identify the nature of it.

They also have a [blog post](https://developers.soundcloud.com/blog/waveforms-let-s-talk-about-them) which describes how to use the waveform based on its image. It is hard to use the same techniques to generate the waveform in a _React Native_ app. Their [**Waveform.js**](https://github.com/soundcloud/waveformjs) **SDK** _translates a waveform into floating points to render on an HTML5 canvas_ and is currently _no longer operational._

In this article we’ll discuss how to use the same waveform for our React Native apps.

### Why Should I use SoundCloud’s Waveforms?

![Image](https://cdn-media-1.freecodecamp.org/images/kB4RbN318B8fU2hED2jFXFaXDB8G8--O9HfB)
_Image Credits — [KnowYourMeme](https://knowyourmeme.com/photos/1269398-arthurs-headphones" rel="noopener" target="_blank" title=")_

* The SoundCloud’s waveform looks more impressive than the old boring way of showing the _progress bar._
* The pre-loaded waveform will give the user an idea of the different frequencies present in the song.
* It is also much easier to show the _buffered track percentage_ on a waveform rather than showing it on a blank progress bar.

### Let’s learn more about SoundCloud’s Waveforms

![Image](https://cdn-media-1.freecodecamp.org/images/LQ0a-DVQtUZJ8LmuJEqNenemVj10ylCPKzxJ)
_Image Credits — [Backstage Blog by SoundCloud Developers](http://img.svbtle.com/inline_leemartin_24131769094098_raw.png" rel="noopener" target="_blank" title=")_

The SoundCloud provides a `waveform_url` in its tracks API.

* Each track has its own unique `waveform_url` .
* The `waveform_url` contains a link to the image hoisted over the cloud.

**Example —** [https://w1.sndcdn.com/PP3Eb34ToNki_m.png](https://w1.sndcdn.com/PP3Eb34ToNki_m.png)

![Image](https://cdn-media-1.freecodecamp.org/images/ngCp52SzK2q5vYwSAyokRu5nsw8rs8PZdLAj)
_Image Credits — [SoundCloud’s waveform for the track “Megadeth — Sweating Bullets” by mauriciohaensch](https://w1.sndcdn.com/PP3Eb34ToNki_m.png" rel="noopener" target="_blank" title=")_

As of now, every argument is static hence it is unusable in this current state. Therefore we need to re-create the waveform based on it using **React Native’s** _containers_ in order to have access to the _touch events, styles etc._

### Getting Started

![Image](https://cdn-media-1.freecodecamp.org/images/g9wt8pkrRv-xcPBH8AhI4e-oZcJcUEst0bcc)
_Image Credits — [ImgFlip](https://imgflip.com/memegenerator/4081988/What-if-i-told-you" rel="noopener" target="_blank" title=")_

Here is a list of stuff that you will need:

* [d3-scale](https://github.com/d3/d3-scale)
* [d3-array](https://github.com/d3/d3-array)

First, we need the sampling of the waveform. The trick is to replace `.png` with `.json` for the `waveform_url` . A `GET` call to it would give us a response object that contains

* **width** (Width of the waveform)
* **height** (Height of the waveform)
* **samples** (Array)

For more info, you can try out the following link [https://w1.sndcdn.com/PP3Eb34ToNki_m.json](https://w1.sndcdn.com/PP3Eb34ToNki_m.json).

### Dive into the code

![Image](https://cdn-media-1.freecodecamp.org/images/bdodPYaqbZeIjm8lEuNdAIXa9BFywxEkmY3C)
_Image Credits — [Unsplash](https://images.unsplash.com/photo-1466477234737-8a3b3faed8c3?ixlib=rb-0.3.5&amp;s=919a7e046d85dc25ac72f4c3070228b6&amp;auto=format&amp;fit=crop&amp;w=800&amp;q=60" rel="noopener" target="_blank" title=")_

#### Add a Custom SoundCloudWave Component

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

It would be better to create a custom _SoundCloudWave_ component that can be used in multiple places as required. Here are the required `props`:

* **waveformUrl** — The URL object to the waveform (accessible through the Tracks API)
* **height** — Height of the waveform
* **width** — Width of the waveform component
* **percentPlayable** — The duration of the track buffered in seconds
* **percentPlayed** — The duration of the track played in seconds
* **setTime —** The callback handler to change the current track time.

#### Get the samples

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

Get the samples by using a simple `GET` API call and store the result in the `state`.

#### Create a Waveform Component

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

The **Waveform Component** works as follows:

* The Chunks split the `samples` object based on the `width` that the user wants to render on the screen.
* The Chunks are then mapped into a `Touchable` event. The styles as `width:2` and `height: scaleLinearHeight(mean(chunk))`. This generates the `mean` from the `d3-array`.
* The `backgroundColor` is being passed as a method with different parameters to the `getColor` method. This will then determine the color to return based on the conditions set.
* The `Touchable onPress` event will call the custom handler passed into it, to set the new _seek time_ of the track.

Now this stateless component can be rendered to your child component as:

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

Here one of the waveform component is original and one inverted as in the SoundCloud’s player.

### Conclusion

Here are the links to the _react-native-soundcloud-waveform_

* [Github](https://github.com/pritishvaidya/react-native-soundcloud-waveform)
* [npm](https://www.npmjs.com/package/react-native-soundcloud-waveform)

I’ve also made an app in react-native — **MetalCloud** for **Metal Music fans** where you can see the above component at work.

Here are the links:

* [IOS](https://itunes.apple.com/us/app/metalcloud/id1319945253?mt=8)
* [Android](https://play.google.com/store/apps/details?id=com.metalcloud)

Thanks for reading. If you liked this article, show your support by clapping to share with other people on Medium.

_More of the cool stuff can be found on my [StackOverflow](https://stackoverflow.com/users/6606831/pritish-vaidya) and [GitHub](https://github.com/pritishvaidya) profiles._

_Follow me on [LinkedIn](https://www.linkedin.com/in/pritish-vaidya-506686128/), [Medium](https://medium.com/@pritishvaidya94), [Twitter](https://twitter.com/PritishVaidya) for further update new articles._

