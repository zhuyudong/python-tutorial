try:
    ...
except Exception as e:
    # NOTE: 会捕获除 SystemExit, KeyboardInterrupt 和 GeneratorExit 之外的所有异常
    ...
    print(e)

try:
    ...
except BaseException as e:
    # NOTE: 会捕获所有异常
    ...
    print(e)