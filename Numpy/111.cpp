#include<stdio.h>
#include<time.h>


int main(){
    time_t start, end;
    start = time(NULL);
    int value = 1000;
    int result = 0;
    for (int i = 1; i < value; i++){
        result++;
    }
    end = time(NULL);
    printf("Цикл исполльзовал %f \n", difftime(start, end));
    return 0;

}
