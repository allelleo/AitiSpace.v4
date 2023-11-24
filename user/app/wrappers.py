def ignore_error(func):
    def Inner_Function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            pass

    return Inner_Function
