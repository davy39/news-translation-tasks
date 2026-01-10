---
title: Learn React by Building a Mortgage Calculator
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2023-03-27T22:56:14.000Z'
originalURL: https://freecodecamp.org/news/react-mortgage-calculator-tutorial-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/thumbnail_EN--2-.png
tags:
- name: beginner
  slug: beginner
- name: React
  slug: react
seo_title: null
seo_desc: 'Today we will learn and practice ReactJs by building a mortgage calculator
  step by step. This is the project that we will build today 👇



  Heres a live demo of the project

  And here''s the Github Repo Link


  Objectives

  The topics we''ll cover while build...'
---

Today we will learn and practice ReactJs by building a mortgage calculator step by step. This is the project that we will build today 👇

![Project Image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ryoc8jihbyprgp50ulhm.png)

* [Heres a live demo of the project](https://mortgage-calculator-tutorial.vercel.app/)
* [And here's the Github Repo Link](https://github.com/JoyShaheb/mortgage-calculator-tutorial)

## Objectives

The topics we'll cover while building this project are:
* React Functional Components
* Material UI
* User Inputs
* Handling Props
* props destructuring
* useState Hook

And much more! This course is excellent for beginners who want to learn ReactJs by building a real world project.

## You can watch this tutorial on YouTube as well if you like:

%[https://youtu.be/uluphP4xXD8]


## Table of Contents

- [Project Setup](#project-setup)
- [Folder Structure](#folder-structure)
- [Material UI Theme](#material-ui-theme)
- [How to Build the Navbar](#how-to-build-the-navbar)
- [Material UI Grid System](#material-ui-grid-system)
- [How to Build the Slider Component](#how-to-build-the-slider-component)
- [Take a Break](#take-a-break)
- [How to Use the useState Hook](#how-to-use-the-usestate-hook)
- [How to Build the SliderSelect component](#how-to-build-the-sliderselect-component)
- [How to Build the TenureSelect component](#how-to-build-the-tenureselect-component)
- [How to Build the Result Component](#how-to-build-the-result-component)
- [Conclusion](#heading-conclusion)
- [My Social Media Links](#my-social-media-links)

## Project Setup

![Project Setup](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/02wjpjpo4k6tjg78ynu4.png)

In order to setup the project we need to install `react`, `material-ui`, and other necessary packages. 

First create a folder named `mortgage-calculator`, open it on VS Code, and then run the following command in the terminal:

```bash
npx create-react-app .
npm install @mui/material @emotion/react @emotion/styled
npm install --save chart.js react-chartjs-2
```

### App.js

We will remove all the boilerplate code from `app.js` and keep up to this portion 👇

```js
import React from "react";

function App() {
  return <div className="App">Hello everyone</div>;
}

export default App;
```

Then run this command in the terminal to start the server:

```bash
npm start
```

The project should look totally blank on the web browser now.

### Let's start coding

![Lets start coding](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qew6q8zwn723s86md4rf.png)

Everything is setup and ready to go. Now we will start building the project :)

## Folder Structure

![Folder Structure](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7hujbmnjhri7470r2rxk.png)

Our folder structure should look like this so that we can easily manage and maintain our files & folders:

```bash
mortgage-calculator/
├── src/
│   ├── Components/
│   │   ├── Common/
│   │   │   └── SliderComponent.js
│   │   ├── Navbar.js
│   │   ├── Result.js
│   │   ├── SliderSelect.js
│   │   ├── TenureSelect.js
│   ├── theme.js
│   ├── App.js
│   ├── index.js
├── .gitignore
├── package.json
└── package-lock.json
```

Here's an image of our project folder structure if you're feeling confused:

![Folder Structure](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9q9ezw36rp0mcfo12qsw.png)

## Material UI Theme

![MUI Theme](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mxoseeckq7zgnidn4yol.png)

We will be using the dark theme of Material UI. For that we need to create a file named `theme.js` in the `src` folder and add the following code:

### theme.js

```js
import { createTheme } from '@mui/material/styles';

export const theme = createTheme({
  palette: {
    mode: 'dark',
  },
})
```

### index.js

Next up, we need to import the `theme` in the `index.js` file and wrap the app with the `ThemeProvider`. Follow along below: 👇

```js
import { ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import { theme } from "./theme";

<React.StrictMode>
  <ThemeProvider theme={theme}>
    <App />
    <CssBaseline />
  </ThemeProvider>
</React.StrictMode>
```

**Note:** If you don't pass the `CssBaseline` component we will not be able to see the MUI dark theme.

This is the result so far: 👇

![Result so far](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/j117t2x35qebkx3qf21r.png)

The entire screen will be dark. This means that dark mode has been applied to our project from Material UI.

## How to Build the Navbar

![Navbar Setup](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tx7urj6lh5710anwtqa8.png)

Next up, we will be creating a very simple Navbar to show the Logo. For that we need to create a file named `Navbar.js` in the `src/Components` folder and add the following code:

### Navbar.js

```js
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import { Container } from "@mui/system";

const Navbar = () => {
  return (
    <AppBar position="static">
      <Container maxWidth='xl'>
        <Toolbar>
          <Typography variant="h5">
            Bank of React
          </Typography>
        </Toolbar>
      </Container>
    </AppBar>
  );
};

export default Navbar;
```

Here's a quick explanation of the components used from Material UI:

- **AppBar :** The Appbar component of Material UI is used for creating a top navigation bar in the user interface. [Read more about it here](https://mui.com/material-ui/react-app-bar/)
- **Container :** The Container component of Material UI is used for creating a container element that can be used to create a responsive layout, and center and contain other elements in a user interface. [Read more about it here](https://mui.com/material-ui/react-container/)
- **ToolBar :** The Toolbar component can contain elements such as buttons, text, and icons, and can also be used for creating a responsive layout that adapts to different screen sizes. [Read more about it here](https://mui.com/material-ui/api/toolbar/)
- **Typography :** Material UI's typography component is used for applying pre-defined typographic styles to text elements. It helps create a consistent and visually pleasing layout with customizable font family, size, weight and spacing. [Read more about it here](https://mui.com/material-ui/react-typography/)

### App.js

Finally, import it to `App.js` and write the code like this: 👇

```js
import React from "react";
import Navbar from "./Components/Navbar";

function App() {
  return (
    <div className="App">
      <Navbar />
    </div>
  );
}

export default App;
```

This is the result so far: 👇

![Navbar result](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lv52resgdtg2wpgqq4xa.png)

## Material UI Grid System

![MUI Grid System](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bd60xyrgs28g75eulshc.png)

In the finalized project, we can see that our content is divided into 2 portions. On the left we have the slider components and on the right we have the pie chart. This is made possible using the [Grid system of material UI](https://mui.com/material-ui/react-grid/).

![Finalized project image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ezdk2jrt1dg88wac6iyu.png)

Not only that, we can also see that the content is responsive on smaller screen sizes. This is also made possible using the Grid system of material UI.

![Responsive content](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5a1e5356nbnr74y6r6ze.png)

To replicate this, we need to write these things on our App.js file. You can follow along here. 👇

First of all, we need to import all of our required components from Material UI and our components folder:

```js
import React, { useState } from "react";
import { Grid } from "@mui/material";
import { Container } from "@mui/system";
import Navbar from "./Components/Navbar";
import Result from "./Components/Result";
import SliderSelect from "./Components/SliderSelect";
import TenureSelect from "./Components/TenureSelect";
```

Next up, we write this code inside the `return` statement like this: 👇

```js
<div className="App">
  <Navbar />
  <Container maxWidth="xl" sx={{marginTop:4}}>
    <Grid container spacing={5} alignItems="center">
      <Grid item xs={12} md={6}>
        <SliderSelect />
        <TenureSelect />
      </Grid>
      <Grid item xs={12} md={6}>
        <Result/>
      </Grid>
    </Grid>
  </Container>
</div>
```

Explanation of the code:

- **Container:** On the `Container` we wrote something called `sx={{marginTop:4}}`. This is the way to add inline-style to a component in Material UI.
- **Grid:** The Grid component is used to create a responsive layout that adapts to different screen sizes. `Grid container` represents the parent element and `Grid item` represents the child element.
- On the `Grid` component we wrote something called `spacing={5}`. This is the way to add spacing between the grid items.
- On the `Grid` component we also wrote `xs={12}` which means that the grid item will take up the entire width of the screen on extra small screens. Similarly, `md={6}` means that the grid item will take up half of the screen on medium and bigger screens. That's how we made our components responsive.

This is the result so far: 👇

![Result image of Grid system](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jr80ud2oawv7nj6xti75.png)

## How to Build the Slider Component

![Slider Component](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1psq4l7lbwl1c2aizo6j.png)

Next up, we will be creating a slider component to get the input amount from the user. It will look something like this: 👇

![Slider Component](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/oth4rtfgebeylr1kjktn.png)

For that we need to create a file named `SliderComponent.js` in the `src/Components/Common` folder. First let's list out all the props we need to pass to our re-usable slider component:

- **label**
- **min**
- **max**
- **defaultValue**
- **unit**
- **value**
- **steps**
- **amount**
- **onChange**

### SliderComponent.js

Let's get going. First of all, import the following components from MUI inside the `SliderComponent.js` file:

```js
import React from "react";
import Slider from "@mui/material/Slider";
import { Typography } from "@mui/material";
import { Stack } from "@mui/system";
```

We will be using the [Stack component from MUI](https://mui.com/material-ui/react-stack/) to stack the components vertically. `my` is the shorthand for `marginY` [margin-top & margin-bottom]. We will be using the `Typography` component from MUI to display the label, unit, and other data. We will be using the `Slider` component from MUI to display the slider.

Write this small amount of code first, with our props destructured:

```js
const SliderComponent = ({
  defaultValue,
  min,
  max,
  label,
  unit,
  onChange,
  amount,
  value,
  steps
}) => {
  return (
    <Stack my={1.4}>

    </Stack>
  )
}

export default SliderComponent
```

We will write this code to display the label, unit, and amount.

```jsx
<Stack gap={1}>
  <Typography variant="subtitle2">{label}</Typography>
  <Typography variant="h5">
    {unit} {amount}
  </Typography>
</Stack>
```

We will write this code to display the slider. We will be passing the props to the slider component like this: 👇

```jsx
<Slider
  min={min}
  max={max}
  defaultValue={defaultValue}
  aria-label="Default"
  valueLabelDisplay="auto"
  onChange={onChange}
  value={value}
  marks
  step={steps}
/>
```

We will write this code to display the min and max values of the slider. We will be using the `Stack` component from MUI to stack the components horizontally. `direction="row"` is the shorthand for `flex-direction: row`. `justifyContent="space-between"` is the shorthand for `justify-content: space-between`.

```js
<Stack direction="row" justifyContent="space-between">
  <Typography variant="caption" color="text.secondary">
    {unit} {min}
  </Typography>
  <Typography variant="caption" color="text.secondary">
    {unit} {max}
  </Typography>
</Stack>
```

Good Job so far!

## Take a break

![Take a break](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/k9s9yorz1gwt380tbr7t.png)

Take a break – you deserve it! 🎉

## How to Use the useState Hook

![useState Hook](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/89cx3gxzdl5h7q0okf8f.png)

We need to use the useState hook from React in our project. But before that, we need to understand what this hook is and why we need to use it.

The useState hook is a built-in React function that allows you to add state to functional components. It returns an `array` containing two elements: the current state value and a function to update that value. The general syntax of the useState hook is as follows:

```js
const [state, setState] = useState(initialState);
```

Here's what's going on: 👇

- `state`: The name of the constant or variable that will store the state.
- `setState`: A function to update the state.
- `initialState`: The initial value of the state.

### Example of the useState hook

We will create a toggle button that changes its text between "ON" and "OFF" when clicked.

```js
import React, { useState } from 'react';

const ToggleButton = () => {
  const [isOn, setIsOn] = useState(false);

  const toggle = () => setIsOn(!isOn)

  return (
      <button onClick={toggle}>{isOn ? 'ON' : 'OFF'}</button>
  );
};

export default ToggleButton;

```

Here, we initialize the `isOn` state with an initial value of `false`. The `toggle` function updates the `isOn` state to its opposite value when the user clicks the button. We use a `ternary operator` to render the text inside the button based on the current value of `isOn`.

### App.js

Now lets come back to our project. First, come over to the `App.js` file and import the `useState` hook from React.

```js
import React, { useState } from 'react';
```

Next up, we will declare a state to store the value of the sliders using the `useState` hook. We will be passing the initial value of the state as `{}` inside the `useState` hook, because we are storing our data as an object.

```js
function App() {
  const [data, setData] = useState({})

  // other codes are here
}
```

We're using the useState hook to create a new state variable called `data` and a function called `setData` that we can use to update the state.

Next up, we will pass these values as default values for our slider component.

```js
function App() {
  const [data, setData] = useState({
    homeValue: 3000,
    downPayment: 3000 * 0.2,
    loanAmount: 3000 * 0.8,
    loanTerm: 5,
    interestRate: 5,
  })

  // other codes are here
}
```

Then, we will be passing the `data` and `setData` state as a prop to the `SliderSelect` component like this: 👇

```js
<div className="App">
  <Navbar />
  <Container maxWidth="xl" sx={{marginTop:4}}>
    <Grid container spacing={5} alignItems="center">
      <Grid item xs={12} md={6}>

        {/* this is where we write the code  👇 */}
        <SliderSelect data={data} setData={setData}/>

        <TenureSelect />
      </Grid>
      <Grid item xs={12} md={6}>
        <Result/>
      </Grid>
    </Grid>
  </Container>
</div>
```

## How to Build the SliderSelect Component

![SliderSelect.js component](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/001ovrcapajjl5i480dn.png)

So now that we have our re-usable `SliderComponent` ready, let's use it in our `SliderSelect.js` component. First of all, import the `SliderComponent` component from the `Common` folder.

### SliderSelect.js

```js
import SliderComponent from "./Common/SliderComponent";
```

Next up, we will destructure our props that we are receiveing from `App.js`. And also, we'll create a variable called `bank_limit` and assign it a value of `10000`. This represents the maximum amount of money a person can borrow from our bank.

```js
import React from "react";
import SliderComponent from "./Common/SliderComponent";

const SliderSelect = ({ data, setData }) => {
  const bank_limit = 10000;
  return (
    <div>
      
    </div>
  );
};

export default SliderSelect;

```

Next up, we will use our `SliderComponent` to display the slider named `Home Value`. Here we will pass the props like this to the `SliderComponent` component.

```js
const SliderSelect = ({ data, setData }) => {
  const bank_limit = 10000;
  return (
    <div>
      <SliderComponent
        onChange={(e, value) => {
          setData({
            ...data,
            homeValue: value.toFixed(0),
            downPayment: (0.2 * value).toFixed(0),
            loanAmount: (0.8 * value).toFixed(0),
          });
        }}
        defaultValue={data.homeValue}
        min={1000}
        max={bank_limit}
        steps={100}
        unit="$"
        amount={data.homeValue}
        label="Home Value"
        value={data.homeValue}
      />
    </div>
  );
};

```

Here's the result so far: 👇

![Home Value Slider](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tc8ymi79urkugw7kd4ci.png)

In the same way, we will create the sliders for `Down Payment` and `Loan Amount` like this: 👇

```js
  return (
    <div>
      {/* other codes are here */}

      <SliderComponent
        onChange={(e, value) =>
          setData({
            ...data,
            downPayment: value.toFixed(0),
            loanAmount: (data.homeValue - value).toFixed(0),
          })
        }
        defaultValue={data.downPayment}
        min={0}
        max={data.homeValue}
        steps={100}
        unit="$"
        amount={data.downPayment}
        label="Down Payment"
        value={data.downPayment}
      />

      <SliderComponent
        onChange={(e, value) =>
          setData({
            ...data,
            loanAmount: value.toFixed(0),
            downPayment: (data.homeValue - value).toFixed(0),
          })
        }
        defaultValue={data.loanAmount}
        min={0}
        max={data.homeValue}
        steps={100}
        unit="$"
        amount={data.loanAmount}
        label="Loan Amount"
        value={data.loanAmount}
      />
    </div>
  );
```

Again, here's the result so far: 👇

![the result so far](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nvhfgzpf1aq02p3kwdqz.png)

Finally we will create the slider for our `Interest Rate`. You can follow along here: 👇

```js
return (
    <div>
      {/* other codes are here */}

      <SliderComponent
        onChange={(e, value) =>
          setData({
            ...data,
            interestRate: value,
          })
        }
        defaultValue={data.interestRate}
        min={2}
        max={18}
        steps={0.5}
        unit="%"
        amount={data.interestRate}
        label="Interest Rate"
        value={data.interestRate}
      />
    </div>
  );
```

Here's the result so far: 👇

![Interest Rate slider](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/snlpyvu2qfqzt81ecbvo.png)

## How to Build the TenureSelect Component

Next up, we will build the `TenureSelect` component. This component will be used to select the tenure of the loan. It will look like this: 👇

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/70arqood9dwqj9j46apk.png)

### App.js

First of all, pass the `data` and `setData` state as a prop to the `TenureSelect` component like this: 👇

```js
return (
  <div className="App">
    <Navbar />
    <Container maxWidth="xl" sx={{marginTop:4}}>
      <Grid container spacing={5} alignItems="center">
        <Grid item xs={12} md={6}>
          <SliderSelect data={data} setData={setData} />

          {/* this is where we write the code  👇 */}
          <TenureSelect data={data} setData={setData}/>

        </Grid>
        <Grid item xs={12} md={6}>
          <Result data={data}/>
        </Grid>
      </Grid>
    </Container>
  </div>
);
```

### TenureSelect.js

Then, import these required components from the `MUI` library:

```js
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
```

Then destructure the props that we are receiving from `App.js`. Also create a function named `handleChange` that will be used to set the `tenure` state, like this: 👇

```js
const TenureSelect = ({ data, setData }) => {

  const handleChange = (event) => {
    setData({...data, loanTerm: event.target.value});
  };

  return ()
};

export default TenureSelect;
```

Next up, we will build the `TenureSelect` component. It will look like this: 👇

```js
return (
  <FormControl fullWidth>
    <InputLabel id="demo-simple-select-label">Tenure</InputLabel>
    <Select
      labelId="demo-simple-select-label"
      id="demo-simple-select"
      value={data.loanTerm}
      label="Tenure"
      defaultValue={5}
      onChange={handleChange}
    >
      <MenuItem value={5}>5 years</MenuItem>
      <MenuItem value={10}>10 years</MenuItem>
      <MenuItem value={15}>15 years</MenuItem>
      <MenuItem value={20}>20 years</MenuItem>
      <MenuItem value={25}>25 years</MenuItem>
    </Select>
  </FormControl>
);
```

The result so far: 👇

![The result so far](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fl0fsfk2lv9dnh588eyh.png)

## How to Build the Result Component

Finally we will build the `Result` component. This component will be used to display the loan installment per month and the pie chart. It will look like this: 👇

![Result component](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7f5vgfcsk6aj6yseqvi1.png)

### App.js

First of all, pass the `data` state as a prop to the `Result` component like this: 👇

```js
return (
  <div className="App">
    <Navbar />
    <Container maxWidth="xl" sx={{marginTop:4}}>
      <Grid container spacing={5} alignItems="center">
        <Grid item xs={12} md={6}>
          <SliderSelect data={data} setData={setData} />
          <TenureSelect data={data} setData={setData}/>
        </Grid>
        <Grid item xs={12} md={6}>

          {/* this is where we write the code  👇 */}
          <Result data={data}/>
          
        </Grid>
      </Grid>
    </Container>
  </div>
);
```

### Result.js

Next up, import the required components like this: 👇

```js
import React from "react";
import { Stack, Typography } from "@mui/material";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Pie } from "react-chartjs-2";

ChartJS.register(ArcElement, Tooltip, Legend);
```

Then destruct the `data` state that we are receiving from `App.js` like this: 👇

```js
const Result = ({ data }) => {
  const { homeValue, loanAmount, loanTerm, interestRate } = data;
  return ();
};

export default Result;
```

Next up we will write all of these things that will help us do the calculation: 👇

```js
  const totalLoanMonths = loanTerm * 12;
  const interestPerMonth = interestRate / 100 / 12;
  const monthlyPayment =
    (loanAmount *
      interestPerMonth *
      (1 + interestPerMonth) ** totalLoanMonths) /
    ((1 + interestPerMonth) ** totalLoanMonths - 1);

  const totalInterestGenerated = monthlyPayment * totalLoanMonths - loanAmount;
```

Then we need this variable to store all the data for our pie chart, like this: 👇

```js
const pieChartData = {
  labels: ["Principle", "Interest"],
  datasets: [
    {
      label: "Ratio of Principle and Interest",
      data: [homeValue, totalInterestGenerated],
      backgroundColor: ["rgba(255, 99, 132, 0.2)", "rgba(54, 162, 235, 0.2)"],
      borderColor: ["rgba(255, 99, 132, 1)", "rgba(54, 162, 235, 1)"],
      borderWidth: 1,
    },
  ],
};
```

Finally, we will build the `Result` component. It will look like this: 👇

```js
return (
  <Stack gap={3}>
    <Typography textAlign="center" variant="h5">
      Monthly Payment: $ {monthlyPayment.toFixed(2)}
    </Typography>
    <Stack direction="row" justifyContent="center">
      <div>
        <Pie data={pieChartData} />
      </div>
    </Stack>
  </Stack>
);
```

Here's the final result: 👇

![The result so far](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gqs2st1o5fhlpoqnpqol.png)

## Conclusion

![Congratulations](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/z7w7p11dm81ggzxd6a1t.png)

Congratulations for reading until the end! Now you can confidently and efficiently use React JS and Material UI to build cool projects.

You have also learned how to use React's useState hook and how to handle props. I hope you enjoyed this tutorial.

## Mentorship Program

If you are interested in learning more about React JS and web development, I am offering a mentorship program. You can check out the details here 👉 [Mentor Labs Academy](https://www.mentorlabs.academy/)

![Mentorship Program](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/v5oyscu7l16tr636ekqj.png)

## My Social Media Links

- [LinkedIn/ JoyShaheb](https://www.linkedin.com/in/joyshaheb/)
- [YouTube / JoyShaheb](https://www.youtube.com/c/joyshaheb)
- [Twitter / JoyShaheb](https://twitter.com/JoyShaheb)
- [Instagram / JoyShaheb](https://www.instagram.com/joyshaheb/)



