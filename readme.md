# Welcome to Coding best practices

For full documentation about MkDocs visit [mkdocs.org](https://www.mkdocs.org).

## Installation

Install MkDocs and plugins: 

```shell
    pip install mkdocs      
    pip install mkdocs-material // style
    pip install mkdocs-embed-external-markdown // external inclusions
    pip install mkdocs-include-markdown-plugin // internal inclusions
    pip install mkdocs-glightbox // image gallery modal
    pip install mkdocs-git-revision-date-plugin // add git revision date
    pip install mkdocs-page-pdf // single page downloadable pdf
    pip install mkdocs-with-pdf // full document pdf
    pip install mkdocs-git-authors-plugin // add git author
    pip install neoteroi-mkdocs // add openAi Docs plugin
    pip install pygments // add plugin to highlight code
    pip install include-markdown // allow inclusions
```

Install commit to change-log features:

```shell
    npm install // install node package
    npm run prepare // prepare Husky
```

## Node Commands
* `npm run serve` - Start the live-reloading docs server (`http://localhost:8000/`).
* `npm run build` - Build the documentation site with full pdf generation.
* `npm run deploy` - Deploy on git with full pdf generation.
* `npm run kill` - Kill the dev server process (only on Mac).
* `npm run format` - Run Prettier on all markdown files.
* `npm run combine` - Combine all the markdowns in a unique file

## MkDocs Commands
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `ENABLE_PDF_EXPORT=1 mkdocs build` - Build the documentation site with full pdf generation.
* `mkdocs -h` - Print help message and exit.
* `mkdocs gh-deploy` - Deploy on git.
* `ENABLE_PDF_EXPORT=1 mkdocs build` - Deploy on git with full pdf generation.
 
## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

