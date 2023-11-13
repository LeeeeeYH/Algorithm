import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int R, C;
	static int[][] board;
	// 알파벳을 사용했는지 : 마지막 값을 board 테두리에 두를 값(항상 true로 dfs탐색 불가)을 저장
	// 아스키코드상 'Z'다음인 '['값
//	static boolean[] useAlpha = new boolean[27]; // 이 알파벳 썼나?
//	static int[][] dir = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
	static int res = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		board = new int[R + 2][C + 2];
		for (int i = 0; i <= R + 1; i++)
			board[i][0] = board[i][C + 1] = 26;
		for (int i = 0; i <= C + 1; i++)
			board[0][i] = board[R + 1][i] = 26;

		String line;
		for (int i = 1; i <= R; i++) {
			line = br.readLine();
			for (int j = 1; j <= C; j++)
				board[i][j] = (char)(line.charAt(j - 1) - 'A');
		}
		// 1,1좌표 값과 마지막값(테두리'[') 초기화
//		useAlpha[board[1][1]] = useAlpha[26] = true;
		// 여기까지 입력, 세팅

		dfs(1, 1, 1, 1<<26 | 1<<board[1][1]);

		System.out.println(res);
	}

	private static void dfs(int cnt, int x, int y, int flag) {
        if(res == 26) return;
		res = Math.max(res, cnt); // 여기까지 온게 많이 온건가?

		int idx = board[x-1][y];
		if((flag & (1<<idx)) == 0)
			dfs(cnt + 1, x-1, y, flag | 1<<idx);
		idx = board[x][y+1];
		if((flag & (1<<idx)) == 0)
			dfs(cnt + 1, x, y+1, flag | 1<<idx);
		idx = board[x+1][y];
		if((flag & (1<<idx)) == 0)
			dfs(cnt + 1, x+1, y, flag | 1<<idx);
		idx = board[x][y-1];
		if((flag & (1<<idx)) == 0)
			dfs(cnt + 1, x, y-1, flag | 1<<idx);
		
//		int dx, dy, idx;
//		for (int i = 0; i < dir.length; i++) {
//			dx = x + dir[i][0];
//			dy = y + dir[i][1];
//			idx = board[dx][dy]; // 어느 알파벳인지, boolean check접근
//			if ((flag & (1<<idx)) == 0) // 안가본 알파벳이네?
//				dfs(cnt + 1, dx, dy, flag | 1<<idx);
//			
//			if (!useAlpha[idx]) { // 안가본 알파벳이네?
//				useAlpha[idx] = true;
//				dfs(cnt + 1, dx, dy); // 더가자
//				useAlpha[idx] = false;
//			}
//		}
	}
}
