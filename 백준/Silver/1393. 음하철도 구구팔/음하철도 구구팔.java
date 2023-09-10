import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int xs, ys;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		xs = Integer.parseInt(st.nextToken());
		ys = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine(), " ");
		int xe = Integer.parseInt(st.nextToken());
		int ye = Integer.parseInt(st.nextToken());
		int dx = Integer.parseInt(st.nextToken());
		int dy = Integer.parseInt(st.nextToken());

		// 최대공약수를 구해서 열차 정수 진행 준비
		int div = gcd(dx, dy);
		dx /= div; dy /= div;
		
		int x = xe + dx;
		int y = ye + dy;
		double bfDis = dis(xe, ye);
		double curDis = dis(x, y);
		while(bfDis > curDis) {
			bfDis = curDis;
			x += dx;
			y += dy;
			curDis = dis(x, y);
		}
		
		System.out.println((x-dx) + " " + (y-dy));
		

// 수학으로 하려다 직선이아닌 반직선임을 깨달음
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		StringBuilder sb = new StringBuilder();
//		
//		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
//		
//		int x = (int) Math.round(((dy/dx*xe + dx/dy*xs-ye+ys)/(dy/dx+dx/dy)));
//		int y = (int) Math.round((dy/dx)*(x-xe)+ye);
//		
//		if(dx > 0)
//		System.out.println(x + " " + y);
	} // end of main
	
	public static int gcd(int a, int b) {
		if(b==0) return a;
		return gcd(b, a%b);
	}

	public static double dis(int x, int y) {
		return Math.sqrt((x - xs) * (x - xs) + (y - ys) * (y - ys));
	}
} // end of class