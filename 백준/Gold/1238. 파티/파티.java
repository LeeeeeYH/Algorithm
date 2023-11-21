import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static final int INF = 987654321;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int X = Integer.parseInt(st.nextToken());
		
		int[][] adj = new int[N+1][N+1];
		for (int i = 1; i <= M; i++) {
			st = new StringTokenizer(br.readLine());
			adj[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())] = Integer.parseInt(st.nextToken());
		}
		
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= N; j++)
				if(adj[i][j] == 0)
					adj[i][j] = INF;
		
		for (int i = 1; i <= N; i++)
			adj[i][i] = 0;
		
		for (int k = 1; k <= N; k++)
			for (int i = 1; i <= N; i++)
				for (int j = 1; j <= N; j++)
					adj[i][j] = Math.min(adj[i][j], adj[i][k] + adj[k][j]);
		
		int max = 0;
		for (int i = 1; i <= N; i++) {
			max = Math.max(max, adj[i][X]+adj[X][i]);
		}
		
		System.out.println(max);
	}
}