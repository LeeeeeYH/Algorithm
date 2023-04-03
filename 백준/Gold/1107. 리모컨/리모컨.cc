//이방법으로 풀이시 up, down의 계산후 비교처리 순서가 중요함
//down, up이 범위를 넘어가면 처리해줘야함,,,,ㅠ
//10개 버튼이 다 고장나면 불쌍하게도 +,-로만 채널변경을 해야한다,,,
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

char broken[10];

int main()
{
	int N, M, in, count = 0;
	cin >> N >> M;
	for (int i = 0; i < M; i++)
		cin >> broken[i];
	
	int up = N;
	int down = N;
	bool canu, cand;
	string tmpu, tmpd;

	if (M != 10) {
		while (1) {
			cand = true;
			canu = true;
			if (down < 0) cand = false;
			tmpd = to_string(down);
			tmpu = to_string(up);
			for (int i = 0; i < M; i++)
			{
				//고장난버튼이 하나라도 포함되어있으면
				if (tmpd.find(broken[i]) != string::npos)
					cand = false;
				if (tmpu.find(broken[i]) != string::npos)
					canu = false;
			}

			if (cand) {
				count += tmpd.length();
				break;
			}
			else if (canu) {
				count += tmpu.length();
				break;
			}

			down--;
			up++;
			count++;
		}
	}
	else count = 500010;

	if (count > abs(N - 100)) count = abs(N - 100);
	
	cout << count;
}