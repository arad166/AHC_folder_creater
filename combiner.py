import re
import sys
import os
from typing import Set

def read_file_content(file_name: str) -> str:
    with open(file_name, "r") as f:
        return f.read()


def make_converted_file_content(
        file_name: str,
        stack: list[str],
        added_file_names: Set[str]) -> str:
    content = read_file_content(file_name)
    content_lines = content.split("\n")
    for i in range(len(content_lines)):
        line = content_lines[i]
        match = re.match(r"^\s*#include\s+\"(.*)\"\s*$", line)
        if match:
            srcmatch = os.path.join("src", match.group(1))
            if srcmatch not in added_file_names:
                if srcmatch in stack:
                    print("Circular dependency detected: "
                          f"{' > '.join(stack + [srcmatch])}")
                    exit(1)
                stack.append(srcmatch)
                content_lines[i] = make_converted_file_content(
                    srcmatch, stack, added_file_names)
                added_file_names.add(srcmatch)
                stack.pop()
            else:
                content_lines[i] = ""
    return "\n".join(content_lines)


def main(argv: list[str]):
    if len(argv) != 3:
        print("Usage: python3 combiner.py <source_file> <output_file>")
        sys.exit(1)
    converted_main_file_content = make_converted_file_content(
        argv[1], [argv[1]], set())
    with open(argv[2], "w") as f:
        f.write(converted_main_file_content)
    print("complete")


if __name__ == "__main__":
    main(sys.argv)