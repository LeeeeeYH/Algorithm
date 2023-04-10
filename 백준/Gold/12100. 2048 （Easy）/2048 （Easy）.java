import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[][][] board; // [level][row][col]
	static int res = 0;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		board = new int[6][N][N]; // level:0~5

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < N; j++)
				board[0][i][j] = Integer.parseInt(st.nextToken());
		}
		////////////// 입력끝

		dfs(1);
		
		System.out.println(res);
	} // end of main
	
	public static void dfs(int lv) {
		if(lv == 6) return;
		
		for (int d = 0; d < 4; d++) {
			copy(board[lv], board[lv-1]);
			move(lv, d);
			// 최대값 갱신
			for (int i = 0; i < N; i++)
				for (int j = 0; j < N; j++)
					if(res < board[lv][i][j])
						res = board[lv][i][j];
			dfs(lv+1);
		}
	}

	public static void move(int lv, int dir) { // 방향(0123 : 상하좌우), level:움직인 횟수(저장할 곳)
		if (dir == 0) {// 위쪽으로 이동
			int putIndex;
			for (int j = 0; j < N; j++) { // 열마다
				ArrayList<Integer> list = new ArrayList<Integer>();
				for (int i = 0; i < N; i++) // 일단 있는 숫자 전부 저장해서 처리할 것.
					if(board[lv-1][i][j] != 0)
						list.add(board[lv-1][i][j]);
				list.add(0); // i번째와 i+1번째를 비교해 같은지 다른지를 비교하는데, 마지막 인덱스 비교를 위해 임의로 0 삽입
				
				putIndex = 0;
				for (int i = 0; i < list.size()-1; i++) { // 마지막에 넣어준 0을 제외한 size까지
					if(list.get(i).equals(list.get(i+1))) { // 현재와 다음값이 같으면
						board[lv][putIndex++][j] = 2 * list.get(i); // 두배를 넣어주고
						i++; // 다음꺼는 jump
					}
					else { // 현재와 다음값이 다르면
						board[lv][putIndex++][j] = list.get(i); // 그냥 넣어준다
					}
				}
				
				for (int i = putIndex; i < N; i++)
					board[lv][i][j] = 0; // 다 처리했으니까 뒷부분은 모두 빈공간 !
			}
		} else if(dir == 1) { // 아래쪽으로 이동
			int putIndex;
			for (int j = 0; j < N; j++) { // 열마다
				ArrayList<Integer> list = new ArrayList<Integer>();
				for (int i = N-1; i >= 0; i--) // 일단 있는 숫자 전부 저장해서 처리할 것.
					if(board[lv-1][i][j] != 0)
						list.add(board[lv-1][i][j]);
				list.add(0); // i번째와 i+1번째를 비교해 같은지 다른지를 비교하는데, 마지막 인덱스 비교를 위해 임의로 0 삽입
				
				putIndex = N-1;
				for (int i = 0; i < list.size()-1; i++) { // 마지막에 넣어준 0을 제외한 size까지
					if(list.get(i).equals(list.get(i+1))) { // 현재와 다음값이 같으면
						board[lv][putIndex--][j] = 2 * list.get(i); // 두배를 넣어주고
						i++; // 다음꺼는 jump
					} else { // 현재와 다음값이 다르면
						board[lv][putIndex--][j] = list.get(i); // 그냥 넣어준다
					}
				}
				
				for (int i = putIndex; i >= 0; i--)
					board[lv][i][j] = 0; // 다 처리했으니까 뒷부분은 모두 빈공간 !
			}
		} else if(dir == 2) { // 왼쪽으로 이동
			int putIndex;
			for (int i = 0; i < N; i++) { // 행마다
				ArrayList<Integer> list = new ArrayList<Integer>();
				for (int j = 0; j < N; j++) // 일단 있는 숫자 전부 저장해서 처리할 것.
					if(board[lv-1][i][j] != 0)
						list.add(board[lv-1][i][j]);
				list.add(0); // i번째와 i+1번째를 비교해 같은지 다른지를 비교하는데, 마지막 인덱스 비교를 위해 임의로 0 삽입
				
				putIndex = 0;
				for (int j = 0; j < list.size()-1; j++) { // 마지막에 넣어준 0을 제외한 size까지
					if(list.get(j).equals(list.get(j+1))) { // 현재와 다음값이 같으면
						board[lv][i][putIndex++] = 2 * list.get(j); // 두배를 넣어주고
						j++; // 다음꺼는 jump
					} else { // 현재와 다음값이 다르면
						board[lv][i][putIndex++] = list.get(j); // 그냥 넣어준다
					}
				}
				
				for (int j = putIndex; j < N; j++)
					board[lv][i][j] = 0; // 다 처리했으니까 뒷부분은 모두 빈공간 !
			}
		} else if(dir == 3) { // 오른쪽으로 이동
			int putIndex;
			for (int i = 0; i < N; i++) { // 행마다
				ArrayList<Integer> list = new ArrayList<Integer>();
				for (int j = N-1; j >= 0; j--) // 일단 있는 숫자 전부 저장해서 처리할 것.
					if(board[lv-1][i][j] != 0)
						list.add(board[lv-1][i][j]);
				list.add(0); // i번째와 i+1번째를 비교해 같은지 다른지를 비교하는데, 마지막 인덱스 비교를 위해 임의로 0 삽입
				
				putIndex = N-1;
				for (int j = 0; j < list.size()-1; j++) { // 마지막에 넣어준 0을 제외한 size까지
					if(list.get(j).equals(list.get(j+1))) { // 현재와 다음값이 같으면
						board[lv][i][putIndex--] = 2 * list.get(j); // 두배를 넣어주고
						j++; // 다음꺼는 jump
					} else { // 현재와 다음값이 다르면
						board[lv][i][putIndex--] = list.get(j); // 그냥 넣어준다
					}
				}
				
				for (int j = putIndex; j >= 0; j--)
					board[lv][i][j] = 0; // 다 처리했으니까 뒷부분은 모두 빈공간 !
			}
		}
	}
	
	// board2를 board1에 복사
	public static void copy(int[][] board1, int[][] board2) {
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				board1[i][j] = board2[i][j];
	}
} // end of class