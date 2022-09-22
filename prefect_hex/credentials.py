"""Credential classes used to perform authenticated interactions with Hex"""

from typing import Any, Dict, Optional

from httpx import AsyncClient
from prefect.blocks.core import Block
from pydantic import SecretStr


class HexCredentials(Block):
    """
    Block used to manage Hex authentication.

    Attributes:
        hex_tenant:
            Hex tenant used in formatting the endpoint URL.
        token: The token to authenticate with Hex.


    Examples:
        Load stored Hex credentials:
        ```python
        from prefect_hex import HexCredentials
        hex_credentials_block = HexCredentials.load("BLOCK_NAME")
        ```
    """

    _block_type_name = "Hex Credentials"
    # _logo_url = "<LOGO_URL_HERE>"  # noqa

    hex_tenant: str
    token: SecretStr
    client_kwargs: Optional[Dict[str, Any]] = None

    def get_client(self) -> AsyncClient:
        """
        Gets an Hex REST AsyncClient.

        Returns:
            An Hex REST AsyncClient.

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
        base_url = f"https://{self.hex_tenant}.hex.tech/api/v1"

        client_kwargs = self.client_kwargs or {}
        client_kwargs["headers"] = {
            "Authorization": f"Bearer {self.token.get_secret_value()}"
        }
        client = AsyncClient(base_url=base_url, **client_kwargs)
        return client
