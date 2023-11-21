import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int blue, white;
	static int[][] paper;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(br.readLine());
		paper = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < N; j++)
				paper[i][j] = Integer.parseInt(st.nextToken());
		}
		find(0,0,N);
		sb.append(white).append("\n").append(blue);
		System.out.println(sb.toString());
	} // end of main
	
	public static void find(int x, int y, int len) {
		if(len == 1) {
			if(paper[x][y] == 0) white++;
			else blue++; // paper[x][y] == 1
			return;
		}
		
		int sum = 0;
		for (int i = x; i < x+len; i++)
			for (int j = y; j < y+len; j++)
				sum += paper[i][j];
		if(sum == 0) white++;
		else if(sum == len*len) blue++;
		else {
			find(x,			y,		len/2);
			find(x,			y+len/2,len/2);
			find(x+len/2,	y,		len/2);
			find(x+len/2,	y+len/2,len/2);
		}
		
	}
} // end of class