# Betonotes

A Jupyter Book v2 project with integrated Python modules, managed by uv.

## Project Structure

```
betonotes/
├── book/              # Jupyter Book content
│   ├── _config.yml   # Book configuration
│   ├── _toc.yml      # Table of contents
│   ├── index.md      # Home page
│   └── notebooks/    # Content pages
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

### Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   uv sync
   ```

### Building the Book

Build the Jupyter Book:

```bash
uv run jupyter-book build book/
```

The generated HTML will be in `book/_build/html/`. Open `book/_build/html/index.html` in your browser to view the book.

### Development

- Add Python code to `src/betonotes/`
- Add book content to `book/` directory
- Update `book/_toc.yml` to include new pages
- Add dependencies to `pyproject.toml` and run `uv sync`

## Features

- **Jupyter Book v2**: Latest version with improved features
- **Python Package**: Reusable code in `src/` directory
- **uv**: Fast and modern Python package management
- **MyST Markdown**: Rich content with executable code cells
