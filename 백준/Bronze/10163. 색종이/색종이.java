	
import java.io.BufferedReader;


import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        
        int[][] board = new int[1002][1002]; // 평면 판
        int N = Integer.parseInt(br.readLine());
        int[] count = new int[N+1]; // 보이는 색종이 개수 담을 배열
        int x1, y1, x2, y2;
        for (int pap = 1; pap <= N; pap++) {
			st = new StringTokenizer(br.readLine(), " ");
			x1 = Integer.parseInt(st.nextToken());
			y1 = Integer.parseInt(st.nextToken());
			x2 = Integer.parseInt(st.nextToken());
			y2 = Integer.parseInt(st.nextToken());
			for (int i = x1; i < x1+x2; i++)
				for (int j = y1; j < y1+y2; j++)
					board[i][j] = pap;
		}
        for (int i = 0; i <= 1001; i++)
			for (int j = 0; j < 1001; j++)
				count[board[i][j]]++;
        
        for (int i = 1; i <= N; i++)
			sb.append(count[i]).append("\n");
        System.out.println(sb.toString());
    }
}
