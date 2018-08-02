set -euo pipefail

if [[ $ORGANIZER_DIR != $PWD ]]
then
	echo "Not executing script in proper directory: ${PWD}"
	exit 1
fi

rm -r build/
mkdir build

cp organizer/static/style.css build/

npm run webpack
npm run babel

rm -r webpack
