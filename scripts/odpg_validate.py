import argparse
from pathlib import Path

from odpg_toolkit_core import command_validate


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate graph structure, node integrity, edge integrity, confidence values, and core ODPG semantics.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("-i", "--input", required=True, type=Path, help="Path to ODPG YAML graph file")
    parser.add_argument("-o", "--output", type=Path, help="Optional JSON output file")
    return parser


def main() -> int:
    return command_validate(build_parser().parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
