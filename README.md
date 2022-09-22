# prefect-hex

<a href="https://pypi.python.org/pypi/prefect-hex/" alt="PyPI Version">
    <img src="https://badge.fury.io/py/prefect-hex.svg" /></a>
<a href="https://github.com/PrefectHQ/prefect-hex/" alt="Stars">
    <img src="https://img.shields.io/github/stars/PrefectHQ/prefect-hex" /></a>
<a href="https://pepy.tech/badge/prefect-hex/" alt="Downloads">
    <img src="https://pepy.tech/badge/prefect-hex" /></a>
<a href="https://github.com/PrefectHQ/prefect-hex/pulse" alt="Activity">
    <img src="https://img.shields.io/github/commit-activity/m/PrefectHQ/prefect-hex" /></a>
<a href="https://github.com/PrefectHQ/prefect-hex/graphs/contributors" alt="Contributors">
    <img src="https://img.shields.io/github/contributors/PrefectHQ/prefect-hex" /></a>
<br>
<a href="https://prefect-community.slack.com" alt="Slack">
    <img src="https://img.shields.io/badge/slack-join_community-red.svg?logo=slack" /></a>
<a href="https://discourse.prefect.io/" alt="Discourse">
    <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?logo=discourse" /></a>

## Welcome!

Prefect integrations for interacting with Hex.

The tasks within this collection were created by a code generator using the service's OpenAPI spec.

The service's REST API documentation can be found [here](replace_this_with_link_to_api_docs).

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-hex` with `pip`:

```bash
pip install prefect-hex
```

### Write and run a flow

```python
from prefect import flow
from prefect_hex.tasks import (
    goodbye_prefect_hex,
    hello_prefect_hex,
)


@flow
def example_flow():
    hello_prefect_hex
    goodbye_prefect_hex

example_flow()
```

## Resources

If you encounter any bugs while using `prefect-hex`, feel free to open an issue in the [prefect-hex](https://github.com/PrefectHQ/prefect-hex) repository.

If you have any questions or issues while using `prefect-hex`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-hex` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-hex.git

cd prefect-hex/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
