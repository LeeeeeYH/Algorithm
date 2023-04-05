import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int N = Integer.parseInt(st.nextToken()); // 벨트에 놓인 접시의 수 	2 ~ 3,000,000
		int d = Integer.parseInt(st.nextToken()); // 초밥의 가짓수 			2 ~ 3,000
		int k = Integer.parseInt(st.nextToken()); // 연속해서 먹는 접시의 수	2 ~ 3,000 (~ N)
		int c = Integer.parseInt(st.nextToken()); // 쿠폰 번호				1 ~ d
		
		int[] belt = new int[N+k]; // 0번째 인덱스 버림
		Queue<Integer> q = new ArrayDeque<Integer>();
		int[] m = new int[d+1];
		
		for (int i = 1; i <= N; i++)
			belt[i] = Integer.parseInt(br.readLine());
		for (int i = N+1; i <= N+k-1; i++)
			belt[i] = belt[i-N];
		////////////////////////// 입력
		
		// 초기화
		int types = 1;
		
		m[c] = 1;
		int cur;
		for (int i = 1; i <= k; i++) {
			cur = belt[i];
			if(m[cur] == 0)
				++types; // 종류 ++
			++m[cur];
		}
		
		int res = types;
		
		for (int i = 1; i <= N-1; i++) {
			// 앞에꺼 빼주고
			cur = belt[i];
			if(m[cur] == 1)
				--types;
			--m[cur];
			
			// 뒤에꺼 더해주고
			cur = belt[i+k];
			if(m[cur] == 0)
				++types; // 종류 ++
			++m[cur];
			
			if(res < types)
				res = types;
		}
		
		System.out.println(res);
	}
	
	// Map 사용  976ms
//	public static void main(String[] args) throws Exception {
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
//		
//		int N = Integer.parseInt(st.nextToken()); // 벨트에 놓인 접시의 수 	2 ~ 3,000,000
//		int d = Integer.parseInt(st.nextToken()); // 초밥의 가짓수 			2 ~ 3,000
//		int k = Integer.parseInt(st.nextToken()); // 연속해서 먹는 접시의 수	2 ~ 3,000 (~ N)
//		int c = Integer.parseInt(st.nextToken()); // 쿠폰 번호				1 ~ d
//		
//		int[] belt = new int[N+k]; // 0번째 인덱스 버림
//		Queue<Integer> q = new ArrayDeque<Integer>();
//		Map<Integer, Integer> m = new HashMap<Integer, Integer>();
//		
//		for (int i = 1; i <= N; i++)
//			belt[i] = Integer.parseInt(br.readLine());
//		for (int i = N+1; i <= N+k-1; i++)
//			belt[i] = belt[i-N];
//		////////////////////////// 입력
//		
//		// 초기화
//		m.put(c, 1);
//		int cur;
//		for (int i = 1; i <= k; i++) {
//			cur = belt[i];
//			if(m.containsKey(cur))
//				m.put(cur, m.get(cur)+1);
//			else m.put(cur, 1);
//		}
//		
//		int res = m.size();
//		
//		for (int i = 1; i <= N-1; i++) {
//			// 앞에꺼 빼주고
//			cur = belt[i];
//			if(m.get(cur) == 1) m.remove(cur);
//			else m.put(cur, m.get(cur)-1);
//			
//			// 뒤에꺼 더해주고
//			cur = belt[i+k];
//			if(m.containsKey(cur))
//				m.put(cur, m.get(cur)+1);
//			else m.put(cur, 1);
//			
//			res = Math.max(res, m.size());
//		}
//		
//		System.out.println(res);
//	}
}