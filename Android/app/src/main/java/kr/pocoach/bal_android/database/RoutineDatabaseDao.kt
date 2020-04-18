package kr.pocoach.bal_android.database

import androidx.lifecycle.LiveData
import androidx.room.Dao
import androidx.room.Insert
import androidx.room.Query
import androidx.room.Update

@Dao
interface RoutineDatabaseDao {

    @Insert
    fun insert(ae : AssistanceExercise)

    @Query("SELECT * FROM assistance_exercise_table ORDER BY assistanceExerciseId DESC LIMIT 1")
    fun getFirstAe() : AssistanceExercise?


}