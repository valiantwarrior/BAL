from typing import *

class BALLiftingSet :
    
    def __init__(self) :
        self.__lifting_category: str = None
        self.__reps: List = []
        self.__session: Dict = {}

        for index in range(1,7) :
            self.__session.setdefault('set%s' % index)


    def init_lifting_set(self, category:str, session_list: List, reps_list: List ) :
        self.lifting_category = category
        self.reps = reps_list
        self.session = session_list
        self.__clear()

    @property
    def lifting_category(self) :
        return self.__lifting_category
    
    @lifting_category.setter
    def lifting_category(self, category: str) :
        self.__lifting_category = category

    @property
    def session(self) :
        return self.__session
    
    @session.setter
    def session(self, session_list) :
        index = 0
        for key in self.__session.keys() :
            if self.__reps[index] is None :
                break
            else : 
                self.__session[key] = session_list[index]
                index = index + 1
       
    @property
    def reps(self) :
        return self.__reps
    
    @reps.setter
    def reps(self, _reps) :
        self.__reps = _reps
        

    def __clear(self) :
        while None in self.__reps :
            self.__reps.remove(None)
        self.__session = {key: value for key, value in self.__session.items() if value != None}
