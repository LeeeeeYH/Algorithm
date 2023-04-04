import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, L;
	static int[][] board; // 지도
	static int res = 0; // 지나갈 수 있는 길의 개수
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		L = Integer.parseInt(st.nextToken());
		/* 위에서 아래로, 왼쪽에서 오른쪽으로 탐색할 건데,
		 * 범위체크를 안하기 위해 경사로 길이만큼 여유분을 준다 */
		board = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < N; j++)
				board[i][j] = Integer.parseInt(st.nextToken());
		}
		
		boolean path;
		// 가로길 검사
		for (int i = 0; i < N; i++) {
			path = true;
			for (int j = 0; j < N-1; j++) {
				if(board[i][j] == board[i][j+1]+1) { // 다음 칸이 한 칸 아래면
					for (int k = 0; k < L; k++) { // 경사로 만큼
						// 범위가 넘어가거나 경사로를 다 세우기 전에 높이가 변하면 실패
						if(j+1 + k >= N || board[i][j+1] != board[i][j+1 + k]) {
							path = false;
							break;
						}
					}
				} else if(board[i][j] == board[i][j+1]-1) { // 다음칸이 한 칸 위면
					for (int k = 0; k < 2*L; k++) { // 경사로 길이 두배만큼
						if(j-k >= 0 && board[i][j] == board[i][j-k]-1) { // 나보다 한칸 높았다면? 슬로프가 있을테니까
							path = false; // 지나가기 실패
							break;
						}
					}
					if(!path) break;
					
					for (int k = 0; k < L; k++) { // 경사로 만큼
						if(j-k < 0 || board[i][j] != board[i][j-k]) { // 평지가 있지 않다면
							path = false; // 지나가기 실패
							break;
						}
					}
				} else if(board[i][j] == board[i][j+1]) {
					continue; // 같으면 개꿀
				} else { // 두칸 이상 차이면
					path = false; // 못지나가
				}
				
				if(!path) break;
			}
			if(path) res++;
		}
		// 세로길 검사
		for (int i = 0; i < N; i++) {
			path = true;
			for (int j = 0; j < N-1; j++) {
				if(board[j][i] == board[j+1][i]+1) { // 다음 칸이 한 칸 아래면
					for (int k = 0; k < L; k++) { // 경사로 만큼
						// 범위가 넘어가거나 경사로를 다 세우기 전에 높이가 변하면 실패
						if(j+1 + k >= N || board[j+1][i] != board[j+1 + k][i]) {
							path = false;
							break;
						}
					}
				} else if(board[j][i] == board[j+1][i]-1) { // 다음칸이 한 칸 위면
					for (int k = 0; k < 2*L; k++) { // 경사로 길이 두배만큼
						if(j-k >= 0 && board[j][i] == board[j-k][i]-1) { // 나보다 한칸 높았다면? 슬로프가 있을테니까
							path = false; // 지나가기 실패
							break;
						}
					}
					if(!path) break;
					
					for (int k = 0; k < L; k++) { // 경사로 만큼
						if(j-k < 0 || board[j][i] != board[j-k][i]) { // 평지가 있지 않다면
							path = false; // 지나가기 실패
							break;
						}
					}
				} else if(board[j][i] == board[j+1][i]) {
					continue; // 같으면 개꿀
				} else { // 두칸 이상 차이면
					path = false; // 못지나가
				}
				
				if(!path) break;
			}
			if(path) res++;
		}
		
		System.out.println(res);
	} // end of main
	
} // end of class