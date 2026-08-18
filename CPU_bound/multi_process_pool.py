import time
from typing import Tuple, Sequence
import multiprocessing
from concurrent.futures import ProcessPoolExecutor, wait

SequenceInt = Sequence[int]
TupleIntDivisors = Tuple[int]

numbers = (
    1_248_376,
    3_517_920,
    7_264_815,
    9_831_442,
    12_458_760,
    18_327_645,
    21_764_832,
    27_915_360,
)

def factorize_single(number: int) -> TupleIntDivisors:
    return tuple(x for x in range(1, number + 1) if number % x == 0)


def factorize_single_print(index: int, number: int) -> None:
    print(f"start task {index}")
    dividers = factorize_single(number)
    print(f"result of task {index}: factorize single({number} = {dividers})")
    print("-" * 100)


def main_multiprocessing(in_numbers: SequenceInt = numbers) -> None:
    futures = []

    with ProcessPoolExecutor(multiprocessing.cpu_count() - 1) as executor:
        for index, number in enumerate(in_numbers):
            futures.append(
                executor.submit(
                    factorize_single_print,
                    index,
                    number
                    )
                )

    wait(futures)



if __name__ == "__main__":
    start = time.perf_counter()
    main_multiprocessing()
    process_duration = time.perf_counter() - start
    print(process_duration)

