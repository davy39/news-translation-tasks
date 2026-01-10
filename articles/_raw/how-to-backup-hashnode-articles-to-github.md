---
title: How to Backup Your Hashnode Articles to GitHub
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-05-16T15:21:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-backup-hashnode-articles-to-github
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/gradient-color-Modern-Music-Playlist-YouTube-Thumbnail.gif
tags:
- name: Backup
  slug: backup
- name: Blogging
  slug: blogging
seo_title: null
seo_desc: "Many developers have a personal blog on Hashnode, one of the most popular\
  \ blogging communities for people exploring tech. \nI also write on Hashnode, but\
  \ recently I was thinking about whether there is any way to backup my published\
  \ articles to GitHub...."
---

Many developers have a personal blog on [Hashnode](https://hashnode.com/), one of the most popular blogging communities for people exploring tech. 

I also write on Hashnode, but recently I was thinking about whether there is any way to backup my published articles to GitHub. Fortunately, I have found an easy way to do that directly from Hashnode itself.

So, in this article, I will share the process so that you can also create an automatic backup of your articles to your GitHub repository. There's no harm in trying something new, right? 😊

✨ I have also created a full length video showing the process of creating that automatic backup to your GitHub repo. I have attached the video later in this article. You can also check that out.

Firstly, let me show you my Hashnode account. This is just a sample of a typical profile there.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_00_31_58.Still002.jpg)

I have published only one article (as of today, 15 May 2022). But I still want to create an automatic backup process for this account so that whenever I write something new, all of the articles get copied into my selected GitHub repository as a backup.

So let's do that, shall we? 😁

### How to Backup Your Hashnode Articles to GitHub

Go to your GitHub account. We need to create a special repository first where we will create an automatic backup process.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-15-093838.png)

Now simply click on the `+` button on the top right of the webpage.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_01_54_29.Still004.jpg)

Now click **New repository**.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_02_00_23.Still005-1.jpg)

Now we have to create a new repository. The process is similar to creating any other repository.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_02_03_28.Still006.jpg)

You can make the repository Public or Private as you see fit for yourself. I am making it a Private repository, but you do not have to do that if you don't want to.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_02_41_42.Still008.jpg)

Give the repository any name you want.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_02_57_02.Still009.jpg)

For the latter, you can select anything you want. For this article, I am keeping it simple as it was.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_03_18_19.Still010.jpg)

Then click **Create repository**.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_03_37_16.Still011.jpg)

After that, you actually do not need to do anything in that repository for now.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_03_41_19.Still012.jpg)

So, I am keeping it as it is right now.

Now, head over to your Hashnode account. 

Click your profile icon on the top right of the profile page.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_03_46_36.Still013.jpg)

Select the blog you want to backup. For me, it is [https://fahimbinamin.hashnode.dev/](https://fahimbinamin.hashnode.dev/).

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_03_47_50.Still014.jpg)

Click Blog Dashboard.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_03_53_36.Still015.jpg)

The blog dashboard will appear before you.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_03_58_22.Still016.jpg)

Simply scroll down until you find Backup. You will find that on the lower left side of the webpage. Click on that.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_04_12_46.Still017.jpg)

You will find the GitHub Backup page now. 

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_05_03_47.Still020.jpg)

Click on Back up all my posts.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_05_03_47.Still020-1.jpg)

Select where you want to install it.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_05_06_45.Still021.jpg)

As I am involved in 5 GitHub organizations right now, it's suggesting all of them to me. As I want to create the backup on my personal GitHub account, I will select my profile **FahimFBA**.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_05_33_05.Still022.jpg)

The install and authorize section will appear.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_05_44_25.Still023.jpg)

By default, it will select "All repositories". **But keep in mind, that you shouldn't select All repositories, as that will rewrite all of the repositories you currently have in your personal GitHub account.**

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_05_50_45.Still024.jpg)

Select "Only select repositories", and find the repository which you have created for backing up your Hashnode blogs.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_06_14_16.Still025.jpg)

Simply click and select the repository.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_06_19_37.Still026.jpg)

If everything is okay, then you can click "Install & Authorize", **but again** **keep in mind that you must not select All repositories.**

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_06_39_58.Still029.jpg)

Provide your GitHub account's password if it asks for that.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_06_42_26.Still030.jpg)

If will redirect you to Hashnode to continue the installation process.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_06_47_38.Still031.jpg)

You've now created your automatic backup. If you want to back up the existing posts, then you have to click "Back up all my posts".

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_07_31_47.Still032.jpg)

It will backup every post you had before creating the automatic backup.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_07_33_09.Still033.jpg)

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_07_38_56.Still034.jpg)

Now, if you simply refresh the GitHub repo webpage (the repo you created only for backing up this Hashnode blog), you will see that it has been updated as well!

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_07_59_50.Still036.jpg)

You can even read the article directly from your backed up repo.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-04-28-13-42-26.00_08_02_00.Still037.jpg)

That's it! 

If you want to watch a video that covers the whole process, then you can check out the following video that I made:

%[https://www.youtube.com/watch?v=a2PZPR9ul6c]

## Conclusion

Thanks for reading the entire article. If it helps you then you can also check out other articles of mine at [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

If you want to get in touch with me, then you can do so using [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), and [GitHub](https://github.com/FahimFBA). 

You can also [SUBSCRIBE to my YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) if you want to learn various kinds of programming languages with a lot of practical examples regularly.

If you want to check out my highlights, then you can do so at my [Polywork timeline](https://www.polywork.com/fahimbinamin).

You can also [visit my website](https://fahimbinamin.com/) to learn more about me and what I'm working on.

Thanks a bunch!




