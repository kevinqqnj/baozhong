#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A pt.taskapp worker -l INFO
