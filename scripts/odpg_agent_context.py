import argparse
from pathlib import Path

from odpg_toolkit_core import command_agent_context


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Extract trusted ODPG graph context around a focus node for AI-agent use.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("-i", "--input", required=True, type=Path, help="Path to ODPG YAML graph file")
    parser.add_argument("-o", "--output", type=Path, help="Optional JSON output file")
    parser.add_argument("--node", required=True, help="Focus node id")
    parser.add_argument("--depth", type=int, default=2, help="Context traversal depth")
    return parser


def main() -> int:
    return command_agent_context(build_parser().parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
