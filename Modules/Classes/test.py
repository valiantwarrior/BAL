import bal_workout_program as wp
import bal_lifting_set as ls
import bal_daily_routine as dr

program = wp.BALWorkoutProgram("Dmitry klokov", 3, "kg", "Sample schedules")
program.training_day = ["Mon", "Wed", "Fri"]
print(program.training_day)


daily_routine = dr.BALDailyRoutine()

ls_list = []

ls_list.append(ls.BALLiftingSet())
ls_list[0].init_lifting_set("Barbell-Benchpress", [ [1,2,3], [1,2,3], [1,2,3] ], [5,5,5,None,None,None])


ls_list.append(ls.BALLiftingSet())
ls_list[1].init_lifting_set("Barbell-Squat", [ [1,2,3,4], [1,2,3,5], [1,2,3,6] ], [6,5,4,None,None,None])


ls_list.append(ls.BALLiftingSet())
ls_list[2].init_lifting_set("Barbell-Deadlift", [ [1,2,3,4], [1,2,3,5], [1,2,3,6] ], [6,5,4,None,None,None])


daily_routine.lifting_set_list = ls_list
daily_routine.day = "Mon"
daily_routine.assistance_exercises = {'Category' : 'Pull up', 'Volume' : '5x12'}

print(daily_routine.lifting_set_list[0].session)
print(daily_routine.day)
print(daily_routine.assistance_exercises)

print('a')