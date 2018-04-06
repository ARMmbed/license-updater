#!/usr/bin/env python3

import argparse
import glob

def add_license(fname, license):
    '''Add license text to file'''
    with open(fname, 'r') as f:
        original_text = f.read()
    # Check if a license already exists
    if 'copyright' in original_text.lower() or 'license' in original_text.lower():
        print("%s appears to already contains a copyright or license. Not changing." % fname)
        return
    original_lines = original_text.splitlines(True)
    # If the first line is a shebang, keep it as first line
    first_line = []
    if original_lines[0].startswith('#!'):
        first_line.append(original_lines.pop(0))
    # Write the file
    with open(fname, 'w') as f:
        f.write("".join(first_line + license + original_lines))
        print("Added license to %s" % fname)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add License Text to files')
    parser.add_argument('license_filename',
                        help='file containing license text')
    parser.add_argument('filenames', nargs='+',
                        help='filenames to add text to')
    args = parser.parse_args()
    # Read license text
    with open(args.license_filename, 'r') as f:
        license = f.readlines()
    # Add text to files
    for fname in args.filenames:
        add_license(fname, license)

