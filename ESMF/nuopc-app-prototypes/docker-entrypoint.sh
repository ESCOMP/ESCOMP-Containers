#!/usr/bin/env bash
set -Eeuxo pipefail

case "${1}" in

  testProtos)
    # Catch || to true require to allow scripts to continue? Seems like a hack
    # and it is, but is required given testing.
    ./testProtos.sh 2>&1 | tee "${ESMF_ARTIFACTS}"/testProtos.out || true
  ;;

  meta_test)
    python /opt/meta_test.py -v 2>&1 | tee "${ESMF_ARTIFACTS}"/meta_test.out
  ;;

  prep_artifacts)
    cd "${ESMF_ARTIFACTS}"/.. && zip -rv artifacts.zip artifacts
  ;;

  *)
    echo "ERROR: Command not found"; exit 1
  ;;

esac
