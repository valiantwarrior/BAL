class BALWorkoutProgram : 
    
    def __init__(self, author, num, w_unit, program_name) :
        self.__author = author
        self.__num_of_training = num
        self.__weight_unit = w_unit
        self.__program_name = program_name
        self.__training_day = []
        self.__routines_list = []
    
    @property
    def routines_list(self) :
        return self.__routines_list
    
    @routines_list.setter
    def routines_list(self, routines) :
        self.__routines_list = routines

    @property
    def training_day(self) :
        return self.__training_day

    @training_day.setter
    def training_day(self, training_day_list) :
        self.__training_day = training_day_list
    
    @property
    def author(self) : 
        return self.__author
    
    @author.setter
    def author(self, author) :
        self.__author = author
    
    @property
    def num_of_training(self) :
        return self.__num_of_training
    
    @num_of_training.setter
    def num_of_training(self, num) :
        self.__num_of_training = num
    
    @property
    def weight_unit(self) :
        return self.__weight_unit
    
    @weight_unit.setter
    def weight_unit(self, weight_unit) :
        self.__weight_unit = weight_unit

    @property
    def program_name(self) :
        return self.__program_name
    
    @program_name.setter
    def program_name(self, name) :
        self.__program_name = name

   