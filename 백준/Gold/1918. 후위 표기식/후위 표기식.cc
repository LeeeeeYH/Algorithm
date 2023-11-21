//다시봐야함 ㅠ
#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
	string in; cin >> in;
	stack<char> s;
	char c;

	for (int i = 0; i < in.length(); i++) {
		c = in[i];
		if (c >= 'A' && c <= 'Z')		//피연산자이면 바로출력
			cout << c;
		else if (c == '(') s.push(c);	//'('는 그냥 push
		else if (c == '*' || c == '/') {
			while (!s.empty() && (s.top() == '*' || s.top() == '/')) {	
				cout << s.top();	//*와 /는 우선순위가 같으므로 출력후
				s.pop();
			}	
			s.push(c);				//push
		}
		else if (c == '+' || c == '-') {
			while (!s.empty() && s.top() != '(') {
				cout << s.top();	//+와 -는 *와 /보다 우선순위가 뒤므로 모두출력후
				s.pop();
			}
			s.push(c);				//push
		}
		else if (c == ')') {
			while (!s.empty() && s.top() != '(') {
				cout << s.top();	//'('나올떄까지 계산후에
				s.pop();
			}
			s.pop();				//'('pop
		}
	}
	while (!s.empty()) {	//stack에 남은연산 모두 출력
		cout << s.top();
		s.pop();
	}
}