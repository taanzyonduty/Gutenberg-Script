import argparse
import os
import sys
from . import cleaner
from . import epub_cleaner

def main():
    parser = argparse.ArgumentParser(
        description="Clean Project Gutenberg ebooks for LLM consumption."
    )
    parser.add_argument(
        "input_paths",
        nargs="+",
        help="One or more paths to input files or directories.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default=".",
        help="The directory to save the cleaned files to. Defaults to the current directory.",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output."
    )

    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    for input_path in args.input_paths:
        if os.path.isfile(input_path):
            process_file(input_path, args.output_dir, args.verbose)
        elif os.path.isdir(input_path):
            for root, _, files in os.walk(input_path):
                for file in files:
                    if file.endswith(('.txt', '.html', '.epub')):
                        file_path = os.path.join(root, file)
                        process_file(file_path, args.output_dir, args.verbose)

def process_file(input_path, output_dir, verbose):
    if verbose:
        print(f"Processing {input_path}...")

    if input_path.endswith('.epub'):
        output_filename = os.path.splitext(os.path.basename(input_path))[0] + "_cleaned.epub"
        output_path = os.path.join(output_dir, output_filename)
        try:
            epub_cleaner.clean_epub(input_path, output_path)
        except Exception as e:
            if verbose:
                print(f"Error processing EPUB {input_path}: {e}")
            return
    else:
        try:
            with open(input_path, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            if verbose:
                print(f"Error reading {input_path}: {e}")
            return

        cleaned_text = cleaner.clean_ebook(text)

        output_filename = os.path.splitext(os.path.basename(input_path))[0] + "_cleaned.txt"
        output_path = os.path.join(output_dir, output_filename)

        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(cleaned_text)
        except Exception as e:
            if verbose:
                print(f"Error writing {output_path}: {e}")
            return

    if verbose:
        print(f"Cleaned file saved to {output_path}")

if __name__ == "__main__":
    main()
