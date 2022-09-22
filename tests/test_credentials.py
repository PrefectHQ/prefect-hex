from httpx import AsyncClient

from prefect_hex import HexCredentials


def test_hex_credentials_get_client():
    client = HexCredentials(hex_tenant="hex_tenant", token="token_value").get_client()
    assert isinstance(client, AsyncClient)
    assert client.headers["authorization"] == "Bearer token_value"
