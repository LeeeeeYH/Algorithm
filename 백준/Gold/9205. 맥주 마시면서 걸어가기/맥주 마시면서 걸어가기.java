import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[][] loc = new int[102][2]; // 일단 거리 저장하는 배열
	static boolean[][] adj = new boolean[102][102]; // 저장된 거리(loc)배열을 이용하여 맥주를 마시고 도달할 수 있는지 모두 미리 계산
	static boolean[] visited; // 방문
	static boolean goFestival; // 도착
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine());
			for (int i = 0; i < N+2; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				loc[i][0] = Integer.parseInt(st.nextToken());
				loc[i][1] = Integer.parseInt(st.nextToken());
			}
			
			// 계산해서 인접행렬 초기화
			for (int i = 0; i < N+1; i++) {
				for (int j = i+1; j < N+2; j++) {
					if(dis(loc[i], loc[j]) <= 1000)
						adj[i][j] = adj[j][i] = true;
					else adj[i][j] = adj[j][i] = false;
				}
			}
			visited = new boolean[N+2];
			goFestival = false;
			
			dfs(0);
			
			if(goFestival) sb.append("happy").append("\n");
			else sb.append("sad").append("\n");
		}
		System.out.println(sb.toString());
	}
	
	public static void dfs(int idx) {
		if(goFestival) return; // 도착 했으니 모든 callStack에 있는 재귀함수 없애기
		
		// 페스티벌 도착?
		if(idx == N+1) {
			goFestival = true;
			return;
		}
		
		// 방문후 dfs
		for (int i = 1; i <= N+1; i++) {
			if(!visited[i] && adj[idx][i]) {
				visited[i] = true;
				dfs(i);
			}
			if(goFestival) return;
		}
	}
	
	public static int dis(int[] xy1, int[] xy2) {
		return Math.abs(xy1[0]-xy2[0]) + Math.abs(xy1[1]-xy2[1]);
	}
}
