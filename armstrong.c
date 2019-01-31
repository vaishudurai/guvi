void main()
{
    int N, sum = 0, rem = 0, cube = 0, temp;
 
    scanf("%d", &N);
    temp = N;
    while (N != 0)
    {
        rem = N % 10;
        cube = pow(rem, 3);
        sum = sum + cube;
        N = N / 10;
    }
    if (sum == temp)
        printf ("yes");
    else
        printf ("no");
}
