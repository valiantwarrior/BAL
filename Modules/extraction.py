'''
import Modules.Scraper.bal_excel_scraper as Scraper
import Modules.Classes.bal_daily_routine as dr
import Modules.Classes.bal_lifting_set as ls
import Modules.Classes.bal_workout_program as wp
'''

from Modules.Scraper import bal_excel_scraper as Scraper
from Modules.Classes import bal_daily_routine as dr
from Modules.Classes import bal_lifting_set as ls
from Modules.Classes import bal_workout_program as wp

EXCEL_SHEET_DIR = "../test.xlsx"

num_lifting_category = len(Scraper.bal_get_lifting_category(sheet))

def init_workout_program() :
    
    sheet = Scraper.bal_load_excel(EXCEL_SHEET_DIR)
    
    workout_program = wp.BALWorkoutProgram(
        Scraper.bal_get_author(sheet),
        Scraper.bal_get_training_per_weeks(sheet),
        Scraper.bal_get_weight_unit(sheet),
        Scraper.bal_get_routine_name(sheet)
    )

    workout_program.training_day = Scraper.bal_get_training_days(sheet)

    index = 0
    while index < len(workout_program.training_day) :
        workout_program_data.append(init_daily_routine(index*num_lifting_category, workout_program.training_day[index]))
        index += 1

    workout_program.routines_list = workout_program_data

    return workout_program


# RET : bal_lifting_set
def init_lifting_set(position) :

    sheet = Scraper.bal_load_excel(EXCEL_SHEET_DIR)

    lifting_set = ls.BALLiftingSet()
    lifting_set_data = Scraper.bal_get_lifting_set(sheet, position)
    lifting_set.init_lifting_set(lifting_set_data[0], lifting_set_data[2], lifting_set_data[1])

    return lifting_set


# RET : bal_daily_routine
def init_daily_routine(position, day) :
    # using init_lifting_set(position)
    sheet = Scraper.bal_load_excel(EXCEL_SHEET_DIR)
    
    
    daily_routine = dr.BALDailyRoutine()
    daily_routine.day = day
    daily_routine.assistance_exercises = Scraper.bal_get_assistance_exercise(sheet, position/num_lifting_category)
    for index in range(position, position + num_lifting_category):
        if init_lifting_set(index) is None:
            break
        else:
            daily_routine_data.append(init_lifting_set(index))
        
    daily_routine.lifting_set_list = daily_routine_data
    

    return daily_routine








