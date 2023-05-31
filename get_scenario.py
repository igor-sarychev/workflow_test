#!/usr/bin/env python3
# some additional comment

"""
This script prints a comma separated string of scenario ids for given environment, and failed if environment does not
defined or scenario ids list is empty
"""

import argparse
import json
import sys
from pathlib import Path


def main() -> None:
    pars = argparse.ArgumentParser()

    pars.add_argument("-f", "--file", required=True, help="JSON file with scenario IDs")
    pars.add_argument("-e", "--env", required=True, help="Environment name")

    args = pars.parse_args()

    file_content = json.loads(Path(args.file).read_text())

    ids = file_content.get(args.env, "")

    if not ids:
        sys.exit(1)

    print(",".join(ids))


if __name__ == "__main__":
    main()
