package kr.pocoach.bal_android

import android.content.Context
import androidx.room.Room
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.platform.app.InstrumentationRegistry
import kr.pocoach.bal_android.database.AssistanceExercise
import kr.pocoach.bal_android.database.RoutineDatabase
import kr.pocoach.bal_android.database.RoutineDatabaseDao
import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import java.io.IOException

@RunWith(AndroidJUnit4::class)
class RoutineDatabaseTest {

    private lateinit var routineDao: RoutineDatabaseDao
    private lateinit var db : RoutineDatabase

    @Before
    fun createDb() {
        val context =  InstrumentationRegistry.getInstrumentation().targetContext
        db = Room.inMemoryDatabaseBuilder(context, RoutineDatabase::class.java)
            .allowMainThreadQueries()
            .build()
        routineDao = db.routineDatabaseDao
    }

    @After
    @Throws(IOException::class)
    fun closeDb() {
        db.close()
    }

    @Test
    @Throws(Exception::class)
    fun insertAndGetAE() {
        val ae = AssistanceExercise()
        ae.day = "Mon"
        ae.category = "Pull up"
        ae.volume = "5x10"

        routineDao.insert(ae)

        val result = routineDao.getFirstAe()

        assertEquals(result?.day, "Mon")
        assertEquals(result?.category, "Pull up")
        assertEquals(result?.volume, "5x10")

    }
}