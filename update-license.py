import os
import re
import sys

new_license = """/* mbed Microcontroller Library
 * Copyright (c) 2018 ARM Limited
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */"""

file_exts = ['.h', '.c', '.cpp']

def rewrite_file(f, new_text):
    of.seek(0)
    of.write(txt)
    of.truncate()
    of.close()


if __name__ == "__main__":
    if(len(sys.argv) > 1):
        target_dir = sys.argv[1]
    else:
        target_dir = '.'
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
                            kw = 'range' if m.group('range') else 'start'
                            kw2 = 'end' if m.group('end') else 'start'
                            start_index = m.start(kw)
                            end_index = m.end(kw)
                            extra_text = m.group('range')+',' if m.group('range') else m.group('start')+','
                            # Check if the license is out of date
                            if(int(m.group(kw2)) < 2018):
                                # Format the file with updated license header
                                txt = '%s%s%s%s'%(txt[:start_index],extra_text,'2018', txt[end_index:])
                                # Rewrite the file
                                rewrite_file(of, txt)

