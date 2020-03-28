package kr.pocoach.bal_android.ui.home

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
import kr.pocoach.bal_android.RoutineViewAdapter

class HomeFragment : Fragment() {

    private lateinit var homeViewModel: HomeViewModel
    private var list = ArrayList<Int>()
    private val llm = LinearLayoutManager(activity)
    private lateinit var routine_view : RecyclerView
    private var i : Int = 0

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        homeViewModel =
            ViewModelProviders.of(this).get(HomeViewModel::class.java)
        val root = inflater.inflate(R.layout.fragment_home, container, false)

        routine_view = root.findViewById(R.id.routine_view)
        routine_view.setHasFixedSize(true)
        routine_view.layoutManager = llm

        for(i in 1..10) {
            list.add(i)
            routine_view.adapter = activity?.let { RoutineViewAdapter(it, list, i) }
        }

        return root
    }
}