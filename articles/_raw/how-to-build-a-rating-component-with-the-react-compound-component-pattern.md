---
title: How to Build a Rating Component with the React Compound Component Pattern
subtitle: ''
author: David Jaja
co_authors: []
series: null
date: '2024-06-03T22:03:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-rating-component-with-the-react-compound-component-pattern
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/Group-341.png
tags:
- name: components
  slug: components
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: "Have you ever watched a captivating movie or used a fantastic product and\
  \ wanted to share your experience? In today's world, feedback is critical, and ratings\
  \ are like currency. \nRating systems are everywhere, from the classic star ratings\
  \ on movie r..."
---

Have you ever watched a captivating movie or used a fantastic product and wanted to share your experience? In today's world, feedback is critical, and ratings are like currency. 

Rating systems are everywhere, from the classic star ratings on movie review websites to the ubiquitous thumbs up/down on streaming platforms. They guide our choices, shape our opinions, and ultimately influence the success of products and services.

In this article, we will create a movie-themed rating component using the Compound Component pattern in React. I'll guide you through structuring the component, managing its state, and designing an interactive user interface that captures the essence of rating.

## Prerequisites

While this article is tailored to be as low-level as possible, having a base understanding of the React compound component pattern is beneficial. 

If you don’t have any experience with it, don't worry – I've got you! Just head over to [this compound component article](https://www.freecodecamp.org/news/build-a-dynamic-dropdown-component/) where I break it down more extensively. Other prerequisites include.

* Fundamentals of HTML, CSS, and Tailwind CSS
* Fundamentals of JavaScript, React, and React Hooks.

## **What We'll Cover:**

1. [Understanding Rating Components](#heading-understanding-rating-components)  
– [What Comprises a Rating Component](#heading-what-comprises-a-rating-component)  
– [Advantages of Rating Component](#heading-advantages-of-rating-components)
2. [How to Build a Rating Componen](#heading-regular-react-method-1)t                                                                                – [Regular React Method](#heading-regular-react-method-1)  
 – [Compound Component Method](#heading-compound-component-method)
3. [How to Upgrade Rating Component](#heading-how-to-upgrade-the-rating-component)
4. [And just for fun](#heading-and-just-for-fun)
5. [Conclusion](#heading-conclusion)

## Understanding Rating Components

Rating components are an essential part of modern web applications, particularly in contexts where user feedback is critical. These components provide a user-friendly interface for people to express their opinions, often in a quantifiable manner.

### What Comprises a Rating Component?

A rating component is a UI element that allows users to provide a rating, usually on a fixed scale. Here are the typical elements that make up a rating component:

* **Icons or Symbols**: These are the visual representations of the rating scale. Common examples include stars, hearts, thumbs, or numerical values.
* **Interactive States**: These components often change appearance based on user interaction, such as hovering or clicking.
* **Feedback Mechanism**: Some rating components display immediate feedback, such as highlighting the selected icons or showing the rating value.
* **Accessibility Features**: Ensuring that the component is accessible to all users, including keyboard navigation and screen readers, is crucial.
* **Custom Feedback**: Some rating components include a text area allowing users to comment. This feedback helps clarify the reasons behind their ratings and enables them to raise any issues they encounter.

### Advantages of Rating Components

Rating components offer several benefits, both for users and developers:

* **User Engagement**: They make it easy and enjoyable for users to provide feedback, which can increase engagement.
* **Quantifiable Feedback**: Ratings provide clear, quantifiable data that can be easily analyzed to gauge user satisfaction.
* **Guiding Decisions**: For other users, ratings help in making informed decisions about movies, products, services, and more.
* **Improving Products**: For businesses, ratings are invaluable for understanding user preferences and areas for improvement.

## How to Build a Rating Component

I've prepared a GitHub repository with starter files to speed things up. Simply clone [this repo](https://github.com/Daiveedjay/Rating-Component) and install the dependencies.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Let-s-get-this-party-started.gif)
_Let's get this party started_

In this section, we'll build a single rating component with regular React, and then rebuild it with the CC pattern.

### Regular React Method

You’re probably wondering why we’re going through the hassle of first building the component without the component pattern.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/woah-peter-griffin.gif)
_woah peter griffin_

Well, while learning the component pattern, I struggled to fully wrap my head around the logic and ended up with a couple of bugs which could have been prevented with better understanding. 

To help with this, I found that building a smaller version of the feature before fully implementing the CCP eventually sped up my development process.

To begin, create a `RatingComponent` and import it into your `App` component.

```js
import RatingComponent from "./RatingComponent";
import { Toaster } from "react-hot-toast";

export default function App() {
  return (
    <main className=" bg-[#EAF2F8]  gap-4 min-h-[100dvh] flex justify-center items-center flex-col">
      <Toaster />
      <h1 className="text-3xl ">My Ratings Component</h1>
      <RatingComponent />
    </main>
  );
}
```

Then head over to your `RatingComponent` and add some basic boilerplate to create a standard rating UI.

```js
import { FiStar } from "react-icons/fi";
export default function RatingComponent() {
  return (
    <div className="flex bg-white items-center justify-between  border border-black rounded-md min-w-[600px]  p-2">
      <div className="p-2 text-base font-semibold">
        Intersteller <span className="text-gray-400 ">(2014)</span>
      </div>
      <div className="flex gap-4 p-2">
        {Array.from({ length: 5 }).map((_, index) => (
          <div key={index} className="flex justify-center">
            <FiStar
              size={25}
              strokeWidth={0}
              fill={"gold"}
              cursor="pointer"
              className="star"
            />
          </div>
        ))}
      </div>
    </div>
  );
}
```

This makes your UI look like this:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/1-Ratings-UI-created.png)
_Ratings UI created_

At the moment, your UI is static and has no way of changing the rating values. To add interactivity, create a state which holds the initial value of the rating.

```js
const [stars, setStarts] = useState(0);
```

Then attach the setting handler to update the value of the stars when you click on a star.

```js
<FiStar
    size={25}
    strokeWidth={0}
    fill={"gold"}
    cursor="pointer"
    className="star"
    onClick={() => setStarts(index + 1)}
 />
```

**Note**: We’re adding 1 to the set value since arrays are zero-based.

To confirm the value of the star being set on click, add a dynamic fill value to each star.

```js
 <FiStar
   size={25}
   strokeWidth={0}
   fill={index + 1 <= stars ? "gold" : "#D6DBDF"}
   cursor="pointer"
   className="star"
   onClick={() => setStarts(index + 1)}
/>
```

Which yields the following:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/testing-the-rating-component-1.gif)
_Testing the rating component_

To further improve the user feedback, we can convert the meaning of each star and display it to them.

Start by creating an array of labels and colours for the stars.

```js
 const ratingData = [
    { label: "Poor", color: "#E74C3C" },
    { label: "Bad", color: "#E59866" },
    { label: "Okay", color: "#F7DC6F" },
    { label: "Good", color: "#76D7C4" },
    { label: "Great", color: "#229954" },
  ];
```

Then apply this data to reflect whatever the current ratings are.

```js
export default function RatingComponent() {
  const [stars, setStarts] = useState(0);

  const ratingData = [
    { label: "Poor", color: "#E74C3C" },
    { label: "Bad", color: "#E59866" },
    { label: "Okay", color: "#F7DC6F" },
    { label: "Good", color: "#76D7C4" },
    { label: "Great", color: "#229954" },
  ];
  return (
    <div className="flex bg-white items-center justify-between  border border-black rounded-md min-w-[600px]  p-2">
      <div className="p-2 text-base font-semibold">
        Intersteller <span className="text-gray-400 ">(2014)</span>
      </div>
      <div className="flex gap-4 p-2">
        {Array.from({ length: 5 }).map((_, index) => (
          <div key={index} className="flex justify-center">
            <FiStar
              size={25}
              strokeWidth={0}
              fill={index + 1 <= stars ? "gold" : "#D6DBDF"}
              cursor="pointer"
              className="star"
              onClick={() => setStarts(index + 1)}
            />
          </div>
        ))}
      </div>
      {stars > 0 ? (
        <div
          className="font-semibold min-w-[60px] p-2"
          style={{ color: ratingData[stars - 1]?.color }}>
          {ratingData[stars - 1]?.label}
        </div>
      ) : (
        <p className="font-semibold text-gray-400">No ratings yet...</p>
      )}
    </div>
  );
}
```

Which gives this:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/testing-the-rating-component-with-label-cues.gif)
_Testing the rating component with label cues_

And ta-da! Your ratings component is fully functional and every user can effectively use it to drop an accurate review.

### Compound Component Method

For this method, we’ll take it a step further and create multiple rating components, because if we’re not doing the most, what are we doing? 😌

Start by creating the context for the component.

```js
const RatingContext = createContext();

const MultiRatingsComponent = ({
  children,
  ratingsData,

}) => {
  return (
    <RatingContext.Provider
      value={{
        ratingsData,
      }}>
      <div className="relative">{children}</div>
    </RatingContext.Provider>
  );
};
```

Since we’re going to be working with multiple sets of data to create numerous rating components, the structure of the data being passed in would differ.

```js
export default function App() {
  const multiRatings = [
    { name: "The Dark Knight", year: 2008, length: 5, rating: 0 },
    { name: "Knives Out", year: 2019, length: 5, rating: 0 },
    { name: "Serendipity", year: 2001, length: 5, rating: 0 },
    { name: "The Dressmaker", year: 2015, length: 5, rating: 0 },
    { name: "The Grand Budapest Hotel", year: 2015, length: 5, rating: 0 },
  ];
  const [ratings, setRatings] = useState(multiRatings);

  return (
    <main className="bg-[#EAF2F8] gap-4 min-h-[100vh] flex justify-center items-center flex-col">
      <Toaster />
      <h1 className="text-3xl">My Ratings Component</h1>
      <MultiRatingsComponent
        ratingsData={ratings}>
      </MultiRatingsComponent>
    </main>
  );
}
```

Next, flesh out the rest of the component required to make our UI look like the single component we created earlier.

```js
const MultiRatingsComponent = ({
  children,
  ratingsData,

}) => {
  const [userFeedback, setUserFeedback] = useState([]);
  return (
    <RatingContext.Provider
      value={{
        ratingsData,
      }}>
      <div className="relative ">{children}</div>
    </RatingContext.Provider>
  );
};

const Label = ({ name, year }) => {
  return (
    <div className="flex flex-col justify-center gap-1 text-base font-semibold min-w-[220px]">
      <h3>{name}</h3>
      <span className=" text-[12px]  text-[#AAB7B8]">{year}</span>
    </div>
  );
};

const RatingsContainer = () => {
  const { ratingsData, updateRating } = useContext(RatingContext);

  return (
    <div className="min-w-[600px] bg-white rounded-md flex flex-col">
      {ratingsData &&
        ratingsData.map((singleData, index) => (
          <div
            key={index}
            className="flex items-center px-4 py-6 border-[#f7f8f9] gap-[75px] border-[0.5px]">
            <Label name={singleData.name} year={singleData.year} />
            <div className="flex gap-4 ">
              {Array.from({ length: 5 }).map((_, starIndex) => (
                <RatingIcon
                  key={starIndex}
                  filled={starIndex < singleData.rating}
                />
              ))}
            </div>
          </div>
        ))}
    </div>
  );
};

const RatingIcon = ({ filled }) => {
  return (
    <FiStar
      size={25}
      strokeWidth={0}
      fill={filled ? "gold" : "#AAB7B8"}
      cursor="pointer"
      className="star"
    />
  );
};
```

Then assign each component to its parent to form the compound component.

```js
MultiRatingsComponent.Label = Label;
MultiRatingsComponent.RatingsContainer = RatingsContainer;
MultiRatingsComponent.RatingIcon = RatingIcon;
```

To see your component UI, nest the `RatingsContainer` inside its parent (the `App` component).

```js
export default function App() {
  const multiRatings = [
    { name: "The Dark Knight", year: 2008, length: 5, rating: 0 },
    { name: "Knives Out", year: 2019, length: 5, rating: 0 },
    { name: "Serendipity", year: 2001, length: 5, rating: 0 },
    { name: "The Dressmaker", year: 2015, length: 5, rating: 0 },
    { name: "The Grand Budapest Hotel", year: 2015, length: 5, rating: 0 },
  ];

  const [ratings, setRatings] = useState(multiRatings);

  return (
    <main className="bg-[#EAF2F8] gap-4 min-h-[100vh] flex justify-center items-center flex-col">
      <Toaster />
      <h1 className="text-3xl">My Ratings Component</h1>
      <MultiRatingsComponent
        ratingsData={ratings}>
        <MultiRatingsComponent.RatingsContainer />
      </MultiRatingsComponent>
    </main>
  );
}
```

With that, your UI should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/2-Ratings-UI-with-CC-pattern.png)
_Ratings UI with CC pattern_

To add our previous functionality where we could set ratings, as well as show their meaning via labels, start by creating an update function in the `App` component.

```js
  const updateRating = (index, newRating) => {
    setRatings((prevRatings) =>
      prevRatings.map((r, i) => (i === index ? { ...r, rating: newRating } : r))
    );
    console.log(ratings);
  };
```

This function uses the index of the clicked component to find the particular data, the modifies the rating property based on the star you click on.

To use it, pass it into the `MultiRatingsComponent` via props, then share it with all its children with its context.

```js
const MultiRatingsComponent = ({
  children,
  ratingsData,
  updateRating,
}) => {
  const [userFeedback, setUserFeedback] = useState([]);
  return (
    <RatingContext.Provider
      value={{
        ratingsData,
        updateRating,
      }}>
      <div className="relative ">{children}</div>
    </RatingContext.Provider>
  );
};
```

Then consume that context in `RatingsContainer`.

```js
const RatingsContainer = () => {
  const { ratingsData, updateRating } = useContext(RatingContext);

  return (
    <div className="min-w-[600px] bg-white rounded-md flex flex-col">
      {ratingsData &&
        ratingsData.map((singleData, index) => (
          <div
            key={index}
            className="flex items-center px-4 py-6 border-[#f7f8f9] gap-[75px] border-[0.5px]">
            <Label name={singleData.name} year={singleData.year} />
            <div className="flex gap-4 ">
              {Array.from({ length: 5 }).map((_, starIndex) => (
                <RatingIcon
                  key={starIndex}
                  filled={starIndex < singleData.rating}
                    onClick={() => updateRating(index, starIndex + 1)}
                />
              ))}
            </div>
          </div>
        ))}
    </div>
  );
};
```

Just before you check the UI, create a `RatingsLabel` component to show the meaning of each star right next to each star.

```js
const RatingLabel = ({ ratingValue }) => {
  const ratingLabel = [
    { label: "Poor", color: "#E74C3C" },
    { label: "Bad", color: "#E59866" },
    { label: "Okay", color: "#F7DC6F" },
    { label: "Good", color: "#76D7C4" },
    { label: "Great", color: "#229954" },
  ];
  return (
    <>
      {ratingValue > 0 ? (
        <div
          className="font-semibold min-w-[60px] p-2"
          style={{ color: ratingLabel[ratingValue - 1]?.color }}>
          {ratingLabel[ratingValue - 1]?.label}
        </div>
      ) : (
        <p className="font-semibold text-gray-400">No ratings yet...</p>
      )}
    </>
  );
};

MultiRatingsComponent.RatingLabel = RatingLabel;
```

And nest it in the `RatingsContainer`.

```js
const RatingsContainer = () => {
  const { ratingsData, updateRating } = useContext(RatingContext);

  return (
    <div className="min-w-[600px] bg-white rounded-md flex flex-col">
      {ratingsData &&
        ratingsData.map((singleData, index) => (
          <div
            key={index}
            className="flex items-center px-4 py-6 border-[#f7f8f9] gap-[75px] border-[0.5px]">
            <Label name={singleData.name} year={singleData.year} />
            <div className="flex gap-4 ">
              {Array.from({ length: 5 }).map((_, starIndex) => (
                <RatingIcon
                  key={starIndex}
                  filled={starIndex < singleData.rating}
                  onClick={() => updateRating(index, starIndex + 1)}
                />
              ))}
            </div>
            <RatingLabel ratingValue={singleData.rating} />
          </div>
        ))}
    </div>
  );
};
```

Drumroll, please…

![Image](https://www.freecodecamp.org/news/content/images/2024/06/testing-the-rating-component-with-CC-pattern-and-label-cues.gif)
_Testing the rating component with CC pattern and label cues_

With this implementation, you can easily have multiple rating bars, and managing each state would be a breeze.

## How to Upgrade the Rating Component

Alas, there’s one functionality we haven't implemented. No great rating component is complete without a form which allows users to express their opinions past a couple of stars.

To create a comment component, create a form and some state to manage that form.

```js
const Comment = () => {
  const [comment, setComment] = useState("");

  return (
    <div className="w-full mt-2 ">
      <label className="p-2 text-base font-semibold ">Comment</label>
      <form className="relative " onSubmit={(e)=> handleSubmit(e)}>
        <textarea
          name="comment"
          placeholder="Add a review"
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          className="w-full p-4 rounded-md resize-none min-h-20"></textarea>
        <button className="font-semibold absolute -bottom-1/2 right-0 border bg-[#5499C7] transition-all hover:bg-[#21618C] rounded-md py-2 px-4 text-white">
          Submit
        </button>
      </form>
    </div>
  );
};

MultiRatingsComponent.Comment = Comment;
```

Then create a handler function for that form.

```js
  const handleSubmit = (e) => {
    e.preventDefault();

    if (comment.length < 3) {
      toast.error("Please add more text");
      return;
    }

    // Clear the comment input
    setComment("");
  };
```

To see the comments after a user submits the form, create a state to hold those comments in the parent context.

```js
const MultiRatingsComponent = ({
  children,
  ratingsData,
  updateRating,

}) => {
  const [userFeedback, setUserFeedback] = useState([]);
  return (
    <RatingContext.Provider
      value={{
        ratingsData,
        updateRating,
        userFeedback,
        setUserFeedback,
        
      }}>
      <div className="relative ">{children}</div>
    </RatingContext.Provider>
  );
};
```

Then consume that context and store the submitted data in the parent context.

```js
 const { userFeedback, setUserFeedback,} =
    useContext(RatingContext);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (comment.length < 3) {
      toast.error("Please add more text");
      return;
    }

    // Create a new feedback object
    const newFeedback = { comment };

    // Update the userFeedback state
    setUserFeedback([...userFeedback, newFeedback]);

    // Clear the comment input
    setComment("");
  };
```

To view all the comments left by users, create a `UserFeedback` component like so:

```js
const UserFeedback = () => {
  const { userFeedback } = useContext(RatingContext);
  return (
    <div className="absolute top-0 px-8 py-2 translate-x-full bg-white rounded-md max-w-[300px] -right-5">
      {userFeedback.length > 0 ? (
        <>
          <h3 className="mb-2 text-xl font-semibold">
            Here are what user think
          </h3>
          <ul>
            {userFeedback.map((user, index) => (
              <li key={index} className="px-2 ">
                <h4>
                  {index + 1}.{" "}
                  <span className="font-semibold ">{user.name} </span> --{" "}
                  {user.text}
                </h4>
              </li>
            ))}
          </ul>
        </>
      ) : (
        <p className="font-semibold ext-xl">No user feedback yet...</p>
      )}
    </div>
  );
};
MultiRatingsComponent.UserFeedback = UserFeedback;
```

This component consumes the state holding the user comments and displays them on the screen.

Just before we test it out, I wanted to replicate a fun quirk I notice from Google whenever someone views your docs. They assign a random name to each user and so will we.

Head over to your `App` component and create this array:

```js
 const randomNames = [
    "Anonymous Llama",
    "Mysterious Moose",
    "Stealthy Sloth",
    "Phantom Panda",
    "Incognito Iguana",
    "Unknown Unicorn",
    "Enigmatic Elephant",
    "Ghostly Giraffe",
    "Shadowy Shark",
    "Cryptic Cobra",
    "Silent Swan",
    "Nameless Narwhal",
    "Obscure Octopus",
    "Unseen Uakari",
    "Hidden Hedgehog",
    "Masked Macaw",
    "Veiled Vulture",
    "Concealed Chameleon",
    "Covert Cockatoo",
    "Invisible Impala",
  ];
```

Then pass it into your `MultiRatingsComponent` via props.

```js
const MultiRatingsComponent = ({
  children,
  ratingsData,
  updateRating,
  randomNames,
}) => {
  const [userFeedback, setUserFeedback] = useState([]);
  return (
    <RatingContext.Provider
      value={{
        ratingsData,
        updateRating,
        userFeedback,
        setUserFeedback,
        randomNames,
      }}>
      <div className="relative ">{children}</div>
    </RatingContext.Provider>
  );
};
```

Finally, modify your form handler function to send a random name with the comment.

```js
const Comment = () => {
  const [comment, setComment] = useState("");
  const { userFeedback, setUserFeedback, randomNames } =
    useContext(RatingContext);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (comment.length < 3) {
      toast.error("Please add more text");
      return;
    }

    // Generate a random name between 1 and the length of the array
    const randomName =
      randomNames[Math.floor(Math.random() * randomNames.length)];

    // Create a new feedback object
    const newFeedback = { name: randomName, comment };

    // Update the userFeedback state
    setUserFeedback([...userFeedback, newFeedback]);

    // Clear the comment input
    setComment("");
  };
```

Finally, render the `Comment` and `UserFeedback` components in their parent inside the `App` component.

```js
export default function App() {
  const multiRatings = [
    { name: "The Dark Knight", year: 2008, length: 5, rating: 0 },
    { name: "Knives Out", year: 2019, length: 5, rating: 0 },
    { name: "Serendipity", year: 2001, length: 5, rating: 0 },
    { name: "The Dressmaker", year: 2015, length: 5, rating: 0 },
    { name: "The Grand Budapest Hotel", year: 2015, length: 5, rating: 0 },
  ];

  const randomNames = [...];

  const [ratings, setRatings] = useState(multiRatings);

  const updateRating = (index, newRating) => {
    setRatings((prevRatings) =>
      prevRatings.map((r, i) => (i === index ? { ...r, rating: newRating } : r))
    );
  };
  return (
    <main className="bg-[#EAF2F8] gap-4 min-h-[100vh] flex justify-center items-center flex-col">
      <Toaster />
      <h1 className="text-3xl">My Ratings Component</h1>
      <MultiRatingsComponent
        ratingsData={ratings}
        updateRating={updateRating}
        randomNames={randomNames}>
        <MultiRatingsComponent.RatingsContainer />
        <MultiRatingsComponent.Comment />
        <MultiRatingsComponent.UserFeedback />
      </MultiRatingsComponent>
    </main>
  );
}
```

And…Presto!

![Image](https://www.freecodecamp.org/news/content/images/2024/06/testing-the-rating-component-with-CC-pattern--label-cues-and-comments.gif)
_Testing the rating component with CC pattern, label cues and comments_

Your rating component is completed, with the added functionality of comments. ⭐  
How would you rate the ride throughout this build? 5 stars? 😉

### Additional Information

Here are links to all the resources you may need from this article.

* [Starter files](https://github.com/Daiveedjay/Rating-Component)
* [Regular React Pattern](https://github.com/Daiveedjay/Rating-Component/tree/Single-Rating-Component)
* [Compound Component Pattern](https://github.com/Daiveedjay/Rating-Component/tree/Compound-Component-Rating)

### And just for fun...

Since we built a rating component centered around movies, here are 5 movies I consider to be worth 5 stars in no particular order.

* [The Grand Budapest Hotel](https://www.google.com/search?q=The+Grand+Budapest+Hotel&oq=The+Grand+Budapest+Hotel&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiPAjIHCAIQABiPAjIGCAMQRRhA0gEHMzUyajBqN6gCALACAA&sourceid=chrome&ie=UTF-8) (Comedy/Crime)
* [The Magnificent Seven](https://www.google.com/search?gs_ssp=eJzj4tVP1zc0TDLPNi5JKzE2YPSSKslIVchNTM_LTMtMTs0rUShOLUvNUzAyMDQDACXhDZw&q=the+magnificent+seven+2016&oq=the+magnifi&gs_lcrp=EgZjaHJvbWUqDAgCEC4YQxiABBiKBTIGCAAQRRg5MgoIARAuGNQCGIAEMgwIAhAuGEMYgAQYigUyBwgDEAAYgAQyBwgEEC4YgAQyCggFEC4Y1AIYgAQyCggGEC4Y1AIYgAQyBwgHEAAYgAQyBwgIEC4YgAQyBwgJEAAYjwLSAQg0NjQxajBqN6gCALACAA&sourceid=chrome&ie=UTF-8) (Western/Action)
* [Django Unchained](https://www.google.com/search?q=django+unchained&sca_esv=616ade3b683ed7c0&sxsrf=ADLYWIK4xUiB8xs1iwXWvE9LfHZsNyCFsg%3A1717326804304&ei=1FNcZqaeEtqyhbIPzYCtwQU&gs_ssp=eJzj4tLP1TdIL88qN0g2YPQSSMlKzEvPVyjNS85IzMxLTQEAlJcKLw&oq=django&gs_lp=Egxnd3Mtd2l6LXNlcnAiBmRqYW5nbyoCCAAyDRAuGIAEGLEDGEMYigUyChAAGIAEGEMYigUyChAuGIAEGEMYigUyDRAAGIAEGLEDGEMYigUyChAAGIAEGEMYigUyChAuGIAEGEMYigUyChAAGIAEGEMYigUyChAAGIAEGBQYhwIyBRAAGIAEMgUQABiABDIoEC4YgAQYsQMYQxiKBRiXBRjcBBjeBBjgBBj0AxjxAxj1Axj2A9gBA0jCHlDHBFiUEXACeAGQAQCYAZgCoAH0C6oBAzItNrgBAcgBAPgBAZgCCKACtwyoAhHCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICDhAAGLADGOQCGNYE2AEBwgITEC4YgAQYsAMYQxjIAxiKBdgBAsICBxAjGCcY6gLCAhYQLhiABBhDGLQCGMgDGIoFGOoC2AECwgIKECMYgAQYJxiKBcICBBAjGCfCAhAQLhiABBixAxhDGIMBGIoFwgIIEAAYgAQYsQPCAgQQABgDwgILEAAYgAQYsQMYgwHCAiUQLhiABBhDGIoFGJcFGNwEGN4EGOAEGPQDGPEDGPUDGPYD2AEDwgIFEC4YgATCAigQLhiABBixAxhDGIoFGJcFGNwEGN4EGOAEGPQDGPEDGPUDGPYD2AEDmAMJiAYBkAYTugYGCAEQARgJugYGCAIQARgIugYGCAMQARgUkgcFMi4wLjagB72FAQ&sclient=gws-wiz-serp) (Western/Action)
* [Ford vs Ferrari](https://www.google.com/search?q=ford+vs+ferrari&sca_esv=616ade3b683ed7c0&sxsrf=ADLYWIL6hL7o3cnMX0eikkhJDvlhvLACHg%3A1717327001772&ei=mVRcZpjqLr6whbIP-eS7kAw&gs_ssp=eJzj4tVP1zc0TDOrNC5IK6o0YPTiT8svSlEoK1ZISy0qSizKBACjAwqR&oq=ford+vs+fer&gs_lp=Egxnd3Mtd2l6LXNlcnAiC2ZvcmQgdnMgZmVyKgIIADINEC4YgAQYsQMYQxiKBTIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIoEC4YgAQYsQMYQxiKBRiXBRjcBBjeBBjgBBj0AxjxAxj1Axj2A9gBA0jnMFCGA1jZJHAEeAGQAQCYAY8CoAHRF6oBBjAuMi4xMbgBAcgBAPgBAZgCEqACuiSoAhLCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICDhAAGLADGOQCGNYE2AEBwgITEC4YgAQYsAMYQxjIAxiKBdgBAsICBxAjGCcY6gLCAhYQLhiABBhDGLQCGMgDGIoFGOoC2AECwgIZEC4YgAQYQxjUAhi0AhjIAxiKBRjqAtgBAsICChAjGIAEGCcYigXCAgQQIxgnwgIKEC4YgAQYQxiKBcICERAuGIAEGLEDGNEDGIMBGMcBwgIIEAAYgAQYsQPCAgsQABiABBixAxiDAcICChAAGIAEGEMYigXCAhAQABiABBixAxhDGIMBGIoFwgIrEC4YgAQYsQMYQxiKBRiXBRjcBBjeBBjgBBj0AxjxAxj1Axj2Axj3A9gBA8ICDRAAGIAEGLEDGEMYigXCAhAQABiABBixAxhDGMkDGIoFwgILEAAYgAQYkgMYigXCAgoQABiABBgUGIcCmAMKiAYBkAYTugYGCAEQARgJugYGCAIQARgIugYGCAMQARgUkgcKNC4wLjEzLjctMaAH3qsB&sclient=gws-wiz-serp) (Sports/Action)
* [Inception](https://www.imdb.com/title/tt1375666/) (Action/Sci-fi)

## Conclusion

In conclusion, crafting a movie-themed rating component using the Compound Component pattern in React is a surefire blockbuster for your projects. This approach enables you to create a sleek, modular, and maintainable codebase. 

Mastering this technique ensures your rating system is both functional and ready for the future. Lights, camera, action – may your coding journey dazzle with five-star reviews and standing ovations!

### Like my articles?

Feel free to [buy me a coffee here](https://www.buymeacoffee.com/JajaDavid), to keep my brain chugging and provide more articles like this.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/coffee-tom.gif)
_Coffee Tom_

### Contact Information

Want to connect or contact me? Feel free to hit me up on the following:

* Twitter / X: [@jajadavid8](https://twitter.com/JajaDavid8)
* LinkedIn: [David Jaja](https://www.linkedin.com/in/david-jaja-8084251b4/)
* Email: Jajadavidjid@gmail.com

  

