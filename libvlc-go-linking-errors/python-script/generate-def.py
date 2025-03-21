#!/usr/bin/env python3
import re
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_def.py <input_exports.txt> <output.def>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    library_name = "libvlccore.dll"
    with open(input_file, "r", encoding="utf-8") as fin:
        content = fin.read()
    #     ordinal hint RVA      name
    pattern = r'^\s*\d+\s+[\dA-Za-z]+\s+[0-9A-Fa-f]+\s+(\S+)'
    symbols = re.findall(pattern, content, re.MULTILINE)
    if not symbols:
        print("No symbols found. Check the format of your input file.")
        sys.exit(1)
    with open(output_file, "w", encoding="utf-8") as fout:
        fout.write(f'LIBRARY "{library_name}"\n')
        fout.write("EXPORTS\n")
        for sym in symbols:
            fout.write(f"    {sym}\n")
    print(f"DEF file generated with {len(symbols)} symbols and written to {output_file}")
if __name__ == "__main__":
    main()
