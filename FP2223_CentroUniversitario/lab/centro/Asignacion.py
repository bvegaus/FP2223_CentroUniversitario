'''
Created on 11 nov 2022

@author: belen
'''
from __future__ import annotations
from dataclasses import dataclass
    
@dataclass(frozen=True)
class Asignacion:
    dni:str
    ida:int
    idg:int
    
    @staticmethod
    def of(dni:str,ida:int,idg:int)->Asignacion:
        return Asignacion(dni,ida,idg)
    
    @staticmethod
    def parse(text:str)->Asignacion:
        pass
    
    def __str__(self)->str:
        return f'{self.dni},{self.ida},{self.idg}'