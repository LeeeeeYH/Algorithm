import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[][][] can = new int[10][10][10]; // 각 질문마다 맞는 정보 저장 (ex: 324가 가능할 때 -> [3][2][4]++;해줌)
	static String info; // 정보
	static int str, bal; // 스트라잌, 볼
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st;
		for (int n = 0; n < N; n++) {
			st = new StringTokenizer(br.readLine());
			info = st.nextToken();
			str = Integer.parseInt(st.nextToken());
			bal = Integer.parseInt(st.nextToken());
			for (int i = 1; i <= 9; i++) {
				for (int j = 1; j <= 9; j++) {
					if(i == j) continue;
					for (int k = 1; k <= 9; k++) {
						if(i==k || j==k) continue;
						if(cal(i*100+j*10+k+"") == str*10+bal){ // 스트라이크, 볼 정보가 같다면
							can[i][j][k]++;
						}
					}
				}
			}
		}
		
		int res = 0;
		for (int i = 1; i <= 9; i++) {
			for (int j = 1; j <= 9; j++) {
				for (int k = 1; k <= 9; k++) {
					if(can[i][j][k] == N) // 4번받았는데 
						res++;
				}
			}
		}
		
		System.out.println(res);
	} // end of main
	
	// 세자리 정수 두개를 받아 스트라이크, 볼 여부를 두자리(XX)로 반환해주는 함수
	public static int cal(String comp) {
		int s = 0, b = 0;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if(info.charAt(i) == comp.charAt(j)) { // 같은 숫자가 있냐 판별해서
					if(i == j) s++; // 자리까지 같으면 스트라이크고
					else b++; // 다르면 볼이지
				}
			}
		}
		
		return s*10 + b; // 그냥 int로 처리해봄
	}
} // end of class
