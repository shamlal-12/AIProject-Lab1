"""
===================================================================
AIR UNIVERSITY ISLAMABAD - Faculty of Computing & AI
Department of Creative Technologies
Course: AI Project Design and Development (AI-316)
Lab 01: Foundations of AI Engineering & Project Setup
Task 1: GitHub-Ready AI Repository Directory Structure Setup

Student Name: Sham Lal
Roll Number: 231183
Class: BSAI-7B
Lab Instructor: Farhan Zafar
===================================================================
"""

import os
import sys
from pathlib import Path

# Ensure UTF-8 output encoding for Windows terminal
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Standard production-ready AI repository directories
DIRECTORIES = [
    "data/raw",
    "data/processed",
    "models",
    "notebooks",
    "src",
    "configs",
    "logs",
]

def create_directory_structure(root_path: Path):
    """Creates directory structure and inserts .gitkeep files for empty tracking."""
    print(f"[+] Setting up directory structure in: {root_path.resolve()}\n")
    
    for relative_path in DIRECTORIES:
        dir_path = root_path / relative_path
        dir_path.mkdir(parents=True, exist_ok=True)
        gitkeep_path = dir_path / ".gitkeep"
        if not gitkeep_path.exists():
            gitkeep_path.touch()
        print(f"  [OK] Created directory & .gitkeep: {relative_path}/")

def print_tree(directory: Path, prefix: str = "", ignore_dirs=None):
    """Prints a visual tree representation of the repository."""
    if ignore_dirs is None:
        ignore_dirs = {".git", "aipdd_env", "__pycache__", ".venv", ".ipynb_checkpoints"}
    
    entries = sorted([e for e in directory.iterdir() if e.name not in ignore_dirs], key=lambda x: (not x.is_dir(), x.name))
    for i, entry in enumerate(entries):
        is_last = (i == len(entries) - 1)
        connector = "+-- " if is_last else "|-- "
        print(f"{prefix}{connector}{entry.name}")
        if entry.is_dir():
            new_prefix = prefix + ("    " if is_last else "|   ")
            print_tree(entry, new_prefix, ignore_dirs)

if __name__ == "__main__":
    project_root = Path(__file__).parent
    create_directory_structure(project_root)
    print("\n[+] Project Tree View:")
    print(f"{project_root.name}/")
    print_tree(project_root)
