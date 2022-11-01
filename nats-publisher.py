# JUST A PUBLISHER MOCK
import asyncio
import json

import nats


async def main():
  try:
    nc = await nats.connect("tls://localhost:4222")
    while True:
      if input()=='k':
        try: 
          ans = await nc.request("hello", json.dumps({'dev_id': 502, 'command': 117}, indent=0).encode('utf-8'))
          print(ans)
        except Exception as e:
          print(f'[ERROR on request] {e}')
      if input()=='q':
        break;
    await nc.drain()
  except Exception as e:
    print(f'[ERROR] {e}')

if __name__ == '__main__':
    asyncio.run(main())
