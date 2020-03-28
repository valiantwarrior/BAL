package kr.pocoach.bal_android

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import org.jetbrains.annotations.TestOnly
import org.w3c.dom.Text

class RoutineViewAdapter constructor(context : Context, items : List<Int>, i : Int)
    : RecyclerView.Adapter<RoutineViewHolder>() {

    /* Test data */

    private var context : Context
    private var items : List<Int>
    private var i :Int

    init {
        this.context = context
        this.items = items
        this.i = i
    }


    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RoutineViewHolder {
        var view = LayoutInflater.from(parent.context).inflate(R.layout.routine_item, parent, false)
        var routineViewHolder = RoutineViewHolder(view)

        return routineViewHolder
    }

    override fun getItemCount(): Int = this.items.size

    /* Test */
    override fun onBindViewHolder(holder: RoutineViewHolder, position: Int) {
        val item : Int = items.get(position)
        holder.title.setText("Barbell-Benchpress set#$item")
        holder.content.setText("50kg 5 reps")

    }
}

class RoutineViewHolder constructor(itemView : View)
    : RecyclerView.ViewHolder(itemView) {
    /* Test */
    var title = itemView.findViewById<TextView>(R.id.item_tv_title)
    var content = itemView.findViewById<TextView>(R.id.item_tv_content)
}
