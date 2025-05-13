import multiprocessing

print(multiprocessing.cpu_count())


def worker(num):
    print(f'Worker: {num} is working')


processes = []

if __name__ == '__main__':
    for proc_number in range(5):
        process = multiprocessing.Process(target=worker, args=(proc_number,))
        processes.append(process)
        process.start()

    for p in processes:
        p.join()
