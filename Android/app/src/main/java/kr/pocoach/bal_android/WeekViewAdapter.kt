package kr.pocoach.bal_android

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import org.w3c.dom.Text

class WeekViewAdapter constructor(context : Context, items : List<Int>, i : Int)
    : RecyclerView.Adapter<WeekViewHolder>(){

    private var context : Context
    private var items : List<Int>
    private var i : Int

    init {
        this.context = context
        this.items = items
        this.i = i
    }
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): WeekViewHolder {
        var view : View = LayoutInflater.from(parent.context).inflate(R.layout.week_item, parent, false)
        var weekViewHolder = WeekViewHolder(view)

        return weekViewHolder
    }

    override fun getItemCount(): Int = this.items.size

    override fun onBindViewHolder(holder: WeekViewHolder, position: Int) {
        val item : Int = items.get(position)
        holder.title.setText("Session #$item")
        if(item%3 == 0) {
            holder.main_content1.setText("Barbell-Benchpress")
            holder.main_content2.setText("Barbell-Squat")
            holder.main_content3.setText("Barbell-Row")
            holder.sub_content.setText("Pull Up")
        }
        else if(item%3 == 1) {
            holder.main_content1.setText("Barbell-OHP")
            holder.main_content2.setText("Barbell-Shrug")
            holder.main_content3.setText("Barbell-Extension")
            holder.sub_content.setText("Power Clean")
        }

        else {
            holder.main_content1.setText("Barbell-Deadlift")
            holder.main_content2.setText("Barbell-Squat")
            holder.main_content3.setText("Barbell-OHP")
            holder.sub_content.setText("Dumbell-Press")
        }
    }
}

class WeekViewHolder constructor(itemView : View)
    :RecyclerView.ViewHolder(itemView) {
    var title = itemView.findViewById<TextView>(R.id.item_week_title)
    var main_content1 = itemView.findViewById<TextView>(R.id.item_week_main_content1)
    var main_content2 = itemView.findViewById<TextView>(R.id.item_week_main_content2)
    var main_content3 = itemView.findViewById<TextView>(R.id.item_week_main_content3)
    var sub_content = itemView.findViewById<TextView>(R.id.item_week_assistance_content)
}
