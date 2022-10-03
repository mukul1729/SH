
import java.lang.Character.*;
import static java.lang.Math.*;
import java.util.*;
interface Operator{
	int a =0 ;
	int b =0 ;
	int res =0 ;
}

class faltu implements Operator{
	int addition(){
		return a;
	}
}
class Calculator{
	int x;
	int y;
 	int res;
	public Calculator(int x,int y){
		this.x=x;
		this.y=y;
	}
	public int addition(){
		res = x+y;
		return res;
	}
	public int display(){
		return res;
	}
}

class addition{
	class subtract{
		public int sub(int a,int b){
			int res;
			res = a-b;
			return res;
		}
	}
	public int a,b,res;
	public addition(int a,int b){
		res = a+b;
	}
	public int display(){
		return res;
	}
}

class Parent{
	private static int a = 1;
	void test()
	{
		int a = 10;
		while(a-- !=0){
			System.out.println(a);
		}
	}
}


public class ArrayDemo{
	addition a = new addition(1,2);
	Scanner sc = new Scanner(System.in);
	public static int test(int num){
		int res = 0;
		while(num-- !=0){
			res += num;
		}
		return res;
	}
	public static void main(String[] args){
    Float f1 = new Float("3.0");
    int x = f1.intValue();
    byte b = f1.byteValue();
    double d = f1.doubleValue();
    System.out.println(x + b + d);
		}
}
