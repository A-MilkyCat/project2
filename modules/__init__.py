# modules/__init__.py
"""modules package - convenience re-exports"""
from .fetch_html import fetch_html
from .html2md import html_to_markdown
from .exploit_generator import exec_genrb_from_main
from .auto_msf import run_auto_msf

__all__ = ["fetch_html", "html_to_markdown", "exec_genrb_from_main", "run_auto_msf"]
