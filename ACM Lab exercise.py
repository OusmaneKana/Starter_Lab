
# coding: utf-8

# In[6]:


def sphere_volume(rad):
    pi = 3.141
    sv = (4/3)*pi*(rad)**3
    print(sv)
sphere_volume(int(input('Radius value:')))


# In[2]:


def ran_check(num,low,high):
    if num in range(low,high+1):
        print('In range')
    else:
        print('Not in range')

ran_check(3,1,10)


# In[7]:


def ran_check(num,low,high):
      return num in range(low,high+1)

ran_check(3,1,10)


# In[4]:


def multiply(number):
  product =1
  for x in number:
      product *=x
  return(product)
print(multiply([1,2,3,-4]))


# In[19]:


def unique_list(l):
    x=[]
    for n in l:
        if n not in x:
            x.append(n)
        return(x)
unique_list([1,1,1,2,2,2,3,4,5,5,6,5,4,3,3])


# In[13]:


def up_low(s):
    isLower = 0
    isUpper = 0
    for c in s:
        if c.isupper():
            isUpper+=1
        elif c.islower():
            isLower+=1
        
    print('The string:',s)
    print('Has {} number of uppercase and{} number of lower case'.format(isUpper, isLower))
s = 'fEw ef ef fwe ef'
up_low(s)


# In[22]:


def palindrome(s):
    s=s.replace(' ','')
    return s==s[::-1]
palindrome('nurses run')

