import asyncio


async def start_strongman(name: str, power: float) -> None:
    print(f"силач {name} начал соревнования!")
    for i in range(5):
        await asyncio.sleep(power)
        print(f"силач {name} поднял {i}-й шар!")
    print(f"силач {name} всё !")


async def start_tournament(*args) -> None:
    if len(args) % 2 != 0 or len(args) == 0:
        raise Exception("аргументы должно быть в формате (name, power, name, power, ...)")
    N = len(args) // 2  # к-во силачей
    tasks = []
    for k in range(N):
        tasks.append(asyncio.create_task(start_strongman(args[2 * k], args[2 * k + 1])))
    for t in tasks:
        await t
    # TaskGroup круче!


asyncio.run(start_tournament('Petya', 2, 'Vasya', 3, 'Kolya', 4))
