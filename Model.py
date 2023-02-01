import os
import random


class Model:

    def __init__(self):
        self.databases_name = "TAK22_Names.txt"
        self.tasks = random.choice(os.listdir("databases"))
        pass
