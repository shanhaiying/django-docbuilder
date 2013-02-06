Doc Builder
===========

Automatically build your git based documentation written in reStructuredText
into LaTeX through you Django app.

Motivations
-----------

Most of the time when writing documentation I don't need all the LaTeX complex
things, just the gorgeous rendering.

To hide this unnecessary complexity, I decided to use a simpler language like
reStructuredText (at the beginning it was Markdown), and then transform it to LaTeX.

Many tools already exists to do so, like
[Pandoc](http://johnmacfarlane.net/pandoc/) but what if you want to split your
documentation into multiple files? What if you don't want to install the whole
Haskell stack? What if you want to share the compilation process with non
technical colleges?

After many unsuccessful researches I was unable to find the simple tool I was
looking for. As I said, many tools exists to transform reStructuredText into
LaTeX, but there are for most painful to install.

I have decided to build a tool that is simple to install, that can be run remotely,
where I can easily define the resulting template and where the sources are
pulled from a git repository.

Requirements
------------

To run the app, you need `docutils` and `django` python package (pip FTW). 

In addition, the `pdflatex` and `git` programme should be installed on the system.


Technical choices
------------------

As I was unable to find a working python Markdown to LaTeX parser, I switched
to reStructuredText which is quite the same think but have a great support
thanks the Sphinx engine.
If you know a good Markdown parser, let me know ;)

The default helper is intended to work with Django, but any other web framework
can be used, a command line interface or what ever you want.

Configuration
--------------

As usual, remember to add `docbuilder` to your django module list.

You will need an already cloned git repository, configured in `local_settings.py`.
Checkout other settings.

Some generic urls are provided in `urls.py`.

Documents and template
----------------------

Three types of Documents can be used:

 * Articles: a title and multiple subtitles / paragraphs.
 * Reports: multiple titles with subtitles and paragraphs.
 * Slides: a beamer presentation

The build document can be either a document or a repository. In this case, all
the file in it are merged alphabetically.

### Write an article

An article looks like that:

~~~~
My article title
================

A subtitle
----------

Blabla

Another subtitle
----------------

Blabla...
~~~~

The simplest template you can defined to build your article:

~~~~
\documentclass{article}

\title{$title}
\date{\today}

\begin{document}
\maketitle

$body
\end{document}
~~~~

### Writing a report

~~~~
Title 1
=======

Title 1.1
---------

Blabla

Title 1.2
---------

Blabla

Title 2
=======

Blabla
~~~~

~~~~
\documentclass{report}

\title{THETITLE}
\date{\today}

\begin{document}
\maketitle

$body
\end{document}
~~~~

You noticed that the title variable changed. This new variable is deduced from
the filename or directory (camel case is transformed: TechnicalNote becomes Technical Note).

You can also set dynamically the title with a title query string like
`?title=Hello` or hard code it to the view via the title parameter 

### Write a presentation

The structure of a presentation is the same as the article. The main article
will represent the presentation title.

Each subtitle will becomes the slide title and the content between those each slide contents.

A minimalistic beamer template looks like:

~~~
\documentclass{beamer}

\title{$title}
\author{Myself}
\date{\today}

\begin{document}
\begin{frame}[t,plain]
 \titlepage
 $body
\end{frame}
\end{document}
~~~


Interested to use it?
---------------------

Bug reports, feature/pull request, comments, suggestions welcome!
