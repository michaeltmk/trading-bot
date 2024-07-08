from trading_bot.bot import signal_generator
# from apscheduler import AsyncScheduler # for apscheduler 4
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pytest
import asyncio

@pytest.fixture
def anyio_backend():
    return 'asyncio'

async def _test_bot():
    signal_generator_1 = signal_generator()
    signal_generator_1.append('ma_in_sequence')
    signal_generator_1.append('trailing_stop_orders')

    async with AsyncScheduler() as scheduler:
        scheduler_1 = scheduler()
        scheduler_1.append(60, signal_generator_1)
        scheduler_1.run()

async def test_main2(anyio_backend):
    signal_generator_1 = signal_generator()
    signal_generator_1.append('ma_in_sequence')
    signal_generator_1.append('trailing_stop_orders')

    scheduler = AsyncIOScheduler()
    scheduler.add_job(signal_generator_1.run, 'interval', seconds=3)
    scheduler.start()
    while True:
        await asyncio.sleep(1000)

    asyncio.run(bot_1())