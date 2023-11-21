import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static final int[][] dir = {{-1,0},{0,1},{1,0},{0,-1}};
	static final int INF = Integer.MAX_VALUE;
	static int[][] loc; // 부대와 탈영병의 xy좌표 저장
	static int soldierNum = 0;
	static int[][] adj; // 부대, 탈영병의 최소거리 저장
	
	static int[] num; // 순열 담을 배열
	static int res = Integer.MAX_VALUE; // 최소비용
	
	static class Node implements Comparable<Node> {
		int x, y;
		int w;
		
		public Node(int x, int y, int w) {
			this.x = x;
			this.y = y;
			this.w = w;
		}
		public int compareTo(Node o) {
			return this.w - o.w;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
//		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		StringTokenizer st;
		int[][] board = new int[N+2][N+2];
		adj = new int[6][6];
		int[][] dis;
		loc = new int[6][2];
		int input;
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 1; j <= N; j++) {
				board[i][j] = input = Integer.parseInt(st.nextToken());
				switch (input) {
				case -1:
					loc[0][0] = i;
					loc[0][1] = j;
					board[i][j] = 0;
					break;
				case 0:
					loc[++soldierNum][0] = i;
					loc[soldierNum][1] = j;
//					board[i][j] = -soldierNum; // 지도에는 -로 몇번째 군인인지 확인
					break;
				}
			}
		}
		
		num = new int[soldierNum+2];
		
		PriorityQueue<Node> pq;
		int x,y,w,dx,dy,dw;
		
		for (int sol = 0; sol <= soldierNum; sol++) { // 부대부터 탈영병까지
			dis = new int[N+2][N+2];
			for (int i = 1; i <= N; i++)
				for (int j = 1; j <= N; j++)
					dis[i][j] = INF;
			
			
			pq = new PriorityQueue<Node>();
			pq.add(new Node(loc[sol][0], loc[sol][1], 0));
			dis[loc[sol][0]][loc[sol][1]] = 0;
			
			while(!pq.isEmpty()) {
				x = pq.peek().x;
				y = pq.peek().y;
				w = pq.poll().w;
				
				if(dis[x][y] < w) continue;
				for (int d = 0; d < 4; d++) {
					dx = x + dir[d][0];
					dy = y + dir[d][1];
					dw = w + board[dx][dy];
					if(dis[dx][dy] > dw) {
						pq.add(new Node(dx,dy,dw));
						dis[dx][dy] = dw;
					}
				}
			}
			
			for (int i = 0; i <= soldierNum; i++) {
				adj[sol][i] = dis[loc[i][0]][loc[i][1]];
			}
		}
		
		per(1, 0);
		System.out.println(res);
	}
	
	public static int tmp = 0;
	public static void per(int cnt, int flag) {
		if(cnt == soldierNum+1) {
			int sum = 0;
			for (int i = 0; i <= soldierNum; i++)
				sum += adj[num[i]][num[i+1]];
			if(res > sum)
				res = sum;
		}
		
		for (int i = 1; i <= soldierNum; i++) {
			if((flag & (1<<i)) == 0) {
				num[cnt] = i;
				per(cnt+1, flag | (1<<i));
			}
		}
	}
}