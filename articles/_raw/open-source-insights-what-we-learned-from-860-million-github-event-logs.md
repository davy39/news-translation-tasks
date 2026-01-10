---
title: Open Source Insights – What We Learned from 860 Million GitHub Event Logs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-09T00:19:50.000Z'
originalURL: https://freecodecamp.org/news/open-source-insights-what-we-learned-from-860-million-github-event-logs
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-08-at-7.00.31-AM.png
tags:
- name: community
  slug: community
- name: GitHub
  slug: github
- name: open source
  slug: open-source
seo_title: null
seo_desc: "By Xue (Xander) Wu\nOpen source software has become a cornerstone of our\
  \ digital world. And open collaboration plays an enormous role in the development\
  \ of human digital civilization. \nGitHub, the world's largest open source collaboration\
  \ platform, pr..."
---

By Xue (Xander) Wu

Open source software has become a cornerstone of our digital world. And open collaboration plays an enormous role in the development of human digital civilization. 

GitHub, the world's largest open source collaboration platform, produces a massive amount of developer behavior data. So what can we do with this data?

## The Problem – How to Measure Productivity 

As management guru Peter Drucker famously said, "If you cannot measure it, you cannot manage it," and, consequently, you cannot improve it. 

The software industry has yet to find a method that can effectively measure the productivity of software development. This holds true especially for the entire open source ecosystem. How individuals and communities are measured and how managers can use these metrics to make better decisions are still open questions. 

In our view, these are both challenges and opportunities. When you're governing an open source project, it is difficult to circumvent the problem of measurement. But GitHub event logs offer an excellent opportunity to solve the problem.

Measurement is also a double-edged sword. Given its strong guiding nature, it motivates you to pay attention to and improve the elements that can be measured. 

However, measurement may also cause you to ignore and worsen the elements that you can't measure. How can you find the right metrics and use them wisely in the process of building large-scale open source communities and ecosystems around the world?

Well, we obtained 860 million GitHub event logs generated in 2020 and analyzed the data from over 14 million active developers and more than 54 million active projects. And in this article, we'll share our insights.

## The GitHub 2020 Digital Insight Report

In our newly released [GitHub 2020 Digital Insight Report](http://oss.x-lab.info/github-insight-report-2020-en.pdf), which is also an open source [project](https://github.com/X-lab2017/github-analysis-report) on GitHub, we explored the status of global trends in open source. 

The purpose of the report was to produce a worldwide open source ecosystem map, promote the open source social innovation, and foster open collaboration.

The report starts with a general analysis of the global state of open source today. The following sections include a discussion of in-depth developer and project analyses, case studies, and star projects of the month.

We defined metrics and built models by paying attention to information in the dimensions of time, diversity, and collaborative networks. We also introduced two important concepts, **OpenGalaxy** and **Open Source Quadrant**.

## Key Takeaways from the Report

### The global open source industry has developed a lot

The total number of GitHub global event logs was about 860 million in 2020, representing an increase of about 42.6% from 610 million in 2019. 

We also found that the number of global active projects on GitHub in 2020 was about 54.21 million, while the number of active developer accounts was about 14.54 million. This marked an increase of 36.4% and 21.8%, respectively, over 2019.

![Image](https://uploader.shimo.im/f/DzxnbbSnebkLsGvR.png!thumbnail)

### Developers are at the core of the open source world

An activity model based on massive data can effectively and continuously reflect the overall status of developers and communities.

Following the spirit of the Apache maxim ‘Community Over Code’ promoted by [The Apache Way](https://www.apache.org/theapacheway/), the developer community is crucial to open source vitality. 

We tried to present a comprehensive analysis of all GitHub developers in 2020 from multiple perspectives such as the activity level of developers, GitHub Apps usage, typical working hours, global developer time zone distribution, and developer language distribution.

We introduced the **developer activity metric**, which reflects the level of activity of a specific GitHub account in a specific GitHub project over a period of time. 

We determine the developer activity metric by the account behavior data in the project. The behaviors detailed in this report include Issue comment, Open issue, Open pull request, Pull request review comment, Pull request merged, Watch, and Fork, with weights of 1, 2, 3, 4, 2, 1, 2, respectively.

![Image](https://uploader.shimo.im/f/sdTTqriJNU0Hbj02.png!thumbnail)

Among them, the count of pull requests merged is determined by the piecewise function:

![Image](https://uploader.shimo.im/f/NJjU0HEawJp0uHwi.png!thumbnail)

![Image](https://uploader.shimo.im/f/P4lMIinXV5K7PUtm.png!thumbnail)

Statistics suggest that 5,445 developers’ activity metric is over 2,000, equivalent to fewer than 6 out of 10,000 Github developers. 

Most developers’ activity metric falls into the range of [0,500], accounting for 99.45% of the total number of Github developers, which suggests that most developers still have a low level of activity. 

At the end of the curve, the number of active repositories shows an increase, likely attributable to the huge number of active repositories for some unfiltered automated collaboration accounts, which far exceed the number of human developers. This results in a V-shaped tail end of the curve.

### Automation is key

The automation of the open source software pipeline has improved a lot, and diversified digital collaborative robots have begun to enter the mainstream.

We found that 8 of the top 10 most active developers are GitHub Apps, and the other two are developer accounts for automated collaboration.

![Image](https://uploader.shimo.im/f/oapQVMWMYm3C6BTY.png!thumbnail)

The automated collaborative robots can serve many projects concurrently because they run on the server side. This results in an extremely high level of activity and a huge number of collaborative repositories.

As shown in the above table, the majority of the most active developer accounts across GitHub are GitHub Apps. This report analyzes relevant GitHub Apps data. 

For example, the following figure shows the trend of both the number of active GitHub Apps (total active accounts) and the ratio of logs generated by GitHub Apps to all GitHub event logs (proportion of logs) from 2015 to 2020.

![Image](https://uploader.shimo.im/f/XpPx8PdIpmQrbYSo.png!thumbnail)

GitHub Apps have developed rapidly in recent years since their launch in 2016. In terms of proportion of logs, the total number had increased by 288% in 2019 compared to 2018, and it increased by 141% in 2020 compared to 2019 to as high as over 12%.

We open-sourced this [report project](https://github.com/X-lab2017/github-analysis-report) on GitHub. To automate the code development and data analysis for this project, we developed analysis-report-bot[bot], a GitHub collaborative robot, in August 2020. 

It is worth mentioning that analysis-report-bot[bot] ranks 289th in activity ranking across all GitHub Apps as of today.

Having benefited from this automated collaborative bot, we believe bots that are based on GitHub Apps will be more widely used to help better manage large-scale collaborations for open source projects in the future.

### Open source contributions generally coincide with developers' working hours 

The working hours of mainstream developers in GitHub communities show clear patterns and gradually overlap with developers’ working hours in their jobs. 

Corporate open source has become the absolute mainstream, and ‘996' working hour open source projects’ have cropped up.

Since the GitHub event log has detailed time stamp information, we can glean insights through statistical analysis of the time dimension. For example, in UTC standard time, the global working time distribution is shown in the following figure:

![Image](https://uploader.shimo.im/f/8OcbweiWxnwLlEsr.png!thumbnail)

Let's say that normal working hours for mainstream developers are from 9:00 to 21:00 every day. From a global perspective, through the log volume, we can see that developers on the GitHub platform come mainly from Europe and the United States. 

Also, we can see that the activity on weekends is significantly lower than on weekdays. This is consistent with the [GitHub Octoverse 2020](https://octoverse.github.com/) report which found that more developers use GitHub to work instead of developing merely based on their interests.

### We can learn a lot about the global distribution of developers using GitHub

The Americas have the largest distribution of developers. Europe has the highest percentage of developers in a single time zone, while the number of Asian developers is still on the low end. Compared with other Asian countries, China boasts a higher level of open source activity.

The geographic distribution of developers has always been an important aspect of the globalization indicators of open source projects. 

Based on the statistics of the top 50,000 developers in GitHub developer Activity ranking, we can estimate the distribution of all GitHub developers in various time zones as shown in the following figure.

![Image](https://uploader.shimo.im/f/EX0YQQFq1LILNkzm.png!thumbnail)

We can see that the Americas (the United States, Canada, and South America) have the largest distribution of developers among highly active developers. Although the proportion of developers in a single time zone is not the highest, the overall proportion of developers in this region is as high as about 33%. 

Europe has the highest proportion of developers in a single time zone. The UTC+1 time zone is as high as nearly 10%, with the total proportion of the three time zones being about 26%. 

In general, the number of developers in Asia is still relatively small, but we can see a small peak in the UTC+7 and UTC+8 region, indicating that developers in China and Russia are still more active in open source than other countries. 

The Pacific region has the lowest proportion of developers due to population distribution.

### JavaScript and Python rank first and second globally

No surprise here – JS and Python still occupy the first and second place, respectively, in language rankings. HTML and CSS are more popular in the context of global developers, while TypeScript and Rust have significantly gained in prominence.

The following figure shows the distribution of languages used by active developers across all GitHub projects in 2020 and the distribution of languages used by the top 100,000 active developers. Comparing the distribution of project languages, we can see some fluctuation in the rankings.

![Image](https://uploader.shimo.im/f/IiqgJfInx4daKyXr.png!thumbnail)

JavaScript and Python are consistent winners and runners-up in the rankings, while HTML and CSS are clearly more popular in the context of all GitHub developers. 

This is due to the large number of blog sites and other similar repositories on GitHub. These projects are generally small, independent, and maintained by individual developers.

### Big companies like Google and Microsoft are major contributors to open source. 

Also, China-headquartered e-commerce giant Alibaba ranks topmost in terms of activity metric among its peers, while PingCAP has recorded an impressive performance.

According to the definition of project activity metric (details in the full report), we have collected activity statistics and the ranking of active projects in 2020. 

Below is a list of the world’s top 20 most active projects. Since this is the report for 2020, the data used in this table were all newly generated during 2020 (and historically reported data was not included).

![Image](https://uploader.shimo.im/f/ewWjIC1qkM6DliIu.png!thumbnail)

We also collected a list of Chinese-initiated projects through various channels and gave a ranking of the activity metric of Chinese projects.

![Image](https://uploader.shimo.im/f/vBHnAhK05haIDqQ7.png!thumbnail)

From the above list, we found that PingCAP has stellar performance in open source. They represent 6 projects on the list of the Top 20 projects. Alibaba's contribution in open source is nothing short of impressive. They have 2 projects on the Top 10 list.

Baidu has demonstrated an outstanding performance in the field of artificial intelligence. Two projects of its deep learning platform PaddlePaddle, namely the core framework Paddle and related tool libraries, made the list. 

The list of China’s Top 20 most active projects includes Alibaba’s Ant Design component library, JD’s development framework taro, which is based on the React front-end framework, and the Vue UI component library Element, open-sourced by the front-end team of Ele.me (acquired by Alibaba).

### Open Galaxy helped us gain a more complete picture 

For the first time, we were able to see a more complete picture of GitHub open source projects thanks to OpenGalaxy. We introduced it in the report.

The results we get through activity metric analysis will be affected by automated collaboration behavior. Also, the activity metric of projects of different maturity levels may not be comparable. 

So in this report we used OpenGalaxy, a collaborative relationship network for global projects.

OpenGalaxy is based on the definition of developer activity metric, and builds a collaborative relationship between projects through all developers' collaboration behaviors on GitHub. It provides a way to calculate influence and clustering through graph algorithms.

You can find the specific calculation method from the full report.

![Image](https://uploader.shimo.im/f/krqTmc94ylG57peq.png!thumbnail)

The above is a collaboration network diagram composed of the most active 221,000 open source projects on GitHub in 2020. The size of the node in the figure indicates the influence of the project, and the color of the node indicates the collaborative clustering result to which the node belongs.

The top 20 projects with the greatest influence among all GitHub projects in 2020 were evaluated on the influence of the collaborative network. They are shown in the following table:

![Image](https://uploader.shimo.im/f/FVBoMaAsOY6r3bBz.png!thumbnail)

From the table we can see that VS Code has jumped to #1 when measured by influence, from #5 when measured by activity. With its influence about 64.7% higher than Flutter, which ranks 2nd, VS Code has become the world's most influential project.

We built a developer collaboration network for VS Code using the repository’s event logs of 2020, as shown in the following figure.

![Image](https://uploader.shimo.im/f/3SrjeuxHRLualC7S.png!thumbnail)

The collaborative network is composed of more than 20,000 developers. The nodes are the developers' GitHub accounts, the edges are the collaboration relationships, and the size of the nodes reflects the activity level of the corresponding developer accounts. 

In this collaborative network, the larger nodes at the core of the network are the core team members of VS Code. They not only have a high activity metric, but also have a high collaborative relationship with other developers. There are about a hundred members in the team group. 

The outside nodes that closely follow are active users of or contributors to VS Code. They may submit Issues or PRs for discussion or contribution at any time. The members in this group number in the thousands. 

The outermost and largest number of developers are general users of VS Code and occasional contributors, most of whom only ask questions or discuss issues that they care about.

OpenGalaxy has a feature that links excellent projects by excellent developers who work on them. As a result, the influence index will not be falsely high due to automated behavior, but has a better algorithm stability instead. 

Since the change in influence reveals the developer community's activity change, influence becomes a better metric to reflect a project’s influence level among all GitHub projects.

### 9. Open Source Quadrant takes it a step further

In the report, we also introduced Open Source Quadrant, which can further distinguish between different development stages and maturity levels of similar open source projects.

The open source quadrant analysis is represented by a scatter chart. The horizontal and vertical dimensions indicate the project's influence and the project's globalization, respectively. 

We use the logarithmic form of the two indicators and the size of the dots to depict the number of active participants in the project as well as reflecting the scale of a community.

You can find the specific calculation methods for influence, globalization, and the number of participants in the full report.

Here is an example of the **Open Source Quadrant** analysis of the Linux Foundation AI and Data projects:

![Image](https://uploader.shimo.im/f/21BE7xA2gFGCT3q5.png!thumbnail)

### The open source community is diverse and robust

Developer time zone distribution maps and developer collaboration networks have become effective means of reflecting the diversity and robustness of open source communities. And they can helps us better govern the open source community.

We'll take the Linux Foundation AI and Data projects as an example.

![Image](https://uploader.shimo.im/f/sHn39h0qplzPFrMP.png!thumbnail)

We can see that the developer time zone distribution of projects in this field has changed a lot compared with all GitHub projects. About 16% of developers are from UTC+7 to UTC+8. 

In these time zones, Chinese developers are the most involved, which reflects that China has more data and artificial intelligence practitioners.

## What else did we learn?

We did in-depth case studies of developer collaboration networks within specific projects from the Cloud Native Computing Foundation (CNCF), Linux Foundation (LF), and Apache Software Foundation (ASF) among others.

### Star of the Month

In addition to top-level projects, some projects on GitHub have received a lot of attention from developers in a short period of time. These projects may be phenomenon projects, they may become top-level projects in the future, or they may relate to social hot spots, such as the COVID-19 pandemic. 

It is meaningful to discover and explain why they have received a lot of attention during a specific period. Therefore, the Star of the Month section lists the projects that have received a lot of attention each month in 2020.

Based on the log data, projects that received the most stars per month were screened first, and then we selected one example for each month.

* January: microsoft/playwright
* February: wuhan2020/wuhan2020
* March: CSSEGISandData/COVID-19
* April: labuladong/fucking-algorithm
* May: design-resources-for-developers
* June: CnC_Remastered_Collection
* July: JaidedAI/EasyOCR
* August: geekxh/hello-algorithm
* September: cli/cli
* October: developer-roadmap
* November: ytdl-org/youtube-dl
* December: beurtschipper/Depix

## Summary and Outlook

As a data-driven visualization tool, the **GitHub 2020 Digital Insight Report** mainly provides you with a new perspective on today's open source world as well as insights from intersecting with industrial experiences. 

Starting from this annual report, we will also maintain the work as an open source project, shorten the release cycle, and provide professional consulting services on demand.

You can get the full report from this link: [http://oss.x-lab.info/github-insight-report-2020-en.pdf](http://oss.x-lab.info/github-insight-report-2020-en.pdf)

If you find any data errors or omissions, please submit an Issue or PR to GitHub. The text of this report adopts the CC-BY-4.0 license agreement, and the project address is: [https://github.com/X-lab2017/github-analysis-report](https://github.com/X-lab2017/github-analysis-report)

## Acknowledgements

The GitHub 2020 Digital Insights Report was initiated by X-lab, planned by the Allumos open source technology media, and jointly completed with East China Normal University, Kaiyuanshe, Shanghai Open Source Information Technology Association, along with many other scientific research institutions and open source community institutes.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-27.png)

Contributors to this report are:

Shengyu (Frank) Zhao, Wei (Will) Wang, Tianyi Zhou, Zhenjie Weng, Haoyue Wang, Xiaoya Xia, Xiangning Zhu, Ming Yang, Zexin Ning, Haiming Lin, Fuzheng Wang, Jingben Shi, Zehua Lou, Yeming Gu, Xue (Xander) Wu, Jia (Kate) Yang, Siying (Mabel) Li.

Contributors to the English version of the report are:

Xue (Xander) Wu, Puyu (Paul) Wang, Xiaoya Xia, Shengyu (Frank) Zhao, Xiaotian Dai, Siying (Mabel) Li, Yu (Atena) Chen. A special word of thanks to [Aleksey Zaitsev](https://vistal.media/) (WeChat: vistal-media) for his invaluable help with editing.

We welcome more open source enthusiasts to join us and jointly promote the development of open source in the world.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-26.png)


