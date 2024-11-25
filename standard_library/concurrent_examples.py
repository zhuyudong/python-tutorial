"""
https://www.packetswitch.co.uk/what-is-concurrent-futures-and-how-can-it-boost-your-python-performance/
"""

import concurrent.futures
import random
import time


def mail_letter(letter: str):
    duration = random.randint(1, 2)
    print(f"Started mailing letter {letter} (duration: {duration}s)")
    time.sleep(duration)
    print(f"Finished mailing letter {letter}")
    return f"Letter {letter} mailed"


if __name__ == "__main__":
    letters = ["A", "B", "C"]
    results = []

    # NOTE: version 1
    # for letter in letters:
    #     results.append(mail_letter(letter))

    # print("Mailing results:")
    # for result in results:
    #     print(result)
    """
    Started mailing letter A (duration: 2s)
    Finished mailing letter A
    Started mailing letter B (duration: 2s)
    Finished mailing letter B
    Started mailing letter C (duration: 2s)
    Finished mailing letter C
    Mailing results:
    Letter A mailed
    Letter B mailed
    Letter C mailed
    """

    # NOTE: version 2
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     results = executor.map(mail_letter, letters)

    # print("Mailing results:")
    # for result in results:
    #     print(result)
    """
    # NOTE: 同时开始执行 mail_letter 函数
    Started mailing letter A (duration: 2s)
    Started mailing letter B (duration: 1s)
    Started mailing letter C (duration: 1s)
    Finished mailing letter B
    Finished mailing letter C
    Finished mailing letter A
    Mailing results:
    Letter A mailed
    Letter B mailed
    Letter C mailed
    """

    # NOTE: version 3
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(mail_letter, letter): letter for letter in letters}

        for future in concurrent.futures.as_completed(futures):
            letter = futures[future]
            try:
                result = future.result()
            except Exception as e:
                print(f"Letter {letter} failed: {e}")
            else:
                print(f"Results: {result}")
    """
    # NOTE: 同时开始执行 mail_letter 函数
    Started mailing letter A (duration: 1s)
    Started mailing letter B (duration: 1s)
    Started mailing letter C (duration: 1s)
    Finished mailing letter A
    Results: Letter A mailed
    Finished mailing letter B
    Results: Letter B mailed
    Finished mailing letter C
    Results: Letter C mailed
    """
