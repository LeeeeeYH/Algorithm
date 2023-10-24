import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int num = 0;

        int testCase = Integer.parseInt(br.readLine());
        int[] moveY = {-2, -1, 1, 2, 2, 1, -1, -2};
        int[] moveX = {1, 2, 2, 1, -1, -2, -2, -1};

        for(int t = 0; t < testCase; t++) {
            Queue<int[]> q = new ArrayDeque<>();
            int l = Integer.parseInt(br.readLine());
            int[][] map = new int[l][l];
            boolean[][] visited = new boolean[l][l];
            int[] start = new int[2];
            StringTokenizer st = new StringTokenizer(br.readLine());
            start[0] = Integer.parseInt(st.nextToken());
            start[1] = Integer.parseInt(st.nextToken());
            int[] end = new int[2];
            st = new StringTokenizer(br.readLine());
            end[0] = Integer.parseInt(st.nextToken());
            end[1] = Integer.parseInt(st.nextToken());

            q.offer(new int[] {start[0], start[1], 0});
            visited[start[0]][start[1]] = true;

            while(!q.isEmpty()) {
                int[] curr = q.poll();

                if(curr[0] == end[0] && curr[1] == end[1]) {
                    sb.append(curr[2]).append("\n");
                    break;
                }

                for(int i = 0; i < 8; i++) {
                    int nextY = curr[0] + moveY[i];
                    int nextX = curr[1] + moveX[i];

                    if(nextY < 0 || nextY >= l) continue;
                    if(nextX < 0 || nextX >= l) continue;

                    if (!visited[nextY][nextX]) {
                        visited[nextY][nextX] = true;
                        q.offer(new int[]{nextY, nextX, curr[2] + 1});
                    }
                }
            }
        }

        System.out.println(sb.toString());
    }
}