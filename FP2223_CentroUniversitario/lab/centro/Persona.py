'''
Created on 8 nov 2022

@author: belen
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, date
from us.lsi.tools.Preconditions import check_argument
import locale
from lab.centro.Direccion import Direccion
from dateutil.relativedelta import relativedelta



locale.setlocale(locale.LC_ALL, 'es_ES')
@dataclass(frozen=True,order=True)
class Persona:
    apellidos: str
    nombre: str
    dni: str
    fecha_de_nacimiento: datetime
    telefono: str
    direccion:Direccion
    
    @staticmethod
    def of(apellidos: str, nombre: str, dni: str, fecha_de_nacimiento: datetime, telefono:str,direccion:Direccion) -> Persona:
        pass
    
    @staticmethod
    def parse(text:str, ft:str = "%Y-%m-%d %H:%M")->Persona:
        pass
    
    @staticmethod
    def parse_list(ls:list[str], ft:str = "%Y-%m-%d %H:%M")->Persona:
        pass
     
    
    @staticmethod
    def _check_dni(text:str)->bool:
        ls = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
        pn = text[0:-1]
        lt = text[-1:]
        n = int(pn) % 23
        return ls[n] == lt
        
    @property
    def edad(self)->int:
        nw:datetime = datetime.now()
        return relativedelta(nw, self.fecha_de_nacimiento).years
   
    @property
    def dia_semana_nacimiento(self)->str: 
        pass
    
    @property
    def mes_cumple(self)->str: 
        return self.fecha_de_nacimiento.strftime("%B")
    
    @property
    def siguiente_cumple(self)->date:
        pass
        
    @property
    def dia_semana_siguiente_cumple(self)->str: 
        pass
        
         
    def __str__(self)->str:
        return f'{self.nombre} {self.apellidos} de {self.edad} anyos, nacido el {self.dia_semana_nacimiento} {self.fecha_de_nacimiento.day} de {self.mes_cumple} de {self.fecha_de_nacimiento.year}'


if __name__ == '__main__':
    p:Persona = Persona.parse('Casares Amador,Ramiro,00895902Y,2003-06-14 10:02,+34721510926,Ronda de Samanta Cobos 392;Málaga;29316')


