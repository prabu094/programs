#include <stdio.h>
char ascitobinary();

int main(void){
   ascitobinary();
}
char ascitobinary(){
      char	x ;
      int 	y;
      printf("Input a word to transmit: " );
      scanf("%c",&x);
       for(y = 0; y < sizeof(char) * 15; y++)
	 printf("%c ", ( x & (1 << y) ) ? '1' : '0' );
                 puts("");
       return 0;

}
