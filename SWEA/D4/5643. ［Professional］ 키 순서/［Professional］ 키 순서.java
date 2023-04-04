import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		int N, M;
		ArrayList<Integer>[] biggerList; // 커지는인접리스트
		ArrayList<Integer>[] smallerList; // 작아지는인접리스트
		int[] knows; // 키를 알고있는 사람 수
		boolean[] visited;
		Queue<Integer> q;
		int res;
		
		int a, b;
		int cur, next;
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());
			biggerList = new ArrayList[N+1];
			smallerList = new ArrayList[N+1];
			for (int i = 1; i <= N; i++) {
				biggerList[i] = new ArrayList<Integer>();
				smallerList[i] = new ArrayList<Integer>();
			}
			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				a = Integer.parseInt(st.nextToken());
				b = Integer.parseInt(st.nextToken());
				biggerList[a].add(b);
				smallerList[b].add(a);
			}
			knows = new int[N+1];
			
			for (int stu = 1; stu <= N; stu++) {
				q = new ArrayDeque<Integer>();
				visited = new boolean[N+1];
				q.add(stu);
				visited[stu] = true;
				
				while(!q.isEmpty()) {
					cur = q.poll();
					
					for (int i = 0; i < biggerList[cur].size(); i++) {
						next = biggerList[cur].get(i);
						if(!visited[next]) {
							visited[next] = true;
							q.add(next);
							knows[next]++;
						}
					}
				}
			}
			for (int stu = 1; stu <= N; stu++) {
				q = new ArrayDeque<Integer>();
				visited = new boolean[N+1];
				q.add(stu);
				visited[stu] = true;
				
				while(!q.isEmpty()) {
					cur = q.poll();
					
					for (int i = 0; i < smallerList[cur].size(); i++) {
						next = smallerList[cur].get(i);
						if(!visited[next]) {
							visited[next] = true;
							q.add(next);
							knows[next]++;
						}
					}
				}
			}
			
			res = 0;
			for (int i = 1; i <= N; i++)
				if(knows[i] == N-1)
					res++;
			
			sb.append("#").append(tc).append(" ").append(res).append("\n");
		}
		
		System.out.println(sb.toString());
	}
}
