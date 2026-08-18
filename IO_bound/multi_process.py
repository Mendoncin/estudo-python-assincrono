import time
import httpx
import multiprocessing

from typing import Tuple


Urls = Tuple[str, ...]

urls = ("https://www.google.com",) * 50


def send_request(count: int, url: str):
    print(f"sending request #{count}")
    response = httpx.get(url)
    print(
        f"got response for request {count}, "
        f"status code: {response.status_code}"
    )


def main_process(in_urls: Urls = urls):
    tasks = []

    for num, url in enumerate(in_urls):
        tasks.append(
            multiprocessing.Process(
                target=send_request,
                args=(num, url),
            )
        )
        tasks[-1].start()

    for task in tasks:
        task.join()


if __name__ == "__main__":
    start = time.perf_counter()

    main_process(urls)

    process_duration = time.perf_counter() - start
    print(process_duration)



# Nãoo usa Client pq são processos diferentes, não compartilha objetos em comum. Rápido, mas mais lento que o threads. Para uso comum é pior que o de multithreading pois é muito mais caro, utiliza mais nucleos e nao aumenta eficiencia. Separando um nucleo pra fazer uma tarefa muito simples.
