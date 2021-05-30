#include <stdio.h>
int main()
{
  int i,j,r,c;
  scanf("%d%d",&r,&c);
  int arr1[r][c],brr1[c][r];
   for(int i=0;i<r;i++)
  for(int j=0;j<c;j++)
  scanf("%d",&arr1[i][j]);
  for(i=0;i<r;i++)
      for(j=0;j<c;j++)
        brr1[j][i]=arr1[i][j];
  for(i=0;i<c;i++){
      for(j=0;j<r;j++){
           printf("%d ",brr1[i][j]);
      }
      printf("\n");}
  return 0;
}
