# license-updater

## `update-license.py`

The Python script can be used to update the Apache license headers in a given directory. If a source file does not have a header, it will add one. 

To use:
```
python update-license.py -d [source directory] -f [text file of license header] --ftype [list of file types]
```

For example:
```
python update-license.py -d ref-wem-firmware/ -f licenses/c_header_license.txt --ftype .c .h .cpp
```
This command will update the source files in the directory `ref-wem-firmware`. It will apply the header in [c_header_license.txt](https://github.com/sarahmarshy/license-updater/blob/master/licenses/c_header_license.txt) to all files with endings `.c`, `.cpp`, `.h` that are missing a license. If a license is present in the source file, it will update the date to 2018. 

## `push-updates.sh`

This shell script will clone all repos in a given text file, then it will call `update-license.py` for `c`, `cpp`, `h`, `py`, and `js` files in the cloned repos. It will also update the LICENSE file in the cloned repo. It uses the licenses [here]( https://github.com/sarahmarshy/license-updater/tree/master/licenses). 

The script takes 2 paramaters: a GitHub organization/username and a text file.  The text file will contain repo names separated by a new line. 


For example:

A text file `repos.txt` might contain:
```
ref-wem-firmware
ref-wem-webapp
```

Running the script:
`sh push-updates.sh repos.txt sarahmarshy`

This will update the following repos:
* https://github.com/sarahmarshy/ref-wem-firmware
* https://github.com/sarahmarshy/ref-wem-webapp

The script will create a commit message that says "Added Apache licenses." Then, it will push the changes to a branch called `license-test`.

