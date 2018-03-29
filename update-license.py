import os
import re
import sys
import argparse

CURRENT_YEAR = 2018

def rewrite_file(f, txt, shebang_line = None):
    f.seek(0)
    if shebang_line:
        f.write(shebang_line)
    f.write(txt)
    f.truncate()
    f.close()


def update_licenses(target_dir, file_exts, new_license):
    for root, dirs, files in os.walk(target_dir):
        for f in files:
            # Get the file extension
            ext = os.path.splitext(f)[1]
            # Check if extension is in list of target extensions
            if(ext in file_exts):
                fname = os.path.join(root, f)
                # Open the file
                with open(fname, 'r+') as of:
                    first_line = of.readline()
                    shebang_line = first_line if first_line.startswith('#!') else None
                    txt = of.read()
                    # Check if there is no license
                    if('Apache' not in txt):
                        # Format file with license header
                        txt = '%s\n\n%s'%(new_license, txt) 
                        # Rewrite the file
                        rewrite_file(of, txt, shebang_line)
                    else:
                        # Search for copyright date
                        m = re.search('Copyright.*?[0-9,-]*?(?P<end>\d+)\s', txt)
                        if(m):
                            # Check if the license is out of date
                            end_date = int(m.group('end'))
                            if(end_date < CURRENT_YEAR):
                                end_index = m.end('end')
                                start_index = m.start('end') if end_date == CURRENT_YEAR - 1 else end_index
                                replacement_txt = ',2018' if start_index == end_index else '2018'
                                # Format the file with updated license header
                                txt = '%s%s%s'%(txt[:start_index],replacement_txt, txt[end_index:])
                                # Rewrite the file
                                rewrite_file(of, txt, first_line)

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update Apache licenses')
    parser.add_argument('--ftypes', dest='ftypes',  nargs='+', default = ['.c', '.cpp', '.h'],
                    help='a list of filetypes')
    parser.add_argument('-d', dest='target_dir', default = '.',
                    help='source directory')
    parser.add_argument('-f', dest='header_file', default = 'c_header_license.txt',
                    help='text file with new header text')
    args = parser.parse_args()
    ftypes = args.ftypes
    header_text_file = args.header_file
    target_dir = args.target_dir
    with open(header_text_file, 'r') as f:
        update_licenses(target_dir, ftypes, f.read())
