import asyncio
import random


class Philosopher:
    def __init__(self, name, left_fork, right_fork):
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    async def eat(self):
        async with self.left_fork:
            async with self.right_fork:
                print(f"{self.name} is eating.")
                await asyncio.sleep(random.uniform(1, 2))

    async def think(self):
        print(f"{self.name} is thinking.")
        await asyncio.sleep(random.uniform(1, 2))

    async def run(self):
        while True:
            await self.think()
            await self.eat()


async def main():
    forks = [asyncio.Lock() for _ in range(5)]

    philosophers = [
        Philosopher("Philosopher 1", forks[0], forks[1]),
        Philosopher("Philosopher 2", forks[1], forks[2]),
        Philosopher("Philosopher 3", forks[2], forks[3]),
        Philosopher("Philosopher 4", forks[3], forks[4]),
        Philosopher("Philosopher 5", forks[4], forks[0])
    ]

    tasks = [asyncio.create_task(philosopher.run()) for philosopher in philosophers]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
