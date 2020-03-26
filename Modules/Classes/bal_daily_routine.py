class BALDailyRoutine :

    def __init__(self) :
        
        self.__lifting_set_list = []
        self.__day = None
        self.__assistance_exercises = {}
    

    @property
    def lifting_set_list(self) :
        return self.__lifting_set_list

    @lifting_set_list.setter
    def lifting_set_list(self, ls_list) :
        self.__lifting_set_list = ls_list
    
    @property
    def day(self) :
        return self.__day
    
    @day.setter
    def day(self, day) :
        self.__day = day

    @property
    def assistance_exercises(self) :
        return self.__assistance_exercises
    
    @assistance_exercises.setter
    def assistance_exercises(self, dict) :
        self.__assistance_exercises = dict