#include<stdio.h>
#include<string.h>
int main()
{
    char str[50];
    int count=0,flag=0;
    scanf("%s",str);
    if(strlen(str)>31){flag=1;}
    if(flag==0)
    {
        if( (str[0]>='a'&&str[0]<='z') //small letter
        ||
        (str[0]>='A'&&str[0]<='Z') //cap letter
        ||
        (str[0]=='_')   //underscore
       )
        {
            for(int i=0;i<strlen(str);i++)
    
           {
                if((str[i]>='a'&& str[i]<='z')||
                  (str[i]>='A' && str[i]<='Z')||
                  (str[i]>='0'&& str[i]<='9')||
                  (str[i]=='_'))
                  {
                      count++;
                  }
           }
            if(count==strlen(str))
            {
                flag=0;
            }
            else
            {
                flag=1;
            }
        }
        else
        {
            flag=1;
        }
    }
    if(flag==0)
    {
        if (!strcmp(str, "auto") || !strcmp(str, "default")  
            || !strcmp(str, "signed") || !strcmp(str, "enum")  
            ||!strcmp(str, "extern") || !strcmp(str, "for")  
            || !strcmp(str, "register") || !strcmp(str, "if")  
            || !strcmp(str, "else")  || !strcmp(str, "int") 
            || !strcmp(str, "while") || !strcmp(str, "do") 
            || !strcmp(str, "break") || !strcmp(str, "continue")  
            || !strcmp(str, "double") || !strcmp(str, "float") 
            || !strcmp(str, "return") || !strcmp(str, "char") 
            || !strcmp(str, "case") || !strcmp(str, "const") 
            || !strcmp(str, "sizeof") || !strcmp(str, "long") 
            || !strcmp(str, "short") || !strcmp(str, "typedef") 
            || !strcmp(str, "switch") || !strcmp(str, "unsigned") 
            || !strcmp(str, "void") || !strcmp(str, "static") 
            || !strcmp(str, "struct") || !strcmp(str, "goto") 
            || !strcmp(str, "union") || !strcmp(str, "volatile"))
            {
                flag = 1;
            }
        else
        {
            flag = 0;
        }
    }
    if(flag==1)
    {
        printf("%s is invalid",str);
    }
    else
    {
        printf("%s is valid",str);
    }
    return 0;
}
