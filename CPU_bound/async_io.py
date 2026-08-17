import time
from typing import Tuple, Sequence
import asyncio

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

async def async_factorize_single(number: int) -> TupleIntDivisors:
    return tuple(x for x in range(1, number + 1) if number % x == 0)


async def async_factorize_single_print(index: int, number: int) -> None:
    print(f"start task {index}")
    dividers = await async_factorize_single(number)
    print(f"result of task {index}: factorize single({number} = {dividers})")
    print("-" * 100)


async def main_async(in_numbers: SequenceInt = numbers) -> None:
    async with asyncio.TaskGroup() as tg:
        [
            tg.create_task(async_factorize_single_print(index, number))
            for index, number in enumerate(in_numbers)
        ]
    

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main_async(numbers))
    async_duration = time.perf_counter() - start
    print(async_duration)


# Não deixa mais eficiente!! O gargalo é o calculo em si. No io bound ele aproveita o periodo que o processador nao tem nada pra fazer pra continuar executando tasks. Aqui o processador sempre tem algo pra fazer