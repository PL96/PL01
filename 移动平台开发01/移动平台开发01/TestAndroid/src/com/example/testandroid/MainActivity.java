package com.example.testandroid;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.text.Spannable;
import android.text.SpannableStringBuilder;
import android.text.method.LinkMovementMethod;
import android.text.style.ClickableSpan;
import android.text.style.ForegroundColorSpan;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.Window;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends Activity {
	private SharedPreferences pref;
	private SharedPreferences.Editor editor;
	private CheckBox checkBox1;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		getWindow().setBackgroundDrawableResource(R.drawable.test);
		
		//setTitle("");//隐藏标题文本但是标题框还在
		requestWindowFeature(Window.FEATURE_NO_TITLE);//隐藏标题框
		
		setContentView(R.layout.activity_main);
		
		Button btn=(Button)findViewById(R.id.button1);
		
		TextView tv =(TextView) findViewById(R.id.textView4);//忘记密码
		
		tv.setClickable(true);
		
		tv.setTextColor(Color.RED);
		
		checkBox1=(CheckBox) findViewById(R.id.checkBox1);//记住密码
		
		final EditText psd=(EditText)findViewById(R.id.psd);//密码
		
		final EditText uname=(EditText)findViewById(R.id.username);//用户名
		
		final String name=uname.getText().toString();
		
		//记住密码
		
		pref=PreferenceManager.getDefaultSharedPreferences(this);
		
		Boolean isRemember=pref.getBoolean("remember_passdword", false);
		
		if(isRemember){//
		
			String username1=pref.getString("named", "");
			
			String password=pref.getString("psdd", "");
			
			uname.setText(username1);
			
			psd.setText(password);
			
			checkBox1.setChecked(true);
		}
		
		
		//忘记密码
		
		tv.setOnClickListener(new OnClickListener() {
		
			@Override
			
			public void onClick(View v) {
			
				// TODO Auto-generated method stub
				
				Toast.makeText(MainActivity.this, "老表，此功能正在开发中哦", Toast.LENGTH_SHORT).show();
			}
			
		});
		
		
		btn.setOnClickListener(new OnClickListener() {
		
			@Override
			
			public void onClick(View v) {
			
				// TODO Auto-generated method stub
				
				if(uname.getText().toString()==null || uname.getText().toString().equals("") || psd.getText().toString()==null||psd.getText().toString().equals("")){
				
					if(uname.getText().toString()==null || uname.getText().toString().equals("")){
					
						Toast.makeText(MainActivity.this, "用户名不允许为空，请重新输入正确的用户名", Toast.LENGTH_SHORT).show();
					}else{
					
						Toast.makeText(MainActivity.this, "密码不允许为空，请重新输入密码", Toast.LENGTH_SHORT).show();
					}
					
				}else{
				
					if(uname.getText().toString().equals("admin") && psd.getText().toString().equals("123456")){
					
						editor=pref.edit();//写入数据
						
						if(checkBox1.isChecked()){//
						
							editor.putBoolean("remember_passdword", true);
							
							editor.putString("named", uname.getText().toString());
							
							editor.putString("psdd", psd.getText().toString());
						}else{
						
							editor.clear();
						}
						
						
						editor.commit();
						
						Intent intent=new Intent( MainActivity.this,IndexActivity.class);
					
						intent.putExtra("name", name);//传值
						
						startActivity(intent);
						
						finish();
						
						Toast.makeText(MainActivity.this, "欢迎用户："+uname.getText().toString(), Toast.LENGTH_SHORT).show();
					}else{
					
						Toast.makeText(MainActivity.this, "请输入正确的用户名或密码！", Toast.LENGTH_SHORT).show();
					}
					
				}
				
			}
			
		});
		
	}
	

	
	
	@Override
	
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
	
		getMenuInflater().inflate(R.menu.main, menu);
		
		return true;
	}
	

	
	
	@Override
	
	public boolean onOptionsItemSelected(MenuItem item) {
	
		// Handle action bar item clicks here. The action bar will
		
		// automatically handle clicks on the Home/Up button, so long
		
		// as you specify a parent activity in AndroidManifest.xml.
		
		int id = item.getItemId();
		
		if (id == R.id.action_settings) {
		
			return true;
		}
		
		
		return super.onOptionsItemSelected(item);
	}
	
}
