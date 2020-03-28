package kr.pocoach.bal_android.ui.dashboard

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProviders
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import kr.pocoach.bal_android.R
import kr.pocoach.bal_android.WeekViewAdapter


class DashboardFragment : Fragment() {

    private lateinit var dashboardViewModel: DashboardViewModel
    private var list = ArrayList<Int>()
    private val llm = LinearLayoutManager(activity)
    private lateinit var week_view : RecyclerView
    private var i : Int = 0

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        dashboardViewModel =
            ViewModelProviders.of(this).get(DashboardViewModel::class.java)
        val root = inflater.inflate(R.layout.fragment_dashboard, container, false)

        week_view = root.findViewById(R.id.week_view)
        week_view.setHasFixedSize(true)
        week_view.layoutManager = llm

        for(i in 1..12) {
            list.add(i)
            week_view.adapter = context?.let { WeekViewAdapter(it, list, i) }
        }

        return root
    }
}