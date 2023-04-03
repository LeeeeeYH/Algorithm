import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		int N;
		int[][] adj;
		int min, sum;
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine(), " ");
			N = Integer.parseInt(st.nextToken());
			adj = new int[N][N];
			for (int i = 0; i < N*N; i++)
				adj[i/N][i%N] = Integer.parseInt(st.nextToken())==1?1:5000;
			for (int i = 0; i < N; i++)
				adj[i][i] = 0;
			
			for (int k = 0; k < N; k++)
				for (int i = 0; i < N; i++)
					for (int j = 0; j < N; j++)
						if(adj[i][j] > adj[i][k] + adj[k][j])
							adj[i][j] = adj[i][k] + adj[k][j];
			
			min = Integer.MAX_VALUE;
			for (int i = 0; i < N; i++) {
				sum = 0;
				for (int j = 0; j < N; j++)
					sum += adj[i][j];
				min = Math.min(min, sum);
			}
			
			sb.append("#").append(tc).append(" ").append(min).append("\n");
		}
		System.out.println(sb.toString());
	}
}
