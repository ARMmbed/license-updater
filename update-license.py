import os
import re
import sys
import argparse

def rewrite_file(f, txt):
    f.seek(0)
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
                    txt = of.read()
                    # Check if there is no license
                    if('Apache' not in txt):
                        # Format file with license header
                        txt = '%s\n\n%s'%(new_license, txt) 
                        # Rewrite the file
                        rewrite_file(of, txt)
                    else:
                        # Search for copyright date
                        m = re.search('Copyright.*?((?P<range>(\d+)-(?P<end>\d+))|(?P<start>\d+))', txt)
                        if(m):
                            dates = 'range' if m.group('range') else 'start'
                            last_date = 'end' if m.group('end') else 'start'
                            start_index = m.start(dates)
                            end_index = m.end(dates)
                            extra_text = m.group(dates)+','
                            # Check if the license is out of date
                            if(int(m.group(last_date)) < 2018):
                                # Format the file with updated license header
                                txt = '%s%s%s%s'%(txt[:start_index],extra_text,'2018', txt[end_index:])
                                # Rewrite the file
                                rewrite_file(of, txt)

    

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
