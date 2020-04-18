package kr.pocoach.bal_android.database

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase

@Database(entities = [AssistanceExercise::class], version = 1, exportSchema = false)
abstract class RoutineDatabase : RoomDatabase() {
    abstract val routineDatabaseDao : RoutineDatabaseDao

    companion object{
        @Volatile
        private var INSTANCE : RoutineDatabase? = null

        fun getInstance(context: Context) : RoutineDatabase {
            synchronized(this) {
                var instance = INSTANCE
                if (instance == null) {
                    instance = Room.databaseBuilder(
                        context.applicationContext,
                        RoutineDatabase::class.java,
                        "routine_database")
                        .fallbackToDestructiveMigration()
                        .build()
                    INSTANCE = instance
                }
                return instance
            }
        }
    }
}