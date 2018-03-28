#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


celery -A pt.taskapp worker -l INFO
