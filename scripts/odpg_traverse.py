import argparse
from pathlib import Path

from odpg_toolkit_core import command_traverse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Discover relationship paths from an ODPG node.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("-i", "--input", required=True, type=Path, help="Path to ODPG YAML graph file")
    parser.add_argument("-o", "--output", type=Path, help="Optional JSON output file")
    parser.add_argument("--start", required=True, help="Starting node id")
    parser.add_argument("--depth", type=int, default=2, help="Maximum traversal depth")
    parser.add_argument("--relationship", help="Optional relationship type filter")
    parser.add_argument("--reverse", action="store_true", help="Traverse incoming relationships")
    return parser


def main() -> int:
    return command_traverse(build_parser().parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
