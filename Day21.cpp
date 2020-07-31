
template <class T> 
void printArray(vector<T> i) 
 { 
    for(int j=0;j<i.size();j++) 
        cout<<i[j]<<endl;
 } 
/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here
void printArray(vector<auto> a)
{
    for(auto i:a)
        cout<<i<<endl;
}


