import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static final int[][] dir = {{-1,0},{0,1},{1,0},{0,-1}};
	static int R, C;
	static char[][] board;
	static int dx, dy; // 비버 굴 위치
	static int sx, sy; // 고슴도치 위치
	static Queue<int[]> water = new ArrayDeque<int[]>(); // 물 위치들 저장 -> 시간 빠르게 하기 위함
	static Queue<int[]> hog = new ArrayDeque<int[]>(); // 고슴도치가 갈 수 있는 위치 저장 

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		board = new char[R+2][C+2];
		
		String line;
		char input;
		for (int i = 1; i <= R; i++) {
			line = br.readLine();
			for (int j = 1; j <= C; j++) {
				board[i][j] = input = line.charAt(j - 1);
				switch (input) {
				case 'D':
					dx = i; dy = j;
					break;
				case 'S':
					sx = i; sy = j;
					hog.add(new int[] {i,j});
					break;
				case '*':
					water.add(new int[] {i,j});
					break;
				}
			}
		}
		// 테두리
		for (int i = 1; i <= R; i++)
			board[i][0] = board[i][C+1] = 'X';
		for (int i = 1; i <= C; i++)
			board[0][i] = board[R+1][i] = 'X';
		
		/////////////////////////입력
		
		int res = 1;
		while(!hog.isEmpty()) {
			waterSpread();
			if(hogSpread()) {
				System.out.println(res);
				System.exit(0);
			}
			res++;
		}
		
		System.out.println("KAKTUS");
	}
	
	public static void waterSpread() {
		Queue<int[]> nextWater = new ArrayDeque<int[]>(); // 다음 물 확산때 물위치 저장
		
		int x, y, dx, dy;
		while(!water.isEmpty()) {
			x = water.peek()[0];
			y = water.poll()[1];
			
			for (int d = 0; d < 4; d++) {
				dx = x + dir[d][0];
				dy = y + dir[d][1];
				if(board[dx][dy] == '.' || board[dx][dy] == 'S') {
					board[dx][dy] = '*';
					nextWater.add(new int[] {dx,dy});
				}
			}
		}
		
		water = nextWater;
	}
	
	public static boolean hogSpread() {
		Queue<int[]> nextHog = new ArrayDeque<int[]>();
		
		int x, y, dx, dy;
		while(!hog.isEmpty()) {
			x = hog.peek()[0];
			y = hog.poll()[1];
			
			for (int d = 0; d < 4; d++) {
				dx = x + dir[d][0];
				dy = y + dir[d][1];
				
				if(board[dx][dy] == 'D') // 동굴 도착!
					return true;
				
				if(board[dx][dy] == '.') {
					board[dx][dy] = 'S';
					nextHog.add(new int[] {dx,dy});
				}
			}
		}
		
		hog = nextHog;
		
		return false;
	}
}