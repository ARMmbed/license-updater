#!/bin/sh

update_license()
{
    dir=$1
    fork_remote="https://github.com/$2/$1"
    echo "Cloning $fork_remote"
    git clone $fork_remote
    python update-license.py -d $dir -f c_header_license.txt --ftype .c .h .cpp .js 
    python update-license.py -d $dir -f python_header_license.txt --ftype .py
    cd $dir
    cat ../LICENSE > LICENSE
    git checkout -b 'license-test'
    git add -A 
    git commit -m "Add Apache licenses"
    git push origin -u license-test
    cd ..
}

while read p; do
    update_license $p $2
done < $1

