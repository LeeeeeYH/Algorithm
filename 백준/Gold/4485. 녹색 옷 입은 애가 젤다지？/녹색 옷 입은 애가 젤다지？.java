import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final int max = (125+124)*9;
		final int[][] dir = {{-1,0},{0,-1},{1,0},{0,1}};
		
		int cnt = 0;
		int N;
		int[][] board;
		int[][] dp;
		Queue<int[]> q;
		
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		while((N = Integer.parseInt(br.readLine())) != 0) {
			board = new int[N+2][N+2];
			for (int i = 0; i <= N+1; i++)
				board[i][0] = board[i][N+1] = 2*max;
			for (int i = 1; i <= N; i++)
				board[0][i] = board[N+1][i] = 2*max;
			for (int i = 1; i <= N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 1; j <= N; j++)
					board[i][j] = Integer.parseInt(st.nextToken());
			}
			dp = new int[N+2][N+2];
			for (int i = 0; i <= N+1; i++)
				for (int j = 0; j <= N+1; j++)
					dp[i][j] = max;
			dp[1][1] = board[1][1];
			q = new ArrayDeque<int[]>();
			q.add(new int[] {1,1});
			int x, y, dx, dy;
			while(!q.isEmpty()) {
				x = q.peek()[0];
				y = q.poll()[1];
				
				for (int d = 0; d < 4; d++) {
					dx = x + dir[d][0];
					dy = y + dir[d][1];
					if(dp[dx][dy] > board[dx][dy] + dp[x][y]) {
						dp[dx][dy] = board[dx][dy] + dp[x][y];
						q.add(new int[] {dx, dy});
					}
				}
			}
			sb.append("Problem ").append(++cnt).append(": ").append(dp[N][N]).append("\n");
		}
		System.out.println(sb.toString());
	}
}
