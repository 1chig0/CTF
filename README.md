# CTF
CtfTools

Defence.py

栅栏密码解密工具：

  1.列出所有可能项：
    Usage: DeFence.py -c content
  
  2.指定某个栅栏数：
    Usage: DeFence.py -c content -n (A number)

KeyBoard.py

键盘密码解密工具：

  Usage: KeyBoardPw.py -c (your content)


FairPlay.py

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
  
  Ps:今天心情很糟糕，所以就写了这个像一坨屎一样的代码，很多代码的格式还有简洁都有问题，不符合规范，我要冷静一下。
  
  
