from concurrent.futures import ThreadPoolExecutor


class MyTask(object):
    done = False
    executor = ThreadPoolExecutor(max_workers=2)

    def shutdown(self):
        print('shutdown is called')
        self.done = True

    @staticmethod
    def do_something():
        print('do something')

    def wait_on_done(self):
        while not self.done:
            self.do_something()
            print('waiting')

    def run(self):
        self.executor.submit(self.wait_on_done)
        self.executor.submit(self.shutdown)


task = MyTask()
task.run()
