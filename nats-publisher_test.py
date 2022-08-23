# JUST A PUBLISHER MOCK
import asyncio
import json

import nats


async def main():
  try:
    nc = await nats.connect("nats://localhost:4222", connect_timeout=1000)
    ans = await nc.request("qparking-device-commands", json.dumps({'dev_id': 502, 'command': 117}, indent=2).encode('utf-8'))
    print(ans)
    await nc.drain()
  except Exception as e:
    print(f'[ERROR] {e}')

if __name__ == '__main__':
    asyncio.run(main())
