import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[] sq1, sq2;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		boolean[][] paper;
		int N = Integer.parseInt(br.readLine());
		int x, y;
		int res = 0;
		paper = new boolean[101][101];
		
		for (int p = 1; p <= N; p++) {
			st = new StringTokenizer(br.readLine());
			x = Integer.parseInt(st.nextToken());
			y = Integer.parseInt(st.nextToken());
			
			for (int i = x; i < x+10; i++)
				for (int j = y; j < y+10; j++)
					paper[i][j] = true;
			
		}
		for (int i = 1; i <= 100; i++)
			for (int j = 1; j <= 100; j++)
				if(paper[i][j])
					res++;
		System.out.println(res);
	}
}