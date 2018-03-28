#!/bin/sh

update_license()
{
    remote="https://github.com/ARMmbed/$1"
    dir=$1
    fork_remote="https://github.com/$2/$1"
    echo "Cloning $remote"
    git clone $remote
    python update-license.py -d $dir -f c_header_license.txt --ftype .c .h .cpp .js 
    python update-license.py -d $dir -f python_header_license.txt --ftype .py
    cd $dir
    cat ../LICENSE > LICENSE
    git remote add my_fork $fork_remote
    git checkout -b 'license-test'
    git add -A 
    git commit -m "Add Apache licenses"
    git push my_fork -u license-test
    cd ..
}

while read p; do
    update_license $p $2
done < $1

