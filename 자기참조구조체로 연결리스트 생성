#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#pragma warning (disable : 4996)
#define SIZE 20

typedef struct NODE {
	char name[SIZE];
	int age;
	struct NODE* link;
}NODE;

int main() {
	NODE* list = NULL; //list의 초깃값은 반드시 NULL값
	NODE* p_prev = NULL, * p, * p_next; //p_prev의 초깃값은 반드시 NULL값
	char buffer[SIZE];
	int age;

	while (1) {
		printf("성명입력(그냥 Enter을 치면 종료): ");
		gets_s(buffer, SIZE);
		if (buffer[0] == '\0') break; //enter키 입력해서 반복문 빠져나감

		p = (NODE*)malloc(sizeof(NODE)); //동적으로 생성된 구조체 주소를 반환하고 이 주소를 포인터 p에 저장
		strcpy_s(p->name, sizeof(p->name), buffer);
		printf("나이 입력: ");
		gets_s(buffer, SIZE);
		age = atoi(buffer);
		p->age = age;

		if (list == NULL) list = p;
		else {
			p_prev->link = p;
			p->link = NULL;
		}
		p_prev = p;
	}
	p = list; //연결리스트의 첫번째 노드를  list변수를 사용
	while (p != NULL) {
		printf("%s %d", p->name, p->age);
		p = p->link;
		if (p != NULL) printf("->");
	}
	p = list;
	while (p != NULL) {
		p_next = p->link;
		free(p);
		p = p_next;
	}
	return 0;
}
