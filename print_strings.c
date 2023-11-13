#include<stdio.h>
// mayur Kyatham 
int main(){
    // char str[] = "Mayur";
    char str[] = {'M', 'a', 'y', 'u', 'r', '\0'};
    char *ptr = str;
    while(*ptr!='\0'){
        printf("%c", *ptr);
        ptr++;
    }
    return 0;
}
