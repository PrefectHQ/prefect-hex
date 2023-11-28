"""Credential classes used to perform authenticated interactions with Hex"""

from httpx import AsyncClient
from prefect.blocks.core import Block
from pydantic import VERSION as PYDANTIC_VERSION

if PYDANTIC_VERSION.startswith("2."):
    from pydantic.v1 import Field, SecretStr
else:
    from pydantic import Field, SecretStr


class HexCredentials(Block):
    """
    Block used to manage Hex authentication.

    Attributes:
        domain: Domain to make API requests against.
        token: The token to authenticate with Hex.


    Examples:
        Load stored Hex credentials:
        ```python
        from prefect_hex import HexCredentials

        hex_credentials_block = HexCredentials.load("BLOCK_NAME")
        ```
    """

    _block_type_name = "Hex Credentials"
    _logo_url = "https://cdn.sanity.io/images/3ugk85nk/production/59acfd21aae4732c0046a18e44da08db78822baf-250x250.png"  # noqa
    _documentation_url = "https://prefecthq.github.io/prefect-hex/credentials/#prefect_hex.credentials.HexCredentials"  # noqa

    domain: str = Field(
        default="app.hex.tech", description="Domain to make API requests against."
    )
    token: SecretStr = Field(default=..., description="Token used for authentication.")

    def get_client(self) -> AsyncClient:
        """
        Gets a Hex REST AsyncClient.

        Returns:
            A Hex REST AsyncClient.

        Example:
            Gets a Hex REST AsyncClient.
            ```python
            from prefect import flow
            from prefect_hex import HexCredentials

            @flow
            def example_get_client_flow():
                token = "consumer_key"
                hex_credentials = HexCredentials(token=token)
                client = hex_credentials.get_client()
                return client

            example_get_client_flow()
            ```
        """
        client_kwargs = {
            "base_url": f"https://{self.domain}/api/v1",
            "headers": {"Authorization": f"Bearer {self.token.get_secret_value()}"},
        }
        client = AsyncClient(**client_kwargs)
        return client
