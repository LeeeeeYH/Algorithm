import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static final int[][] dir = {{1,0},{0,-1},{-1,0},{0,1}};
	static boolean[][] board = new boolean[101][101];
	static ArrayList<int[]> curve; // 드래곤 커브 [좌표번호][x,y]
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());

		int x, y, d, g;
		for (int n = 0; n < N; n++) {
			st = new StringTokenizer(br.readLine(), " ");
			x = Integer.parseInt(st.nextToken());
			y = Integer.parseInt(st.nextToken());
			d = Integer.parseInt(st.nextToken());
			g = Integer.parseInt(st.nextToken());
			curve = new ArrayList<int[]>();
			curve.add(new int[] {x, y});
			curve.add(new int[] {x + dir[d][0], y + dir[d][1]});
			
			// 세대 진행
			for (int i = 0; i < g; i++)
				nextG();
			
			// 커브 다구했으니 board 갱신
			for (int[] p : curve)
				board[p[0]][p[1]] = true;
		}
		
		// 다 구했으니 세자
		int cnt = 0;
		for (int i = 0; i <= 99; i++)
			for (int j = 0; j <= 99; j++)
				if(board[i][j] && board[i+1][j] && board[i][j+1] && board[i+1][j+1])
					cnt++;
		
		System.out.println(cnt);
	}
	
	public static void nextG() {
		int last = curve.size() - 1;
		
		for (int i = 1; i <= last; i++)
			curve.add(rot(curve.get(last), curve.get(last-i)));
	}
	
	public static int[] rot(int[] p1, int p2[]) { // param : 기준점, 돌려야 하는 점
		// x증가량 만큼 y증가, y증가량만큼 x감소
		return new int[] {p1[0] -p2[1]+p1[1], p1[1] +p2[0]-p1[0]};
	}
}