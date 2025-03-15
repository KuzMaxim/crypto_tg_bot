import pytest#type: ignore
from coinmarketcap import CoinMarketAPI



@pytest.fixture
def API():
    return CoinMarketAPI()
    
@pytest.mark.asyncio
async def test_get_coin(API):
    assert type(await API.get_coin('eth')) == str, "basic check with eth"
    with pytest.raises(KeyError):
        await API.get_coin('invalid_ticker')
        
@pytest.mark.asyncio
async def test_get_top_coins(API):
    assert type(await API.get_top_coins()) == list, "basic check type"
    assert len(await API.get_top_coins()) == 100, "basic check length"
    with pytest.raises(TypeError):
        await API.get_top_coins('ticker')

def test_get_top_coins_synch(API):
    assert type(API.get_top_coins_synch()) == dict, "basic check type"
    assert len(API.get_top_coins_synch()) == 100, "basic check length"
    with pytest.raises(Exception):
        API.get_top_coins('ticker')
        