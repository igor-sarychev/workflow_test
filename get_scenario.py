#!/usr/bin/env python3

import argparse
import json
import logging
from pathlib import Path
from typing import Optional


def parse_args() -> argparse.Namespace:
    args = argparse.ArgumentParser()

    args.add_argument("-f", "--file", required=True, help="JSON file with scenario IDs")
    args.add_argument("-e", "--env", required=True, help="Environment name")

    return args.parse_args()


def scenario_ids(content: dict, environ: str, separator=",") -> Optional[str]:
    ids = content.get(environ, "")

    if not ids:
        return None

    return separator.join(ids)


def main() -> None:
    args = parse_args()

    content = json.loads(Path(args.file).read_text())

    print(scenario_ids(content=content, environ=args.env))


if __name__ == "__main__":
    main()
