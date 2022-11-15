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

Hex is a powerful platform for collaborative data science and analytics. For information getting started with Hex, check out Hex's [quickstart guide](https://learn.hex.tech/quickstart).

The tasks within this collection were created by a code generator using Hex's OpenAPI spec.

Hex's REST API documentation can be found [here](https://learn.hex.tech/docs/develop-logic/hex-api/api-reference).

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

### Gather and store authentication

1. Create new token on app.hex.tech Settings page:

![image](https://user-images.githubusercontent.com/15331990/201996947-07765380-50c4-4c61-9044-bd93e4b8efc7.png)

2. Store token on https://app.prefect.cloud/ Blocks page:

![image](https://user-images.githubusercontent.com/15331990/201997292-b3a18254-229f-4689-aaec-07a990cdaf87.png)

3. Copy project ID from browser URL:

![image](https://user-images.githubusercontent.com/15331990/201998085-4c2c43ba-f180-41ec-a322-07be268021de.png)

### Write and run a flow

```python
from prefect import flow
from prefect_hex import HexCredentials

from prefect_hex.project import get_project_runs

@flow
def get_project_runs_flow():
    hex_credentials = HexCredentials.load("hex-token")
    project_runs = get_project_runs(
        project_id='5a8591dd-4039-49df-9202-96385ba3eff8',
        hex_credentials=hex_credentials
    )
    return project_runs

get_project_runs_flow()
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
