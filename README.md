# license-updater

## Using `update-license.py`

The Python script can be used to update the Apache license headers in a given directory. If a source file does not have a header, it will add one. 

To use:
```
python update-license.py -d [source directory] -f [text file of license header] --ftype [list of file types]
```

For example:
```
python update-license.py -d ref-wem-firmware/ -f c_header_license.txt --ftype .c .h .cpp
```
This command will update the source files in the directory `ref-wem-firmware`. It will apply the header in [c_header_license.txt](https://github.com/sarahmarshy/license-updater/blob/master/c_header_license.txt) to all files with endings `.c`, `.cpp`, `.h` that are missing a license. If a license is present in the source file, it will update the date to 2018. 
