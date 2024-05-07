package com.example.patientdatausingblockchain;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.app.ProgressDialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.drawable.Drawable;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.util.Log;
import android.util.Patterns;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.RadioButton;
import android.widget.Spinner;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.android.material.textfield.TextInputEditText;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;

public class profile extends AppCompatActivity {

    String  fname,lname,place,post,pin,phone,email,dob;
    TextInputEditText e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11;
//    EditText e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11;
    String res;
    Button b2;
    String fileName = "", path = "";
    private static final int FILE_SELECT_CODE = 0;
    String gender = "";
    String url, ip, lid,title,url1;
    String PathHolder="";
    byte[] filedt=null;
    SharedPreferences sh;
    RadioButton r1,r2,r3;
    Spinner s1;
    ImageView i1;
    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Intent i=new Intent(getApplicationContext(),homepage.class);
        startActivity(i);

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        e1=findViewById(R.id.FISTNAME);
        e2=findViewById(R.id.lname);
        e3=findViewById(R.id.place);
        e4=findViewById(R.id.phone);
        e5=findViewById(R.id.email);
        e8=findViewById(R.id.post);
        e9=findViewById(R.id.pin);
        e10=findViewById(R.id.dob);
        b2=findViewById(R.id.button14);
        r2=findViewById(R.id.radioButton2);
        r3=findViewById(R.id.radioButton3);
        r1=findViewById(R.id.radioButton);
        i1=findViewById(R.id.imageView2);

        i1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
                intent.setType("*/*");
//            intent.setType("application/pdf");
                intent.addCategory(Intent.CATEGORY_OPENABLE);
                startActivityForResult(intent, 7);

            }
        });

        RequestQueue queue = Volley.newRequestQueue(profile.this);
        String url1 = "http://" + sh.getString("ip", "") + ":5000/viewprofile";
        StringRequest stringRequest = new StringRequest(Request.Method.POST, url1, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++", response);
                try {

                    JSONArray ar = new JSONArray(response);

                    {
                        JSONObject jo = ar.getJSONObject(0);
                        e1.setText(jo.getString("fname"));
                        e2.setText(jo.getString("lname"));
                        e3.setText(jo.getString("place"));
                        e4.setText(jo.getString("phone"));
                        e5.setText(jo.getString("email"));
                        e8.setText(jo.getString("post"));
                        e9.setText(jo.getString("pin"));

                        e10.setText(jo.getString("dob"));
                        String gender = jo.getString("gender");
                        if (gender.equalsIgnoreCase("male")) {
                            r1.setChecked(true);
                        } else {
                            r2.setChecked(true);
                        }


                        if (android.os.Build.VERSION.SDK_INT > 9) {
                            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                            StrictMode.setThreadPolicy(policy);
                        }

//        i1.setImageDrawable(Drawable.createFromPath(getIntent().getStringExtra("photo")));
                        java.net.URL thumb_u;
                        try {

                            //thumb_u = new java.net.URL("http://192.168.43.57:5000/static/photo/flyer.jpg");

                            thumb_u = new java.net.URL("http://" + sh.getString("ip", "") + ":5000" + jo.getString("photo"));
                            Drawable thumb_d = Drawable.createFromStream(thumb_u.openStream(), "src");
                            i1.setImageDrawable(thumb_d);

                        } catch (Exception e) {
                            Log.d("errsssssssssssss", "" + e);
                        }
                    }


                } catch (JSONException e) {
                    e.printStackTrace();
                }

            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(getApplicationContext(), "Error", Toast.LENGTH_LONG).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<String, String>();

                params.put("lid", sh.getString("lid", ""));


                return params;
            }
        };
        // Add the request to the RequestQueue.
        queue.add(stringRequest);


        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                fname = e1.getText().toString();
                lname = e2.getText().toString();
                place = e3.getText().toString();
                pin = e9.getText().toString();
                post = e8.getText().toString();
                dob = e10.getText().toString();
                email = e5.getText().toString();
                phone = e4.getText().toString();
                if (r1.isChecked()) {
                    gender = r1.getText().toString();
                } else {
                    gender = r2.getText().toString();

                }

                if (r1.isChecked()) {
                    gender = r1.getText().toString();
                } else if (r2.isChecked()) {
                    gender = r2.getText().toString();
                } else {
                    gender = r3.getText().toString();
                }


                if (fname.equalsIgnoreCase("")) {
                    e1.setError("Please Enter Your FirstName");
                } else if (!fname.matches("^[a-z A-Z]*$")) {
                    e1.setError("characters allowed");
                    e1.requestFocus();
                } else if (lname.equalsIgnoreCase("")) {
                    e2.setError("Please Enter Your lastname");
                } else if (!lname.matches("^[a-z A-Z]*$")) {
                    e2.setError("characters allowed");
                    e2.requestFocus();
                } else if (place.equalsIgnoreCase("")) {
                    e3.setError("Please Enter Your place");
                } else if (!place.matches("^[a-z A-Z]+$")) {
                    e3.setError("characters are allowed");
                } else if (post.equals("")) {
                    e8.setError("Please Enter Your post");
                } else if (!post.matches("^[a-z A-Z]+$")) {
                    e8.setError("characters are allowed");
                } else if (pin.equals("")) {
                    e9.setError("enter pin");
                } else if (pin.length() != 6) {
                    e9.setError("Minimum 6 nos required");
                    e9.requestFocus();
                } else if (phone.equalsIgnoreCase("")) {
                    e4.setError("Enter Your Phone No");
                } else if (phone.length() != 10) {
                    e4.setError("Minimum 10 nos required");
                    e4.requestFocus();
                } else if (email.equalsIgnoreCase("")) {
                    e5.setError("Enter Your Email");
                } else if (!Patterns.EMAIL_ADDRESS.matcher(email).matches()) {
                    e5.setError("Enter Valid Email");
                    e5.requestFocus();
                } else {

                    uploadBitmap(title);
                }

            }
        });

    }

    ProgressDialog pd;
    private void uploadBitmap(final String title) {
        url = "http://" + sh.getString("ip", "") + ":5000/and_update_profile";

        pd=new ProgressDialog(profile.this);
        pd.setMessage("Uploading....");
        pd.show();
        VolleyMultipartRequest volleyMultipartRequest = new VolleyMultipartRequest(Request.Method.POST, url,
                new Response.Listener<NetworkResponse>() {
                    @Override
                    public void onResponse(NetworkResponse response1) {
                        pd.dismiss();
                        String x=new String(response1.data);
                        try {
                            JSONObject obj = new JSONObject(new String(response1.data));
//                        Toast.makeText(Upload_agreement.this, "Report Sent Successfully", Toast.LENGTH_LONG).show();
                            if (obj.getString("task").equalsIgnoreCase("valid")) {

                                Toast.makeText(profile.this, "Saved Successfully ", Toast.LENGTH_LONG).show();
                                Intent i=new Intent(getApplicationContext(),homepage.class);
                                startActivity(i);
                            } else {
                                Toast.makeText(getApplicationContext(), "failed", Toast.LENGTH_LONG).show();
                            }
                        } catch (Exception e) {
                            Toast.makeText(getApplicationContext(), "Error" + e.getMessage().toString(), Toast.LENGTH_SHORT).show();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
//                        Toast.makeText(getApplicationContext(), error.getMessage(), Toast.LENGTH_SHORT).show();
                        RequestQueue queue = Volley.newRequestQueue(profile.this);
                        url = "http://" + sh.getString("ip","") + ":5000/and_update_profile";
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
                                        Toast.makeText(profile.this, "success", Toast.LENGTH_SHORT).show();


                                        Intent ik = new Intent(getApplicationContext(), homepage.class);
                                        startActivity(ik);

                                    } else {

                                        Toast.makeText(profile.this, "Invalid", Toast.LENGTH_SHORT).show();

                                    }
                                } catch (JSONException e) {
                                    e.printStackTrace();
                                }


                            }
                        }, new Response.ErrorListener() {
                            @Override
                            public void onErrorResponse(VolleyError error) {


                                Toast.makeText(getApplicationContext(), "Error" + error, Toast.LENGTH_LONG).show();
                            }
                        }) {
                            @Override
                            protected Map<String, String> getParams() {
                                Map<String, String> params = new HashMap<String, String>();
                                params.put("Fname", fname);
                                params.put("Lname", lname);
                                params.put("place", place);
                                params.put("phone_number", phone);
                                params.put("gender", gender);
                                params.put("post", post);
                                params.put("pin", pin);
                                params.put("email_id", email);
                                params.put("dob", dob);
                                params.put("lid",sh.getString("lid",""));

                                return params;
                            }
                        };
                        queue.add(stringRequest);

                    }
                }) {

            @Override
            protected Map<String, String> getParams() throws AuthFailureError {
                Map<String, String> params = new HashMap<>();

                params.put("Fname", fname);
                params.put("Lname", lname);
                params.put("place", place);
                params.put("phone_number", phone);
                params.put("gender", gender);
                params.put("post", post);
                params.put("pin", pin);
                params.put("email_id", email);
                params.put("dob", dob);
                params.put("lid",sh.getString("lid",""));

                return params;
            }

            @Override
            protected Map<String, DataPart> getByteData() {
                Map<String, DataPart> params = new HashMap<>();
                long imagename = System.currentTimeMillis();
                params.put("file", new DataPart(PathHolder , filedt ));


                return params;
            }
        };

        Volley.newRequestQueue(this).add(volleyMultipartRequest);
    }

    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        switch (requestCode) {
            case 7:
                if (resultCode == RESULT_OK) {
                    Uri uri = data.getData();
                    Log.d("File Uri", "File Uri: " + uri.toString());
                    // Get the path
                    try {
                        PathHolder = FileUtils.getPathFromURI(this, uri);
//                        PathHolder = data.getData().getPath();
//                        Toast.makeText(this, PathHolder, Toast.LENGTH_SHORT).show();

                        filedt = getbyteData(PathHolder);
                        Log.d("filedataaa", filedt + "");
//                        Toast.makeText(this, filedt+"", Toast.LENGTH_SHORT).show();
                        path = FileUtils.getPath(this, uri);
                        //e4.setText(path1);
                        Log.d("path", path);
                        File fil = new File(path);
                        int fln = (int) fil.length();
                        //  e2.setText(path);

                        File file = new File(path);

                        byte[] byteArray = null;
                        try {
                            InputStream inputStream = new FileInputStream(fil);
                            ByteArrayOutputStream bos = new ByteArrayOutputStream();
                            byte[] b = new byte[fln];
                            int bytesRead = 0;

                            while ((bytesRead = inputStream.read(b)) != -1) {
                                bos.write(b, 0, bytesRead);
                            }

                            byteArray = bos.toByteArray();
                            inputStream.close();
                            Bitmap bmp= BitmapFactory.decodeByteArray(byteArray, 0, byteArray.length);
                            if(bmp!=null){
//
//
//                                i1.setVisibility(View.VISIBLE);
                                i1.setImageBitmap(bmp);
                            }
                        } catch (Exception e) {
                            // TODO: handle exception
                        }

                    } catch (Exception e) {
                        Toast.makeText(this, "" + e.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                }
                break;
        }
    }

    private byte[] getbyteData(String pathHolder) {
        Log.d("path", pathHolder);
        File fil = new File(pathHolder);
        int fln = (int) fil.length();
        byte[] byteArray = null;
        try {
            InputStream inputStream = new FileInputStream(fil);
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            byte[] b = new byte[fln];
            int bytesRead = 0;

            while ((bytesRead = inputStream.read(b)) != -1) {
                bos.write(b, 0, bytesRead);
            }
            byteArray = bos.toByteArray();
            inputStream.close();
        } catch (Exception e) {
        }
        return byteArray;
    }




}
