# JUST A RECEIVER MOCK
import asyncio

import nats


async def main():
  nc = await nats.connect("nats://localhost:4222", connect_timeout=1000)

  async def request_handler(msg):
    print('[request_handler]')
    subject = msg.subject
    reply = msg.reply
    data = msg.data.decode()
    print(f"Received a message on '{subject} {reply}': {data}")
    await nc.publish(reply, b'I can help')

  sub = await nc.subscribe("qparking-device-commands")

  while True:
    try:
      msg = await sub.next_msg()
      print('Received', msg)
      await request_handler(msg)
    except Exception as e:
      print('[LOOP ERROR]', e)

if __name__ == '__main__':
    asyncio.run(main())
