import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static final int[][] dir = {{-1,0},{0,1},{1,0},{0,-1}};
	static int[][] board;
	static boolean[][] canSpread;
	static int[][] spreadBoard;
	static int R, C;
	static int cleanerR = -1;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		int T = Integer.parseInt(st.nextToken());
		canSpread = new boolean[R+2][C+2]; // 또 테두리 씌울것이므로 가장 바깥쪽한줄씩과 청정기는 false로 확산못하게 할거임
		for (int i = 1; i <= R; i++)
			for (int j = 1; j <= C; j++)
				canSpread[i][j] = true; // 확산 가능한 부분
		
		board = new int[R+2][C+2];
		for (int i = 1; i <= R; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 1; j <= C; j++)
				board[i][j] = Integer.parseInt(st.nextToken());
			if(board[i][1] == -1) {
				cleanerR = i-1; // 클리너 위쪽 행정보 저장 -> 두번의 입력이 들어올텐데 아래쪽이 후순으로 걸렸을때 윗부분(i-1)이 저장됨. 이미 짰는데 문제점을 나중에 발견하여 강제로 i-1로 해야했음 ㅠ
				board[i][1] = 0; // 나중에 미세먼지 더할때 0으로해줌
				canSpread[i][1] = false; // 청정기는 확산X
			}
		}
		
		while(T-- > 0) {
			spread();
			wind();
		}
		
		int sum = 0;
		for (int i = 1; i <= R; i++)
			for (int j = 1; j <= C; j++)
				sum += board[i][j];
		
		System.out.println(sum);
	}
	
	public static void spread() {
		spreadBoard = new int[R+2][C+2];
		
		// 확산 시키고 확산된 것들은 spreadBoard로
		for (int i = 1; i <= R; i++)
			for (int j = 1; j <= C; j++)
				if(board[i][j] > 0)
					spreadSingle(i, j);
		
		// 확산된것들(spreadBoard)에 있는 것들은 진짜 board에 합산 
		for (int i = 1; i <= R; i++)
			for (int j = 1; j <= C; j++)
				board[i][j] += spreadBoard[i][j];
	}
	
	public static void spreadSingle(int x, int y) {
		int spreadDirNum = 0; // 확산방향 가능수
		
		// 상하좌우에서 확산되는 방향 검사 후 확산 될 방향을 계산
		for (int d = 0; d < 4; d++)
			if(canSpread[x+dir[d][0]][y+dir[d][1]]) // 확산 가능하면 +1
				spreadDirNum++;
		
		int spreadAmount = board[x][y] / 5; // 확산되는 정도
		if(spreadAmount == 0) return; // 0이면 굳이 아래꺼 안해도 되잖아
		board[x][y] = board[x][y] - spreadAmount*spreadDirNum;
		
		// 확산 정보를 spreadBoard에 합산 하여 저장 -> spreadAll함수 마지막에 원래 board에 더해줄 것
		int dx, dy;
		for (int d = 0; d < 4; d++) {
			dx = x+dir[d][0];
			dy = y+dir[d][1];
			if(canSpread[dx][dy])
				spreadBoard[dx][dy] += spreadAmount;
		}
	}
	
	public static void wind() {
		// 위쪽 순환 : 왼쪽, 위, 오른쪽, 아래 순으로 순환
		// 왼쪽 : 위에서 아래
		for (int i = cleanerR-1; i >= 2; i--)
			board[i][1] = board[i-1][1];
		// 위쪽 : 오른쪽에서 왼쪽
		for (int j = 1; j <= C-1; j++)
			board[1][j] = board[1][j+1];
		// 오른쪽 : 아래에서 위
		for (int i = 1; i <= cleanerR-1; i++)
			board[i][C] = board[i+1][C];
		// 아래쪽 : 왼쪽에서 오른쪽
		for (int j = C; j >= 2 ; j--)
			board[cleanerR][j] = board[cleanerR][j-1];
		
		// 아래쪽 순환 : 왼쪽, 아래, 오른쪽, 위 순으로 순환
		// 왼쪽 : 아래에서 위
		for (int i = cleanerR+2; i <= R-1; i++)
			board[i][1] = board[i+1][1];
		// 아래쪽 : 오른쪽에서 왼쪽
		for (int j = 1; j <= C-1; j++)
			board[R][j] = board[R][j+1];
		// 오른쪽 : 위에서 아래
		for (int i = R; i >= cleanerR+2; i--)
			board[i][C] = board[i-1][C];
		// 위쪽 : 왼쪽에서 오른쪽
		for (int j = C; j >= 2; j--)
			board[cleanerR+1][j] = board[cleanerR+1][j-1];
	}
}
