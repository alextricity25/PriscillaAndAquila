#-----------------------------------------------------------------------------
#
# Name: release_alpha_minor
# Description:
# Creates an alpha minor release for the PriscillaAndAquila project by:
# 1. Updating setup.py with the next minor number
# 2. Rebuilding wheels
# 3. Uploading package to pypi via twine
# Author: Alex Cantu
# Date: 06/10/2019
#
#
#-----------------------------------------------------------------------------

# MAIN -----------------------------------------------------------------------

## Obtaining next version
CURRENT_VERSION=`cat setup.py | grep -E 'a[0-9]+' -o | head -n1 | sed 's/a//g'`
NEXT_VERSION=$(( CURRENT_VERSION + 1 ))
echo "Next version is: ${NEXT_VERSION}"

if ! [[ -f setup.py ]]; then 
    exit
fi
# Update version number in setup.py
sed "s/a[0-9][0-9]/a${NEXT_VERSION}/g" setup.py -i

# Remove build and dist directories

rm -rf build/
rm -rf dist/

# Build new wheel
python setup.py bdist_wheel

# Making git tag
git add setup.py
git commit -m "Prepare setup,py for Alpha Release ${NEXT_VERSION}"
git push
git tag 0.0.1a${NEXT_VERSION} -m "Alpha Release ${NEXT_VERSION}"
git push --tags

# Upload to PyPI
twine upload dist/*
