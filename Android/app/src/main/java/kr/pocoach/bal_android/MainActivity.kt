package kr.pocoach.bal_android

import android.os.Bundle
import android.widget.Toast
import com.google.android.material.bottomnavigation.BottomNavigationView
import androidx.appcompat.app.AppCompatActivity
import androidx.navigation.findNavController
import androidx.navigation.ui.AppBarConfiguration
import androidx.navigation.ui.setupActionBarWithNavController
import androidx.navigation.ui.setupWithNavController

class MainActivity : AppCompatActivity() {
    private var pressedTime : Int = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val navView: BottomNavigationView = findViewById(R.id.nav_view)

        val navController = findNavController(R.id.nav_host_fragment)
        // Passing each menu ID as a set of Ids because each
        // menu should be considered as top level destinations.
        val appBarConfiguration = AppBarConfiguration(
            setOf(
                R.id.navigation_home, R.id.navigation_dashboard, R.id.navigation_notifications
            )
        )
        setupActionBarWithNavController(navController, appBarConfiguration)
        navView.setupWithNavController(navController)
    }

    override fun onBackPressed() {
        if (pressedTime == 0) {
            Toast.makeText(this, "Press back again to exit", Toast.LENGTH_LONG).show()
            pressedTime =  System.currentTimeMillis().toInt()
        }
        else {
            var seconds : Int = System.currentTimeMillis().toInt() - pressedTime

            if (seconds > 2000) {
                Toast.makeText(this, "Press back again to exit", Toast.LENGTH_LONG).show()
                pressedTime = 0
            }
            else {
                super.onBackPressed()
            }
        }

    }
}
