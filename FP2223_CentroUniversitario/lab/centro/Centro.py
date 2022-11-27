'''
Created on 22 nov 2022

@author: belen
'''
from __future__ import annotations
from lab.centro.Alumno import Alumno
from lab.centro.Profesor import Profesor
from lab.centro.Asignatura import Asignatura
from lab.centro.Matricula import Matricula
from lab.centro.Asignacion import Asignacion
from typing import Iterable
from us.lsi.tools.File import absolute_path, lineas_de_fichero
from us.lsi.tools.Iterable import strfiter

class Centro:
    
    centro = None

    def __init__(self, alumnos:list[Alumno], profesores:list[Profesor],asignaturas:list[Asignatura],\
            matriculas:set[Matricula], \
            asignacion_de_profesores:set[Asignacion])->None:
        self.alumnos = alumnos
        self.profesores = profesores
        self.asignaturas = asignaturas
        self.matriculas = matriculas
        self.asignacion_de_profesores = asignacion_de_profesores 
        
        self.alumnos_dni:dict[str,Alumno] = pass
        self.profesores_dni:dict[str,Profesor] = pass
        

    @staticmethod
    def of()->Centro:
        if Centro.centro is None:
            Centro.centro = Centro.of_files()
        return Centro.centro

        
    @staticmethod
    def of_files(fichero_alumnos:str=absolute_path('/ficheros/alumnos.txt'),
           fichero_profesores:str=absolute_path('/ficheros/profesores.txt'),
           fichero_asignaturas:str=absolute_path('/ficheros/asignaturas.txt'))->Centro:
        pass
    
    def add_asignaciones(self,fichero:str=absolute_path('/ficheros/asignaciones.txt'))->None:
        pass
               
    def add_asignacion(self,profesor:Profesor,asignatura:Asignatura,grupo:int)->None:
        self.asignacion_de_profesores.add(Asignacion.of(profesor.dni,asignatura.id,grupo))      
    
    def add_matriculas(self,fichero:str=absolute_path('/ficheros/matriculas.txt'))->None:
        pass
            
    def add_matricula(self,alumno:Alumno,asignatura:Asignatura,grupo:int)->None:
        self.matriculas.add(Matricula.of(alumno.dni,asignatura.id,grupo))
    
    @property
    def numero_profesores(self)->int: 
        return len(self.profesores)
    
    @property
    def numero_alumnos(self)->int: 
        return len(self.alumnos)
    
    @property
    def numero_asignaturas(self)->int: 
        return len(self.asignaturas)
    
    @property
    def numero_grupos(self)->int: 
        pass
    
    def profesor(self,i:int)->Profesor: 
        return self.profesores[i]
    
    def profesor_de_dni(self,dni:str)->Profesor: 
        pass
    
    def alumno_de_dni(self,dni:str)->Alumno: 
        pass
    
    def asignatura(self,i:int)->Asignatura: 
        return self.asignaturas[i]
    
    def alumno(self,i:int)->Alumno: 
        return self.alumnos[i]
    
    def asignaturas_impartidas(self,profesor:Profesor)->set[Asignatura]: 
        pass
    def asignaturas_cursadas(self,alumno:Alumno)->set[Asignatura]: 
        pass

if __name__ == '__main__':
    Centro.of()
    print(f'- Hay {Centro.of().numero_alumnos} alumnos en el centro')
    