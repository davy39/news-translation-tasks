---
title: How to Create Notice Blocks in Markdown
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2024-06-10T09:00:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-notice-blocks-in-markdown
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/Note--Tip--Warning---Caution-specific-blocks-in-MarkDown-1.png
tags:
- name: markdown
  slug: markdown
seo_title: null
seo_desc: 'Markdown is a very popular lightweight markup language. It is used for
  writing documentation and even for creating a complete website. Therefore, almost
  all of us frequently use this markup language every once in a while.

  However, there are some limi...'
---

Markdown is a very popular lightweight markup language. It is used for writing documentation and even for creating a complete website. Therefore, almost all of us frequently use this markup language every once in a while.

However, there are some limitations to this language. In some cases, we can not add that much styling or modifications. 

Luckily for us, there are five highlighting features for specific segment blocks such as notice, tip, caution, important, and warning. These are also applicable in GitHub Markdown as well. 

In this article, I am going to talk about these features in detail.

## Video Walkthrough

If you would like to watch a complete video with step-by-step guidelines, then you can watch the video right now!

%[https://www.youtube.com/watch?v=HMeCXobi90E]

## How to Create a Note Block in Markdown

Use a Note block if you want to highlight information that users should take into account – even when they are just skimming the text.

To write any Note related segment, you need to start it with an angle bracket ( `>` ), and then you need to specify the highlighting block as Note with `[!NOTE]`.

After that, you need to add an angle bracket ( `>` ) in each new line that you want to include in your specific Note block.

If you want to close the Note block, then remove the additional angle bracket in the new line.

```markdown
> [!NOTE]
> I want the readers to read it carefully as it contains many important docs.
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-085135.png)
_Note block_

You see that the preview already has a nice Note related symbol.

## How to Create a Tip Block in Markdown

Use a Tip block if you want to provide optional information to help a user be more successful.

To write any Tip related segment, you need to start it with an angle bracket ( `>` ), and then you need to specify the highlighting block as Tip with `[!TIP]`.

After that, you need to add an angle bracket ( `>` ) in each new line that you want to include in your specific Tip block.

If you want to close the Tip block, then remove the additional angle bracket in the new line. 

```markdown
> [!TIP]
> Use the command line to detect and resolve the errors!
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-085600.png)
_Tip block_

You see that the preview already has a nice Tip related symbol.

## How to Create a Warning Block in Markdown

Use a Warning block if you want to provide critical content that demands immediate user attention due to potential risks.

To write any Warning related segment, you need to start it with an angle bracket ( `>` ), and then you need to specify the highlighting block as a Warning with `[!WARNING]`.

After that, you need to add an angle bracket ( `>` ) in each new line that you want to include in your specific Warning block.

If you want to close the Warning block, then remove the additional angle bracket in the new line. 

```markdown
> [!WARNING]
> DON'T DELETE THE `package.json` file!
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-085842.png)
_Warning block_

You see that the preview already has a nice Warning related symbol.

## How to Create a Caution Block in Markdown

Use a caution block if you want to make users aware of the potential negative consequences of an action.

To write any Caution related segment, you need to start it with an angle bracket ( `>` ), and then you need to specify the highlighting block as a Warning with `[!CAUTION]`.

After that you need to add an angle bracket ( `>` ) in each new line that you want to include in your specific Caution block.

If you want to close the Caution block, then remove the additional angle bracket in the new line. 

```markdown
> [!CAUTION]
> Don't execute the code without commenting the test cases.
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-090155.png)
_Caution block_

You see that the preview already has a nice Caution related symbol.

## How to Create an Important Block in Markdown

Use an important block if you want to provide crucial information that is necessary for users to succeed.

To write any Important related segment, you need to start it with an angle bracket ( `>` ), and then you need to specify the highlighting block as a Warning with `[!IMPORTANT]`.

After that, you need to add an angle bracket ( `>` ) in each new line that you want to include in your specific Important block.

If you want to close the Important block, then remove the additional angle bracket in the new line.

```markdown
> [!IMPORTANT]  
> Read the contribution guideline before adding a pull request.
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-090430.png)
_Important block_

You see that the preview already has a nice Important related symbol.

## Conclusion

Thank you for reading the entire article. I hope you have learned something new here.

If you have enjoyed the procedures step-by-step, then don't forget to let me know on [Twitter/X](https://twitter.com/Fahim_FBA) or [LinkedIn](https://www.linkedin.com/in/fahimfba/). I would appreciate it if you could endorse me for some relevant skillsets on [LinkedIn](https://www.linkedin.com/in/fahimfba/). I would also recommend you to subscribe to my [YouTube channel](https://youtube.com/@FahimAmin) for regular programming related content.

You can follow me on [GitHub](https://github.com/FahimFBA) as well if you are interested in open source. Make sure to check [my website](https://fahimbinamin.com/) as well.

Thank you so much! 😀

### Reference

[[Markdown] An option to highlight a "Note" and "Warning" using blockquote (Beta) #16925](https://github.com/orgs/community/discussions/16925)


