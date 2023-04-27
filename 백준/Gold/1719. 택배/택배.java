import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static final int INF = 987654321;
	static class Node implements Comparable<Node> {
		int v, w;
		public Node(int v, int w) {
			super();
			this.v = v;
			this.w = w;
		}
		public int compareTo(Node o) {
			return this.w - o.w;
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[][] adj = new int[n+1][n+1];
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				adj[i][j] = INF;
			}
		}
		for (int i = 1; i <= n; i++)
			adj[i][i] = 0;
		
		int[][] res = new int[n+1][n+1];
		
		int start, end, wei;
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			start = Integer.parseInt(st.nextToken());
			end = Integer.parseInt(st.nextToken());
			wei = Integer.parseInt(st.nextToken());
			adj[start][end] = adj[end][start] = wei;
			res[start][end] = end;
			res[end][start] = start;
		}
		
		for (int k = 1; k <= n; k++) {
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= n; j++) {
					if(adj[i][j] > adj[i][k] + adj[k][j]) {
						adj[i][j] = adj[i][k] + adj[k][j];
						res[i][j] = res[i][k];
					}
				}
			}
		}
		
		StringBuilder sb = new StringBuilder();
		
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++)
				sb.append(i==j?"-":res[i][j]).append(" ");
			sb.append("\n");
		}
		
		System.out.println(sb.toString());
	} // end of main
} // end of class