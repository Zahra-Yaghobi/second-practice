// Programmer : Zahra Yaghubi
#include <iostream>
using namespace std;
int main()
{
	int n;
	float avg , sum=0;
	int max =0 , min=0;
	int score[1200];
	cout<<"enter number of student :";
	cin>>n;
	for (int i=0;i<n;i++)
	{
		cin>>score[i];
		sum+=score[i];
	}
	avg=sum/n;
	cout<<"  avg is :" ;
	cout<<avg;
	min =score[0];
	max =score[0];
	for (int j=0;j<n;j++){
		if(score[j] >max)
			max =score[j];
		if(score[j] <min)
			min =score[j];
	}
	cout <<" \nMinimum is :";
	cout<< min;
	cout<<" \nMaximum is :";
	cout<<max;
}