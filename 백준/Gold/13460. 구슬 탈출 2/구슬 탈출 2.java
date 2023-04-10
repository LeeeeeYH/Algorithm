import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static class State {
		int loc; // 빨간구슬, 파란구슬의 위치를 담을 4자리 정수, (ex: 2365 : 빨간구슬 좌표 2,3 파란구슬 좌표 6,5)
		int bfMove; // 이전 움직임 저장 1234 : 상좌우하
		int moveNum; // 몇번 움직였니?

		public State() {
		}

		public State(int loc, int bfMove, int moveNum) {
			this.loc = loc;
			this.bfMove = bfMove;
			this.moveNum = moveNum;
		}
	}

	static char[][] board;
	static int N, M;
	static boolean find = false;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		board = new char[N][M];
//		int rx0, ry0, bx0, by0;
		int loc0 = 0;
		String line;
		char input;
		for (int i = 0; i < N; i++) {
			line = br.readLine();
			for (int j = 0; j < M; j++) {
				board[i][j] = input = line.charAt(j);
				switch (input) {
				case 'R':
					loc0 += i * 1000 + j * 100;
					board[i][j] = '.';
					break;
				case 'B':
					loc0 += i * 10 + j;
					board[i][j] = '.';
					break;
				}
			}
		}

		Queue<State> q = new ArrayDeque<State>();
		q.add(new State(loc0, 0, 0));
		State cur;
		int afMove = 0;
		while(!q.isEmpty()) {
			cur = q.poll();
			
			for (int d = 1; d <= 4; d++) {
				if(d != 5 - cur.bfMove) { // 이전 움직임의 반대방향이 아니면 ㄱㄱ
					switch (d) {
					case 1:
						afMove = moveUp(cur.loc);
						break;
					case 2:
						afMove = moveLeft(cur.loc);
						break;
					case 3:
						afMove = moveRight(cur.loc);
						break;
					case 4:
						afMove = moveDown(cur.loc);
						break;
					}
					if(afMove == 1) { // 빨간 구슬만 빠졌네 ?
						System.out.println(cur.moveNum+1);
						System.exit(0); // 끝
					}
					
					if(cur.moveNum < 9 && cur.loc != afMove && afMove != 0) // 10번 이내의 움직이기 전과 움직인 후의 구슬의 위치가 변화가 있고 파란구슬이 빠지지 않으면
						q.add(new State(afMove, d, cur.moveNum+1));
				}
			}
		}
		
		// queue가 끝났네?
		System.out.println(-1); // 못빼냄 ㅠ
	} // end of main

	// 빨간구슬, 파란구슬 담을 숫자로 반환 : 가로세로 크기 10 미만이므로 각각 한 자리 정수로 표현 가능
	// 빨간 구슬이 빠질 경우 1, 파란 구슬이 빠질 경우 0 반환
	public static int moveUp(int loc) {
		int rx = loc / 1000, ry = (loc / 100) % 10, bx = (loc / 10) % 10, by = loc % 10;
		while (true) { // 파란구슬 가자 : 둘다 빠질 경우 실패이므로 파란구슬을 먼저 굴려줘야 return 0이 됨
			if (board[bx - 1][by] == '.')
				--bx;
			else if (board[bx - 1][by] == 'O')
				return 0;
			else
				break;
		}
		while (true) { // 빨간구슬 가자
			if (board[rx - 1][ry] == '.')
				--rx;
			else if (board[rx - 1][ry] == 'O')
				return 1;
			else
				break;
		}

		if (ry == by && rx == bx) { // 같은 위치에 있으면
			if(loc/1000 < (loc/10)%10) // 처음 rx < bx : 빨간 구슬이 더 위
				++bx; // 파란색 하나 내려줌
			else ++rx;
		}
		
		return rx*1000 + ry*100 + bx*10 + by;
	}
	
	// 빨간구슬, 파란구슬 담을 숫자로 반환 : 가로세로 크기 10 미만이므로 각각 한 자리 정수로 표현 가능
	// 빨간 구슬이 빠질 경우 1, 파란 구슬이 빠질 경우 0 반환
	public static int moveLeft(int loc) {
		int rx = loc / 1000, ry = (loc / 100) % 10, bx = (loc / 10) % 10, by = loc % 10;
		while (true) { // 파란구슬 가자 : 둘다 빠질 경우 실패이므로 파란구슬을 먼저 굴려줘야 return 0이 됨
			if (board[bx][by - 1] == '.')
				--by;
			else if (board[bx][by - 1] == 'O')
				return 0;
			else
				break;
		}
		while (true) { // 빨간구슬 가자
			if (board[rx][ry - 1] == '.')
				--ry;
			else if (board[rx][ry - 1] == 'O')
				return 1;
			else
				break;
		}
		
		if (rx == bx && ry == by) { // 같은 위치에 있으면
			if((loc/100)%10 < loc%10) // 처음 ry < by : 빨간 구슬이 더 왼쪽
				++by; // 파란색 하나 오른쪽으로
			else ++ry;
		}
		
		return rx*1000 + ry*100 + bx*10 + by;
	}
	
	// 빨간구슬, 파란구슬 담을 숫자로 반환 : 가로세로 크기 10 미만이므로 각각 한 자리 정수로 표현 가능
	// 빨간 구슬이 빠질 경우 1, 파란 구슬이 빠질 경우 0 반환
	public static int moveRight(int loc) {
		int rx = loc / 1000, ry = (loc / 100) % 10, bx = (loc / 10) % 10, by = loc % 10;
		while (true) { // 파란구슬 가자 : 둘다 빠질 경우 실패이므로 파란구슬을 먼저 굴려줘야 return 0이 됨
			if (board[bx][by + 1] == '.')
				++by;
			else if (board[bx][by + 1] == 'O')
				return 0;
			else
				break;
		}
		while (true) { // 빨간구슬 가자
			if (board[rx][ry + 1] == '.')
				++ry;
			else if (board[rx][ry + 1] == 'O')
				return 1;
			else
				break;
		}
		
		if (rx == bx && ry == by) { // 같은 위치에 있으면
			if((loc/100)%10 < loc%10) // 처음 ry < by : 빨간 구슬이 더 왼쪽
				--ry; // 파란색 하나 오른쪽으로
			else --by;
		}
		
		return rx*1000 + ry*100 + bx*10 + by;
	}
	
	// 빨간구슬, 파란구슬 담을 숫자로 반환 : 가로세로 크기 10 미만이므로 각각 한 자리 정수로 표현 가능
	// 빨간 구슬이 빠질 경우 1, 파란 구슬이 빠질 경우 0 반환
	public static int moveDown(int loc) {
		int rx = loc / 1000, ry = (loc / 100) % 10, bx = (loc / 10) % 10, by = loc % 10;
		while (true) { // 파란구슬 가자 : 둘다 빠질 경우 실패이므로 파란구슬을 먼저 굴려줘야 return 0이 됨
			if (board[bx + 1][by] == '.')
				++bx;
			else if (board[bx + 1][by] == 'O')
				return 0;
			else
				break;
		}
		while (true) { // 빨간구슬 가자
			if (board[rx + 1][ry] == '.')
				++rx;
			else if (board[rx + 1][ry] == 'O')
				return 1;
			else
				break;
		}
		
		if (ry == by && rx == bx) { // 같은 위치에 있으면
			if(loc/1000 < (loc/10)%10) // 처음 rx < bx : 빨간 구슬이 더 위
				--rx; // 빨간색 하나 올려줌
			else --bx;
		}
		
		return rx*1000 + ry*100 + bx*10 + by;
	}
} // end of class