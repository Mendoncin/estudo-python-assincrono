import time
from typing import Tuple, Sequence
import multiprocessing

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
    tasks = []
    for index, number in enumerate(in_numbers):
        tasks.append(
            multiprocessing.Process(
                target=factorize_single_print,
                args=(
                    index,
                    number
                )
            )
        )
        tasks[-1].start()

    for task in tasks:
        task.join()


if __name__ == "__main__":
    start = time.perf_counter()
    main_multiprocessing()
    process_duration = time.perf_counter() - start
    print(process_duration)

#Utiliza todos os cores do processador e consegue diminuir o tempo de execução