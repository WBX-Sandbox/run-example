# WBX Sandbox Run – example

This repository runs its tests in an isolated [WBX Sandbox](https://sandbox.wbx.cz) microVM using the [WBX Sandbox Run](https://github.com/marketplace/actions/wbx-sandbox-run) GitHub Action – see [`.github/workflows/tests.yml`](.github/workflows/tests.yml).

Each push downloads the repository at that commit into a fresh sandbox, installs `pytest` (network limited to PyPI), runs the tests with a price limit and uploads `report.xml` and the signed execution receipt as workflow artifacts.

To use it in your repository, add an API key as the secret `WBXSANDBOX_API_KEY` and copy the workflow.
