import pytest#type: ignore
from confirming_email import send_email
from dotenv import load_dotenv#type:ignore
import os

load_dotenv()

@pytest.mark.asyncio
async def test_send_email():
    assert type(await send_email(getter=os.getenv("SERVER_EMAIL"), salt='Unit test message')) == str
    with pytest.raises(Exception):
        await send_email(getter = 'fake_email', salt = 'This must cause Error')
    