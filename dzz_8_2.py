from datetime import datetime, timezone
def logger(fn):
    def inner(*args, **kwargs):
        called_at = datetime.now(timezone.utc)
        to_execute = fn(*args, **kwargs)
        print('{0} executed. Logged at {1}'.format(fn.__name__, called_at))
        return to_execute

    return inner

@logger
def function_1():
    pass

@logger
def function_2():
    pass

@logger
def function_3():
    pass

@logger
def function_4():
    pass

function_1()
function_4()
function_2()
function_3()
function_1()
function_4()