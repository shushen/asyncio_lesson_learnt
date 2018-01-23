# asyncio lessons learnt

This is the demo code repository for [`asyncio lessions
learnt`](http://bit.ly/2Du4Iyw) presentation.

# threads.py

This is threading-based code showing a scenario of two threads, one of which
sets a `done` flag to trigger the other to exit from a while loop.

# coroutines_aha.py

This is asyncio-based code with two coroutines, implementing a similar scenario
as `threads.py` but using asyncio coroutines. This code shows a direct
translation of the threading pattern may not work as expected and the coroutine
with `while` loop never yields and runs forever and the coroutine to set the
done flag never gets run.

# coroutines.py

This is the asyncio-based code that yield properly in the `while` loop to allow
the other coroutine to run and set the `done` flag.

