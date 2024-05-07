package com.example.patientdatausingblockchain;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Appointments extends AppCompatActivity implements AdapterView.OnItemClickListener {
    ListView l1;
    String url;
    SharedPreferences sp;
    ArrayList<String> hospital_name,Department,doctor_name,time,Date,status,aid,check;

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Intent i=new Intent(getApplicationContext(),homepage.class);
        startActivity(i);

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_appointments);
        l1=findViewById(R.id.list);
        sp= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());



        url ="http://"+sp.getString("ip", "") + ":5000/and_viewappointment";
        RequestQueue queue = Volley.newRequestQueue(Appointments.this);

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
                try {

                    JSONArray ar=new JSONArray(response);
                    hospital_name= new ArrayList<>();
                    Department=new ArrayList<>();
                    doctor_name= new ArrayList<>();
                    time= new ArrayList<>();
                    Date=new ArrayList<>();
                    status=new ArrayList<>();
                    aid=new ArrayList<>();
                    check=new ArrayList<>();


                    for(int i=0;i<ar.length();i++)
                    {
                        JSONObject jo=ar.getJSONObject(i);
                        hospital_name.add(jo.getString("hospital"));
                        Department.add(jo.getString("department"));
                        doctor_name.add(jo.getString("doctor"));
                        time.add(jo.getString("date"));
                        Date.add(jo.getString("time"));
                        status.add(jo.getString("status"));
                        aid.add(jo.getString("aid"));
                        check.add(jo.getString("r"));


                    }

                    // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                    //lv.setAdapter(ad);

                    l1.setAdapter(new Custom_appointment(Appointments.this,hospital_name,Department,doctor_name,time,Date,status,aid,check));
                    l1.setOnItemClickListener(Appointments.this);

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(Appointments.this, "err"+error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("lid",sp.getString("lid",""));

                return params;
            }

        };
        queue.add(stringRequest);



    }

    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
//        if (status.get(position).equals("pending")) {
//            AlertDialog.Builder ald = new AlertDialog.Builder(Appointments.this);
//            ald.setTitle("Are you sure want to confirm the appointment?")
//                    .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
//
//                        @Override
//                        public void onClick(DialogInterface arg0, int arg1) {
//                            try {
//                                RequestQueue queue = Volley.newRequestQueue(Appointments.this);
//                                url = "http://" + sp.getString("ip", "") + ":5000/verifyotp";
//
//                                // Request a string response from the provided URL.
//                                StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
//                                    @Override
//                                    public void onResponse(String response) {
//                                        // Display the response string.
//                                        Log.d("+++++++++++++++++", response);
//                                        try {
//                                            JSONObject json = new JSONObject(response);
//                                            String res = json.getString("task");
//
//                                            if (res.equalsIgnoreCase("valid")) {
//                                                String otp = json.getString("otp");
//
//                                                Intent ik = new Intent(getApplicationContext(), appointment_confirmation.class);
//                                                ik.putExtra("otp", otp);
//                                                ik.putExtra("aid", aid.get(position));
//                                                startActivity(ik);
//
//                                            } else {
//
//                                                Toast.makeText(Appointments.this, "Invalid username or password", Toast.LENGTH_SHORT).show();
//
//                                            }
//                                        } catch (JSONException e) {
//                                            e.printStackTrace();
//                                        }
//
//
//                                    }
//                                }, new Response.ErrorListener() {
//                                    @Override
//                                    public void onErrorResponse(VolleyError error) {
//
//
//                                        Toast.makeText(getApplicationContext(), "Error" + error, Toast.LENGTH_LONG).show();
//                                    }
//                                }) {
//                                    @Override
//                                    protected Map<String, String> getParams() {
//                                        Map<String, String> params = new HashMap<String, String>();
//                                        params.put("lid", sp.getString("lid", ""));
//                                        params.put("aid", aid.get(position));
//
//
//                                        return params;
//                                    }
//                                };
//                                int MY_SOCKET_TIMEOUT_MS = 100000;
//
//                                stringRequest.setRetryPolicy(new DefaultRetryPolicy(
//                                        MY_SOCKET_TIMEOUT_MS,
//                                        DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
//                                        DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
//                                queue.add(stringRequest);
//
//
//                            } catch (Exception e) {
//                                Toast.makeText(getApplicationContext(), e + "", Toast.LENGTH_LONG).show();
//                            }
//
//                        }
//                    })
//                    .setNegativeButton("No", new DialogInterface.OnClickListener() {
//
//                        @Override
//                        public void onClick(DialogInterface arg0, int arg1) {
//
//
//                        }
//                    });
//
//            AlertDialog al = ald.create();
//            al.show();
//
//        }
//        else {
//            Toast.makeText(Appointments.this, "already accepted", Toast.LENGTH_SHORT).show();
//
//
//
//        }
    }}
