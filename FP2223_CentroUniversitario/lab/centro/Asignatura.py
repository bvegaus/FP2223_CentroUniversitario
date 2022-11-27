'''
Created on 8 nov 2022

@author: belen
'''
from __future__ import annotations
from dataclasses import dataclass



@dataclass(frozen=True)
class Asignatura:
    id:int
    nombre:str
    creditos:int
    num_grupos:int
    
    @staticmethod
    def parse(text:str)->Asignatura:
        pass
        
    def __str__(self)->str:
        return f'{self.nombre},{self.creditos},{self.num_grupos}'


