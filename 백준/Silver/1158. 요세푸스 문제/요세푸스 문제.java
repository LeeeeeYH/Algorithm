import java.util.Scanner;

// 링크드리스트 만들어보자
// 비효율적인데 재밌다
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); // 짧으니까 스캐너..
		StringBuilder sb = new StringBuilder("<");
		
		int N = sc.nextInt();
		int K = sc.nextInt();
		
		Node first = new Node(1); // head
		Node iter = first; // 계속 순회할 노드
		for (int i = 2; i <= N; i++) {
			iter.next = new Node(i);
			iter = iter.next;
		}
		iter.next = first; // 마지막 (= head 전 노드)가리키는 중으로 시작
		
		while(N-- != 0) {
			for (int i = 0; i < K-1; i++) // 삭제할 노드의 직전 노드에 도착
				iter = iter.next;
			sb.append(iter.next.data).append(", ");
			iter.next = iter.next.next; // 삭제할 노드 무시 -> 삭제
		}
		
//		sb.delete(sb.length()-2, sb.length());
		sb.setLength(sb.length()-2); // 지우기는 이 두가지 쓰면 되겠네요
		sb.append(">");
		System.out.println(sb.toString());
	}
}
class Node{
	public int data;
	public Node next = null;
	public Node() {}
	public Node(int data) {
		this.data = data;
	}
}

// 하려다 말기
//class CircularLinkedList {
//	public Node first;
//	int size = 0;
//	
//	public void add(int data) {
//		if(size == 0) {
//			first = new Node(data);
//			first.next = first;
//		} else {
//			Node iter = first;
//			for (int i = 1; i < size; i++) {
//				iter = iter.next;
//			}
//			Node tmp = new Node(data);
//			tmp.next = iter.next;
//			iter.next = tmp;
//		}
//		size++;
//	}
//
//	@Override
//	public String toString() {
//		StringBuilder sb = new StringBuilder();
//		Node iter = first;
//		for (int i = 0; i < size; i++) {
//			sb.append(iter.data).append(" ");
//			iter = iter.next;
//		}
//		return sb.toString();
//	}
//	
//	
//}

