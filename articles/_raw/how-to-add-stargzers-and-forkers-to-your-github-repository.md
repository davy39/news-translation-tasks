---
title: How to Add Stargazers and Forkers Cards to Your GitHub Repository
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-07-17T22:39:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-stargzers-and-forkers-to-your-github-repository
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/viktor-forgacs-LNwIJHUtED4-unsplash.jpg
tags:
- name: GitHub
  slug: github
- name: open source
  slug: open-source
seo_title: null
seo_desc: 'It is a common practice for open source projects to welcome newcomers and
  help get them interested in contributing more. And there are various ways to do
  this.

  Two popular examples are using stargazers cards and forkers cards. Stargazers highlight
  th...'
---

It is a common practice for open source projects to welcome newcomers and help get them interested in contributing more. And there are various ways to do this.

Two popular examples are using stargazers cards and forkers cards. Stargazers highlight the GitHub users' profiles who starred the repository. And forkers show the people who have already forked the repository.

These are not mandatory for projects to provide, of course. But if you have a new project and want to include these features on your GitHub repository to welcome new contributors, you'll want to know how to add them.

🎥 If you like video tutorials, then I have also created a complete video to show you the entire process:

%[https://www.youtube.com/watch?v=9w2c6f-_ies]

## How to Add Stargazers and Forkers to Your Repo

You can add these features in many ways. I have seen people who like to use different GitHub workflows for this. But in this article, I am going to show you the simplest way to add stargazers cards and forkers cards to your GitHub repo. 

We will use a well-known and widely used open source project named [**Repo Roster**](http://reporoster.com/) ([http://reporoster.com/](http://reporoster.com/)) to do this.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/2023-07-16_18-32.png)
_Repo Roster: https://github.com/nastyox/Repo-Roster_

You can check out their GitHub repository here: [https://github.com/nastyox/Repo-Roster](https://github.com/nastyox/Repo-Roster).

I will use their live website directly which you can find here: [http://reporoster.com/](http://reporoster.com/).

Go to the website. 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/2023-07-16_18-34.png)

You will see a dedicated text box for adding the GitHub repository's URL. Simply copy your entire repository URL and paste the URL there. You will get a unique link appearing in the Stargazers section and another unique link appearing in the Forkers section shortly after that.

For example, I have used my Automate Text Bombing repository here. You can see the results for yourself here:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/2023-07-16_18-35.png)

If you want, you can add two more customizations directly here. You can keep or remove dark mode in the card, and you can also choose whether you want to keep the text inside the card or not.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/2023-07-16_18-36.png)

After that, you simply copy the generated URLs and add them to your `README.md` file in your GitHub repository. 

For example, here is the code that I have added to my repository's README file.

```
[![Stargazers repo roster for @FahimFBA/Automate-Text-Bombing](https://reporoster.com/stars/FahimFBA/Automate-Text-Bombing)](https://github.com/FahimFBA/Automate-Text-Bombing/stargazers)


[![Forkers repo roster for @FahimFBA/Automate-Text-Bombing](https://reporoster.com/forks/FahimFBA/Automate-Text-Bombing)](https://github.com/FahimFBA/Automate-Text-Bombing/network/members)
```

This code generated the following two cards:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/2023-07-16_18-40.png)

You can add more customization like changing the width or length of the cards and so on.

# Conclusion

I hope you have enjoyed this short article. Now you can also add those popular cards to your GitHub repo. 😊

If you have any questions then please let me know using [Twitter](https://twitter.com/Fahim_FBA) or [LinkedIn](https://www.linkedin.com/in/fahimfba/).

You can also follow me on:  
🎁GitHub: [FahimFBA](https://github.com/FahimFBA)  
🎁YouTube: [@FahimAmin](https://www.youtube.com/@FahimAmin?sub_confirmation=1)

If you are interested then you can also check my website: [https://fahimbinamin.com/](https://fahimbinamin.com/)

Have a great day! 😊

Cover: Photo by [Viktor Forgacs](https://unsplash.com/@sonance?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/LNwIJHUtED4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

