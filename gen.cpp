#pragma GCC optimize("Ofast")
#include<bits/stdc++.h>

using namespace std;

int main(int argc,char* argv[]) {
	if (argc < 2) printf("Usage: gen.o N V");
	srand (time(NULL) + clock());
	
	long long int N = atoi(argv[1]);
	long long int V = atoi(argv[2]);
	printf("%lli %lli\n", N, V);

	for (int i = 0; i < V; i++) {
		printf("%lli %lli\n", rand() % N, rand() % N);
	}

}
