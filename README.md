# Betonotes

A Jupyter Book v2 project with integrated Python modules, managed by uv.

## Project Structure

```
betonotes/
├── book/              # Jupyter Book content
│   ├── myst.yml      # Book configuration
│   ├── intro.md      # Home page
│   ├── getting-started.md
│   └── using-python-modules.md
├── src/              # Python source code
│   └── betonotes/    # Python package
│       ├── __init__.py
│       └── utils.py  # Utility functions
├── pyproject.toml    # Project dependencies
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager
- Node.js (for Jupyter Book v2)

### Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   uv sync
   ```

### Building the Book

Build the Jupyter Book:

```bash
cd book
jupyter-book build --html
```

Or using uv:

```bash
cd book
uv run jupyter-book build --html
```

The generated site will be in `book/_build/site/`. 

### Local Development

Start the development server:

```bash
cd book
jupyter-book start
```

Then open your browser to view the live site.

### Development

- Add Python code to `src/betonotes/`
- Add book content as markdown files in `book/` directory
- Update `book/myst.yml` table of contents to include new pages
- Add dependencies to `pyproject.toml` and run `uv sync`

## Features

- **Jupyter Book v2**: Built on MyST Document Engine
- **Python Package**: Reusable code in `src/` directory
- **uv**: Fast and modern Python package management
- **MyST Markdown**: Rich content with executable code cells
- **GitHub Pages**: Automatically deploys on push to main branch
