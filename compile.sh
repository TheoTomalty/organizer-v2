set -euo pipefail

rm build/*

cp organizer/static/style.css build/

npm run babel
