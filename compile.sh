#!/usr/bin/env bash

echo ">>> Initializing submodules"
git submodule init
git submodule update

# compile gbbs
echo ">>> Building gbbs pybindings"
cd gbbs
git submodule init
git submodule update
bazel build //pybindings:gbbs_lib.so
cd ..

# compile pargeo
echo ">>> Building pargeo pybindings"
cd pargeo
git submodule init
git submodule update
mkdir build
cd build
cmake ..
cd pybindings
make
cd ../../..

# create symbolic links for pybinding libraries
echo ">>> Creating symbolic links"
cd pybindings
ln -s ../gbbs/bazel-bin/pybindings/*.so .
ln -s ../gbbs/gbbs.py .
ln -s ../pargeo/build/pybindings/*.so .
