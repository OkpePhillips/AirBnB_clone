#!/usr/bin/env bash
#Script to generate list of contributors to the repository.


set -e

cat > "AUTHORS" <<- EOF

	$(git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf)
EOF
