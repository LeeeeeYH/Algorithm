import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
//		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		int G;
		int[] id; // 학번
		Set<Integer> s = new HashSet<Integer>(); // id를 i로 나눴을때 true로 만들어줌
		int m;
		int tmpMod;
		boolean found;
		for (int tc = 0; tc < T; tc++) {
			G = Integer.parseInt(br.readLine());
			id = new int[G];
			for (int i = 0; i < id.length; i++)
				id[i] = Integer.parseInt(br.readLine());
			
			
			m = 0;
			while(true) {
				++m;
				found = false;
				for (int i = 0; i < id.length; i++) {
					tmpMod = id[i]%m;
					if(!s.contains(tmpMod)) s.add(tmpMod);
					else {
						found = true;
						break;
					}
				}
				s.clear();
				if(!found) {
					sb.append(m).append("\n");
					break;
				}
			} // end of while
		} // end of testCase
		System.out.println(sb.toString());
	} // end of main
} // end of class