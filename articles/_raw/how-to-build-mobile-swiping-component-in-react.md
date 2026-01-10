---
title: How to Build a Mobile Swiping Component in React
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-02-02T17:43:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-mobile-swiping-component-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/MobileSwiping-splash--1-.png
tags:
- name: Accessibility
  slug: accessibility
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: React
  slug: react
seo_title: null
seo_desc: "Everyone wants to be able to access the web from their mobile phones these\
  \ days. So it's important to consider the accessibility of your web app on Android\
  \ and iPhones. \nThe most difficult part is building the navigation – and swiping\
  \ in particular c..."
---

Everyone wants to be able to access the web from their mobile phones these days. So it's important to consider the accessibility of your web app on Android and iPhones. 

The most difficult part is building the navigation – and swiping in particular can cause a lot of headaches. There are libraries you can use to help with this, but why not build it on your own? 

In this tutorial, I will teach you how to create your own mobile swiping component in React. You can do it in 50 lines of JavaScript. 

Initially, I created this component for my pet project, the 2048 Game in React, and have now decided to share how I did it. 

If you want to try it out before reading the whole article, you can [play the game here](https://mateuszsokola.github.io/2048-in-react/) (use your mobile device). In this tutorial, we will focus on mobile swiping only.  
  
You can find the following resources on GitHub:

* 📱 [Source code of the component](https://gist.github.com/mateuszsokola/80b2a939ad521eb26f488fcdc659e0ca)
* 🕹️ [Source code of 2048 Game](https://github.com/mateuszsokola/2048-in-react/)

Here is the sneak peak (the quality isn't the best because I was trying to keep the size small):

![Image](https://www.freecodecamp.org/news/content/images/2024/01/MobilePreview-low--1-.gif)
_The final result in my pet project_

## Table of Contents:

1. [Prerequisites](#heading-prerequisites)
2. [How to Simulate a Mobile Device in Your Browser](#heading-how-to-simulate-a-mobile-device-in-your-browser)
3. [The MobileSwiper Component](#heading-the-mobileswiper-component)
4. [Let's Make it Swipable](#heading-lets-make-it-swipable)
5. [Summary](#heading-summary)

## 🛠️ P**rerequisites**

Before we start, make sure you know a little bit about React and JavaScript. You don't need any sophisticated tools, but if you want to run the example project on your computer, then you will need to install [Node.js](https://nodejs.org/en) first.

Also, I'm using [Google Chrome](https://www.google.com/chrome/) to simulate a mobile device on my computer. Keep in mind that if you use any different browser, then the steps might be slightly different.

## 🔍 **How to Simulate a Mobile Device in Your Browser**

Before we start coding, I need to show you how to simulate a mobile device in Google Chrome. 

Open your browser, right click on your page, and choose "_Inspect_" from the dropdown menu.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/MobileSwiper-1.png)
_How to open Developer Tools in Google Chrome_

Your browser view should now be split into two parts. The second part contains Chrome's Developer Tools. 

Now, click on the "laptop & mobile" icon (1 in the image below) in top left corner of the Developer tools. Then select the "Dimensions" (2) of the device you want to simulate. I chose iPhone SE because this device has the smallest resolution supported by my game.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/MobileSwiper-2.png)
_Choose device dimensions in Developer Tools (Google Chrome)_

Now we are ready to simulate swiping by using our mouse or touchpad. Just pay attention to the GIF below – my cursor turned into a circle which is supposed to visualize the area covered by a person's finger. 

When I try to swipe, my browser thinks I am actually scrolling through the website. In my case, this isn't an expected behavior. I would like to instead use swipes to play the game.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/game-v2-broken.gif)
_By default, scrolling events are associated with swipes_

## 🤓 The MobileSwiper Component

First, we need to create a **mobile-swiper**.**jsx** file. In this file, we declare a standard React component. Our component needs to accept two properties – `children` and `onSwipe`.

```js
export default function MobileSwiper({ children, onSwipe }) {
	return null   
}
```

Let me briefly explain them:

* `children` allows `MobileSwiper` to accept and render any content placed between its opening and closing tags. It enables you to inject the entire board inside this component – but we will get to this later.
* `onSwipe` is a callback that our component will trigger each time the user swipes within the "swipable" area. 

Let's define the swipable area now. First, you need to add a reference to the DOM element in which you want to allow swiping. You can do this by using the `useRef` hook. So declare a constant called `wrapperRef`:

```js
import { useRef } from "react"

export default function MobileSwiper({ children, onSwipe }) {
	const wrapperRef = useRef(null)

    return null
    
} 
```

Side note: The `useRef` is a React Hook that lets you reference a value that’s not needed for rendering. It’s particularly common to use it to manipulate the [DOM](https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API). React has built-in support for this.

Now you just need to return the `<div />` that references the constant you created using the `useRef` hook.

```js
import { useRef } from "react"

export default function MobileSwiper({ children, onSwipe }) {
	const wrapperRef = useRef(null)

    return <div ref={wrapperRef}>{children}</div>
} 
```

Let's think for a moment how we can detect swiping. I believe the easiest way is comparing the starting and ending position of the user's finger. 

This means we need to store the initial position of the user's finger in state. Basically, we will store `x` and `y` coordinates using the `useState` hook.

```js
import { useState, useRef } from "react"

export default function MobileSwiper({ children, onSwipe }) {
	const wrapperRef = useRef(null)
	const [startX, setStartX] = useState(0)
	const [startY, setStartY] = useState(0)    

    return <div ref={wrapperRef}>{children}</div>
} 
```

Now we need to create two event callbacks:

* `handleTouchStart` will set the starting position of the user's finger.
* `handleTouchEnd` will set the final position of the user's finger and calculate the shift (delta) based on the starting point.

Let's start with the `handleTouchStart` event handler:

```js
import { useCallback, useState, useRef } from "react"

export default function MobileSwiper({ children, onSwipe }) {
	const wrapperRef = useRef(null)
	const [startX, setStartX] = useState(0)
	const [startY, setStartY] = useState(0)    

	const handleTouchStart = useCallback((e) => {
        if (!wrapperRef.current.contains(e.target)) {
      		return
    	}

    	e.preventDefault()

	    setStartX(e.touches[0].clientX)
    	setStartY(e.touches[0].clientY)
  	}, [])
    
    return <div ref={wrapperRef}>{children}</div>
} 
```

Let me briefly explain it:

1. I wrapped this helper into the `useCallback` hook to cache and improve its performance. If you don't know this hook, you can read about it in the official [React docs](https://react.dev/reference/react/useCallback).
2. The `if` statement checks if the user is swiping within the swipable area. If they swipe outside of this area, we will proceed with scrolling.
3. `e.preventDefault()` disables the default scrolling event.
4. The last two lines store `x` and `y` coordinates in state.

Now let's implement the `handleTouchEnd` event handler:

```js
import { useCallback, useState, useRef } from "react"

export default function MobileSwiper({ children, onSwipe }) {
	const wrapperRef = useRef(null)
	const [startX, setStartX] = useState(0)
	const [startY, setStartY] = useState(0)    

	const handleTouchStart = useCallback((e) => {
        if (!wrapperRef.current.contains(e.target)) {
      		return
    	}

    	e.preventDefault()

	    setStartX(e.touches[0].clientX)
    	setStartY(e.touches[0].clientY)
    }, [])
    
  	const handleTouchEnd = useCallback((e) => {
        if (!wrapperRef.current.contains(e.target)) {
            return
        }
        
        e.preventDefault()
        
        const endX = e.changedTouches[0].clientX
        const endY = e.changedTouches[0].clientY
        const deltaX = endX - startX
        const deltaY = endY - startY
        
        onSwipe({ deltaX, deltaY })
    }, [startX, startY, onSwipe])
    
    return <div ref={wrapperRef}>{children}</div>
} 
```

As you can see, steps 1-3 are exactly the same as in the `handleTouchStart` callback. Now, we'll take the final `x` and `y` coordinates of user's finger and deduct the initial `x` and `y` from those. Thanks to that we can calculate horizontal and vertical shift of the user's finger (deltas).

Then we pass those deltas onto the `onSwipe` callback. If you remember, we declared it in the component's props at the beginning. 

Now we need to connect those callbacks into the event listener. To do so, we can use the `useEffect` hook from React.

```js
import { useCallback, useEffect, useState, useRef } from "react"

export default function MobileSwiper({ children, onSwipe }) {
	const wrapperRef = useRef(null)
	const [startX, setStartX] = useState(0)
	const [startY, setStartY] = useState(0)    

	const handleTouchStart = useCallback((e) => {
        if (!wrapperRef.current.contains(e.target)) {
      		return
    	}

    	e.preventDefault()

	    setStartX(e.touches[0].clientX)
    	setStartY(e.touches[0].clientY)
  	}, [])
    
  	const handleTouchEnd = useCallback(
    (e) => {
        if (!wrapperRef.current.contains(e.target)) {
            return
        }
        
        e.preventDefault()
        
        const endX = e.changedTouches[0].clientX
        const endY = e.changedTouches[0].clientY
        const deltaX = endX - startX
        const deltaY = endY - startY
        
        onSwipe({ deltaX, deltaY })
    }, [startX, startY, onSwipe])   
    
 	useEffect(() => {
        window.addEventListener("touchstart", handleTouchStart)
        window.addEventListener("touchend", handleTouchEnd)
        
        return () => {
            window.removeEventListener("touchstart", handleTouchStart)
            window.removeEventListener("touchend", handleTouchEnd)
        }
  	}, [handleTouchStart, handleTouchEnd])
    
    return <div ref={wrapperRef}>{children}</div>
} 
```

You can read more about the `useEffect` hook in the official [React docs](https://react.dev/reference/react/useEffect).

The **MobileSwiper** component is ready now.

## 🔌 Let's Make It Swipable

The last thing we need to do is hook our component to the application. As I mentioned, I will be using this component in my 2048 Game ([Source code](https://github.com/mateuszsokola/2048-in-react/)). If you want to use it somewhere else, the `handleSwipe` helper and the MobileSwiper component will remain the same.

 Let's plug it into the Board component:

```js
import { useCallback, useContext, useEffect, useRef } from "react"
import { Tile as TileModel } from "@/models/tile"
import styles from "@/styles/board.module.css"
import Tile from "./tile"
import { GameContext } from "@/context/game-context"
import MobileSwiper from "./mobile-swiper"

export default function Board() {
	const { getTiles, moveTiles, startGame } = useContext(GameContext);
	
    // ... removed irrelevant parts ...
    
    const handleSwipe = useCallback(({ deltaX, deltaY }) => {
    	if (Math.abs(deltaX) > Math.abs(deltaY)) {
            if (deltaX > 0) {
            	moveTiles("move_right")
            } else {
            	moveTiles("move_left")
            }
        } else {
            if (deltaY > 0) {
                moveTiles("move_down")
            } else {
                moveTiles("move_up")
            }
        }
    }, [moveTiles])

 	// ... removed irrelevant parts ...

	return (
    	<MobileSwiper onSwipe={handleSwipe}>
      		<div className={styles.board}>
        		<div className={styles.tiles}>{renderTiles()}</div>
        		<div className={styles.grid}>{renderGrid()}</div>
      		</div>
    	</MobileSwiper>
  	)
}

```

Let's start with the `handleSwipe` handler. As you can see, we're comparing if `deltaX` is greater than `deltaY` to decide if the user swiped horizontally (left / right) or vertically (top / bottom).

If it was a horizontal swipe, then:

* negative `deltaX` means they swiped to the left.
* positive `deltaX` means they swiped to the right.

If it was a vertical swipe, then:

* negative `deltaY` means they swiped up.
* positive `deltaY` means they swiped down.

Now, let's focus on the MobileSwiper component. You can find it in the `return` statement. We're passing the `handleSwipe` helper to the `onSwipe` property and wrapping the entire HTML code of the Board component to enable swiping on it.

Now when we try it out, the result isn't ideal. Scrolling events are mixed with mobile swipes, as you can see below:

![Image](https://www.freecodecamp.org/news/content/images/2024/01/game-v2-passive-true.gif)
_Board with duplicated events – swipes and scrolling_

This is happening because modern browsers use passive event listeners to improve the scrolling experience on mobile devices. This means that the `preventDefault` we added to our event callbacks never happens. 

To disable scrolling behavior, we need to disable passive listeners on the MobileSwiper component:

```js
import { useCallback, useEffect, useState, useRef } from "react"

export default function MobileSwiper({ children, onSwipe }) {
	// ... removed to improve visibility ...
    
 	useEffect(() => {
        window.addEventListener("touchstart", handleTouchStart, { passive: false })
        window.addEventListener("touchend", handleTouchEnd, { passive: false })
        // ... removed to improve visibility ...
  	}, [handleTouchStart, handleTouchEnd])
    
	// ... removed to improve visibility ...
} 
```

Now the scrolling behavior is gone and the 2048 Game looks just awesome:

![Image](https://www.freecodecamp.org/news/content/images/2024/01/game-v2-works.gif)
_Final result - swiping works!_

## 🏁 Summary

Today I showed you that you don't always need libraries to handle mobile gestures in React. Some simple events such as swiping can be implemented using basic React features. We just used a bunch of React hooks and wrote two simple event handlers. 

The entire implementation has exactly 50 lines of code. I hope I inspired you to try to deal with mobile events on your own.

If this article helped you, please [let me know on Twitter](https://twitter.com/msokola). Educators like me often feel like we are speaking into a vacuum and nobody cares what we teach. A simple "shoutout" shows it was worth an effort and inspires me to create more content like this.

Please share this article on your social media. Thank you!

## 🎥 Create Your Own 2048 Game

This article is a part of my course on Udemy where I teach how to create a fully-functional 2048 Game in Next.js from scratch. 

### 🧑‍🎓 Join my [Next.js course on Udemy](https://www.udemy.com/course/2048-in-react-and-nextjs/?referralCode=AC3FD6336BAB9C402106)  

Use code **FREECODECAMP** to enroll to get a 60% discount.

I believe programming should be fun and unleash creativity. You don't have to build yet another TODO list or a shopping cart. Instead, you can build something that you can show to your friends or maybe even a hiring manager!

PS. If you prefer to watch screencasts, then this lesson is available on Udemy for free. You can find it under the "_Responsive Layout and Missing Game Feature_" section in the lecture called "_Game layout and mobile swipes_".  

