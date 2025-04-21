# file name: genre.py
#author: Leo Sanders
# date: 4/21/2025
#Description: This file is used to contain the details of the genres such as the names and refrences to the samples.


from typing import List


class Genre():
    def __init__(self, name: str, samples: List):
        self.name = name
        self.samples = samples