# guten-clean

A command-line tool to clean Project Gutenberg ebooks for LLM consumption.

## Installation

```bash
pip install .
```

## Usage

```bash
guten-clean <input_path(s)> [options]
```

### Arguments

*   `input_path(s)`: One or more paths to input files or directories.

### Options

*   `-o, --output-dir <directory>`: The directory to save the cleaned files to. Defaults to the current directory.
*   `-v, --verbose`: Enable verbose output.
