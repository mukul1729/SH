#!/usr/bin/rdmd
import std.stdio;

real power(real x) {
	real ans = 2;
	while(ans < x) {
		ans*=ans;
	}
	return ans;
}

void main() {
	real t;
	real mod = 1000000007;
	readf("%s",t);
	real n;
	while(t--) {
		readf(" %s",n);
		if(n<=2)
			writeln(n);
		else if((n&(n-1)) == 0)
			writeln((2*n - 1)%mod);
	}

}
