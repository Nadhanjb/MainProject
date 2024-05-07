package com.example.patientdatausingblockchain;

import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.drawable.Drawable;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AlertDialog;
import androidx.cardview.widget.CardView;

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

public class Custom_appointment extends BaseAdapter {
    private Context context;
    ArrayList<String> a;
    ArrayList<String> b;
    ArrayList<String> c;
    ArrayList<String> d;
    ArrayList<String> e;
    ArrayList<String> f;
    ArrayList<String> g;
    ArrayList<String> h;


    SharedPreferences sh;



    public Custom_appointment(Context applicationContext, ArrayList<String> a, ArrayList<String> b, ArrayList<String> c, ArrayList<String> d, ArrayList<String> e, ArrayList<String> f,ArrayList<String> g,ArrayList<String> h) {
        // TODO Auto-generated constructor stub
        this.context=applicationContext;
        this.a=a;
        this.b=b;
        this.c=c;
        this.d=d;
        this.e=e;
        this.f=f;
        this.g=g;
        this.h=h;

        sh=PreferenceManager.getDefaultSharedPreferences(applicationContext);
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
            gridView=inflator.inflate(R.layout.activity_custom_appointment, null);

        }
        else
        {
            gridView=(View)convertview;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.hs);
        TextView tv2=(TextView)gridView.findViewById(R.id.dept);
        TextView tv3=(TextView)gridView.findViewById(R.id.doc);
        TextView tv4=(TextView)gridView.findViewById(R.id.date);
        TextView tv5=(TextView)gridView.findViewById(R.id.time);
        TextView tv6=(TextView)gridView.findViewById(R.id.status);
        CardView cv=(CardView)gridView.findViewById(R.id.cv);
        Button b1=(Button) gridView.findViewById(R.id.button4);


        if(f.get(position).equalsIgnoreCase("pending")){


            if(h.get(position).equalsIgnoreCase("yes")){
                b1.setVisibility(View.VISIBLE);
            }
            else{
                b1.setVisibility(View.INVISIBLE);

            }
        }
        else{
            b1.setVisibility(View.INVISIBLE);

        }


        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                AlertDialog.Builder ald = new AlertDialog.Builder(context);
                ald.setTitle("Are you sure want to confirm the appointment?")
                        .setPositiveButton("Yes", new DialogInterface.OnClickListener() {

                            @Override
                            public void onClick(DialogInterface arg0, int arg1) {
                                try {
                                    RequestQueue queue = Volley.newRequestQueue(context);
                                    String url = "http://" + sh.getString("ip", "") + ":5000/verifyotp";

                                    // Request a string response from the provided URL.
                                    StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                                        @Override
                                        public void onResponse(String response) {
                                            // Display the response string.
                                            Log.d("+++++++++++++++++", response);
                                            try {
                                                JSONObject json = new JSONObject(response);
                                                String res = json.getString("task");

                                                if (res.equalsIgnoreCase("valid")) {
                                                    String otp = json.getString("otp");

                                                    Intent ik = new Intent(context.getApplicationContext(), appointment_confirmation.class);
                                                    ik.putExtra("otp", otp);
                                                    ik.putExtra("aid", g.get(position));
                                                    context.startActivity(ik);

                                                } else {

                                                    Toast.makeText(context, "Invalid username or password", Toast.LENGTH_SHORT).show();

                                                }
                                            } catch (JSONException e) {
                                                e.printStackTrace();
                                            }


                                        }
                                    }, new Response.ErrorListener() {
                                        @Override
                                        public void onErrorResponse(VolleyError error) {


                                            Toast.makeText(context.getApplicationContext(), "Error" + error, Toast.LENGTH_LONG).show();
                                        }
                                    }) {
                                        @Override
                                        protected Map<String, String> getParams() {
                                            Map<String, String> params = new HashMap<String, String>();
                                            params.put("lid", sh.getString("lid", ""));
                                            params.put("aid", g.get(position));


                                            return params;
                                        }
                                    };
                                    int MY_SOCKET_TIMEOUT_MS = 100000;

                                    stringRequest.setRetryPolicy(new DefaultRetryPolicy(
                                            MY_SOCKET_TIMEOUT_MS,
                                            DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                                            DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
                                    queue.add(stringRequest);


                                } catch (Exception e) {
                                    Toast.makeText(context.getApplicationContext(), e + "", Toast.LENGTH_LONG).show();
                                }

                            }
                        })
                        .setNegativeButton("No", new DialogInterface.OnClickListener() {

                            @Override
                            public void onClick(DialogInterface arg0, int arg1) {



                            }
                        });

                AlertDialog al = ald.create();
                al.show();

            }
        });





        tv1.setText(a.get(position));
        tv2.setText(b.get(position));
        tv3.setText(c.get(position));
        tv4.setText(d.get(position));
        tv5.setText(e.get(position));
        tv6.setText(f.get(position));

if(f.get(position).equalsIgnoreCase("pending"))
{
    cv.setBackgroundColor(Color.LTGRAY);
}
else {
    cv.setBackgroundColor(Color.WHITE);

}



        tv1.setTextColor(Color.BLACK);
        tv2.setTextColor(Color.BLACK);
        tv3.setTextColor(Color.BLACK);
        tv4.setTextColor(Color.BLACK);
        tv5.setTextColor(Color.BLACK);
        tv6.setTextColor(Color.BLACK);











        return gridView;

    }

}





