import asyncio


class MyAsyncioTask(object):
    done = False
    loop = asyncio.get_event_loop()

    async def shutdown(self):
        print('shutdown is called')
        self.done = True

    @staticmethod
    async def do_something():
        print('do something')

    async def wait_on_done(self):
        while not self.done:
            await self.do_something()
            print('waiting')

    def run(self):
        tasks = [
            self.loop.create_task(self.wait_on_done()),
            self.loop.create_task(self.shutdown()),
        ]
        self.loop.run_until_complete(asyncio.gather(*tasks))


task = MyAsyncioTask()
task.run()
