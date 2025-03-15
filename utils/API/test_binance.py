import pytest#type: ignore
from binance import BinanceAPI



@pytest.fixture
def API():
    return BinanceAPI()
    
@pytest.mark.asyncio
async def test_get_coin(API):
    assert type(await API.get_coin('eth')) == str, "basic check with eth"
    with pytest.raises(KeyError):
        await API.get_coin('52')
