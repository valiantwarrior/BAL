package kr.pocoach.bal_android.database

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "assistance_exercise_table")
data class AssistanceExercise(
    @PrimaryKey(autoGenerate = true)
    var assistanceExerciseId : Long = 0L,

    @ColumnInfo(name = "day")
    var day: String = "day",

    @ColumnInfo(name = "category")
    var category: String = "category",

    @ColumnInfo(name = "volume")
    var volume: String = "5x10"

)