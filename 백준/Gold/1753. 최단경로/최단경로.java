import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static class Node implements Comparable<Node>{
		int v;
		int w;
		public Node(int v, int w) {
			this.v = v;
			this.w = w;
		}
		
		public int compareTo(Node o) {
			return this.w - o.w;
		}
		
	}
	
	static final int MAX = 987654321;
	static int V, E;
	static PriorityQueue<Node> pq = new PriorityQueue<Node>();
	static ArrayList<int[]>[] adj;
	static int[] dis;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(br.readLine());
		
		adj = new ArrayList[V+1];
		for (int i = 1; i <= V; i++)
			adj[i] = new ArrayList<int[]>();
		dis = new int[V+1];
		for (int i = 1; i <= V; i++)
			dis[i] = MAX;
		
		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			adj[Integer.parseInt(st.nextToken())].add(new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())});
		}
		pq.add(new Node(K, 0));
		dis[K] = 0;
		
		int cur, curW, next, nextW;
		while(!pq.isEmpty()) {
			cur = pq.peek().v;
			curW = pq.poll().w;
			
			for (int i = 0; i < adj[cur].size(); i++) {
				next = adj[cur].get(i)[0];
				nextW = adj[cur].get(i)[1];
				
				if(dis[next] > curW + nextW) {
					dis[next] = curW + nextW;
					pq.add(new Node(next, dis[next]));
				}
			}
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i <= V; i++) {
			if(dis[i] != MAX) sb.append(dis[i]);
			else sb.append("INF");
			sb.append("\n");
		}
		System.out.println(sb.toString());
	}
}