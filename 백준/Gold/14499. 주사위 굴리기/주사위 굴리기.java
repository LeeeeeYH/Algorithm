import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[][] board;
	static int[] dice = { 0, 0, 0, 0, 0, 0 }; // 위index 0, 아래index 5
	static int N, M, x, y;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		x = Integer.parseInt(st.nextToken());
		y = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		board = new int[N][M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < M; j++)
				board[i][j] = Integer.parseInt(st.nextToken());
		}

		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < K; i++) {
			move(Integer.parseInt(st.nextToken()));
		}
		System.out.println(sb.toString());
	} // end of main

	public static void move(int dir) {
		int[] temp = new int[6];
		for (int i = 0; i < 6; i++)
			temp[i] = dice[i];

		boolean moved = false; // 움직였나?
		switch (dir) { // 방향맞춰 맵탈출여부 확인하고 움직이자
		case 1: // 동쪽
			if (y < M - 1) {
				y++;
				dice[0] = temp[3];
				dice[2] = temp[0];
				dice[3] = temp[5];
				dice[5] = temp[2];
				moved = true;
			}
			break;
		case 2: // 서쪽
			if (y > 0) {
				y--;
				dice[0] = temp[2];
				dice[2] = temp[5];
				dice[3] = temp[0];
				dice[5] = temp[3];
				moved = true;
			}
			break;
		case 3: // 북쪽
			if (x > 0) {
				x--;
				dice[0] = temp[4];
				dice[1] = temp[0];
				dice[4] = temp[5];
				dice[5] = temp[1];
				moved = true;
			}
			break;
		case 4: // 남쪽
			if (x < N - 1) {
				x++;
				dice[0] = temp[1];
				dice[1] = temp[5];
				dice[4] = temp[0];
				dice[5] = temp[4];
				moved = true;
			}
			break;
		}

		if (moved) {
			if (board[x][y] == 0) // 이동한 칸에 쓰여있는 수가 0이면
				board[x][y] = dice[0]; // 주사위의 바닥면에 쓰여있는 수가 칸에 복사
			else { // 0이 아닌 경우에는
				dice[0] = board[x][y]; // 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사
				board[x][y] = 0; // 칸에 쓰여 있는 수는 0이 된다.
			}
			sb.append(dice[5]).append("\n");
		}
	}
} // end of class