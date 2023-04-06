/// 예제 7번만 확인






import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, M, H;
	static int[][] ladder; // 사다리 상태
	static int[][] canAdd; // 조작 사다리 가능 좌표
	static int canAddNum = 0; // 조작할 사다리를 놓을 수 있는 갯수

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());

		ladder = new int[31][12];
		for (int n = 0; n < M; n++) {
			st = new StringTokenizer(br.readLine(), " ");
			ladder[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())] = 1;
		}

		canAdd = new int[301][2];
		for (int i = 1; i <= H; i++) {
			for (int j = 1; j < N; j++) {
				if (ladder[i][j] == 0) {
					canAdd[canAddNum][0] = i;
					canAdd[canAddNum++][1] = j;
				}
			}
		}
		////////////////// 입력

		// 사다리 안놔도 되면 ?
		if (jujak()) {
			System.out.println(0);
			System.exit(0);
		}

		// 사다리 하나 놓는다면 ?
		for (int i = 0; i < canAddNum; i++) {
			ladder[canAdd[i][0]][canAdd[i][1]] = 1;
			if (jujak()) {
				System.out.println(1);
				System.exit(0);
			}
			ladder[canAdd[i][0]][canAdd[i][1]] = 0;
		}

		// 사다리 두개 놓는다면 ?
		for (int i = 0; i < canAddNum - 1; i++) {
			ladder[canAdd[i][0]][canAdd[i][1]] = 1;
			for (int j = i + 1; j < canAddNum; j++) {
				ladder[canAdd[j][0]][canAdd[j][1]] = 1;
				if (jujak()) {
					System.out.println(2);
					System.exit(0);
				}
				ladder[canAdd[j][0]][canAdd[j][1]] = 0;
			}
			ladder[canAdd[i][0]][canAdd[i][1]] = 0;
		}

		// 사다리 세개 놓는다면 ?
		for (int i = 0; i < canAddNum - 2; i++) {
			ladder[canAdd[i][0]][canAdd[i][1]] = 1;
			for (int j = i + 1; j < canAddNum - 1; j++) {
				ladder[canAdd[j][0]][canAdd[j][1]] = 1;
				for (int k = j + 1; k < canAddNum; k++) {
					ladder[canAdd[k][0]][canAdd[k][1]] = 1;
					if (jujak()) {
						System.out.println(3);
						System.exit(0);
					}
					ladder[canAdd[k][0]][canAdd[k][1]] = 0;
				}
				ladder[canAdd[j][0]][canAdd[j][1]] = 0;
			}
			ladder[canAdd[i][0]][canAdd[i][1]] = 0;
		}
		
		System.out.println(-1);
	}

	// 현 상태 사다리로 주작이 가능한 상황이면?
	public static boolean jujak() {
		for (int n = 1; n <= N; n++) {
			if (n != down(n))
				return false;
		}
		return true;
	}

	public static int down(int num) {
		int cur = num;
		for (int i = 1; i <= H; i++) {
			if (ladder[i][cur - 1] == 1)
				--cur;
			else if (ladder[i][cur] == 1)
				++cur;
		}

		return cur;
	}
}