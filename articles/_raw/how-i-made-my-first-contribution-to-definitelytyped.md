---
title: How I Made My First Contribution to DefinitelyTyped, an Open Source TypeScript
  Repo
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-02T17:37:07.000Z'
originalURL: https://freecodecamp.org/news/how-i-made-my-first-contribution-to-definitelytyped
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/definitelytyped.png
tags:
- name: open source
  slug: open-source
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: "By Iva Kop\nTypeScript is awesome. It instantly makes our code safer, easier\
  \ to debug, and better documented. \nFor some time now, I have been using TypeScript\
  \ exclusively in all my projects. And here is the thing – I had never come across\
  \ a package th..."
---

By Iva Kop

TypeScript is awesome. It instantly makes our code safer, easier to debug, and better documented. 

For some time now, I have been using TypeScript exclusively in all my projects. And here is the thing – I had never come across a package that was missing type definitions. Until now...

I admit to being a bit spoiled in this respect. But I was surprised to discover that a small but useful [Gatsby](https://www.gatsbyjs.com/) plugin we were using – [gatsby-plugin-breakpoints](https://www.gatsbyjs.com/plugins/gatsby-plugin-breakpoints/) – did not yet have type definitions. It got me thinking.

# How I Solved the Problem

My initial reaction was to remove the plugin from the project altogether. It provided a simple functionality that I could easily replicate myself. And as a general rule, the less external dependencies we have, the better, right?

But the plugin was already used pretty extensively across the project. So if I wanted to avoid refactoring, I had to replicate its API exactly. This would mean I had to rewrite the already existing (and working) code just for the sake of removing a dependency. This did not seem like a good approach.

Instead, I decided to just add the necessary types to my project. This was simple enough. Before I knew it, it was all done and good to go.

But then I realized something. This was the first time I had to do this for any of the dozens of libraries and plugins I use on a daily basis in my React projects. It presented a unique opportunity for me to jump in and make a tiny contribution to the community that had spoiled me so much in the first place.

So I did. 

# How to Contribute to DefinitelyTyped

[DefinitelyTyped](https://definitelytyped.org/) is a community-led open-source repository for TypeScript type definitions. It's the go-to place for the kind of contribution I was looking to make. 

Although what I describe below is a bit React-centric, I hope it can still serve as a more general guide. 

## Getting Setup to Contribute

Getting started is simple. The first step is to fork the [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped) repo and generate the scaffolding using the following:

```
npx dts-gen --dt --name gatsby-plugin-breakpoints --template module

```

This will create a folder in the DefinitelyTyped project with 4 files:

```
gatsby-plugin-breakpoints-test.ts
index.d.ts
tsconfig.json
tslint.json
```

All of our type definitions will live in `index.d.ts` and the `gatsby-plugin-breakpoints-test.ts` will help us make sure everything works as expected.

Before we start, since we are working with React, a small adjustment is needed in the `tsconfig.json`. We should add `"jsx": "react"` to the compilerOptions and change the test file name to `gatsby-plugin-breakpoints-tests.tsx`. Let's also not forget to rename the actual tests file.

The final `tsconfig.json` should look something like this:

```
{
    "compilerOptions": {
        "module": "commonjs",
        "lib": [
            "es6",
            "DOM"
        ],
        "noImplicitAny": true,
        "noImplicitThis": true,
        "strictFunctionTypes": true,
        "strictNullChecks": true,
        "baseUrl": "../",
        "typeRoots": [
            "../"
        ],
        "types": [],
        "noEmit": true,
        "forceConsistentCasingInFileNames": true,
        "jsx": "react",
        "esModuleInterop": true
    },
    "files": [
        "index.d.ts",
        "gatsby-plugin-breakpoints-tests.tsx"
    ]
}

```

So far so good!

## How to Create the Types and Test Them

By taking a look at the `gatsby-plugin-breakpoints` [docs](https://www.gatsbyjs.com/plugins/gatsby-plugin-breakpoints/) and source code, we can identify the types we need to create. Let's make a quick list:

* Plugin config
* useBreakpoint React hook
* withBreakpoints React HOC (higher order component)
* BreakpointProvider
* BreakpointContext

### Plugin config

Let's tackle the config first.

```
// index.d.ts

// Type definitions for gatsby-plugin-breakpoints 1.3
// Project: https://github.com/JimmyBeldone/gatsby-plugin-breakpoints
// Definitions by: Iva Kop <https://github.com/IvaKop>
// Definitions: https://github.com/DefinitelyTyped/DefinitelyTyped

/**
 * @see https://www.gatsbyjs.com/plugins/gatsby-plugin-breakpoints/
 */


export type QueriesObject = Record<string, string>;

export interface BreakpointOptions {
    queries?: QueriesObject;
}

export interface BreakpointConfig {
    resolve: 'gatsby-plugin-breakpoints';
    options?: BreakpointOptions;
}
```

Cool! Now let's go to the test file and make sure we have done everything correctly:

```
// gatsby-plugin-breakpoints-tests.tsx

import React from 'react';
import {
    BreakpointConfig,
} from 'gatsby-plugin-breakpoints';

const defaultQueries = {
    xs: '(max-width: 320px)',
    sm: '(max-width: 720px)',
    md: '(max-width: 1024px)',
    l: '(max-width: 1536px)',
};

const plugins: BreakpointConfig = {
    resolve: `gatsby-plugin-breakpoints`,
    options: {
        queries: defaultQueries,
    },
};

```

### useBreakpoints

Next let's type the useBreakpoints hook.

```
// index.d.ts
// ...

export type BreakpointsObject = Record<string, boolean>;

export function useBreakpoint(): BreakpointsObject;
```

And test it out.

```
// gatsby-plugin-breakpoints-tests.tsx

import React from 'react';
import {
    // ...
    useBreakpoint
} from 'gatsby-plugin-breakpoints';

function HookComponent() {
    const breakpoints = useBreakpoint();
    return <div>{breakpoints.xs ? <div /> : null}</div>;
}



```

### withBreakpoints

The plugin also provides a HOC (higher order component) which we can use. Let's type it:

```
// index.d.ts
// ...

export interface BreakpointProps {
    breakpoints: BreakpointsObject;
}

export function withBreakpoints<P extends BreakpointProps>(Component: React.ComponentType<P>): React.ComponentType<P>;

```

... and test it out:

```
// gatsby-plugin-breakpoints-tests.tsx

import React from 'react';
import {
    // ...
    withBreakpoints,
    BreakpointProps,
} from 'gatsby-plugin-breakpoints';

const EnhancedFunctionalComponent = withBreakpoints(function Component({ breakpoints }) {
    return breakpoints.xs ? <div /> : <div>Content hidden only on mobile</div>;
});

class Component extends React.Component<BreakpointProps> {
    render() {
        const { breakpoints } = this.props;
        return breakpoints.xs ? <div /> : <div>Content hidden only on mobile</div>;
    }
}

const EnhancedClassComponent = withBreakpoints(Component);

```

### BreakpointContext and BreakpointProvider

Finally, there are two more things to take care of: `BreakpointContext` and `BreakpointProvider`:

```
// index.d.ts
// ...

export type QueriesObject = Record<string, string>;

export const BreakpointContext: React.Context<QueriesObject>;

export const BreakpointProvider: React.Provider<QueriesObject>;
```

Last tests:

```
// gatsby-plugin-breakpoints-tests.tsx

import React from 'react';
import {
    // ...
    BreakpointProvider,
    BreakpointContext,
} from 'gatsby-plugin-breakpoints';

// BreakpointContext
function useContext() {
    const context = React.useContext(BreakpointContext);
    return context;
}

// BreakpointProvider
const ProviderComponent: React.FC = ({ children }) => {
    return <BreakpointProvider value={defaultQueries}>{children}</BreakpointProvider>;
};

```

## Final steps

The hard part is now over. All that is left is to run the DefinitelyTyped lint and test scripts before creating a pull request.

```
npm run lint gatsby-plugin-breakpoints
```

All seems good!

```
npm run test gatsby-plugin-breakpoints
```

Oh, no! There seems to be an error:

```
Cannot find module 'csstype' or its corresponding type declarations.
```

Thankfully, we are not the first ones to encounter it. There is already an [open issue](https://github.com/DefinitelyTyped/DefinitelyTyped/issues/24788) in the DefinitelyTyped repo and the fix seems fairly simple – we need to install the node modules in `types/react`. Let's go for it!

```
cd types/react && npm install && cd ../../ && npm run test gatsby-plugin-breakpoints
```

Phew, it worked! 

At this stage, we are ready to open a PR, make sure all CI checks pass and wait for approval. From my limited experience, the process seems to be fairly quick. This particular PR was approved, merged and published in a little over a day.

Here is the [link](https://github.com/DefinitelyTyped/DefinitelyTyped/pull/50868) if you want to check it out.

# Conclusion

What I described here is a tiny contribution. And it probably can be improved upon (as is the case with all the code we write). But tiny contributions stack up when shared with the community.

The fact that I have used TypeScript exclusively for over a year and this is the first time I came across a project I can type myself is a testament to the awesomeness of open source. I am happy to have made it just a little bit easier for the next person to use TypeScript in their project.

So the next time you find a project that is still looking for its types (or something else altogether), do jump in and contribute, if you can. It makes all the difference!

_If you found this useful, [let's connect](https://twitter.com/iva_kop). For more in-depth React-related articles, check out [my blog](https://blog.whereisthemouse.com/)._


