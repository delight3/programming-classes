# Lesson 02 Notes: HTML Text Elements

## Introduction
HTML text elements are used to display and organize text content on a web page. These elements help structure information, improve readability, and make web pages accessible to users and search engines.

Text elements can be **block-level** or **inline** elements.


## 1. Headings
Headings define the structure and hierarchy of a web page.

### Heading Tags
<h1>Main Heading</h1>
<h2>Sub Heading</h2>
<h3>Section Heading</h3>

<h1> is the most important heading
<h6> is the least important

Use headings in order (do not skip levels)

## 2. Paragraphs and Line Breaks
Paragraphs are used to display blocks of text.

<p>This is a paragraph.</p>

Line Break and Horizontal Rule

<br>   <!-- Line break -->
<hr>   <!-- Horizontal line -->

Avoid using <br> for spacing. Use CSS instead.

## Text Formatting Elements
Formatting elements are used to emphasize text.

| Tag        | Description             |
| ---------- | ----------------------- |
| `<strong>` | Important text          |
| `<b>`      | Bold text (visual only) |
| `<em>`     | Emphasized text         |
| `<i>`      | Italic text             |
| `<u>`      | Underlined text         |
| `<mark>`   | Highlighted text        |
| `<small>`  | Smaller text            |
| `<sup>`    | Superscript             |
| `<sub>`    | Subscript               |
| `<del>`    | Deleted text            |
| `<ins>`    | Inserted text           |

Example:
<p>This is <strong>important</strong> and <em>emphasized</em> text.</p>

## Quotes and Citations
Used to represent quoted text.

<blockquote>
  Learning HTML is the first step to web development.
</blockquote>

Inline Quote
<p>The teacher said <q>practice every day</q>.</p>

Citation
<cite>HTML Documentation</cite>

## Code and Preformatted Text
Used for displaying programming examples.

<pre>
<code>
print("Hello, World!")
</code>
</pre>

Other useful tags:
<kbd> – keyboard input
<samp> – sample output

## Lists

Lists help organize information.

Unordered List:
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
</ul>

Ordered List:
<ol>
  <li>Install editor</li>
  <li>Write code</li>
  <li>Run browser</li>
</ol>

Description List:
<dl>
  <dt>HTML</dt>
  <dd>Structure of a webpage</dd>
</dl>

## Links and media

1. Links (<a>)
The <a> tag creates hyperlinks to other pages or resources.

Example:
<p>Visit my favorite website: 
    <a href="https://www.example.com" target="_blank" title="Go to Example.com">
        Example
    </a>
</p>

Explanation:
href → the URL of the link.
target="_blank" → opens the link in a new tab.
title → shows a tooltip when hovered.

2. Images (<img>)
The <img> tag displays an image on the page.

<img src="cat.jpg" alt="Cute Cat" width="300">

Explanation:
src → path to the image file.
alt → alternative text for accessibility.
width → sets the width of the image.

3. Audio (<audio>)
The <audio> tag embeds audio in the page.

<p>Listen to this music:</p>
<audio controls>
    <source src="song.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio>

Explanation:
controls → shows play/pause buttons.
<source> → specifies the audio file and type.
Fallback text is shown if audio is unsupported.

4. Video (<video>)
The <video> tag embeds video in the page.

<p>Watch this video:</p>
<video width="400" controls>
    <source src="movie.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

Explanation:
width → sets the width of the video player.
controls → shows play/pause and volume controls.
Fallback text is shown if the browser does not support the video.

You can combine links and media like this:
<p>Click <a href="video.html" target="_blank">here</a> to watch more videos!</p>

## Semantic Text Elements
Semantic elements add meaning to content.
There are some semantic elements that can be used to define different parts of a web page.

## Semantic HTML Tags and Their Purpose

| Tag | Purpose |
|-----|--------|
| `<abbr>` | Defines an abbreviation or acronym |
| `<address>` | Contains contact information |
| `<time>` | Represents a specific date or time |
| `<span>` | Inline container for styling text |
| `<header>` | Defines a page or section header |
| `<nav>` | Contains navigation links |
| `<section>` | Groups related content into sections |
| `<article>` | Represents independent, self-contained content |
| `<aside>` | Contains side or related content |
| `<main>` | Specifies the main content of a document |
| `<details>` | Defines additional details that can be shown or hidden |
| `<summary>` | Provides a visible heading for a `<details>` element |
| `<figure>` | Represents self-contained content (images, diagrams, etc.) |
| `<figcaption>` | Defines a caption for a `<figure>` element |
| `<footer>` | Defines footer content |
| `<mark>` | Highlights or marks important text |

## Non-Semantic HTML Tags and Their Purpose
Tells nothing about its content

| Tag | Purpose |
|-----|--------|
| `<div>` | Generic block-level container |
| `<span>` | Generic inline container |
| `<b>` | Bold text (no importance) |
| `<i>` | Italic text (no emphasis) |
| `<u>` | Underlined text |
| `<br>` | Line break |
| `<hr>` | Horizontal line |
| `<small>` | Displays smaller text |
| `<sup>` | Superscript text |
| `<sub>` | Subscript text |

<div> - Container for other HTML elements


