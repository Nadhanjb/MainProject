package com.example.patientdatausingblockchain;
import androidx.appcompat.app.AppCompatActivity;

import android.app.DatePickerDialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.icu.util.Calendar;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Spinner;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
public class previous_record extends AppCompatActivity implements AdapterView.OnItemSelectedListener {
    ListView list1;
    EditText t1;
    Button b1;
    Spinner spinner;
    String url,test,dates;
    SharedPreferences sp;
    ArrayList<String> disease,testname,result,conclution,description,date;
    String array[]={"Tests","HIV Antibody Test (ELISA)","Blood test","Urin test","ECG","X-ray","MRI","CT scan","Spirometry"};

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Intent i=new Intent(getApplicationContext(),homepage.class);
        startActivity(i);

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {




        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_previous_record);
        list1=(ListView)findViewById(R.id.list11);
        t1=findViewById(R.id.t1);
        b1=findViewById(R.id.b1);
        spinner=findViewById(R.id.spinner);
        sp= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        t1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // on below line we are getting
                // the instance of our calendar.
                final Calendar c = Calendar.getInstance();

                // on below line we are getting
                // our day, month and year.
                int year = c.get(Calendar.YEAR);
                int month = c.get(Calendar.MONTH);
                int day = c.get(Calendar.DAY_OF_MONTH);

                // on below line we are creating a variable for date picker dialog.
                DatePickerDialog datePickerDialog = new DatePickerDialog(
                        // on below line we are passing context.
                        previous_record.this,
                        new DatePickerDialog.OnDateSetListener() {
                            @Override
                            public void onDateSet(DatePicker view, int year,
                                                  int monthOfYear, int dayOfMonth) {
                                // on below line we are setting date to our edit text.
                                String d=year+"-";
                                monthOfYear=monthOfYear+1;

                                if (monthOfYear<10)
                                {
                                    d=d+"0"+monthOfYear+"-";
                                }else
                                {
                                    d=d+monthOfYear+"-";
                                }
                                if(dayOfMonth<10)
                                {
                                    d=d+"0"+dayOfMonth;
                                }
                                else
                                {
                                    d=d+dayOfMonth;
                                }
                                t1.setText(d);

                            }
                        },
                        // on below line we are passing year,
                        // month and day for selected date in our date picker.
                        year, month, day);
                // at last we are calling show to
                // display our date picker dialog.
                datePickerDialog.show();
                datePickerDialog.getDatePicker().setMaxDate(System.currentTimeMillis());
            }
        });


        ArrayAdapter<String> ad=new ArrayAdapter<>(previous_record.this, android.R.layout.simple_list_item_1,array);
        spinner.setAdapter(ad);
        spinner.setOnItemSelectedListener(previous_record.this);




        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                dates=t1.getText().toString();
                url ="http://"+sp.getString("ip", "") + ":5000/prev_rec_search_and";
                RequestQueue queue = Volley.newRequestQueue(previous_record.this);
                StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        // Display the response string.
//                        Toast.makeText(previous_record.this, "################p"+response, Toast.LENGTH_SHORT).show();
                        Log.d("+++++++++++++++++",response);
//                        if  (response.equalsIgnoreCase(""))
//                        {
//
//                        }
//                        else {
                        try {
                            JSONArray ar = new JSONArray(response);
//                    Toast.makeText(previous_record.this, "pppppppp"+response, Toast.LENGTH_SHORT).show();
                            disease = new ArrayList<>();
//                            duration = new ArrayList<>();
                            testname = new ArrayList<>();
                            result = new ArrayList<>();
                            conclution = new ArrayList<>();
                            description = new ArrayList<>();
                            date = new ArrayList<>();
                            for (int i = 0; i < ar.length(); i++) {
                                JSONObject jo = ar.getJSONObject(i);
                                disease.add(jo.getString("record"));
//                                duration.add(jo.getString("due"));
                                testname.add(jo.getString("tname"));
                                result.add(jo.getString("image"));
                                conclution.add(jo.getString("trc"));
                                description.add(jo.getString("details"));
                                date.add(jo.getString("date"));
                            }
                            // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                            //lv.setAdapter(ad);
                            list1.setAdapter(new custom_prev_record(previous_record.this, disease, testname, result, conclution, description, date));
                            spinner.setOnItemSelectedListener(previous_record.this);

                        } catch (Exception e) {
                            Log.d("=========", e.toString());
                        }

                    }

                }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(previous_record.this, "err"+error, Toast.LENGTH_SHORT).show();
                    }
                }) {
                    @Override
                    protected Map<String, String> getParams() {
                        Map<String, String> params = new HashMap<>();
                        params.put("uid",sp.getString("lid",""));
                        params.put("textfield",dates);
                        params.put("textfield2",spinner.getSelectedItem().toString());
                        return params;
                    }
                };
                queue.add(stringRequest);



            }
        });


        url ="http://"+sp.getString("ip", "") + ":5000/prev_rec_search_andnew";
        RequestQueue queue = Volley.newRequestQueue(previous_record.this);
        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
//                        Toast.makeText(previous_record.this, "################p"+response, Toast.LENGTH_SHORT).show();
                Log.d("+++++++++++++++++",response);
//                        if  (response.equalsIgnoreCase(""))
//                        {
//
//                        }
//                        else {
                try {
                    JSONArray ar = new JSONArray(response);
//                    Toast.makeText(previous_record.this, "pppppppp"+response, Toast.LENGTH_SHORT).show();
                    disease = new ArrayList<>();
//                            duration = new ArrayList<>();
                    testname = new ArrayList<>();
                    result = new ArrayList<>();
                    conclution = new ArrayList<>();
                    description = new ArrayList<>();
                    date = new ArrayList<>();
                    for (int i = 0; i < ar.length(); i++) {
                        JSONObject jo = ar.getJSONObject(i);
                        disease.add(jo.getString("record"));
//                                duration.add(jo.getString("due"));
                        testname.add(jo.getString("tname"));
                        result.add(jo.getString("image"));
                        conclution.add(jo.getString("trc"));
                        description.add(jo.getString("details"));
                        date.add(jo.getString("date"));
                    }
                    // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                    //lv.setAdapter(ad);
                    list1.setAdapter(new custom_prev_record(previous_record.this, disease, testname, result, conclution, description, date));
                    spinner.setOnItemSelectedListener(previous_record.this);

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }

            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Toast.makeText(previous_record.this, "err"+error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("uid",sp.getString("lid",""));

                return params;
            }
        };
        queue.add(stringRequest);


    }

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
        test=array[position];

    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }
}