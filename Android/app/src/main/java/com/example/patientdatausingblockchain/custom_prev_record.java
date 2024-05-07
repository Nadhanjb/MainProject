package com.example.patientdatausingblockchain;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;

import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.net.Uri;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class custom_prev_record extends BaseAdapter {

    private Context context;
    ArrayList<String> a;
    ArrayList<String> c;
    ArrayList<String> d;
    ArrayList<String> e;
    ArrayList<String> f;
    ArrayList<String> g;



    SharedPreferences sh;



    public custom_prev_record(Context applicationContext, ArrayList<String> a, ArrayList<String> c, ArrayList<String> d, ArrayList<String> e, ArrayList<String> f,ArrayList<String> g) {
        // TODO Auto-generated constructor stub
        this.context=applicationContext;
        this.a=a;

        this.c=c;
        this.d=d;
        this.e=e;
        this.f=f;
        this.g=g;


        sh= PreferenceManager.getDefaultSharedPreferences(applicationContext);
    }

    @Override
    public int getCount() {
        // TODO Auto-generated method stub
        return a.size();
    }

    @Override
    public Object getItem(int arg0) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public long getItemId(int arg0) {
        // TODO Auto-generated method stub
        return 0;
    }
    @Override
    public int getItemViewType(int arg0) {
        // TODO Auto-generated method stub
        return 0;
    }


    @Override
    public View getView(int position, View convertview, ViewGroup parent) {
        // TODO Auto-generated method stub
        LayoutInflater inflator=(LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View gridView;
        if(convertview==null)
        {
            gridView=new View(context);
            gridView=inflator.inflate(R.layout.custom_view_prev_record, null);

        }
        else
        {
            gridView=(View)convertview;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.dis);

        TextView tv3=(TextView)gridView.findViewById(R.id.test);
        TextView tv4=(TextView)gridView.findViewById(R.id.res);
        TextView tv5=(TextView)gridView.findViewById(R.id.conc);
        TextView tv6=(TextView)gridView.findViewById(R.id.des);
        TextView tv7=(TextView)gridView.findViewById(R.id.date);
        tv4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String url ="http://"+sh.getString("ip", "") + ":5000"+d.get(position);
                Intent i = new Intent(Intent.ACTION_VIEW);
                i.setData(Uri.parse(url));
                context.startActivity(i);
            }
        });

        tv1.setText(a.get(position));

        tv3.setText(c.get(position));
        tv4.setText(d.get(position));
        tv5.setText(e.get(position));
        tv6.setText(f.get(position));
        tv7.setText(g.get(position));

        tv1.setTextColor(Color.BLACK);

        tv3.setTextColor(Color.BLACK);
        tv4.setTextColor(Color.GRAY);
        tv5.setTextColor(Color.BLACK);
        tv6.setTextColor(Color.BLACK);
        tv7.setTextColor(Color.BLACK);

        return gridView;

    }
}
