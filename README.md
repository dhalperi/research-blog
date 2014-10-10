To setup
========

```
mkvirtualenv blog
pip install pelican markdown typogrify ghp-import BeautifulSoup4 pillow
git submodules update
make devserver
```

then navigate to <http://localhost:8000> to see the rendering of the blog.

```
make github
```

will push the rendered content to github.
