import java.io.BufferedReader;

import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	public static class State {
		int[][] board;
		int used; // 남은 색종이 개수를 나타내는 5자리 숫자, (ex: 12431 : 55 1장, 44 2장, 33 4장 ...)
		public State(int[][] board, int used) {
			this.board = board;
			this.used = used;
		}
		
		public int paperNum() {
			return used/10000 + (used/1000)%10 + (used/100)%10 + (used/10)%10 + used%10;
		}
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[][] board0 = new int[10][10];
		for (int i = 0; i < 10; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < 10; j++)
				board0[i][j] = Integer.parseInt(st.nextToken());
		}
		
		Queue<State> q = new ArrayDeque<State>();
		q.add(new State(board0, 0));
		State cur;
		boolean find;
		int x = -1, y = -1;
		boolean poss; // n x n 색종이가 가능한지 확인
		int nextUsed; // 사용한 색종이 추가
		while(!q.isEmpty()) {
			cur = q.poll();
			
			// 모두 0인지 세고, 0이 아닌 부분이 나온다면 거기에 색종이를 꾸겨넣어보자
			find = false;
			for (int i = 0; i < 10; i++) {
				for (int j = 0; j < 10; j++) {
					if(cur.board[i][j] == 1) {
						find = true;
						x = i; y = j;
						break;
					}
				}
				if(find) break;
			}
			
			if(!find) { // 모두 0이라면 ?
				System.out.println(cur.paperNum());
				System.exit(0);
			}
			
			for (int len = 1; len <= 5; len++) { // 각 색종이 별로 가능성 확인
				poss = true; // len * len 칸에 색종이를 놓을 수 있나 확인
				for (int i = x; i < x+len; i++) {
					for (int j = y; j < y+len; j++) {
						if(i >= 10 || j >= 10 || cur.board[i][j] == 0) {
							poss = false;
							break;
						}
					}
					if(!poss) break;
				}
				
				if(!poss) break; // len*len을 못붙이면 더 큰것도 못붙임
				else {
					nextUsed = use(len, cur.used); // len을 사용 한 뒤의 색종이 사용현황
					if(nextUsed != -1) { // len 크기 색종이를 사용 가능 했을때
						int[][] next = new int[10][10]; // 다음 보드 현황
						
						// 일단 전체복사
						for (int i = 0; i < 10; i++)
							for (int j = 0; j < 10; j++)
								next[i][j] = cur.board[i][j];
						
						// 붙인 색종이 만큼 복사
						for (int i = x; i < x+len; i++) {
							for (int j = y; j < y+len; j++) {
								next[i][j] = 0;
							}
						}
						q.add(new State(next, nextUsed));
					}
				}
			}
		}
		
		System.out.println(-1);
	} // end of main
	
	public static int use(int idx, int used) {
		int ten = 1;
		for (int i = 0; i < idx-1; i++)
			ten *= 10;
		if((used / ten) % 10 == 5) return -1; // 해당 자릿수 색종이 다썼으면 -1 출력 
		return used + ten; // 아니면 하나 더해주고 return
	}
} // end of class