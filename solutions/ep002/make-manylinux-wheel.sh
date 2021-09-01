#!/usr/bin/env bash
set -euxo pipefail

podman run --rm -ti \
    -v "$PWD:/src:ro" \
    -v "$PWD/dist:/dist:rw" \
    quay.io/pypa/manylinux2014_x86_64 \
    bash -c '\
/opt/python/cp36-cp36m/bin/python -m pip wheel /src -w /tmp && \
auditwheel repair /tmp/*.whl -w /dist \
'
