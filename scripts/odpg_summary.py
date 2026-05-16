import argparse
from pathlib import Path

from odpg_toolkit_core import command_summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Summarize ODPG graph metadata, nodes, edges, relationship types, and confidence values.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("-i", "--input", required=True, type=Path, help="Path to ODPG YAML graph file")
    parser.add_argument("-o", "--output", type=Path, help="Optional JSON output file")
    return parser


def main() -> int:
    return command_summary(build_parser().parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
