#include <stdio.h>
/*       1
        2 2 
       3 3 3 
      4 4 4 4 
     5 5 5 5 5 
    6 6 6 6 6 6*/

int main()
{
   int i,j,spc,rows,k;
   scanf("%d",&rows);
   spc=rows+4-1;
   for(i=1;i<=rows;i++)
   {
         for(k=spc;k>=1;k--)
            {
              printf(" ");
            }
         for(j=1;j<=i;j++)
	   printf("%d ",i);
	printf("\n");
    spc--;
   }
   return 0;
}
