import pytest#type: ignore
from poloniex import PoloniexAPI



@pytest.fixture
def API():
    return PoloniexAPI()
    
@pytest.mark.asyncio
async def test_get_coin(API):
    assert type(await API.get_coin('eth')) == str, "basic check with eth"
    with pytest.raises(KeyError):
        await API.get_coin('invalid_ticker')
