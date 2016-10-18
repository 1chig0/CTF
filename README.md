# CTF
CtfTools



@Defence.py

栅栏密码解密工具：

  1.列出所有可能项：
    Usage: DeFence.py -c content
  
  2.指定某个栅栏数：
    Usage: DeFence.py -c content -n (A number)




@KeyBoard.py

键盘密码解密工具：

  Usage: KeyBoardPw.py -c (your content)






@FairPlay.py

FairPlay密码解密工具：

  Usage：
  
  Input the key:The quick brown fox jumps over the lazy dog
  
  Input the omit:j
  
  ['t', 'h', 'e', 'q', 'u']
  
  ['i', 'c', 'k', 'b', 'r']
  
  ['o', 'w', 'n', 'f', 'x']
  
  ['m', 'p', 's', 'v', 'l']
  
  ['a', 'z', 'y', 'd', 'g']
  
  Input your passwd:smzdodcikmodcismzd
  
  playfairisfairplay
  
  首先输入密钥，接着输入需要去掉的字母，因为这个正方形方阵只有25个，所以可以通过观察加密的字符串。如果没有j出现，就得出要在方阵里面把j去掉。
  
  所以在omit一项输入想要去掉的字母（这里是j）
  
  继续接着输入passwd即密文。
  
  就可以得到解密后的明文了。
  
  有可能出现多个x的情况，因为明文在加密的时候，每对字符若相同则在这两个字符后面都加上x
  
  请自行判定。
  
  Ps:今天心情很糟糕，所以就写了这个像一坨屎一样的代码，很多代码的格式，还有简洁性都有问题，不符合规范，我要冷静一下。
  
  
 
@Bacon.py
 
 培根密码解密工具：
 
   Usage:
   
   bacon.py -a c -b d -p dccdcccdddcdcccddcccccccccddcdccccdccccc
   
   培根密码学中d或者c代表了0或者1，因此上面的例子-a参数代表了c就是0，-b参数代表了d，而-p参数代表了所输入的内容
   
   注意，很多情况下，-a参数的值可能要跟-b参数的值调换一下看看是否的出了自己所要的结果。请自行检查。
 
 

@MoresCode.py

  摩斯密码解密工具：
  
  MorseCode.py
  
  直接输入摩斯电码即可，注意，本脚本主要是以空格来分开。若有特殊情况请自行修改代码。
  
@Vigenere.py

  维吉尼亚密码加密工具：
  
  key指的是密钥
  
  pw输入需要进行加密的密码。
  


@Hill.py

  希尔密码解密工具：
  
  Usage:
  
  输入一个矩阵的格式是 'x1,x2;y1,y2;...'
  
  python Hill.py -k '1,2;0,1' -p dloguszijluswogany
  key is :
  [[ 1.  0.]
   [-2.  1.]]
  ------------------------------------------
  password matrix is:
  [[ 4 12]
   [15  7]
   [21 19]
   [26  9]
   [10 12]
   [21 19]
   [23 15]
   [ 7  1]
   [14 25]]
  ------------------------------------------
  The result matrix is:
  [[-20.  12.]
   [  1.   7.]
   [-17.  19.]
   [  8.   9.]
   [-14.  12.]
   [-17.  19.]
   [ -7.  15.]
   [  5.   1.]
   [-36.  25.]]
  ------------------------------------------
  The final result is:
  flagishillissoeapy


@ColumnSub.py
 
 列置换转换工具:
 
 Usage:
 
 python ColumnSub.py -c OCU{CFTELXOUYDECTNGAHOHRNFIENM}IOTA -o 2.txt
 
 The result is saved as 2.txt
 
 可根据自己的需要改变改变输出文件的名字
 
 此工具是列出所有可能的排列（不是那种单纯的暴力全排列）

  
  
  
  
  
  
  
  
