# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss.
# Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class
# to workers list directly via access to attribute, use getters and setters instead!


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.__workers = []

    @property
    def worker(self):
        return self.__workers

    @worker.setter
    def worker(self, worker_):
        self.__workers.append(worker_)

    def __repr__(self):
        return f'{self.name}({self.company})'

    def __str__(self):
        return f'{self.name}({self.company}):\nWorkers: {self.worker}\n'


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = Worker.check_boss_type(boss)

    @staticmethod
    def check_boss_type(boss):
        if type(boss) == Boss:
            return boss
        else:
            raise ValueError('boss must be type Boss class')

    def __repr__(self):
        return Worker.__str__(self)

    def __str__(self):
        return f'{self.name}({self.boss.__repr__()})'


boss_1 = Boss(1, 'Boss_1', 'Company_1')

worker_1 = Worker(1, 'Worker_1', 'Company_1', boss_1)
worker_2 = Worker(2, 'Worker_2', 'Company_1', boss_1)
worker_3 = Worker(3, 'Worker_3', 'Company_1', boss_1)

boss_1.worker = worker_1
boss_1.worker = worker_2
boss_1.worker = worker_3

print(boss_1)


boss_2 = Boss(2, 'Boss_2', 'Company_2')

worker_4 = Worker(4, 'Worker_4', 'Company_2', boss_2)
worker_5 = Worker(5, 'Worker_5', 'Company_2', boss_2)
worker_6 = Worker(6, 'Worker_6', 'Company_2', boss_2)

boss_2.worker = worker_4
boss_2.worker = worker_5
boss_2.worker = worker_6

print(boss_2)

