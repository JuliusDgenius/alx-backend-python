#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that
waits for a random delay between 0 and max_delay (included and float value)
seconds and eventually returns it.
"""
from random import uniform
import asyncio


async def wait_random(max_delay=10):
    rand_delay = uniform(0, max_delay)
    await asyncio.sleep(rand_delay)

    return rand_delay